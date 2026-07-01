#!/usr/bin/env python3
# strip_ucs_brackets.py
"""
変換表に載っているUCS文字を囲む [ ] / 【 】 のみ除去する。
[A] [左] [未詳] などの注記括弧には触れない。
"""

import csv
import re
import sys
import tempfile
from pathlib import Path

TARGET_COLS = ["漢語_見出し", "漢語_出現形"]
CHAR_COLUMN_CANDIDATES = ["cjkv-char", "cjkv_char", "ucs-char", "ucs_char",
                           "UCS文字", "Unicode文字", "符号化文字"]
HEADERLESS_UCS_COL_INDEX = 3  # 0-indexed、4列目


def load_ucs_chars(map_path: Path) -> set[str]:
    """変換表からUCS文字の集合を返す。ヘッダあり・なし両対応。"""
    with map_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            first_row = next(reader)
        except StopIteration:
            sys.exit(f"変換表が空です: {map_path}")

        char_col_index = None
        for i, cell in enumerate(first_row):
            if cell in CHAR_COLUMN_CANDIDATES:
                char_col_index = i
                break

        chars: set[str] = set()
        if char_col_index is not None:
            # ヘッダあり：1行目はヘッダなので続きを読む
            for row in reader:
                if len(row) > char_col_index:
                    v = row[char_col_index].strip()
                    if v:
                        chars.add(v)
        else:
            # ヘッダなし：1行目もデータ、4列目(index=3)がUCS文字
            if len(first_row) > HEADERLESS_UCS_COL_INDEX:
                v = first_row[HEADERLESS_UCS_COL_INDEX].strip()
                if v:
                    chars.add(v)
            for row in reader:
                if len(row) > HEADERLESS_UCS_COL_INDEX:
                    v = row[HEADERLESS_UCS_COL_INDEX].strip()
                    if v:
                        chars.add(v)
        return chars


def make_pattern(ucs_chars: set[str]) -> re.Pattern:
    """対象UCS文字だけにマッチする括弧パターンを生成。長い順に並べる。"""
    if not ucs_chars:
        raise ValueError("ucs_chars is empty")
    escaped = [re.escape(c) for c in sorted(ucs_chars, key=len, reverse=True)]
    inner = "|".join(escaped)
    return re.compile(rf'[\[【]({inner})[\]】]')


def process(path: Path, pattern: re.Pattern, apply: bool) -> int:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fieldnames = reader.fieldnames
        rows = list(reader)

    changed = 0
    new_rows = []
    for row in rows:
        new_row = dict(row)
        for col in TARGET_COLS:
            if col in new_row:
                orig = new_row[col]
                new_value, n = pattern.subn(r'\1', orig)
                new_row[col] = new_value
                changed += n
        new_rows.append(new_row)

    if changed:
        print(f"{path.name}: {changed}箇所変更")
        if apply:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="",
                    dir=path.parent, delete=False, suffix=".tmp") as tmp:
                w = csv.DictWriter(tmp, fieldnames=fieldnames, delimiter="\t",
                                   lineterminator="\n", extrasaction="ignore")
                w.writeheader()
                w.writerows(new_rows)
            Path(tmp.name).replace(path)

    return changed


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="変換表のUCS文字を囲む括弧を漢語列から除去する"
    )
    parser.add_argument("--map", required=True, help="IDS->UCS変換表TSV")
    parser.add_argument("--data-dir", required=True, help="DHSJR個別TSVディレクトリ")
    parser.add_argument("--apply", action="store_true", help="実際に書き換える")
    args = parser.parse_args()

    ucs_chars = load_ucs_chars(Path(args.map))
    print(f"対象UCS文字数: {len(ucs_chars)}")
    if not ucs_chars:
        sys.exit("UCS文字が1件も読み込めませんでした。変換表を確認してください。")

    pattern = make_pattern(ucs_chars)

    total = 0
    for tsv in sorted(Path(args.data_dir).glob("*.tsv")):
        total += process(tsv, pattern, args.apply)

    print(f"\n合計: {total}箇所変更")
    if not args.apply:
        print("dry-run。--apply を付けると書き換えます。")

