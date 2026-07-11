#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sanity-check each 小韻 (homophone/variant-graph group) in jiyun_juan{N}_groups.tsv:
the first entry of a group (marked by a leading '〇') declares a character
count like "文二十五" (25 chars in this group, e.g. 一東's 〇東 entry). Recount
the characters actually OCR'd in that group and flag mismatches -- these are
either OCR errors (missing/extra/garbled characters) or numeral-OCR errors in
the count itself (e.g. '十' dropped).

Output: ../vol{N}/jiyun_juan{N}_xiaoyun_check.tsv
"""
import csv
import re
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_volume(vol: int):
    vol_dir = ROOT / f"vol{vol}"
    path = vol_dir / f"jiyun_juan{vol}_groups.tsv"
    rows = list(csv.DictReader(path.open(encoding='utf-8'), delimiter='\t'))
    entry_rows = [r for r in rows if r['category'] == 'entry']

    results = []

    # walk grouped by (tone, yun_no, yun_name, xiaoyun_seq)
    groups = {}
    order = []
    for r in entry_rows:
        if not r['xiaoyun_seq']:
            continue
        key = (r['tone'], r['yun_no'], r['yun_name'], r['xiaoyun_seq'])
        if key not in groups:
            groups[key] = {'declared_count': None, 'char_total': 0,
                           'headwords': [], 'row_id_first': r['row_id']}
            order.append(key)
        g = groups[key]
        if r['is_group_marker'] == '1':
            g['declared_count'] = r['declared_count']
        tokens = re.findall(r'⟦[^⟧]+⟧|.', r['headword_run'])
        # '〇' only marks the start of a new 小韻 group; it is not itself one
        # of the counted headword characters.
        g['char_total'] += sum(1 for t in tokens if t != '〇')
        g['headwords'].append(r['headword_run'])

    for key in order:
        tone, yun_no, yun_name, seq = key
        g = groups[key]
        declared = g['declared_count']
        actual = g['char_total']
        status = 'no_count_declared'
        if declared not in (None, ''):
            declared_int = int(declared)
            status = 'match' if declared_int == actual else 'mismatch'
        results.append({
            'tone': tone, 'yun_no': yun_no, 'yun_name': yun_name,
            'xiaoyun_seq': seq, 'declared_count': declared or '',
            'actual_char_count': actual, 'status': status,
            'headwords': ''.join(g['headwords'])[:60],
            'row_id_first': g['row_id_first'],
        })

    out_path = vol_dir / f"jiyun_juan{vol}_xiaoyun_check.tsv"
    fields = ['tone', 'yun_no', 'yun_name', 'xiaoyun_seq', 'declared_count',
              'actual_char_count', 'status', 'headwords', 'row_id_first']
    with out_path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        w.writeheader()
        for r in results:
            w.writerow(r)

    n_match = sum(1 for r in results if r['status'] == 'match')
    n_mismatch = sum(1 for r in results if r['status'] == 'mismatch')
    n_nodecl = sum(1 for r in results if r['status'] == 'no_count_declared')
    print(f"[vol{vol}] xiaoyun groups: {len(results)}  match={n_match} "
          f"mismatch={n_mismatch} no_count_declared={n_nodecl}  wrote: {out_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--volume', type=int)
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()
    if args.all:
        for v in range(1, 11):
            check_volume(v)
    elif args.volume:
        check_volume(args.volume)
    else:
        ap.error('specify --volume N or --all')


if __name__ == '__main__':
    main()
