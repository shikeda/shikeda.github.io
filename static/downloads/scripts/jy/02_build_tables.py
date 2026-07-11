#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flatten jiyun_juan{N}_raw.json into TSVs for cross-checking against other
character-level resources (itaiji_*.json, DHSJR/SBGY, krm_notes.tsv, ...).

Input:  ../vol{N}/jiyun_juan{N}_raw.json
Output: ../vol{N}/jiyun_juan{N}_groups.tsv   (headword-run + trailing note)
        ../vol{N}/jiyun_juan{N}_chars.tsv   (one row per character)
        ../vol{N}/jiyun_juan{N}_toc.tsv     (tone-volume 韻目 index, e.g. "平聲一")

集韻 differs from 龍龕手鑑 in structure:
- sections are two-level: a tone-volume header ("平聲一","上聲上",...) whose
  body is just a 韻目 index (韻名+反切+独用/通用), followed by per-韻 headers
  ("一東","二冬",...) whose body is the actual dictionary entries.
- within a 韻's entries, each 小韻 (homophone/variant-graph group) starts with
  a '〇' marker character glued to the first headword, and that headword's
  note ends with a count assertion like "文二十五" (25 characters in this
  small-韻 group, including itself). This is captured via is_group_marker /
  xiaoyun_seq / declared_count so 03_check_xiaoyun_counts.py can verify it.
