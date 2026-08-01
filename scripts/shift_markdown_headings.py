#!/usr/bin/env python3
"""Shift ATX Markdown heading levels (# .. ######) down by a fixed amount.

Used by scripts/build-krm-docx.sh to nest each KRM Documentation child
page one level below its chapter's _index page when assembling the
combined Word document -- without touching the source .md files, which
must keep their own top-level H1 for Hugo (each page is its own document
there, not a subsection of its parent's page).

Deliberately not a sed one-liner: a bare `#`-at-start-of-line replace
would also rewrite YAML front matter comments (e.g. `# bookCollapseSection:
false`) and any `#` shown literally inside fenced code blocks (Markdown or
shell examples). This script tracks front-matter and fence state so only
genuine ATX headings in the document body are shifted.

Usage: shift_markdown_headings.py INPUT OUTPUT [--by N]
"""

from __future__ import annotations

import argparse
import re
import sys

ATX_RE = re.compile(r"^(?P<indent>[ ]{0,3})(?P<hashes>#{1,6})(?P<rest>[ \t].*|)$")
FENCE_RE = re.compile(r"^[ ]{0,3}(?P<fence>`{3,}|~{3,})")

MAX_ATX_LEVEL = 6


def shift_headings(text: str, by: int) -> str:
    lines = text.split("\n")
    out: list[str] = []

    in_frontmatter = False
    in_fence = False
    fence_char = ""
    fence_len = 0

    for i, line in enumerate(lines):
        # YAML front matter is only recognized when the file's very first
        # line is a bare "---"; everything up to the closing "---" is
        # passed through completely unchanged.
        if i == 0 and line.strip() == "---":
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            if line.strip() == "---":
                in_frontmatter = False
            continue

        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group("fence")
            ch, length = marker[0], len(marker)
            if not in_fence:
                in_fence, fence_char, fence_len = True, ch, length
            elif ch == fence_char and length >= fence_len:
                in_fence, fence_char, fence_len = False, "", 0
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        heading_match = ATX_RE.match(line)
        if heading_match:
            new_level = min(MAX_ATX_LEVEL, len(heading_match.group("hashes")) + by)
            out.append(
                f"{heading_match.group('indent')}{'#' * new_level}{heading_match.group('rest')}"
            )
        else:
            out.append(line)

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--by", type=int, default=1, help="levels to shift down (default: 1)")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        text = f.read()

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(shift_headings(text, args.by))

    return 0


if __name__ == "__main__":
    sys.exit(main())
