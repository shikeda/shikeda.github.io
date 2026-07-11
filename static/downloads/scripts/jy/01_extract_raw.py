#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse a ctext.org 集韻 (Jiyun) saved HTML page into an ordered segment
stream per row (same approach as ~/codex/gls/scripts/01_extract_raw.py).

Input:  ../ctext/jiyun_vol{N}_ctextext.html
Output: ../vol{N}/jiyun_juan{N}_raw.json

Difference from the gls version: rare-character images (<img
alt="ctextchar:NNNN">) can appear *nested inside* an inlinecomment note span
here (集韻's small-韻 definitions embed variant glyphs mid-sentence), not only
as a standalone headword. So text is rendered with a recursive walker that
substitutes any such <img> for a ⟦ctextchar:NNNN⟧ placeholder wherever it
occurs, instead of only handling it as a direct child of <td>.
"""
import re
import json
import sys
import argparse
from pathlib import Path
from lxml import html

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "ctext"


def render_text(node):
    """Recursively render a node's text content, inlining rare-char images
    as ⟦ctextchar:NNNN⟧ wherever they appear in the subtree."""
    parts = []
    if node.text:
        parts.append(node.text)
    for child in node:
        if child.tag == 'img':
            alt = child.get('alt') or ''
            if alt.startswith('ctextchar:'):
                parts.append(f'⟦{alt}⟧')
        else:
            parts.append(render_text(child))
        if child.tail:
            parts.append(child.tail)
    return ''.join(parts)


def walk_ctext_td(td):
    """Return ordered segments: ('char', text) / ('note', text) / ('anchor', id)."""
    segs = []

    def emit_text(t):
        if t:
            segs.append(('char', t))

    emit_text(td.text)
    for child in td:
        tag = child.tag
        cls = child.get('class') or ''
        if tag == 'span' and 'inlinecomment' in cls:
            segs.append(('note', render_text(child)))
        elif tag == 'span' and 'libtarget' in cls:
            segs.append(('anchor', child.get('id')))
        else:
            t = render_text(child)
            if t:
                segs.append(('char', t))
        emit_text(child.tail)
    return segs


def extract_volume(vol: int) -> None:
    src = SRC_DIR / f"jiyun_vol{vol}_ctextext.html"
    out_dir = ROOT / f"vol{vol}"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"jiyun_juan{vol}_raw.json"

    raw = src.read_text(encoding="utf-8", errors="replace")
    doc = html.fromstring(raw)
    tables = doc.xpath('//table')
    table = max(tables, key=lambda t: len(t.xpath('.//tr')))
    rows = table.xpath('.//tr')
    print(f"[vol{vol}] rows: {len(rows)}", file=sys.stderr)

    records = []
    section = None
    section_id = None

    for tr in rows:
        tds = tr.xpath('./td')
        if len(tds) == 1 and tds[0].get('colspan'):
            h2 = tds[0].xpath('.//h2')
            if h2:
                section = ''.join(h2[0].itertext()).strip()
                section_id = h2[0].get('id')
            continue
        if len(tds) < 2:
            continue
        row_id = tr.get('id')
        first_td, ctext_td = tds[0], tds[1]
        if 'ctext' not in (ctext_td.get('class') or ''):
            continue

        page_no_m = re.match(r'\s*(\d+)', first_td.text or '')
        page_no = page_no_m.group(1) if page_no_m else None
        lib_page = None
        m = re.search(r'page=(\d+)', html.tostring(first_td, encoding='unicode'))
        if m:
            lib_page = m.group(1)

        segs = walk_ctext_td(ctext_td)
        records.append({
            'row_id': row_id,
            'section': section,
            'section_id': section_id,
            'page_no_in_row': page_no,
            'scan_page': lib_page,
            'segments': segs,
        })

    out.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[vol{vol}] records: {len(records)}  wrote: {out}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--volume', type=int, help='single volume number (1-10)')
    ap.add_argument('--all', action='store_true', help='process all 10 volumes')
    args = ap.parse_args()

    if args.all:
        for v in range(1, 11):
            extract_volume(v)
    elif args.volume:
        extract_volume(args.volume)
    else:
        ap.error('specify --volume N or --all')


if __name__ == '__main__':
    main()
