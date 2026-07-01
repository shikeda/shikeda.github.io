#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DHSJR 個別 TSV 内の IDS 表記を、対応する符号化済み Unicode 文字へ置換する。

変換表は unmatched_uniq_blocks_idc_with_ucs.tsv のような TSV を想定する。
同じ「資料番号 + 単字_見出し」に複数の異なる置換先がある場合は、自動置換せず
conflicts レポートへ出す。同じ置換先が ids.txt / ids-cdp.txt 由来で重複する場合は
1件にまとめる。

デフォルトは dry-run。実際に書き換えるには --apply を付ける。

例:
  python3 scripts/apply_idc_ucs_replacements.py \
    --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
    --data-dir /home/ikeda/Hdic_data/DHSJR/data \
    --dry-run

  python3 scripts/apply_idc_ucs_replacements.py \
    --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
    --data-dir /home/ikeda/Hdic_data/DHSJR/data \
    --backup-dir /home/ikeda/Hdic_data/DHSJR/data_backup_before_idc_ucs_20260701 \
    --apply
"""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


RESOURCE_COL = "資料番号"
IDS_COL = "単字_見出し"
DEFAULT_TARGET_COLUMNS = ["単字_見出し", "単字_出現形", "漢語_見出し", "漢語_出現形"]
CHAR_COLUMN_CANDIDATES = [
    "cjkv-char",
    "cjkv_char",
    "ucs-char",
    "ucs_char",
    "UCS文字",
    "Unicode文字",
    "符号化文字",
]
HEADERLESS_MAP_COLUMNS = [RESOURCE_COL, IDS_COL, "ucs-hex", "ucs-char"]


@dataclass(frozen=True)
class Replacement:
    resource_id: str
    source: str
    target: str


@dataclass
class MapLoadResult:
    replacements: dict[tuple[str, str], str]
    conflicts: dict[tuple[str, str], set[str]]
    duplicate_rows: int
    usable_rows: int


def die(message: str) -> None:
    raise SystemExit(message)


def pick_char_column(fieldnames: list[str] | None, requested: str | None) -> str:
    if not fieldnames:
        die("変換表のヘッダ行を読めませんでした。")

    if requested:
        if requested not in fieldnames:
            die(f"指定された置換先列が見つかりません: {requested}")
        return requested

    for candidate in CHAR_COLUMN_CANDIDATES:
        if candidate in fieldnames:
            return candidate

    die(
        "置換先文字の列が見つかりません。"
        f" 候補: {', '.join(CHAR_COLUMN_CANDIDATES)}"
        "。必要なら --char-col で指定してください。"
    )


def has_header(first_row: list[str]) -> bool:
    return RESOURCE_COL in first_row and IDS_COL in first_row


def load_replacement_map(map_path: Path, char_col: str | None) -> MapLoadResult:
    raw: dict[tuple[str, str], set[str]] = defaultdict(set)
    duplicate_rows = 0
    usable_rows = 0

    with map_path.open("r", encoding="utf-8-sig", newline="") as fh:
        sample_reader = csv.reader(fh, delimiter="\t")
        try:
            first_row = next(sample_reader)
        except StopIteration:
            die(f"変換表が空です: {map_path}")

        fh.seek(0)
        if has_header(first_row):
            reader = csv.DictReader(fh, delimiter="\t")
            actual_char_col = pick_char_column(reader.fieldnames, char_col)

            missing = [name for name in [RESOURCE_COL, IDS_COL] if name not in (reader.fieldnames or [])]
            if missing:
                die(f"変換表に必要な列がありません: {', '.join(missing)}")
        else:
            if char_col and char_col != "ucs-char":
                die(
                    "ヘッダなし変換表では --char-col は ucs-char のみ指定できます。"
                    "4列目を置換先文字として扱います。"
                )
            reader = csv.DictReader(fh, fieldnames=HEADERLESS_MAP_COLUMNS, delimiter="\t")
            actual_char_col = "ucs-char"

        seen_rows: set[tuple[str, str, str]] = set()
        for row in reader:
            resource_id = (row.get(RESOURCE_COL) or "").strip()
            source = (row.get(IDS_COL) or "").strip()
            target = (row.get(actual_char_col) or "").strip()
            if not resource_id or not source or not target:
                continue

            row_key = (resource_id, source, target)
            if row_key in seen_rows:
                duplicate_rows += 1
            seen_rows.add(row_key)
            raw[(resource_id, source)].add(target)

    replacements: dict[tuple[str, str], str] = {}
    conflicts: dict[tuple[str, str], set[str]] = {}
    for key, targets in raw.items():
        if len(targets) == 1:
            replacements[key] = next(iter(targets))
            usable_rows += 1
        else:
            conflicts[key] = targets

    return MapLoadResult(
        replacements=replacements,
        conflicts=conflicts,
        duplicate_rows=duplicate_rows,
        usable_rows=usable_rows,
    )


def group_replacements(
    replacements: dict[tuple[str, str], str]
) -> dict[str, list[Replacement]]:
    grouped: dict[str, list[Replacement]] = defaultdict(list)
    for (resource_id, source), target in replacements.items():
        grouped[resource_id].append(Replacement(resource_id, source, target))

    for resource_id in grouped:
        grouped[resource_id].sort(key=lambda item: len(item.source), reverse=True)

    return grouped


def expand_with_brackets(
    grouped: dict[str, list[Replacement]]
) -> dict[str, list[Replacement]]:
    """[IDS] / 【IDS】 を、括弧ごと UCS 文字へ置換する候補として追加する。"""
    expanded: dict[str, list[Replacement]] = {}

    for resource_id, replacements in grouped.items():
        items: list[Replacement] = []
        for replacement in replacements:
            items.append(
                Replacement(
                    replacement.resource_id,
                    f"[{replacement.source}]",
                    replacement.target,
                )
            )
            items.append(
                Replacement(
                    replacement.resource_id,
                    f"【{replacement.source}】",
                    replacement.target,
                )
            )
            items.append(replacement)

        items.sort(key=lambda item: len(item.source), reverse=True)
        expanded[resource_id] = items

    return expanded


def replace_row_values(
    row: dict[str, str],
    replacements: list[Replacement],
    target_columns: list[str],
) -> tuple[dict[str, str], Counter[tuple[str, str]]]:
    counts: Counter[tuple[str, str]] = Counter()
    updated = dict(row)

    for column in target_columns:
        value = updated.get(column)
        if not value:
            continue

        for replacement in replacements:
            n = value.count(replacement.source)
            if n:
                value = value.replace(replacement.source, replacement.target)
                counts[(replacement.source, replacement.target)] += n

        updated[column] = value

    return updated, counts


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if not reader.fieldnames:
            return [], []
        return reader.fieldnames, list(reader)


def write_tsv_atomic(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as tmp:
        tmp_path = Path(tmp.name)
        writer = csv.DictWriter(
            tmp,
            fieldnames=fieldnames,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    tmp_path.replace(path)


def write_conflict_report(
    conflicts: dict[tuple[str, str], set[str]],
    path: Path | None,
) -> None:
    if not path or not conflicts:
        return

    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow([RESOURCE_COL, IDS_COL, "candidate_chars"])
        for (resource_id, source), targets in sorted(conflicts.items()):
            writer.writerow([resource_id, source, ",".join(sorted(targets))])


def apply_replacements(
    data_dir: Path,
    grouped: dict[str, list[Replacement]],
    target_columns: list[str],
    apply: bool,
    backup_dir: Path | None,
    sample_limit: int,
) -> tuple[int, int, Counter[tuple[str, str, str]]]:
    changed_files = 0
    changed_rows = 0
    total_counts: Counter[tuple[str, str, str]] = Counter()
    samples: list[str] = []

    for path in sorted(data_dir.glob("*.tsv")):
        fieldnames, rows = read_tsv(path)
        if not fieldnames or RESOURCE_COL not in fieldnames:
            continue

        present_target_columns = [col for col in target_columns if col in fieldnames]
        if not present_target_columns:
            continue

        new_rows: list[dict[str, str]] = []
        file_changed = False
        file_changed_rows = 0
        file_counts: Counter[tuple[str, str, str]] = Counter()

        for index, row in enumerate(rows, start=2):
            resource_id = row.get(RESOURCE_COL, "")
            replacements = grouped.get(resource_id)
            if not replacements:
                new_rows.append(row)
                continue

            updated, counts = replace_row_values(row, replacements, present_target_columns)
            if counts:
                file_changed = True
                file_changed_rows += 1
                for (source, target), count in counts.items():
                    file_counts[(resource_id, source, target)] += count
                    if len(samples) < sample_limit:
                        samples.append(
                            f"{path.name}:{index}\t{resource_id}\t{source} -> {target}\t{count}"
                        )
            new_rows.append(updated)

        if not file_changed:
            continue

        changed_files += 1
        changed_rows += file_changed_rows
        total_counts.update(file_counts)

        print(f"{path.name}: changed rows={file_changed_rows}, replacements={sum(file_counts.values())}")

        if apply:
            if backup_dir:
                backup_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, backup_dir / path.name)
            write_tsv_atomic(path, fieldnames, new_rows)

    if samples:
        print("\nexamples:")
        for sample in samples:
            print(sample)

    return changed_files, changed_rows, total_counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DHSJR 個別 TSV の IDS 表記を UCS 文字へ一括置換する"
    )
    parser.add_argument(
        "--map",
        required=True,
        dest="map_path",
        help="IDS -> UCS 変換表 TSV",
    )
    parser.add_argument(
        "--data-dir",
        required=True,
        help="DHSJR 個別 TSV があるディレクトリ",
    )
    parser.add_argument(
        "--target-cols",
        default=",".join(DEFAULT_TARGET_COLUMNS),
        help="置換対象列。カンマ区切り。デフォルト: "
        + ",".join(DEFAULT_TARGET_COLUMNS),
    )
    parser.add_argument(
        "--char-col",
        help="変換表内の置換先文字列。省略時は cjkv-char 等を自動検出",
    )
    parser.add_argument(
        "--backup-dir",
        help="--apply 時のバックアップ先。省略時は data-dir の隣に自動作成",
    )
    parser.add_argument(
        "--conflicts-out",
        default="idc_ucs_replacement_conflicts.tsv",
        help="衝突候補レポートの出力先。デフォルト: idc_ucs_replacement_conflicts.tsv",
    )
    parser.add_argument(
        "--sample-limit",
        type=int,
        default=20,
        help="画面に表示する変更例の最大件数。デフォルト: 20",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="実際に TSV を書き換える。指定しない場合は dry-run",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="書き換えずに変更予定だけ確認する。明示用オプション",
    )
    args = parser.parse_args()

    map_path = Path(args.map_path)
    data_dir = Path(args.data_dir)
    if not map_path.is_file():
        die(f"変換表が見つかりません: {map_path}")
    if not data_dir.is_dir():
        die(f"DHSJR data ディレクトリが見つかりません: {data_dir}")

    target_columns = [col for col in args.target_cols.split(",") if col]
    if not target_columns:
        die("--target-cols が空です。")

    backup_dir: Path | None = None
    if args.apply:
        if args.backup_dir:
            backup_dir = Path(args.backup_dir)
        else:
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = data_dir.parent / f"{data_dir.name}_backup_before_idc_ucs_{stamp}"

    result = load_replacement_map(map_path, args.char_col)
    grouped = group_replacements(result.replacements)
    grouped = expand_with_brackets(grouped)

    conflicts_out = Path(args.conflicts_out) if args.conflicts_out else None
    write_conflict_report(result.conflicts, conflicts_out)

    print(f"mode: {'apply' if args.apply else 'dry-run'}")
    print(f"map usable entries: {result.usable_rows}")
    print(f"map duplicate rows ignored: {result.duplicate_rows}")
    print(f"map conflicts skipped: {len(result.conflicts)}")
    if conflicts_out and result.conflicts:
        print(f"conflicts report: {conflicts_out}")
    if args.apply and backup_dir:
        print(f"backup dir: {backup_dir}")
    print(f"target columns: {', '.join(target_columns)}")
    print()

    changed_files, changed_rows, total_counts = apply_replacements(
        data_dir=data_dir,
        grouped=grouped,
        target_columns=target_columns,
        apply=args.apply,
        backup_dir=backup_dir,
        sample_limit=args.sample_limit,
    )

    print("\nsummary:")
    print(f"changed files: {changed_files}")
    print(f"changed rows: {changed_rows}")
    print(f"replacement occurrences: {sum(total_counts.values())}")

    if not args.apply:
        print("\nThis was a dry-run. Add --apply to write changes.")

    if result.conflicts:
        print(
            "\nSome mappings were skipped because one IDS had multiple replacement chars. "
            "Review the conflicts report before applying those manually.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
