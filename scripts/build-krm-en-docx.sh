#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

output="publication/KRM_Documentation_en.docx"
file_list="publication/krm-en-files.txt"
cover_file="publication/cover.md"
metadata_file="publication/metadata-en.yaml"
reference_doc="publication/reference.docx"
tmp_dir="$(mktemp -d)"

trap 'rm -rf "$tmp_dir"' EXIT

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is not installed or not in PATH." >&2
  exit 1
fi

if [[ ! -f "$file_list" ]]; then
  echo "Error: file list not found: $file_list" >&2
  exit 1
fi

if [[ ! -f "$cover_file" ]]; then
  echo "Error: cover file not found: $cover_file" >&2
  exit 1
fi

if [[ ! -f "$reference_doc" ]]; then
  echo "Error: reference document not found: $reference_doc" >&2
  echo "Regenerate it with: python3 scripts/build-reference-docx.py" >&2
  exit 1
fi

mapfile -t files < <(
  grep -vE '^[[:space:]]*(#|$)' "$file_list"
)

if [[ ${#files[@]} -eq 0 ]]; then
  echo "Error: no input files are listed in $file_list" >&2
  exit 1
fi

# --file-scope processes every input file's own YAML front matter (needed
# for Hugo's per-page `title:`), and every file's `title:` field overwrites
# the document-wide title in turn -- so without an override, the title page
# ends up showing whichever chapter happens to be *last* in the file list,
# not the book's own title (only `title` collides this way: none of the
# chapter files set `subtitle`/`author`/`date`, so those three come through
# untouched from cover.md's own front matter). Metadata given via -M on the
# command line is the one thing guaranteed to win regardless of file order,
# so the book title is re-asserted that way, read from metadata-en.yaml so
# it can't drift from the value recorded there.
read_metadata_field() {
  local key="$1"
  sed -n "s/^${key}:[[:space:]]*\"\\{0,1\\}\\([^\"]*\\)\"\\{0,1\\}[[:space:]]*\$/\\1/p" \
    "$metadata_file" | head -n1
}

meta_title="$(read_metadata_field title)"

if [[ -z "$meta_title" ]]; then
  echo "Error: could not read 'title' from $metadata_file" >&2
  exit 1
fi

processed_files=("$cover_file")
heading_shift_script="scripts/shift_markdown_headings.py"

for file in "${files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Error: input file not found: $file" >&2
    exit 1
  fi

  # 元のディレクトリ構造を一時ディレクトリ内に再現する
  tmp_file="$tmp_dir/$file"
  mkdir -p "$(dirname "$tmp_file")"

  # Hugo用の絶対画像パスをPandoc用の相対パスに変換する
  sed \
    -e 's#](/images/#](images/#g' \
    -e 's#src="/images/#src="images/#g' \
    "$file" > "$tmp_file"

  # Hugoでは章の _index.en.md と各子ページ（NN-NN-*.en.md）が別ファイル
  # ・別URLであり、hugo-book のサイドバーがディレクトリ構造から自動的に
  # 親子関係を表示するため、そのままで問題ない。一方Pandocはそのような
  # 階層を知らず、連結した各ファイルの見出し1（#）をすべて同格の章として
  # 扱ってしまう。子ページだけ見出しを1段階下げることで、Word版でも
  # 「章の _index = Heading 1」「子ページ = Heading 2以下」の階層を再現する。
  # 元のMarkdownファイルは変更せず、この一時ファイルにのみ適用する。
  if [[ "$(basename "$file")" != _index.* ]]; then
    python3 "$heading_shift_script" "$tmp_file" "$tmp_file" --by 1
  fi

  processed_files+=("$tmp_file")
done

pandoc \
  "${processed_files[@]}" \
  --from=markdown+yaml_metadata_block \
  --file-scope \
  --toc \
  --number-sections \
  --resource-path=".:static:content/docs/krm" \
  --reference-doc="$reference_doc" \
  -M title="$meta_title" \
  -o "$output"

echo "Created: $output"
