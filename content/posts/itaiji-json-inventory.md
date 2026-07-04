---
title: "--itaiji-json 用JSONファイル目録"
date: 2026-07-04T10:30:00+09:00
draft: false
tags:
  - 廣韻
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
summary: "`gy_dhsjr_link.py` の `--itaiji-json` に指定する異体字ペアJSONを、由来・件数・位置づけ・利用上の注意とともに整理した目録。安全寄りの組み合わせと、`unmatched` 減少と `multi` 増加のトレードオフを踏まえた運用方針も示す。"
---

# `--itaiji-json` 用JSONファイル目録

`gy_dhsjr_link.py` の `--itaiji-json` オプションに指定するために作成した
異体字ペアJSONの目録である。各ファイルは基本的に
`[{"c1": "字A", "c2": "字B"}, ...]` 形式のペアリストである。

## 一覧

| ファイル名 | 件数 | 位置づけ | 由来・内容 | 利用上の注意 |
|---|---:|---|---|---|
| [`itaiji_gy_compare.json`](/downloads/data/itaiji_gy_compare.json) | 870 | 本運用寄り | `廣韻.csv` と `sbgy.xml` の見出し字差分から作成した異体字ペア。 | 宋本廣韻データ同士の字体差に基づくため、比較的使いやすい。 |
| [`itaiji_jisx0213.json`](/downloads/data/itaiji_jisx0213.json) | 1,320 | 本運用寄り | CJKVI `jisx0213-variants.txt` 由来の関連字ペア。 | DHSJR の見出し字正規化方針と関係が深い。 |
| [`itaiji_cjkv_simplified-variants.json`](/downloads/data/itaiji_cjkv_simplified-variants.json) | 16,786 | 本運用寄り・要注意 | CJKV 系の簡体字・異体字対応表由来。 | 件数が多く、`unmatched` は減るが `multi` 増加に注意。 |
| [`itaiji_jp-old.json`](/downloads/data/itaiji_jp-old.json) | 1,093 | 補助 | 日本語新旧字体対応由来。 | 全体改善効果は小さいが、一部の新旧字体差の補助に使える。 |
| [`itaiji_krm_gy_attested.json`](/downloads/data/itaiji_krm_gy_attested.json) | 1,618 | 本運用寄り | KRM 側で廣韻同字確認済みとみなした異体字ペア。 | KRM 由来の異体字に有効。DHSJR 全体では `multi` 増加も確認する。 |
| [`itaiji_krm_unverified_20260626.json`](/downloads/data/itaiji_krm_unverified_20260626.json) | 60 | 実験・要確認 | KRM 未収録例から手作業で作成した未検証ペア。 | 検証済みではないため、利用時は差分確認が必要。 |
| [`gy_kakko_itaiji.json`](/downloads/data/gy_kakko_itaiji.json) | 238 | 実験・追加候補 | 廣韻照合過程で抽出した括弧付き字形などの追加異体字候補。 | 出典・採否を確認しながら使う。 |
| [`checked_unmatched_chars_in_cjkvi_variant.json`](/downloads/data/checked_unmatched_chars_in_cjkvi_variant.json) | 4,002 | 確認結果・派生候補 | `unmatched` 字を CJKVI variants 系データで確認した候補。 | そのまま本運用に入れる前に、対応関係の妥当性を精査する。 |

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

## 整理方針

- ファイル名変更やディレクトリ移動は、既存 docs の実行例を更新してから行う。
- 将来的には `itaiji_maps/` などのディレクトリへ集約する。
- 統合JSONを作る場合も、由来別JSONを正本として残す。
- `checked_unmatched_chars_in_cjkvi_variant.json` のような確認結果は、採用済みペアと候補を分けて管理する。
