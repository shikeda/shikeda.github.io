#!/usr/bin/env python3
"""
gy_dhsjr_link.py  —  廣韻 × DHSJR 接続スクリプト

DHSJR TSV の `単字_見出し` を廣韻.csv の音韻地位に接続し、
各字の音韻地位（声母・清濁・等・開合・韻・摂・声調）と
高松・沼本表に基づく漢音・呉音予測仮名形を付与する。

出力:
  - dhsjr_gy_linked.tsv  : DHSJR 行ごとに音韻地位と予測形を付加
  - dhsjr_gy_unmatched.tsv : 廣韻に見つからなかった字の一覧
  - dhsjr_gy_multi.tsv   : 廣韻に複数エントリがある字の一覧（要確認）

使い方:
  # 単一 DHSJR TSV を廣韻に接続
  python gy_dhsjr_link.py --dhsjr path/to/30-017-01_IRS.tsv \\
                           --gy 廣韻.csv \\
                           --outdir ./linked_out/

  # ディレクトリ内の全 TSV を一括処理
  python gy_dhsjr_link.py --dhsjr-dir path/to/DHSJR/data/ \\
                           --gy 廣韻.csv \\
                           --outdir ./linked_out/

  # SGY_fanqie.csv も参照してより詳細な音韻情報を付加
  python gy_dhsjr_link.py --dhsjr path/to/30-017-01_IRS.tsv \\
                           --gy 廣韻.csv \\
                           --sgy SGY_fanqie.csv \\
                           --outdir ./linked_out/

  # HDIC辞書（KTB・SYP・TSJなど）の Entry 列を見出し字として使用
  python gy_dhsjr_link.py --dhsjr path/to/KTB.tsv \\
                           --gy 廣韻.csv \\
                           --entry-col Entry \\
                           --outdir ./linked_out/

  # 見出し字列と声調列を両方指定（独自列名のTSVへの対応）
  python gy_dhsjr_link.py --dhsjr path/to/custom.tsv \\
                           --gy 廣韻.csv \\
                           --entry-col 見出し字 \\
                           --tone-col 声調 \\
                           --outdir ./linked_out/

--entry-col のデフォルトは「単字_見出し」（DHSJR標準）。
--tone-col のデフォルトは「声点」（DHSJR標準）。声調列がない場合は複数音の絞り込みをスキップする。
--itaiji は異体字TSV（NIHUテーブル等）のパス。複数ファイルをカンマ区切りで指定可能。
--itaiji-json は異体字JSON（{"字A":"字B"} や {"字A":["字B","字C"]}、
または [{"c1":"字A","c2":"字B"}] 形式のペアリスト）のパス。
「新字・旧字」のような方向の区別は不要で、廣韻に収録されている側が
自動的に正規化先として選ばれる。
異体字正規化を行う場合、元の字形を GY_正規化前 列に記録する。

Python 3.9 以上。標準ライブラリのみ使用。

---- データ設計メモ ----

廣韻.csv の音韻地位フォーマット:
  声母 (開合)? 等? (開合)? (重紐ABC)? 韻 声調
  例: 端一東平 / 章開三支平 / 見三C東平

SGY_fanqie.csv の主要フィールド:
  hanzi, shengmu, shengmu_deng, she_kaihe_deng, qingzhuo, rhyme_id, tone_volume_code

音韻地位の6次元:
  1. 声母 (shengmu)
  2. 清濁 (qingzhuo: 全清/次清/全濁/次濁)
  3. 等 (deng: 一/二/三/四)
  4. 開合 (kaihe: 開/合/中)
  5. 韻 (yun)
  6. 声調 (tone: 平/上/去/入)

高松・沼本表の予測形は「等が12等か34等か」「開合」「摂」の組み合わせで決まる。
本スクリプトでは声母行（ハ行系など）と韻摂音形を別々に付与し、
合成予測形は付与しない（組み合わせの多対多性のため）。
照合判定は別スクリプト（今後作成）で行う。
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# 定数: 韻 → 摂 マッピング（廣韻58韻 → 16摂）
# ---------------------------------------------------------------------------

YUN_TO_SHE: dict[str, str] = {
    # 通摂
    "東": "通", "冬": "通", "鍾": "通",
    # 江摂
    "江": "江",
    # 止摂
    "支": "止", "脂": "止", "之": "止", "微": "止",
    # 遇摂
    "魚": "遇", "虞": "遇", "模": "遇",
    # 蟹摂
    "齊": "蟹", "祭": "蟹", "泰": "蟹", "佳": "蟹",
    "皆": "蟹", "夬": "蟹", "灰": "蟹", "咍": "蟹", "廢": "蟹",
    # 臻摂
    "真": "臻", "臻": "臻", "殷": "臻", "文": "臻",
    "欣": "臻", "元": "臻", "魂": "臻", "痕": "臻",
    # 山摂
    "寒": "山", "桓": "山", "刪": "山", "山": "山",
    "先": "山", "仙": "山",
    # 效摂
    "蕭": "效", "宵": "效", "肴": "效", "豪": "效",
    # 果摂
    "歌": "果", "戈": "果",
    # 假摂
    "麻": "假",
    # 宕摂
    "陽": "宕", "唐": "宕",
    # 梗摂
    "庚": "梗", "耕": "梗", "清": "梗", "青": "梗",
    # 曽摂
    "蒸": "曽", "登": "曽",
    # 流摂
    "尤": "流", "侯": "流", "幽": "流",
    # 深摂
    "侵": "深",
    # 咸摂
    "覃": "咸", "談": "咸", "鹽": "咸", "添": "咸",
    "咸": "咸", "銜": "咸", "嚴": "咸", "凡": "咸",
}

# ---------------------------------------------------------------------------
# 定数: 声母 → 清濁（廣韻.csvに清濁情報がない場合の補完用）
# ---------------------------------------------------------------------------

SM_QINGZHUO: dict[str, str] = {
    # 全清
    "幫": "全清", "端": "全清", "知": "全清", "精": "全清",
    "心": "全清", "荘": "全清", "莊": "全清", "章": "全清",
    "照": "全清", "見": "全清", "影": "全清", "非": "全清",
    # 次清
    "滂": "次清", "透": "次清", "徹": "次清", "清": "次清",
    "初": "次清", "昌": "次清", "穿": "次清", "溪": "次清",
    "曉": "次清", "敷": "次清",
    # 全濁
    "並": "全濁", "定": "全濁", "澄": "全濁", "從": "全濁",
    "邪": "全濁", "崇": "全濁", "牀": "全濁", "船": "全濁",
    "常": "全濁", "禪": "全濁", "羣": "全濁", "匣": "全濁",
    "奉": "全濁",
    # 次濁
    "明": "次濁", "泥": "次濁", "娘": "次濁", "孃": "次濁",
    "来": "次濁", "來": "次濁", "日": "次濁",
    "疑": "次濁", "云": "次濁", "以": "次濁", "喩": "次濁",
    "于": "次濁", "微": "次濁",
}

# ---------------------------------------------------------------------------
# 定数: 声母 → 行（沼本・高松表に基づく）
# 呉音・漢音で同じ行になる声母はまとめて記載し、
# 異なる場合は (呉音行, 漢音行) のタプルで示す。
# ---------------------------------------------------------------------------

SM_TO_ROW: dict[str, tuple[str, str]] = {
    # ハ行
    "幫": ("ハ", "ハ"), "滂": ("ハ", "ハ"),
    "並": ("バ", "ハ"),   # 全濁→呉音バ行、漢音ハ行
    "非": ("ハ", "ハ"), "敷": ("ハ", "ハ"),
    "奉": ("ハ/バ", "ハ"),
    # マ行
    "明": ("マ", "マ"), "微": ("マ/バ", "マ"),
    # タ行
    "端": ("タ", "タ"), "透": ("タ", "タ"),
    "定": ("ダ", "タ"),   # 全濁→呉音ダ行、漢音タ行
    "知": ("タ", "タ"), "徹": ("タ", "タ"),
    "澄": ("ダ", "タ"),   # 全濁→呉音ダ行、漢音タ行
    # ナ行
    "泥": ("ナ", "ナ"), "娘": ("ナ", "ナ"), "孃": ("ナ", "ナ"),
    # カ行
    "見": ("カ", "カ"), "溪": ("カ", "カ"),
    "羣": ("カ/ガ", "カ"),  # 全濁→呉音ガ行、漢音カ行
    "曉": ("ハ", "カ"),
    "匣": ("カ/ガ", "カ"),
    # ガ行
    "疑": ("カ/ガ", "ガ"),
    # サ行
    "精": ("サ", "サ"), "清": ("サ", "サ"),
    "從": ("ザ", "サ"),   # 全濁→呉音ザ行、漢音サ行
    "心": ("サ", "サ"), "邪": ("ザ", "サ"),
    "荘": ("サ", "サ"), "莊": ("サ", "サ"),
    "初": ("サ", "サ"),
    "崇": ("ザ", "サ"), "牀": ("ザ", "サ"),
    "生": ("サ", "サ"),
    "章": ("サ", "サ"), "照": ("サ", "サ"),
    "昌": ("サ", "サ"), "穿": ("サ", "サ"),
    "船": ("ザ", "サ"), "書": ("サ", "サ"),
    "常": ("ザ", "サ"), "禪": ("ザ", "サ"),
    # ザ行（漢音）
    "日": ("ニ/ザ", "ザ"),
    # アヤワ行
    "影": ("ア/ヤ/ワ", "ア/ヤ/ワ"),
    "云": ("ワ/ヤ", "ワ/ヤ"),
    "于": ("ワ/ヤ", "ワ/ヤ"),
    "以": ("ヤ/ア", "ヤ/ア"), "喩": ("ヤ/ア", "ヤ/ア"),
    # ラ行
    "来": ("ラ", "ラ"), "來": ("ラ", "ラ"),
}

# ---------------------------------------------------------------------------
# 定数: (摂, 等区分) → 漢音韻母形・呉音韻母形
# 等区分: '12' = 一等・二等, '34' = 三等・四等
# 開合: '開' / '合' / '中'（中は開扱い、合は u 冠）
# ---------------------------------------------------------------------------

SHE_YINMU: dict[str, dict[str, dict[str, str]]] = {
    "通": {
        "12": {"漢": "oウ",   "呉": "uウ/oウ"},
        "34": {"漢": "iウ",   "呉": "uウ/oウ/iウ"},
    },
    "江": {
        "12": {"漢": "aウ",   "呉": "aウ/oウ"},
        "34": {"漢": "aウ",   "呉": "aウ/oウ"},
    },
    "止": {
        "34": {"漢": "i",     "呉": "i/e/o"},
    },
    "遇": {
        "12": {"漢": "o",     "呉": "u/o"},
        "34": {"漢": "iヨ/iユ/iウ", "呉": "u/o/iユ/iヨ"},
    },
    "蟹": {
        "12": {"漢": "aイ",   "呉": "aイ/e"},
        "34": {"漢": "eイ",   "呉": "aイ/eイ/e"},
    },
    "臻": {
        "12": {"漢": "oン",   "呉": "uン/oン"},
        "34": {"漢": "iン/iユン/uン", "呉": "iン/iユン/uン/oン"},
    },
    "山": {
        "12": {"漢": "aン",   "呉": "aン/eン"},
        "34": {"漢": "eン",   "呉": "eン/oン/aン"},
    },
    "效": {
        "12": {"漢": "aウ",   "呉": "aウ/eウ/oウ"},
        "34": {"漢": "eウ",   "呉": "eウ"},
    },
    "果": {
        "12": {"漢": "a",     "呉": "a"},
        "34": {"漢": "iヤ",   "呉": "iヤ"},
    },
    "假": {
        "12": {"漢": "a",     "呉": "a/e"},
        "34": {"漢": "iヤ",   "呉": "iヤ"},
    },
    "宕": {
        "12": {"漢": "aウ",   "呉": "aウ"},
        "34": {"漢": "iヤウ", "呉": "aウ/iヤウ"},
    },
    "梗": {
        "12": {"漢": "aウ",   "呉": "aウ/iヤウ"},
        "34": {"漢": "eイ",   "呉": "iヤウ"},
    },
    "曽": {
        "12": {"漢": "oウ",   "呉": "oウ"},
        "34": {"漢": "iヨウ", "呉": "oウ/iヨウ"},
    },
    "流": {
        "12": {"漢": "oウ",   "呉": "u/uウ/oウ"},
        "34": {"漢": "iウ",   "呉": "u/iウ/iユ/eウ"},
    },
    "深": {
        "34": {"漢": "iム",   "呉": "iム/oム"},
    },
    "咸": {
        "12": {"漢": "aム",   "呉": "aム/eム/oム"},
        "34": {"漢": "eム",   "呉": "aム/eム/oム"},
    },
}

# ---------------------------------------------------------------------------
# 廣韻.csv 読み込み・インデックス構築
# ---------------------------------------------------------------------------

GY_ROW_FIELDS = (
    "字頭", "音韻地位", "反切", "韻目原貌", "小韻號", "小韻字號",
)

YYQD_PAT = re.compile(
    r"^(.+?)"          # 声母
    r"(開|合)?"        # 開合（先）
    r"([一二三四])?"   # 等
    r"(開|合)?"        # 開合（後）
    r"([A-Za-z]?)"     # 重紐 A/B/C
    r"(.+?)"           # 韻名
    r"(平|上|去|入)$"  # 声調
)

# 廣韻.csv の補字（附音字）検出パターン
# 小韻字號が "1a1" のような \d+a\d+ 形式の行は sbgy.xml では added_word として扱われる
_SUPPLEMENTARY_JIGO_PAT = re.compile(r'^\d+a\d+$')
_BRACKET_HANZI_PAT = re.compile(r'^［(.+)］$')  # 補字の字頭表記: ［嬹］ → 嬹
_ANGLE_NOTE_HANZI_PAT = re.compile(r'^(.+?)〈.+〉$')  # 字頭注記: 䍧〈牂〉 → 䍧


def gy_headword_keys(hanzi: str) -> list[str]:
    """廣韻の字頭から索引用キーを返す。注記付き字頭は主字でも引けるようにする。"""
    keys = [hanzi]
    m = _ANGLE_NOTE_HANZI_PAT.match(hanzi)
    if m:
        main = m.group(1).strip()
        if main and main not in keys:
            keys.append(main)
    return keys


def parse_yyqd(yyqd: str) -> dict[str, str] | None:
    """廣韻の音韻地位文字列を分解して辞書を返す。"""
    m = YYQD_PAT.match(yyqd)
    if not m:
        return None
    kaihe = m.group(2) or m.group(4) or ""
    deng_raw = m.group(3) or ""
    deng_num = {"一": "1", "二": "2", "三": "3", "四": "4"}.get(deng_raw, "")
    yun = m.group(6)
    she = YUN_TO_SHE.get(yun, "")
    deng_class = "12" if deng_num in ("1", "2") or (not deng_num and she in ("果", "流")) else "34"
    sm = m.group(1)
    qingzhuo = SM_QINGZHUO.get(sm, "")
    rows_go, rows_ka = SM_TO_ROW.get(sm, ("", ""))
    she_deng = SHE_YINMU.get(she, {}).get(deng_class, {})
    yinmu_ka = she_deng.get("漢", "")
    yinmu_go = she_deng.get("呉", "")
    # 合口への u 付加（前舌母音系のみ）
    u_prefix_targets = ("a", "e", "i")
    if kaihe == "合":
        if yinmu_ka and yinmu_ka[0].lower() in u_prefix_targets:
            yinmu_ka = "u" + yinmu_ka
        if yinmu_go and yinmu_go[0].lower() in u_prefix_targets:
            yinmu_go = "u" + yinmu_go
    return {
        "声母": sm,
        "清濁": qingzhuo,
        "等": deng_num,
        "等区分": deng_class,
        "開合": kaihe or "中",
        "重紐": m.group(5),
        "韻": yun,
        "摂": she,
        "声調": m.group(7),
        "漢音行": rows_ka,
        "呉音行": rows_go,
        "漢音韻母形": yinmu_ka,
        "呉音韻母形": yinmu_go,
    }


def build_gy_index(gy_path: Path) -> dict[str, list[dict]]:
    """
    廣韻.csv を読み込み、字頭をキーとした辞書を返す。
    1字が複数音を持つ場合はリストに複数要素が入る。

    小韻字號が "1a1" のような \\d+a\\d+ 形式の補字（sbgy.xml では added_word）は、
    字頭の ［○］ 括弧を除去して通常エントリと同様にインデックス登録する。
    小韻字號の値（"1a1" 等）は parsed["小韻字號"] に保持されるため、
    GY_小韻字號 列でその性質を確認できる。

    字頭が "䍧〈牂〉" のような注記付き表記の場合は、元の字頭に加えて
    主字 "䍧" でも引けるようにする。
    """
    index: dict[str, list[dict]] = defaultdict(list)
    with gy_path.open("r", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            hanzi = row["字頭"].strip()
            if not hanzi:
                continue
            koshu_jigo = row.get("小韻字號", "").strip()
            if _SUPPLEMENTARY_JIGO_PAT.match(koshu_jigo):
                # 補字: ［嬹］ → 嬹 に正規化
                m = _BRACKET_HANZI_PAT.match(hanzi)
                if not m:
                    continue  # ［○］形式でない補字行は想定外のためスキップ
                hanzi = m.group(1)
            parsed = parse_yyqd(row["音韻地位"])
            if parsed is None:
                continue
            parsed["反切"]   = row["反切"]
            parsed["韻目原貌"] = row["韻目原貌"]
            parsed["小韻號"]  = row["小韻號"]
            parsed["小韻字號"] = koshu_jigo
            for key in gy_headword_keys(hanzi):
                index[key].append(parsed)
    return dict(index)


# ---------------------------------------------------------------------------
# SGY_fanqie.csv 読み込み（オプション）
# ---------------------------------------------------------------------------

def build_sgy_index(sgy_path: Path) -> dict[str, list[dict]]:
    """
    SGY_fanqie.csv を読み込み、字頭をキーとした辞書を返す。
    SGY は廣韻より詳細な she_kaihe_deng・shengmu_deng を持つ。
    """
    index: dict[str, list[dict]] = defaultdict(list)
    with sgy_path.open("r", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            hanzi = row["hanzi"].strip()
            if not hanzi:
                continue
            index[hanzi].append({
                "SGY_声母": row["shengmu"],
                "SGY_声母等": row["shengmu_deng"],
                "SGY_清濁": row["qingzhuo"],
                "SGY_摂開合等": row["she_kaihe_deng"],
                "SGY_韻ID": row["rhyme_id"],
                "SGY_反切": row["fanqie"],
            })
    return dict(index)


# ---------------------------------------------------------------------------
# 異体字正規化マップ構築
# ---------------------------------------------------------------------------

def build_itaiji_map(
    nihu_paths: list[str],
    json_paths: list[str],
    gy_index: dict[str, list[dict]],
) -> dict[str, str]:
    """
    異体字テーブルから「廣韻に収録されていない字 → 廣韻に収録されている字」
    の正規化マップを構築する。

    ルール:
      - 等価グループ内で廣韻にある字を代表字（正規化先）とする。
      - 廣韻にある字が複数ある場合は最初の字を採用する。
      - 廣韻にある字が1つもないグループは対象外。
      - JSON形式: {"字A": "字B"} または {"字A": ["字B", "字C"]} または
                  [{"c1": "字A", "c2": "字B"}, ...]（ペアリスト形式）
        いずれもキー・バリューや c1/c2 の方向に意味はなく、
        グループ内で廣韻にある字を代表字とする。

    Args:
        nihu_paths: NIHUテーブル形式TSVのパスリスト
                    列構成: 整理番号, 異体1, Unicode1, 異体2, Unicode2, ...
        json_paths: JSON形式異体字ファイルのパスリスト
        gy_index:   build_gy_index() が返す廣韻インデックス（字が存在するか判定用）

    Returns:
        {非廣韻字: 廣韻字} の辞書
    """
    import json as json_mod

    itaiji_map: dict[str, str] = {}

    def _register_group(group: list[str]) -> None:
        """等価グループを受け取りマップに登録する。"""
        group = [c.strip() for c in group if c.strip()]
        if len(group) < 2:
            return
        in_gy  = [c for c in group if c in gy_index]
        not_gy = [c for c in group if c not in gy_index]
        for src in not_gy:
            if in_gy and src not in itaiji_map:
                itaiji_map[src] = in_gy[0]

    # --- NIHUテーブル形式TSV ---
    for path in nihu_paths:
        p = Path(path.strip())
        if not p.exists():
            print(f"  [itaiji] ファイルが見つかりません: {p}", file=sys.stderr)
            continue
        with p.open("r", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh, delimiter="	"):
                group = [row.get(f"異体{i}", "").strip() for i in ["1","2","3","4"]]
                _register_group(group)
        print(f"  [itaiji] NIHUテーブル読み込み: {p.name}", file=sys.stderr)

    # --- JSON形式 ---
    for path in json_paths:
        p = Path(path.strip())
        if not p.exists():
            print(f"  [itaiji] ファイルが見つかりません: {p}", file=sys.stderr)
            continue
        with p.open("r", encoding="utf-8-sig") as fh:
            data = json_mod.load(fh)
        # {"A": "B"} または {"A": ["B","C"]} または [{"c1":"A","c2":"B"}] を許容
        if isinstance(data, dict):
            for key, val in data.items():
                vals = [val] if isinstance(val, str) else (val if isinstance(val, list) else [])
                _register_group([key] + vals)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    group = list(item.values())
                    _register_group(group)
        print(f"  [itaiji] JSON読み込み: {p.name}", file=sys.stderr)

    return itaiji_map


# ---------------------------------------------------------------------------
# DHSJR TSV 読み込み
# ---------------------------------------------------------------------------

def read_dhsjr(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    header: list[str] | None = None
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        for raw in csv.reader(fh, delimiter="\t"):
            if not raw or all(c == "" for c in raw):
                continue
            first = raw[0].lstrip("\ufeff")
            if first.startswith("#"):
                # SYP など HDIC辞書の「# eof列名	列名...」形式のヘッダー行を検出する。
                # "# eof" に続くトークンがヘッダーとして機能している場合、
                # 先頭要素から "# eof" 前置詞を除去してヘッダーとして採用する。
                if first.lower().startswith("# eof") and len(raw) > 1:
                    raw[0] = re.sub(r"^#\s*eof\S*\s*", "", first, flags=re.IGNORECASE).strip()
                    if not raw[0]:
                        # "# eofSYID" のように列名が接続している場合
                        raw[0] = re.sub(r"^#\s*eof", "", first, flags=re.IGNORECASE).strip()
                    header = raw
                continue
            if header is None:
                header = raw
                continue
            if len(raw) < len(header):
                raw = raw + [""] * (len(header) - len(raw))
            rows.append(dict(zip(header, raw[:len(header)])))
    if header is None:
        raise ValueError(f"ヘッダー行なし: {path}")
    return header, rows


# ---------------------------------------------------------------------------
# リンク処理
# ---------------------------------------------------------------------------

LINKED_EXTRA_FIELDS = [
    "GY_声母", "GY_清濁", "GY_等", "GY_等区分", "GY_開合",
    "GY_重紐", "GY_韻", "GY_摂", "GY_声調",
    "GY_漢音行", "GY_呉音行", "GY_漢音韻母形", "GY_呉音韻母形",
    "GY_反切", "GY_韻目原貌", "GY_小韻號", "GY_小韻字號",
    "GY_マッチ状況",
    "GY_正規化前",   # 異体字正規化が行われた場合に元の字形を記録
    "SGY_声母", "SGY_声母等", "SGY_清濁", "SGY_摂開合等", "SGY_韻ID", "SGY_反切",
]

MATCH_UNIQUE   = "一意"
MATCH_MULTI    = "複数音"
MATCH_NONE     = "未収録"
MATCH_SKIP     = "照合不要"


def link_row(
    row: dict[str, str],
    gy_index: dict[str, list[dict]],
    sgy_index: dict[str, list[dict]] | None,
    entry_col: str = "単字_見出し",
    tone_col: str = "声点",
    itaiji_map: dict[str, str] | None = None,
) -> dict[str, str]:
    """1行分のリンク処理。元の行辞書に音韻情報を追加して返す。

    Args:
        entry_col:   見出し漢字を格納する列名。
                     DHSJR標準は「単字_見出し」、KTB/SYP/TSJは「Entry」など。
        tone_col:    声調情報を格納する列名。
                     DHSJR標準は「声点」。列が存在しない場合は複数音の絞り込みをスキップ。
        itaiji_map:  異体字正規化マップ {非廣韻字: 廣韻字}。
                     指定時、廣韻に未収録の字を正規化してから再照合する。
    """
    out = dict(row)
    for f in LINKED_EXTRA_FIELDS:
        out[f] = ""

    hanzi = row.get(entry_col, "").strip()
    if not hanzi:
        out["GY_マッチ状況"] = MATCH_SKIP
        return out

    gy_entries = gy_index.get(hanzi, [])

    if not gy_entries:
        # 異体字正規化マップがある場合は正規化して再試行
        if itaiji_map and hanzi in itaiji_map:
            normalized = itaiji_map[hanzi]
            gy_entries = gy_index.get(normalized, [])
            if gy_entries:
                out["GY_正規化前"] = hanzi   # 元の字形を記録

    if not gy_entries:
        out["GY_マッチ状況"] = MATCH_NONE
    elif len(gy_entries) == 1:
        out["GY_マッチ状況"] = MATCH_UNIQUE
        _fill_gy(out, gy_entries[0])
    else:
        # 複数音：声調ヒントで絞り込みを試みる
        tone_raw = row.get(tone_col, "").strip()
        matched = _filter_by_tone(gy_entries, tone_raw)
        if len(matched) == 1:
            out["GY_マッチ状況"] = MATCH_UNIQUE
            _fill_gy(out, matched[0])
        else:
            out["GY_マッチ状況"] = f"{MATCH_MULTI}({len(gy_entries)})"
            # 複数の場合は最初のエントリを入れつつ全候補を記録
            _fill_gy(out, gy_entries[0])
            # 全候補の韻・声調を ; 区切りで追記
            all_yun = "/".join(f"{e['韻']}{e['声調']}" for e in gy_entries)
            out["GY_韻目原貌"] = out["GY_韻目原貌"] + f"[候補:{all_yun}]"

    # SGY リンク（オプション）
    if sgy_index is not None:
        sgy_entries = sgy_index.get(hanzi, [])
        if sgy_entries:
            s = sgy_entries[0]
            out["SGY_声母"]    = s["SGY_声母"]
            out["SGY_声母等"]  = s["SGY_声母等"]
            out["SGY_清濁"]    = s["SGY_清濁"]
            out["SGY_摂開合等"] = s["SGY_摂開合等"]
            out["SGY_韻ID"]   = s["SGY_韻ID"]
            out["SGY_反切"]   = s["SGY_反切"]

    return out


def _fill_gy(out: dict, entry: dict) -> None:
    out["GY_声母"]       = entry["声母"]
    out["GY_清濁"]       = entry["清濁"]
    out["GY_等"]         = entry["等"]
    out["GY_等区分"]     = entry["等区分"]
    out["GY_開合"]       = entry["開合"]
    out["GY_重紐"]       = entry["重紐"]
    out["GY_韻"]         = entry["韻"]
    out["GY_摂"]         = entry["摂"]
    out["GY_声調"]       = entry["声調"]
    out["GY_漢音行"]     = entry["漢音行"]
    out["GY_呉音行"]     = entry["呉音行"]
    out["GY_漢音韻母形"] = entry["漢音韻母形"]
    out["GY_呉音韻母形"] = entry["呉音韻母形"]
    out["GY_反切"]       = entry["反切"]
    out["GY_韻目原貌"]   = entry["韻目原貌"]
    out["GY_小韻號"]     = entry["小韻號"]
    out["GY_小韻字號"]   = entry.get("小韻字號", "")


TONE_LABEL_MAP = {
    "平": "平", "平濁": "平", "平軽": "平",
    "上": "上", "上濁": "上", "上軽": "上",
    "去": "去", "去濁": "去", "去軽": "去",
    "入": "入", "入濁": "入", "フ入": "入",
}


def _filter_by_tone(entries: list[dict], tone_raw: str) -> list[dict]:
    """声点から声調を推定して廣韻エントリを絞り込む。"""
    if not tone_raw:
        return entries
    first = re.split(r"[・／\s]", tone_raw)[0]
    tone = TONE_LABEL_MAP.get(first, "")
    if not tone:
        return entries
    filtered = [e for e in entries if e["声調"] == tone]
    return filtered if filtered else entries


# ---------------------------------------------------------------------------
# 出力
# ---------------------------------------------------------------------------

def write_tsv(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=header, delimiter="\t",
                                extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"  → {path} ({len(rows)} 行)", file=sys.stderr)


# ---------------------------------------------------------------------------
# メイン
# ---------------------------------------------------------------------------

def collect_dhsjr_targets(args: argparse.Namespace) -> list[Path]:
    targets: list[Path] = []
    if args.dhsjr:
        targets.append(Path(args.dhsjr))
    if args.dhsjr_dir:
        targets.extend(sorted(Path(args.dhsjr_dir).glob("*.tsv")))
    if not targets:
        raise SystemExit("--dhsjr または --dhsjr-dir を指定してください。")
    return targets


def main() -> None:
    parser = argparse.ArgumentParser(
        description="廣韻 × DHSJR 接続スクリプト",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--dhsjr", help="単一 DHSJR TSV ファイル")
    parser.add_argument("--dhsjr-dir", dest="dhsjr_dir",
                        help="DHSJR TSV ディレクトリ（全 *.tsv を処理）")
    parser.add_argument("--gy", required=True, help="廣韻.csv のパス")
    parser.add_argument("--sgy", help="SGY_fanqie.csv のパス（省略可）")
    parser.add_argument("--outdir", required=True,
                        help="出力ディレクトリ")
    parser.add_argument(
        "--entry-col", dest="entry_col", default="単字_見出し",
        metavar="COL",
        help="見出し漢字を格納する列名（デフォルト: 単字_見出し）。"
             "KTB・SYP・TSJ など HDIC辞書TSVでは Entry を指定する。",
    )
    parser.add_argument(
        "--tone-col", dest="tone_col", default="声点",
        metavar="COL",
        help="声調情報を格納する列名（デフォルト: 声点）。"
             "列が存在しない場合は複数音の絞り込みをスキップする。",
    )
    parser.add_argument(
        "--itaiji", default="",
        metavar="PATH[,PATH...]",
        help="NIHUテーブル形式の異体字TSVのパス（カンマ区切りで複数指定可）。"
             "例: 異体漢字対応テーブル111220版_TSV221111.txt",
    )
    parser.add_argument(
        "--itaiji-json", dest="itaiji_json", default="",
        metavar="PATH[,PATH...]",
        help="JSON形式の異体字ファイルのパス（カンマ区切りで複数指定可）。"
             '形式: {"字A":"字B"} または {"字A":["字B","字C"]} または [{"c1":"A","c2":"B"}]',
    )
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    print("廣韻インデックスを構築中…", file=sys.stderr)
    gy_index = build_gy_index(Path(args.gy))
    print(f"  廣韻 ユニーク字数: {len(gy_index)}", file=sys.stderr)

    sgy_index: dict[str, list[dict]] | None = None
    if args.sgy:
        print("SGY インデックスを構築中…", file=sys.stderr)
        sgy_index = build_sgy_index(Path(args.sgy))
        print(f"  SGY ユニーク字数: {len(sgy_index)}", file=sys.stderr)

    entry_col: str = args.entry_col
    tone_col: str = args.tone_col
    if entry_col != "単字_見出し":
        print(f"  見出し字列: {entry_col}", file=sys.stderr)
    if tone_col != "声点":
        print(f"  声調列: {tone_col}", file=sys.stderr)

    # 異体字正規化マップ構築
    itaiji_map: dict[str, str] | None = None
    nihu_paths = [p for p in args.itaiji.split(",") if p.strip()]
    json_paths = [p for p in args.itaiji_json.split(",") if p.strip()]
    if nihu_paths or json_paths:
        print("異体字マップを構築中…", file=sys.stderr)
        itaiji_map = build_itaiji_map(nihu_paths, json_paths, gy_index)
        print(f"  異体字マップ件数: {len(itaiji_map)}", file=sys.stderr)

    targets = collect_dhsjr_targets(args)

    # 全体の未収録・複数音集計
    all_unmatched: list[dict[str, str]] = []
    all_multi: list[dict[str, str]] = []

    for path in targets:
        print(f"処理中: {path.name}", file=sys.stderr)
        try:
            orig_header, rows = read_dhsjr(path)
        except Exception as e:
            print(f"  スキップ ({e})", file=sys.stderr)
            continue

        out_header = orig_header + [
            f for f in LINKED_EXTRA_FIELDS
            if f not in orig_header
        ]
        linked_rows = [link_row(r, gy_index, sgy_index, entry_col, tone_col, itaiji_map) for r in rows]

        # メイン出力
        out_path = outdir / f"{path.stem}_gy_linked.tsv"
        write_tsv(out_path, out_header, linked_rows)

        # 未収録・複数音を収集
        mat_field = "GY_マッチ状況"
        for r in linked_rows:
            status = r.get(mat_field, "")
            resource_id = r.get("資料番号", path.stem)
            base = {"資料番号": resource_id, "単字_見出し": r.get(entry_col, "")}
            if status == MATCH_NONE:
                all_unmatched.append(base)
            elif status.startswith(MATCH_MULTI):
                all_multi.append({**base, "候補数": status, "GY_韻目原貌": r.get("GY_韻目原貌", "")})

    # まとめ出力
    if all_unmatched:
        write_tsv(
            outdir / "dhsjr_gy_unmatched.tsv",
            ["資料番号", "単字_見出し"],
            all_unmatched,
        )
    if all_multi:
        write_tsv(
            outdir / "dhsjr_gy_multi.tsv",
            ["資料番号", "単字_見出し", "候補数", "GY_韻目原貌"],
            all_multi,
        )

    print("完了。", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