"""
import re
import json
import csv
from pathlib import Path

from cn_numerals import cn2num

ROOT = Path(__file__).resolve().parent.parent

TONE_RE = re.compile(r'^(平聲|上聲|去聲|入聲)(.+)$')
YUN_RE = re.compile(r'^([一二三四五六七八九十百]+)(.+)$')
FRONT_MATTER_SECTIONS = {'提要', '韻例'}
COUNT_RE = re.compile(r'文([一二三四五六七八九十百0-9]+)$')


def classify_section(section_raw):
    """Return (category, tone, yun_no, yun_name) for a raw '《...》' section title."""
    if not section_raw:
        return 'none', None, None, None
    sec = section_raw.strip('《》')
    if sec in FRONT_MATTER_SECTIONS:
        return 'front_matter', None, None, None
    m = TONE_RE.match(sec)
    if m:
        return 'toc', sec, None, None
    m = YUN_RE.match(sec)
    if m:
        return 'entry', None, m.group(1), m.group(2)
    return 'entry', None, None, sec


def merge_segments(segs):
    merged = []
    for kind, text in segs:
        if kind == 'anchor':
            continue
        if merged and merged[-1][0] == kind:
            merged[-1] = (kind, merged[-1][1] + text)
        else:
            merged.append((kind, text))
    return merged


def build_volume(vol: int) -> None:
    vol_dir = ROOT / f"vol{vol}"
    raw_path = vol_dir / f"jiyun_juan{vol}_raw.json"
    data = json.loads(raw_path.read_text(encoding="utf-8"))

    group_rows, char_rows, toc_rows = [], [], []
    group_id_counter = 0
    current_tone = None
    xiaoyun_seq_by_yun = {}

    for r in data:
        section_raw = r['section']
        category, tone_from_header, yun_no, yun_name = classify_section(section_raw)
        if tone_from_header:
            current_tone = tone_from_header
        row_id = r['row_id']
        scan_page = r['scan_page']
        merged = merge_segments(r['segments'])

        yun_key = (current_tone, yun_no, yun_name)

        i, n = 0, len(merged)
        while i < n:
            kind, text = merged[i]
            if kind != 'char':
                # orphan note (rare): keep as a note-only group
                group_id_counter += 1
                group_rows.append({
                    'group_id': group_id_counter, 'category': category,
                    'tone': current_tone or '', 'yun_no': yun_no or '',
                    'yun_name': yun_name or '', 'section': section_raw or '',
                    'row_id': row_id, 'scan_page': scan_page or '',
                    'headword_run': '', 'note': text,
                    'is_group_marker': 0, 'xiaoyun_seq': '', 'declared_count': '',
                })
                i += 1
                continue

            headword_run = text
            note = None
            if i + 1 < n and merged[i + 1][0] == 'note':
                note = merged[i + 1][1]
                i += 2
            else:
                i += 1

            is_marker = int(headword_run.startswith('〇'))
            xiaoyun_seq = ''
            declared_count = ''
            if category == 'entry' and is_marker:
                xiaoyun_seq_by_yun[yun_key] = xiaoyun_seq_by_yun.get(yun_key, 0) + 1
                xiaoyun_seq = xiaoyun_seq_by_yun[yun_key]
                if note:
                    m = COUNT_RE.search(note)
                    if m:
                        declared_count = cn2num(m.group(1))
            elif category == 'entry':
                xiaoyun_seq = xiaoyun_seq_by_yun.get(yun_key, '')

            group_id_counter += 1
            gid = group_id_counter
            row_out = {
                'group_id': gid, 'category': category,
                'tone': current_tone or '', 'yun_no': yun_no or '',
                'yun_name': yun_name or '', 'section': section_raw or '',
                'row_id': row_id, 'scan_page': scan_page or '',
                'headword_run': headword_run, 'note': note or '',
                'is_group_marker': is_marker,
                'xiaoyun_seq': xiaoyun_seq,
                'declared_count': declared_count if declared_count is not None else '',
            }
            (toc_rows if category == 'toc' else group_rows).append(row_out)

            if category != 'toc':
                tokens = re.findall(r'⟦[^⟧]+⟧|.', headword_run)
                for idx, tok in enumerate(tokens):
                    is_rare = tok.startswith('⟦')
                    char_rows.append({
                        'group_id': gid, 'category': category,
                        'tone': current_tone or '', 'yun_no': yun_no or '',
                        'yun_name': yun_name or '', 'row_id': row_id,
                        'scan_page': scan_page or '',
                        'char_index_in_group': idx, 'group_size': len(tokens),
                        'char': tok, 'is_rare': int(is_rare),
                        'is_unrecognized_ocr': int(tok == '●'),
                        'is_group_marker_char': int(tok == '〇'),
                        'ctextchar_id': tok[1:-1] if is_rare else '',
                        'note': note or '', 'xiaoyun_seq': xiaoyun_seq,
                    })

    def write_tsv(path, rows, fields):
        with open(path, 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
            w.writeheader()
            for row in rows:
                w.writerow(row)

    group_fields = ['group_id', 'category', 'tone', 'yun_no', 'yun_name', 'section',
                     'row_id', 'scan_page', 'headword_run', 'note',
                     'is_group_marker', 'xiaoyun_seq', 'declared_count']
    char_fields = ['group_id', 'category', 'tone', 'yun_no', 'yun_name', 'row_id',
                   'scan_page', 'char_index_in_group', 'group_size', 'char',
                   'is_rare', 'is_unrecognized_ocr', 'is_group_marker_char',
                   'ctextchar_id', 'note', 'xiaoyun_seq']

    write_tsv(vol_dir / f"jiyun_juan{vol}_groups.tsv", group_rows, group_fields)
    write_tsv(vol_dir / f"jiyun_juan{vol}_chars.tsv", char_rows, char_fields)
    write_tsv(vol_dir / f"jiyun_juan{vol}_toc.tsv", toc_rows, group_fields)

    rare = sum(1 for c in char_rows if c['is_rare'])
    unrecog = sum(1 for c in char_rows if c['is_unrecognized_ocr'])
    print(f"[vol{vol}] groups={len(group_rows)} chars={len(char_rows)} "
          f"toc={len(toc_rows)} rare={rare} unrecognized={unrecog}")


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--volume', type=int)
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()
    if args.all:
        for v in range(1, 11):
            build_volume(v)
    elif args.volume:
        build_volume(args.volume)
    else:
        ap.error('specify --volume N or --all')


if __name__ == '__main__':
    main()
