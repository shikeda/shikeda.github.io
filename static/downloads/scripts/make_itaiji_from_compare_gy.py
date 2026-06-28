#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compare_gy/char_mismatch_report.tsv から
gy_dhsjr_link.py --itaiji-json 用の JSON ペアリストを生成する。

入力  : ../compare_gy/char_mismatch_report.tsv  (デフォルト)
出力  : itaiji_gy_compare.json                  (デフォルト)

分類ごとの処理:
  単純な字体差    : 廣韻_字頭・sbgy_字頭 が各1文字の場合のみ採用
  表記法の違いのみ : sbgy_字頭（本字）と sbgy_rewrite_word（異体字）のペアを採用
  本字部分も不一致 : デフォルトでスキップ。--include-uncertain で採用

実行例:
  python make_itaiji_from_compare_gy.py
  python make_itaiji_from_compare_gy.py --only-simple --out itaiji_gy_simple.json
  python make_itaiji_from_compare_gy.py --include-uncertain --out itaiji_gy_all.json
"""

import argparse
import csv
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DEFAULT_INPUT = SCRIPT_DIR.parent / "compare_gy" / "char_mismatch_report.tsv"
DEFAULT_OUTPUT = SCRIPT_DIR / "itaiji_gy_compare.json"

CAT_SIMPLE = "単純な字体差（コードポイント相違）"
CAT_NOTATION = "表記法の違いのみ（実質同一: 廣韻が本字〈異体字〉併記）"
CAT_UNCERTAIN = "本字部分も不一致（要確認）"


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--input", default=str(DEFAULT_INPUT),
        help=f"char_mismatch_report.tsv のパス (デフォルト: {DEFAULT_INPUT})",
    )
    ap.add_argument(
        "--out", default=str(DEFAULT_OUTPUT),
        help=f"出力 JSON のパス (デフォルト: {DEFAULT_OUTPUT})",
    )
    ap.add_argument(
        "--include-uncertain", action="store_true",
        help="本字部分も不一致 の行も含める（要確認分）",
    )
    ap.add_argument(
        "--only-simple", action="store_true",
        help="単純な字体差 のみ。表記法の違いのみ（sbgy rewrite）を除外する",
    )
    args = ap.parse_args()

    pairs = []
    counts = {CAT_SIMPLE: 0, CAT_NOTATION: 0, CAT_UNCERTAIN: 0}
    skipped = 0

    with open(args.input, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            cat = row["分類"]
            gy_char = row["廣韻_字頭"]
            sb_char = row["sbgy_字頭"]
            rewrite = row.get("sbgy_rewrite_word", "")

            if cat == CAT_SIMPLE:
                # 廣韻_字頭・sbgy_字頭 がいずれも単一文字の場合のみ採用
                # （｛...｝ や IDS 表記、補字 ［...］ は除外される）
                if len(gy_char) == 1 and len(sb_char) == 1 and gy_char != sb_char:
                    pairs.append({"c1": gy_char, "c2": sb_char})
                    counts[CAT_SIMPLE] += 1
                else:
                    skipped += 1

            elif cat == CAT_NOTATION and not args.only_simple:
                # sbgy_字頭（本字）と sbgy_rewrite_word（異体字）のペア
                # 廣韻_字頭 は「本字〈異体字〉」形式なので sbgy 側から取得する
                if len(sb_char) == 1 and len(rewrite) == 1 and sb_char != rewrite:
                    pairs.append({"c1": sb_char, "c2": rewrite})
                    counts[CAT_NOTATION] += 1
                else:
                    skipped += 1

            elif cat == CAT_UNCERTAIN and args.include_uncertain:
                if len(gy_char) == 1 and len(sb_char) == 1 and gy_char != sb_char:
                    pairs.append({"c1": gy_char, "c2": sb_char})
                    counts[CAT_UNCERTAIN] += 1
                else:
                    skipped += 1

            else:
                skipped += 1

    out_path = Path(args.out)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pairs, f, ensure_ascii=False, indent=2)

    total = sum(counts.values())
    print(f"出力: {out_path}  ({total} ペア)")
    print(f"  単純な字体差         : {counts[CAT_SIMPLE]} ペア")
    print(f"  表記法の違いのみ      : {counts[CAT_NOTATION]} ペア")
    print(f"  本字部分も不一致      : {counts[CAT_UNCERTAIN]} ペア")
    print(f"  スキップ             : {skipped} 行")


if __name__ == "__main__":
    main()
