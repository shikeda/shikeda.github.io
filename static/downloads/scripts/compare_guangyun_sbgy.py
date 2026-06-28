#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
廣韻.csv の 字頭 と sbgy.xml の word_head を
「韻目の出現順」→「韻内の字頭出現順」で対応付け、
同じ出現位置にあるはずなのにコードポイントが異なる文字を抽出する。

前提:
  - 廣韻.csv は 小韻號→小韻字號 の順で全行が出現順に並んでいる
  - sbgy.xml は volume → rhyme → word_head(id順) の順で出現する
  - 両ファイルとも「韻」の出現順は206個で一致するはず
    (catalogの目録部分ではなく、本文 rhyme 要素の出現順を使う)

出力:
  - 韻ごとの字数が一致しない場合 → mismatched_count_report.tsv
  - 字数が一致する韻の中で、同じ位置の文字が異なる場合
    → char_mismatch_report.tsv
"""

import csv
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

_SUPPL_JIGO_PAT = re.compile(r'^\d+a\d+$')  # 補字の小韻字號パターン (例: 1a1)

GY_CSV = "../廣韻.csv"
SBGY_XML = "../sbgy.xml"
OUT_DIR = Path("./")


def load_guangyun_groups(path):
    """廣韻.csv を 小韻號 の出現順にグループ化しつつ、
    韻目原貌が変わるタイミングで韻グループを切る。
    戻り値: [ {"yun": 韻目原貌, "chars": [(小韻號, 小韻字號, 字頭), ...]}, ... ]
    """
    groups = []
    current_yun = None
    current_group = None

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yun = row["韻目原貌"]
            char = row["字頭"]
            xh = row["小韻號"]
            zh = row["小韻字號"]
            if _SUPPL_JIGO_PAT.match(zh):  # 補字行 (1a1 等) は sbgy の added_word に相当するためスキップ
                continue
            if yun != current_yun:
                current_group = {"yun": yun, "chars": []}
                groups.append(current_group)
                current_yun = yun
            current_group["chars"].append((xh, zh, char))
    return groups


def load_sbgy_groups(path):
    """sbgy.xml を rhyme 要素の出現順にグループ化する。
    各 rhyme 内の word_head を id 順（=出現順そのまま）で取得する。
    戻り値: [ {"rhyme_id": ..., "chars": [(word_head_id, 字), ...]}, ... ]
    """
    # ElementTreeで読むには整形式チェックが必要。失敗したらregexで代替。
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        groups = []
        for rhyme in root.iter("rhyme"):
            rid = rhyme.get("id")
            chars = []
            for wh in rhyme.iter("word_head"):
                whid = wh.get("id")
                text = (wh.text or "").strip()
                rewrite = None
                if not text:
                    # original_word / rewrite_word パターン
                    ow = wh.find("original_word")
                    if ow is not None:
                        text = (ow.text or "").strip()
                        rw = ow.find("rewrite_word")
                        if rw is not None:
                            rewrite = (rw.text or "").strip()
                if not text:
                    continue
                head_char = text[0]
                chars.append((whid, head_char, rewrite))
            groups.append({"rhyme_id": rid, "chars": chars})
        return groups
    except ET.ParseError as e:
        raise SystemExit(f"sbgy.xml のXML解析に失敗しました: {e}\n"
                          f"regexベースの代替処理に切り替える必要があります。")


def codepoint_repr(ch):
    if not ch:
        return ""
    parts = []
    for c in ch:
        try:
            name = unicodedata.name(c)
        except ValueError:
            name = "?"
        parts.append(f"U+{ord(c):04X}({name})")
    return f"{ch} [{' '.join(parts)}]"


def classify_mismatch(gy_char, sb_char, sb_rewrite):
    """廣韻側の字頭が「本字〈異体字〉」併記表記かどうかを判定し、
    その場合は本字部分がsbgy側と一致するかで分類する。
    戻り値: カテゴリ文字列
    """
    m = re.match(r"^(.)〈(.+)〉$", gy_char)
    if m:
        base = m.group(1)
        if base == sb_char:
            return "表記法の違いのみ（実質同一: 廣韻が本字〈異体字〉併記）"
        else:
            return "本字部分も不一致（要確認）"
    return "単純な字体差（コードポイント相違）"


def main():
    gy_groups = load_guangyun_groups(GY_CSV)
    sbgy_groups = load_sbgy_groups(SBGY_XML)

    print(f"廣韻.csv: 韻グループ数 = {len(gy_groups)}")
    print(f"sbgy.xml: 韻グループ数 = {len(sbgy_groups)}")

    n = min(len(gy_groups), len(sbgy_groups))
    if len(gy_groups) != len(sbgy_groups):
        print("!! 韻グループ数が一致しません。先頭からminの個数のみ対応付けて処理します。")

    count_mismatch_rows = []
    char_mismatch_rows = []

    for gi in range(n):
        gy_g = gy_groups[gi]
        sb_g = sbgy_groups[gi]
        gy_chars = gy_g["chars"]
        sb_chars = sb_g["chars"]

        if len(gy_chars) != len(sb_chars):
            count_mismatch_rows.append({
                "韻インデックス": gi + 1,
                "廣韻_韻目原貌": gy_g["yun"],
                "sbgy_rhyme_id": sb_g["rhyme_id"],
                "廣韻_字数": len(gy_chars),
                "sbgy_字数": len(sb_chars),
            })

        m = min(len(gy_chars), len(sb_chars))
        for pos in range(m):
            xh, zh, gy_char = gy_chars[pos]
            whid, sb_char, sb_rewrite = sb_chars[pos]
            if gy_char != sb_char:
                category = classify_mismatch(gy_char, sb_char, sb_rewrite)
                char_mismatch_rows.append({
                    "韻インデックス": gi + 1,
                    "韻目原貌": gy_g["yun"],
                    "韻内位置": pos + 1,
                    "廣韻_小韻號": xh,
                    "廣韻_小韻字號": zh,
                    "廣韻_字頭": gy_char,
                    "廣韻_codepoint": codepoint_repr(gy_char),
                    "sbgy_word_head_id": whid,
                    "sbgy_字頭": sb_char,
                    "sbgy_codepoint": codepoint_repr(sb_char),
                    "sbgy_rewrite_word": sb_rewrite or "",
                    "分類": category,
                })

    # 出力
    count_path = OUT_DIR / "mismatched_count_report.tsv"
    with open(count_path, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["韻インデックス", "廣韻_韻目原貌", "sbgy_rhyme_id", "廣韻_字数", "sbgy_字数"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(count_mismatch_rows)

    char_path = OUT_DIR / "char_mismatch_report.tsv"
    with open(char_path, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["韻インデックス", "韻目原貌", "韻内位置", "廣韻_小韻號", "廣韻_小韻字號",
                      "廣韻_字頭", "廣韻_codepoint", "sbgy_word_head_id", "sbgy_字頭", "sbgy_codepoint",
                      "sbgy_rewrite_word", "分類"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(char_mismatch_rows)

    print(f"\n字数が一致しない韻グループ: {len(count_mismatch_rows)} 件 -> {count_path}")
    print(f"字頭コードポイント相違（字数一致区間内）: {len(char_mismatch_rows)} 件 -> {char_path}")

    from collections import Counter
    cat_counter = Counter(r["分類"] for r in char_mismatch_rows)
    print("\n内訳:")
    for cat, cnt in cat_counter.most_common():
        print(f"  {cat}: {cnt} 件")


if __name__ == "__main__":
    main()
