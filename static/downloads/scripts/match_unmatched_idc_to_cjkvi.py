#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unmatched_uniq_blocks_idc.tsv の IDS 見出しを CJKVI IDS データに照合する。

出力は、入力4列に CJKVI 側の Unicode 番号・文字・ファイル名を付加した TSV。
CJKVI 側で同じ IDS が複数ファイルに出る場合は、候補ごとに1行ずつ出力する。

使い方:
  python scripts/match_unmatched_idc_to_cjkvi.py \
    --input linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.tsv \
    --cjkvi-dir ../cjkvi-ids \
    --output linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.cjkvi_encoded.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


INPUT_COLUMNS = ["資料番号", "単字_見出し", "16進Unicode番号", "ブロック"]
OUTPUT_COLUMNS = INPUT_COLUMNS + ["cjkv-hex", "cjkv-char", "cjkv-file-name"]
UCS_LINE_RE = re.compile(r"^U\+")
IDS_VARIANT_NOTE_RE = re.compile(r"\[[^]]+\]$")


def normalize_ids(value: str) -> str:
    """CJKVI IDS 末尾の [G] [J] [GTKV] などの字形注記を外して比較する。"""
    return IDS_VARIANT_NOTE_RE.sub("", value)


def load_cjkvi_matches(cjkvi_dir: Path) -> dict[str, list[tuple[str, str, str]]]:
    matches: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for path in sorted(cjkvi_dir.glob("*.txt")):
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh, delimiter="\t")
            for row in reader:
                if len(row) < 3 or not UCS_LINE_RE.match(row[0]):
                    continue

                cjkv_hex = row[0]
                cjkv_char = row[1]
                for ids in row[2:]:
                    ids_key = normalize_ids(ids)
                    if ids_key:
                        matches[ids_key].append((cjkv_hex, cjkv_char, path.name))

    return matches


def iter_input_rows(input_path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    with input_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        for row in reader:
            if not row:
                continue
            padded = row + [""] * (len(INPUT_COLUMNS) - len(row))
            rows.append(dict(zip(INPUT_COLUMNS, padded[: len(INPUT_COLUMNS)])))

    return rows


def write_matched_rows(
    input_rows: list[dict[str, str]],
    cjkvi_matches: dict[str, list[tuple[str, str, str]]],
    output_path: Path,
) -> int:
    written = 0

    with output_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS, delimiter="\t")
        writer.writeheader()

        for input_row in input_rows:
            ids_key = input_row["単字_見出し"]
            for cjkv_hex, cjkv_char, file_name in cjkvi_matches.get(ids_key, []):
                writer.writerow(
                    {
                        **input_row,
                        "cjkv-hex": cjkv_hex,
                        "cjkv-char": cjkv_char,
                        "cjkv-file-name": file_name,
                    }
                )
                written += 1

    return written


def main() -> None:
    parser = argparse.ArgumentParser(
        description="unmatched_uniq_blocks_idc.tsv の IDS を CJKVI IDS データに照合する"
    )
    parser.add_argument(
        "--input",
        default="linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.tsv",
        help="入力TSV。デフォルト: linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.tsv",
    )
    parser.add_argument(
        "--cjkvi-dir",
        default="../cjkvi-ids",
        help="CJKVI IDS ディレクトリ。デフォルト: ../cjkvi-ids",
    )
    parser.add_argument(
        "--output",
        default="linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.cjkvi_encoded.tsv",
        help="出力TSV。デフォルト: linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc.cjkvi_encoded.tsv",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    cjkvi_dir = Path(args.cjkvi_dir)
    output_path = Path(args.output)

    if not input_path.is_file():
        raise SystemExit(f"入力ファイルが見つかりません: {input_path}")
    if not cjkvi_dir.is_dir():
        raise SystemExit(f"CJKVI IDS ディレクトリが見つかりません: {cjkvi_dir}")

    input_rows = iter_input_rows(input_path)
    cjkvi_matches = load_cjkvi_matches(cjkvi_dir)
    written = write_matched_rows(input_rows, cjkvi_matches, output_path)

    print(f"input rows: {len(input_rows)}")
    print(f"matched output rows: {written}")
    print(f"output: {output_path}")


if __name__ == "__main__":
    main()
