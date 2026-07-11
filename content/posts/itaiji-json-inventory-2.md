---
title: "--itaiji-json 用JSONファイル目録（更新版: 集韻異体字ペア追加）"
date: 2026-07-11T00:00:00+09:00
draft: false
tags:
  - 廣韻
  - 集韻
  - 音韻学
  - 漢字データベース
  - Python
  - 宋本廣韻
  - HDIC
  - DHSJR
  - KRM
  - データ統合
  - 異体字
  - Unicode
categories:
  - デジタル人文学
  - 日本古辞書
summary: "`gy_dhsjr_link.py` の `--itaiji-json` に指定する異体字ペアJSONの目録。2026-07-04版（itaiji-json-inventory.md）に、集韻の headword_run 異体字列記から抽出した `jy_itaiji_pairs.json` を追加した更新版。"
---

# `--itaiji-json` 用JSONファイル目録（更新版）

`gy_dhsjr_link.py` の `--itaiji-json` オプションに指定するために作成した
異体字ペアJSONの目録である。各ファイルは基本的に
`[{"c1": "字A", "c2": "字B"}, ...]` 形式のペアリストである。

本稿は [itaiji-json-inventory.md](itaiji-json-inventory.md)（2026-07-04版）に、
集韻（jiyun）由来の `jy_itaiji_pairs.json` を追加した更新版である。旧版の内容は
そのまま引き継いでいる。

## 一覧

| ファイル名 | 件数 | 位置づけ | 由来・内容 | 利用上の注意 |
|---|---:|---|---|---|
| [`itaiji_gy_compare.json`](/downloads/data/itaiji_gy_compare.json) | 870 | 本運用寄り | `廣韻.csv` と `sbgy.xml` の見出し字差分から作成した異体字ペア。 | 宋本廣韻データ同士の字体差に基づくため、比較的使いやすい。 |
| [`itaiji_jisx0213.json`](/downloads/data/itaiji_jisx0213.json) | 1,320 | 本運用寄り | CJKVI `jisx0213-variants.txt` 由来の関連字ペア。 | DHSJR の見出し字正規化方針と関係が深い。 |
| [`itaiji_cjkv_simplified-variants.json`](/downloads/data/itaiji_cjkv_simplified-variants.json) | 16,786 | 本運用寄り・要注意 | CJKV 系の簡体字・異体字対応表由来。 | 件数が多く、`unmatched` は減るが `multi` 増加に注意。 |
| [`itaiji_jp-old.json`](/downloads/data/itaiji_jp-old.json) | 1,093 | 補助 | 日本語新旧字体対応由来。 | 全体改善効果は小さいが、一部の新旧字体差の補助に使える。 |
| [`itaiji_krm_gy_attested.json`](/downloads/data/itaiji_krm_gy_attested.json) | 1,618 | 本運用寄り | KRM 側で廣韻同字確認済みとみなした異体字ペア。 | KRM 由来の異体字に有効。DHSJR 全体では `multi` 増加も確認する。 |
| [`itaiji_krm_unverified_20260626.json`](/downloads/data/itaiji_krm_unverified_20260626.json) | 60 | 実験・要確認 | KRM 未収録例から手作業で作成した未検証ペア。 | 検証済みではないため、利用時は差分確認が必要。 |
| [`itaiji_dhsjr_unverified.json`](/downloads/data/itaiji_dhsjr_unverified.json) | 20 | 実験・要確認 | DHSJR 全体接続の未照合字を確認して追加した未検証ペア。 | 原則として `c1` に DHSJR 側の出現形、`c2` に `廣韻.csv` で引ける主字を置く。利用時は `unmatched` 減少だけでなく `multi` への移動も確認する。 |
| [`gy_kakko_itaiji.json`](/downloads/data/gy_kakko_itaiji.json) | 238 | 実験・追加候補 | 廣韻照合過程で抽出した括弧付き字形などの追加異体字候補。 | 出典・採否を確認しながら使う。 |
| [`checked_unmatched_chars_in_cjkvi_variant.json`](/downloads/data/checked_unmatched_chars_in_cjkvi_variant.json) | 4,002 | 確認結果・派生候補 | `unmatched` 字を CJKVI variants 系データで確認した候補。 | そのまま本運用に入れる前に、対応関係の妥当性を精査する。 |
| [`jy_itaiji_pairs.json`](/downloads/data/jy_itaiji_pairs.json) | 17,494 | 本運用寄り・新規 | 集韻（`~/codex/jy/vol1`〜`vol10`、ctext.org保存HTML由来）の各小韻の `headword_run` に複数文字が連続する箇所（「或作」「亦作」「籒作」「隷作」等の異体字を示す語を伴う）を異体字集合とみなし、集合内の全組み合わせをペア化。`scripts/extract_itaiji_from_jiyun.py` で生成。 | 集韻内部の字体差に基づくため、廣韻の字体差（`itaiji_gy_compare.json`等）とは独立の系統。巻末書誌情報（「集韻卷N」等の巻末表示、校訂官氏名列記）やOCR編集注記（「●缺字：〇」）は note が空/「臣」の群・「缺字」を含む群として除外済み。`30-048-02_RMK.tsv` 単独接続で `unmatched` 5,545→4,604（-941）、`multi` 6,582→6,897（+315）を確認（他の itaiji JSON 併用なし・このJSON単独の効果）。 |

## 推奨運用

当面は各JSONを統合せず、由来別の正本として保持する。統合版が必要な場合は、
手作業で編集せず、元JSONから生成する派生ファイルとして作成する。

比較的安全に使いやすい組み合わせは次のとおりである。

```bash
--itaiji-json itaiji_gy_compare.json,itaiji_jisx0213.json,itaiji_krm_gy_attested.json
```

より広く拾う場合は、CJKV 簡体字・異体字対応や未検証ペアも追加できるが、
`unmatched` 減少と同時に `multi` が増えるため、実行結果の
`dhsjr_gy_multi.tsv` を必ず確認する。

```bash
--itaiji-json itaiji_gy_compare.json,itaiji_jisx0213.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_gy_attested.json,itaiji_krm_unverified_20260626.json
```

DHSJR 全体の未照合字を追加確認した結果まで含める場合は、
`itaiji_dhsjr_unverified.json` も末尾に追加する。

```bash
--itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_unverified_20260626.json,gy_kakko_itaiji.json,checked_unmatched_chars_in_cjkvi_variant.json,itaiji_dhsjr_unverified.json
```

集韻由来の異体字も加える場合は `jy_itaiji_pairs.json` を末尾に追加する。単独でも
`unmatched` の顕著な減少が確認できているため、他の JSON と独立に検証したい場合は
これ単体でも試す価値がある。

```bash
--itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_unverified_20260626.json,gy_kakko_itaiji.json,checked_unmatched_chars_in_cjkvi_variant.json,itaiji_dhsjr_unverified.json,jy_itaiji_pairs.json
```

## 整理方針

- ファイル名変更やディレクトリ移動は、既存 docs の実行例を更新してから行う。
- 将来的には `itaiji_maps/` などのディレクトリへ集約する。
- 統合JSONを作る場合も、由来別JSONを正本として残す。
- `checked_unmatched_chars_in_cjkvi_variant.json` のような確認結果は、採用済みペアと候補を分けて管理する。
- `jy_itaiji_pairs.json` のように生成スクリプト（`scripts/extract_itaiji_from_jiyun.py`）を伴うファイルは、元データ（`jy/vol{N}/jiyun_juan{N}_groups.tsv`）が更新された場合に再生成すること。手編集はしない。
