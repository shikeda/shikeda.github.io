#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集韻(jiyun, ~/codex/jy/vol{N}/jiyun_juan{N}_groups.tsv) の headword_run から
異体字ペアを抽出し、gy_dhsjr_link.py の --itaiji-json 形式
（[{"c1": ..., "c2": ...}, ...]）で書き出す。

背景: 集韻の1小韻内で、1つの見出し語に複数の字体がある場合は定義を繰り返さず
headword_run に複数文字を連続して並べ、末尾の note に1つだけ語釈（+しばしば
「或作」「亦作」「籒作」等の異体字を示す言い回し）を付ける。したがって
headword_run（先頭の〇マーカーを除く）が2文字以上の group は、その文字群が
すべて同一語の異体字であることを強く示唆する。

方針:
  - 僻字プレースホルダ（⟦ctextchar:N⟧）と OCR不明字（●）は、廣韻.csv の実字と
    突き合わせようがないので候補から除外する。
  - gy_dhsjr_link.py の build_itaiji_map() は JSON 内の各 {c1,c2} ペアを独立
    した2字グループとして扱う（推移的な合流はしない）ため、3字以上の異体字
    セットを「先頭字とだけペアにする」形式で出すと、先頭字が廣韻未収録の場合
    に他の字が救えないことがある。これを避けるため、セット内の全組み合わせ
    （C(n,2)）をペアとして出力する。
  - 巻末の余剰OCRテキスト（上奏文等）が note なしの1グループとして誤混入する
    ケースがあるため、文字数が --max-group-size を超える group は除外する。

使い方:
  python3 scripts/extract_itaiji_from_jiyun.py \
    --jiyun-glob "../../jy/vol*/jiyun_juan*_groups.tsv" \
    --output ../jy_itaiji_pairs.json
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import re
from itertools import combinations
from pathlib import Path

TOKEN_RE = re.compile(r'⟦[^⟧]+⟧|.')


def is_usable(tok: str) -> bool:
    # '〇' は小韻先頭のマーカーとして strip 済みのはずだが、まれに武則天造字など
    # 印刷不能な字の代用として本文中にも現れる（例:「唐武后作〇」）。実字ではない
    # ので候補から除外する。
    return not tok.startswith('⟦') and tok not in ('●', '〇') and not tok.isspace()


# 巻頭・巻末の書誌情報（校訂官氏名列記など）が section 見出しの狭間で category
# 'entry' のまま紛れ込むケース向けの除外ルール。実データ精査で確認済み:
#   - note が空: 「集韻卷四」のような巻末表示、氏名のみの行（何均・沈希曾等）
#   - note が「臣」1文字: 「侍朝校對官中書」等、官職名の後に氏名が続く列記の定型句
#   - headword_run に「缺字」を含む: OCR編集時の「●缺字：〇」という注記で、
#     異体字の列記ではない
BOILERPLATE_NOTE_VALUES = {'', '臣'}


def is_boilerplate(headword_run: str, note: str) -> bool:
    if note.strip() in BOILERPLATE_NOTE_VALUES:
        return True
    if '缺字' in headword_run:
        return True
    return False


def extract_pairs(pattern: str, max_group_size: int) -> tuple[set[tuple[str, str]], dict[str, int]]:
    paths = sorted(glob.glob(pattern))
    if not paths:
        raise SystemExit(f"jiyun groups.tsv が見つかりません: {pattern}")

    pairs: set[tuple[str, str]] = set()
    stats = {
        'groups_scanned': 0,
        'multi_char_groups': 0,
        'excluded_oversized_groups': 0,
        'excluded_boilerplate_groups': 0,
        'pairs_before_dedupe': 0,
    }

    for path in paths:
        with open(path, encoding='utf-8', newline='') as fh:
            reader = csv.DictReader(fh, delimiter='\t')
            for row in reader:
                if row.get('category') != 'entry':
                    continue
                hw = row.get('headword_run', '')
                if hw.startswith('〇'):
                    hw = hw[1:]
                if not hw:
                    continue
                stats['groups_scanned'] += 1

                tokens = [t for t in TOKEN_RE.findall(hw) if is_usable(t)]
                if len(tokens) < 2:
                    continue
                stats['multi_char_groups'] += 1

                if is_boilerplate(hw, row.get('note', '')):
                    stats['excluded_boilerplate_groups'] += 1
                    continue
                if len(tokens) > max_group_size:
                    stats['excluded_oversized_groups'] += 1
                    continue

                for a, b in combinations(tokens, 2):
                    # c1/c2 の向きに意味はないので正規化してから重複除去する
                    # （同じ異体字集合が別の小韻で逆順に現れることがある）
                    pairs.add(tuple(sorted((a, b))))
                    stats['pairs_before_dedupe'] += 1

    return pairs, stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--jiyun-glob', default='../../jy/vol*/jiyun_juan*_groups.tsv',
                     help='jiyun_juan{N}_groups.tsv を集めるglobパターン')
    ap.add_argument('--output', type=Path, default=Path('../jy_itaiji_pairs.json'))
    ap.add_argument('--max-group-size', type=int, default=12,
                     help='headword_run の文字数上限。超えるgroupは巻末混入等とみなして除外')
    args = ap.parse_args()

    pairs, stats = extract_pairs(args.jiyun_glob, args.max_group_size)

    result = [{"c1": c1, "c2": c2} for c1, c2 in sorted(pairs)]
    with args.output.open('w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"groups scanned (category=entry): {stats['groups_scanned']}")
    print(f"multi-char headword_run groups (candidate itaiji sets): {stats['multi_char_groups']}")
    print(f"  excluded as boilerplate (colophon/OCR-note, not real itaiji): "
          f"{stats['excluded_boilerplate_groups']}")
    print(f"  excluded as oversized (> {args.max_group_size} chars, likely OCR contamination): "
          f"{stats['excluded_oversized_groups']}")
    print(f"pairs before dedupe: {stats['pairs_before_dedupe']}")
    print(f"distinct pairs written: {len(result)}")
    print(f"wrote: {args.output}")


if __name__ == '__main__':
    main()
