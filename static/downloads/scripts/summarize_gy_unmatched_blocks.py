#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
summarize_gy_unmatched_blocks.py

dhsjr_gy_unmatched.blocks.tsv を「ブロック」列で集計し、
件数・割合・ユニーク文字数と例を Markdown レポートに書き出す。

Usage:
    python summarize_gy_unmatched_blocks.py
        (reads ./dhsjr_gy_unmatched.blocks.tsv,
         writes ./dhsjr_gy_unmatched.blocks_集計.md)

    python summarize_gy_unmatched_blocks.py --tsv PATH --out PATH

    python summarize_gy_unmatched_blocks.py --examples 8 --detail-top 5
"""
import argparse
import csv
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

COL_BLOCK = "ブロック"
COL_CHAR = "単字_見出し"
COL_HEX = "16進Unicode番号"
COL_MATERIAL = "資料番号"

NOTES = [
    (
        "**IDC**（Ideographic Description Characters）: "
        "漢字構成記述文字（⿰⿱ など）。実字ではなく字形の構造を表す記号。"
    ),
    (
        "**該当なし**: Unicode ブロックに分類されない文字。"
        "例として `〓`（U+3013、欠損記号）が含まれる。"
    ),
    "件数は行数ベース。同一文字が複数の資料番号に登場する場合、行として重複カウントされる。",
]


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fieldnames = reader.fieldnames or []
        for col in (COL_BLOCK, COL_CHAR, COL_HEX, COL_MATERIAL):
            if col not in fieldnames:
                sys.exit(f"Expected column '{col}' not found in {path}. "
                           f"Columns: {fieldnames}")
        return list(reader)


def aggregate_by_block(rows):
    by_block = defaultdict(list)
    for row in rows:
        by_block[row[COL_BLOCK].strip()].append(row)
    return sorted(by_block.items(), key=lambda x: -len(x[1]))


def unique_examples(items, limit):
    """Return up to `limit` distinct (char, hex) pairs in first-seen order."""
    seen = set()
    out = []
    for item in items:
        char = item[COL_CHAR]
        if char in seen:
            continue
        seen.add(char)
        out.append((char, item[COL_HEX]))
        if len(out) >= limit:
            break
    return out


def format_example(char, hex_code):
    return f"`{char}` U+{hex_code}"


def build_summary_table(sorted_blocks, total, examples_per_block):
    lines = [
        "## 集計表",
        "",
        "| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大{}件） |".format(
            examples_per_block),
        "|---------|-----:|-----:|--------------:|--------------|",
    ]
    for block, items in sorted_blocks:
        count = len(items)
        pct = 100 * count / total if total else 0
        unique_chars = len({r[COL_CHAR] for r in items})
        ex = "、".join(
            format_example(c, h) for c, h in unique_examples(items, examples_per_block)
        )
        lines.append(
            f"| {block} | {count:,} | {pct:.1f}% | {unique_chars:,} | {ex} |"
        )
    return lines


def build_detail_section(sorted_blocks, detail_top, detail_examples):
    lines = [
        "",
        "### 件数上位{}ブロックの内訳".format(detail_top),
        "",
    ]
    for block, items in sorted_blocks[:detail_top]:
        lines.append(f"#### {block}（{len(items):,} 件）")
        lines.append("")
        lines.append("| 資料番号 | 単字 | Unicode |")
        lines.append("|---------|------|---------|")
        seen = set()
        shown = 0
        for item in items:
            key = (item[COL_CHAR], item[COL_HEX])
            if key in seen:
                continue
            seen.add(key)
            lines.append(
                f"| {item[COL_MATERIAL]} | {item[COL_CHAR]} | U+{item[COL_HEX]} |"
            )
            shown += 1
            if shown >= detail_examples:
                break
        lines.append("")
    return lines


def build_markdown(rows, tsv_path, examples_per_block, detail_top, detail_examples):
    sorted_blocks = aggregate_by_block(rows)
    total = len(rows)
    stem = Path(tsv_path).name

    lines = [
        f"# {stem} ブロック別集計",
        "",
        date.today().isoformat(),
        "",
        f"対象ファイル: `{stem}`",
        "",
        f"- 総行数: {total:,} 行",
        f"- ブロック種類: {len(sorted_blocks)} 種",
        "",
    ]
    lines.extend(build_summary_table(sorted_blocks, total, examples_per_block))
    lines.extend([
        "",
        "## 補足",
        "",
    ])
    for note in NOTES:
        lines.append(f"- {note}")
    lines.extend(build_detail_section(sorted_blocks, detail_top, detail_examples))
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tsv",
        default="dhsjr_gy_unmatched.blocks.tsv",
        help="Input TSV path (default: dhsjr_gy_unmatched.blocks.tsv)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output Markdown path. Default: <tsv stem>_集計.md",
    )
    parser.add_argument(
        "--examples",
        type=int,
        default=5,
        metavar="N",
        help="Max examples per block in the summary table (default: 5)",
    )
    parser.add_argument(
        "--detail-top",
        type=int,
        default=3,
        metavar="N",
        help="Number of top blocks for the detail section (default: 3)",
    )
    parser.add_argument(
        "--detail-examples",
        type=int,
        default=8,
        metavar="N",
        help="Examples per block in the detail section (default: 8)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv)
    if not tsv_path.is_file():
        sys.exit(f"Input file not found: {tsv_path}")

    if args.out:
        out_path = Path(args.out)
    else:
        out_path = tsv_path.with_name(tsv_path.stem + "_集計.md")

    rows = read_tsv(tsv_path)
    report = build_markdown(
        rows,
        tsv_path,
        examples_per_block=args.examples,
        detail_top=args.detail_top,
        detail_examples=args.detail_examples,
    )
    out_path.write_text(report, encoding="utf-8")

    n_blocks = len(aggregate_by_block(rows))
    print(f"Read {len(rows):,} rows from {tsv_path}")
    print(f"Wrote report ({n_blocks} blocks) to {out_path}")


if __name__ == "__main__":
    main()
