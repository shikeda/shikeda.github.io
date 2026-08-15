#!/usr/bin/env python3
"""Rewrite Hugo-relative/absolute internal links to absolute site URLs.

Used by build-krm-docx.sh: Hugo content uses relative links (./foo/,
../foo/) and root-relative links (/docs/krm/..., /en/docs/krm/...) that
only resolve correctly inside the built Hugo site. Pandoc has no notion
of that site structure, so such links end up broken in the generated
Word document. This script resolves every such link against the site
URL of the page being processed and rewrites it to a full
https://shikeda.github.io/... URL. Image paths (already rewritten to
relative `images/...` by build-krm-docx.sh) and links that are already
absolute (http/https/mailto) or anchor-only (#...) are left untouched.
"""
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://shikeda.github.io"

LINK_RE = re.compile(r'(\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
FENCE_RE = re.compile(r'^(```+|~~~+)')


def page_url(src_path: str, lang: str) -> str:
    rel = Path(src_path)
    if rel.parts and rel.parts[0] == "content":
        rel = rel.relative_to("content")

    suffix = f".{lang}.md"
    stem = str(rel)
    if not stem.endswith(suffix):
        raise ValueError(f"{src_path!r} does not end with {suffix!r}")
    stem = stem[: -len(suffix)]

    parts = [p for p in stem.split("/") if p]
    if parts and parts[-1] == "_index":
        parts = parts[:-1]

    url_path = "/" + "/".join(parts)
    if not url_path.endswith("/"):
        url_path += "/"
    if lang == "en":
        url_path = "/en" + url_path

    return BASE_URL + url_path


def rewrite_line(line: str, base: str) -> str:
    def repl(match: re.Match) -> str:
        target = match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        if target.startswith("images/") or target.startswith("/images/"):
            return match.group(0)
        new_target = urljoin(base, target)
        return f"{match.group(1)}{new_target}{match.group(3)}"

    return LINK_RE.sub(repl, line)


def main() -> None:
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <tmp_file> <src_path> <lang>", file=sys.stderr)
        sys.exit(1)

    tmp_file, src_path, lang = sys.argv[1], sys.argv[2], sys.argv[3]
    base = page_url(src_path, lang)

    text = Path(tmp_file).read_text(encoding="utf-8")
    out_lines = []
    fence_marker = None
    for line in text.splitlines(keepends=True):
        m = FENCE_RE.match(line.strip())
        if fence_marker is None:
            if m:
                fence_marker = m.group(1)[0]  # '`' or '~'
                out_lines.append(line)
                continue
            out_lines.append(rewrite_line(line, base))
        else:
            if m and m.group(1)[0] == fence_marker:
                fence_marker = None
            out_lines.append(line)

    Path(tmp_file).write_text("".join(out_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
