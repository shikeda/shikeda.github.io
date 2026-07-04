---
title: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(5)"
date: 2026-07-01T17:45:19+09:00
draft: false
tags:
  - 廣韻
  - 音韻学
  - 漢字データベース
  - Python
  - awk
  - 宋本廣韻
  - HDIC
  - DHSJR
  - KRM
  - データ統合
  - 異体字
  - IDS
  - Unicode
categories:
  - デジタル人文学
  - 日本古辞書
summary: "前回の連載(4)では、DHSJR全74文献への `gy_dhsjr_link.py` 適用と複数の異体字マップの段階追加により、`unmatched` を22,012→7,523行まで削減しました。今回の(5)では、残る `unmatched` 例を精査します。"
---


## はじめに

前回の
[宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(4)](/posts/sbgy-phonological-data-linking-to-hdic-and-dhsjr-4/)では、
[`gy_dhsjr_link.py`](/downloads/scripts/gy_dhsjr_link.py)の`--itaiji`・`--itaiji-json`オプションを使い、
DHSJR全74文献に `gy_dhsjr_link.py` を適用し、`itaiji_gy_compare.json`・`itaiji_jisx0213.json`・CJKV異体字表・`jp-old-style.txt`・KRM未検証ペアを `--itaiji-json` で段階追加しました。`unmatched` は 22,012→7,523 行（約66%減）まで減る一方 `multi` は増加するトレードオフを定量的に示しました。

今回の(5)は `unmatched` 例を精査します。

まず、DHSJR全74文献から検討対象となる`unmatched` 例を抜き出し、データ入力ミスがないかどうかをチェックします。

## `dhsjr_gy_unmatched.tsv`を分析

`gy_dhsjr_link.py`で生成した`dhsjr_gy_unmatched.tsv`を用意し、重複したレコードを整理しておきます。

まず、[check_blocks.py](/downloads/scripts/check_blocks.py)でUnicodeのCJK統合漢字のブロックの情報を追加します。
`dhsjr_gy_unmatched.tsv`を入力して、`dhsjr_gy_unmatched.blocks.tsv`を自動生成します。
その上でソートして、`unmatched_uniq.tsv`を生成します。

```bash
python3 check_blocks.py
sort -u dhsjr_gy_unmatched.blocks.tsv > unmatched_uniq.tsv

```

次に、ブロック別集計を行います。これは、連載の[(2)](/posts/sbgy-phonological-data-linking-to-hdic-and-dhsjr-1/)で紹介した[summarize_gy_unmatched_blocks.py](/downloads/scripts/summarize_gy_unmatched_blocks.py)を用います。

```bash
python3 summarize_gy_unmatched_blocks.py --tsv unmatched_uniq.blocks.tsv --out unmatched_uniq.blocks_集計.md
Read 4,515 rows from unmatched_uniq.tsv
Wrote report (13 blocks) to unmatched_uniq.blocks_集計.md
```

## unmatched_uniq.blocks.tsv ブロック別集計

2026-06-30

対象ファイル: `unmatched_uniq.blocks.tsv`

- 総行数: 5,214 行
- ブロック種類: 13 種

### 集計表

| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大5件） |
|---------|-----:|-----:|--------------:|--------------|
| CJK統合漢字拡張B | 1,747 | 33.5% | 1,711 | `𢮎` U+22B8E、`𣫘` U+23AD8、`𦞲` U+267B2、`𦡲` U+26872、`𪙁` U+2A641 |
| CJK統合漢字 | 1,506 | 28.9% | 917 | `俎` U+4FCE、`倐` U+5010、`嗅` U+55C5、`嘿` U+563F、`塪` U+586A |
| IDC | 1,280 | 24.5% | 1,278 | `⿰⺼冊` U+2FF0、`⿰⺼胃` U+2FF0、`⿰⺼蚩` U+2FF0、`⿰土虒` U+2FF0、`⿰赤皮` U+2FF0
 |
| CJK統合漢字拡張A | 486 | 9.3% | 426 | `㙈` U+3648、`䏶` U+43F6、`䑌` U+444C、`㑊` U+344A、`㺃` U+3E83 |
| CJK統合漢字拡張F | 87 | 1.7% | 85 | `𮞒` U+2E792、`𮌤` U+2E324、`𮓪` U+2E4EA、`𮢶` U+2E8B6、`𮀉` U+2E009 |
| CJK統合漢字拡張C | 41 | 0.8% | 40 | `𪺲` U+2AEB2、`𪾼` U+2AFBC、`𪜰` U+2A730、`𪜾` U+2A73E、`𪝀` U+2A740 |
| CJK統合漢字拡張E | 27 | 0.5% | 27 | `𫣗` U+2B8D7、`𫥿` U+2B97F、`𫦯` U+2B9AF、`𫪦` U+2BAA6、`𫮈` U+2BB88 |
| 該当なし | 25 | 0.5% | 16 | ` ⿳艹宀⿰衤殳` U+0020、`■` U+25A0、`□` U+25A1、`〓` U+3013、`【⿰冫景】` U+3010 |
| CJK統合漢字拡張G | 5 | 0.1% | 5 | `𱂕` U+31095、`𰊊` U+3028A、`𰢚` U+3089A、`𰢟` U+3089F、`𰧫` U+309EB |
| CJK互換漢字 | 4 | 0.1% | 4 | `契` U+F909、`益` U+FA17、`精` U+FA1D、`杻` U+F9C8 |
| CJK統合漢字拡張H | 4 | 0.1% | 4 | `𱱋` U+31C4B、`𱖞` U+3159E、`𱵒` U+31D52、`𱹫` U+31E6B |
| CJK互換漢字補助 | 1 | 0.0% | 1 | `沿` U+2F8FC |
| CJK統合漢字拡張D | 1 | 0.0% | 1 | `𫞳` U+2B7B3 |


## 検討事項

`unmatched_uniq.blocks.tsv`を通覧すると、次のような検討事項が考えられます。

1. `単字_見出し`に空白など、余分な文字がないかどうかをチェックします。
2. `IDC`1278例は`⿰⺨表` U+2FF0、`該当無し`123例は`⿳艹宀⿰衤殳` U+0020のような例があり、Unicodeですでに符号化されている可能性があるものをチェックします。
3. `CJK互換漢字`4例について、JSON形式の異体字ペアファイルを作成します。
4. `CJK統合漢字`917例について、`不也` U+4E0Dのような明白なエラーの例をピックアップします。

## `単字_見出し`に空白などあるもののチェック

半角の空白` `の混入が1例あります。これは修正が必要です。

```bash
awk -F'\t' '$2 ~ / /' unmatched_uniq.blocks.tsv
20-043-01        ⿳艹宀⿰衤殳   0020    該当なし
```

次に【】でくくった例が3例あります。これは`【`と`】`を削除しておいたほうが扱いやすいでしょう。

```bash
awk -F'\t' '$2 ~ /【/' unmatched_uniq.blocks.tsv
30-024-01       【⿰冫景】      3010    該当なし
30-024-01       【⿰女庾】      3010    該当なし
30-024-01       【⿰彳䓗】      3010    該当なし
30-024-01       【⿰辛風】      3010    該当なし
```

## IDCを含む`単字_見出し`の検討

IDC は Unicode の範囲が U+2FF0～U+2FFF なので、awk であれば正規表現中に直接その範囲を書けます。

次の処理で、1286件を抜き出した`unmatched_uniq_idc.tsv`を生成しました。

```bash
awk -F'\t' '$2 ~ /[⿰-⿿]/ { gsub(/[【】]/, "", $2); print }' unmatched_uniq.blocks.tsv  > unmatched_uniq_blocks_idc.tsv
```

`unmatched_uniq.blocks.tsv`を通覧すると、`単字_見出し`カラムに、平仮名やカタカナを含むデータがあります。

```bash
awk -F'\t' '$2 ~ /[ぁ-ゖァ-ヺ]/' unmatched_uniq.blocks.tsv
資料番号        単字_見出し     16進Unicode番号 ブロック
30-017-01       ⿺辶旋の旁      2FFA    IDC
30-048-02       ⿳亠ニコ        2FF3    IDC
30-048-02       ⿳亠ニ匕        2FF3    IDC
50-055-01       シ      30B7    該当なし
50-055-01       デ      30C7    該当なし
50-055-01       信じ    4FE1    CJK統合漢字
70-054-01       〓（やまいだれに「仙」）        3013    該当なし
70-054-01       字と    5B57    CJK統合漢字
70-054-01       祭り    796D    CJK統合漢字
70-054-01       走る    8D70    CJK統合漢字
```

上記のうち、`字と`のように平仮名を含む例は誤入力ですから、修正の必要があります。

`字と`は`漢語_見出し`が`國人`だから、`人`とすべきでしょう。

`〓（やまいだれに「仙」）`は`𬏣` U+2C3E3があるので、これに変換するのがよいでしょう。

その他の例の説明は省略しますが、手元のDHSJRのデータに修正を加えておきます。

次に`ブロック`カラムが`該当なし`のものを一覧すると、次のような例があります。

```bash
grep "該当なし" unmatched_uniq.blocks.tsv
20-043-01        ⿳艹宀⿰衤殳   0020    該当なし
20-043-01       ■       25A0    該当なし
20-043-01       □       25A1    該当なし
20-045-01       □       25A1    該当なし
20-055-01       〓      3013    該当なし
30-005-01       〓      3013    該当なし
30-005-02       ■       25A0    該当なし
30-008-01       ■       25A0    該当なし
30-017-01       □       25A1    該当なし
30-024-01       【⿰冫景】      3010    該当なし
30-024-01       【⿰女庾】      3010    該当なし
30-024-01       【⿰彳䓗】      3010    該当なし
30-024-01       【⿰辛風】      3010    該当なし
30-037-01       々      3005    該当なし
30-048-02       〓      3013    該当なし
30-048-02       ー（蝳）        30FC    該当なし
30-057-01       □       25A1    該当なし
50-041-01       ？      FF1F    該当なし
50-055-01       シ      30B7    該当なし
50-055-01       デ      30C7    該当なし
60-028-01       々      3005    該当なし
70-042-01       〓（乾左）      3013    該当なし
70-042-01       〓（小＋卑）    3013    該当なし
70-054-01       々      3005    該当なし
70-054-01       〓（やまいだれに「仙」）        3013    該当なし
```

上記の例には、修正の余地がある例も見えます。

たとえば、`〓（乾左`は`乾`の左側の字ということなら`𠦝`としてよいでしょう。`卓`の誤写の可能性も残るので、元に戻っての確認が必要です。


## IDSデータとの照合

UnicodeのIDS関連のデータは、[https://github.com/cjkvi/cjkvi-ids](https://github.com/cjkvi/cjkvi-ids)で公開されています。多数のファイルがありますが、ここでは`ids.txt`を利用してみます。

`ids.txt`は次のような内容です。[CHISE](https://www.chise.org/ids/)のデータに基づいていますが、データ処理の手順を簡単にするため、今回は、`ids.txt`を用いることとします。

```text
# Copyright (c) 2014-2017 CJKVI Database
# Based on CHISE IDS Database
U+03B1  α       α
U+2113  ℓ       ℓ
U+2460  ①       ①
（中略）
U+213D9 𡏙      ⿱囱圶
U+213DA 𡏚      ⿰土虒
U+213DB 𡏛      ⿰土奚
```

`unmatched_uniq_blocks_idc.tsv`の例をいくつか挙げます。

```
資料番号        単字_見出し     16進Unicode番号 ブロック
20-001-01       ⿰⺼冊  2FF0    IDC
20-001-01       ⿰⺼胃  2FF0    IDC
20-001-01       ⿰⺼蚩  2FF0    IDC
20-001-01       ⿰土虒  2FF0    IDC
20-001-01       ⿰赤皮  2FF0    IDC
```
`単字_見出し`の4番目の`⿰土虒`は、`ids.txt`に`𡏚`として見えていました。
つまり、`⿰土虒`を`𡏚`に変換するのがよいでしょう。

次の手順で進めると、`unmatched_uniq_blocks_idc.tsv`のすべての例を`ids.txt`と照合できます。実際に照合したところ、93件を変換できました。

最初に、`ids.txt` はデリミタが半角スペースなので、これをタブ区切りに整形してしまいます。


```bash
awk 'BEGIN{OFS="\t"}{print $1,$2,$3}' ids.txt > ids.tsv
```

としておくと、タブ区切りの`ids.tsv`が得られます。

そして、次を実行します。

```bash
awk -F'\t' 'BEGIN{OFS="\t"}
NR==FNR {
    ids[$3]=$1 OFS $2
    next
}
$2 in ids {
    print $1,$2,ids[$2]
}
' ids.tsv unmatched_uniq_blocks_idc.tsv \
> unmatched_uniq_blocks_idc_with_ucs.tsv
```

出力は次のようにきれいなタブ区切りになります。

```text
20-001-01       ⿰土虒  U+213DA 𡏚
20-001-01       ⿰赤皮  U+27E5E 𧹞
20-043-01       ⿰口臘  U+21158 𡅘
```

## Unicode 符号化済み文字へ一括置換するスクリプト

前述の手順で作成した`unmatched_uniq_blocks_idc_with_ucs.tsv`に基づいて、DHSJRの個別 TSV 内の IDC/IDS 表記をUnicode 符号化済み文字へ一括置換するスクリプト`apply_idc_ucs_replacements.py`を用意しました。

資料番号 + 単字_見出し をキーに変換を適用し、対象列は 単字_見出し、単字_出現形、漢語_見出し、漢語_出現形 に限定されます。デフォルトは dry-run で、--apply 指定時のみバックアップを作成して実ファイルを書き換えます。

作成先は次のとおりです。[apply_idc_ucs_replacements.py](/downloads/scripts/apply_idc_ucs_replacements.py)

使い方は次です。`apply_idc_ucs_replacements.py`はscriptsフォルダに置いており、`--map`の`--data-dir`のフォルダは私の環境のものなので、適宜各自の環境に置き換えてください。

```bash
python3 scripts/apply_idc_ucs_replacements.py \
  --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
  --data-dir /home/ikeda/Hdic_data/DHSJR/data \
  --dry-run
```
実行結果は次のとおりです。

```bash
 python3 scripts/apply_idc_ucs_replacements.py   --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv   --data-dir /home/ikeda/Hdic_data/DHSJR/data   --dry-run
mode: dry-run
map usable entries: 93
map duplicate rows ignored: 0
map conflicts skipped: 0
target columns: 単字_見出し, 単字_出現形, 漢語_見出し, 漢語_出現形

20-001-01_DHN.tsv: changed rows=4, replacements=14
20-043-01_KOJ.tsv: changed rows=6, replacements=24
20-044-01_HOK.tsv: changed rows=1, replacements=4
30-005-01_SKK.tsv: changed rows=2, replacements=6
30-005-02_SKO.tsv: changed rows=9, replacements=30
30-008-01_YSK.tsv: changed rows=5, replacements=16
30-008-02_YSD.tsv: changed rows=2, replacements=6
30-017-01_IRS.tsv: changed rows=5, replacements=18
30-048-02_RMK.tsv: changed rows=70, replacements=248
40-045-01_HOT.tsv: changed rows=2, replacements=6
50-029-01_JSR.tsv: changed rows=4, replacements=16
50-041-01_HNI.tsv: changed rows=1, replacements=4

examples:
20-001-01_DHN.tsv:3136  20-001-01       ⿰土虒 -> 𡏚    4
20-001-01_DHN.tsv:3692  20-001-01       ⿰赤皮 -> 𧹞    4
20-001-01_DHN.tsv:3693  20-001-01       ⿰赤皮 -> 𧹞    2
20-001-01_DHN.tsv:3768  20-001-01       ⿰赤皮 -> 𧹞    4
20-043-01_KOJ.tsv:216   20-043-01       ⿰酉盖 -> 𨢸    4
20-043-01_KOJ.tsv:394   20-043-01       ⿱殸正 -> 𣫆    4
20-043-01_KOJ.tsv:405   20-043-01       ⿰口臘 -> 𡅘    4
20-043-01_KOJ.tsv:406   20-043-01       ⿱商衣 -> 𧜟    4
20-043-01_KOJ.tsv:684   20-043-01       ⿰酉盖 -> 𨢸    4
20-043-01_KOJ.tsv:780   20-043-01       ⿱艹觔 -> 𮏴    4
20-044-01_HOK.tsv:1603  20-044-01       ⿰乞頁 -> 𩑔    4
30-005-01_SKK.tsv:58    30-005-01       ⿰氵盥 -> 𤃗    4
30-005-01_SKK.tsv:59    30-005-01       ⿰氵盥 -> 𤃗    2
30-005-02_SKO.tsv:16    30-005-02       ⿰土睘 -> 𡑡    4
30-005-02_SKO.tsv:17    30-005-02       ⿰土睘 -> 𡑡    2
30-005-02_SKO.tsv:32    30-005-02       ⿱艹嬖 -> 𭒯    4
30-005-02_SKO.tsv:162   30-005-02       ⿰亻遺 -> 𠑌    4
30-005-02_SKO.tsv:163   30-005-02       ⿰亻遺 -> 𠑌    4
30-005-02_SKO.tsv:164   30-005-02       ⿰亻遺 -> 𠑌    2
30-005-02_SKO.tsv:177   30-005-02       ⿰忄害 -> 𢞐    4

summary:
changed files: 12
changed rows: 111
replacement occurrences: 392

This was a dry-run. Add --apply to write changes.
```

問題なければ実適用します。

```bash
python3 scripts/apply_idc_ucs_replacements.py \
  --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
  --data-dir /home/ikeda/Hdic_data/DHSJR/data \
  --backup-dir /home/ikeda/Hdic_data/DHSJR/data_backup_before_idc_ucs_20260701 \
  --apply
```

このスクリプトは次の列だけを置換対象にします。

```text
単字_見出し
単字_出現形
漢語_見出し
漢語_出現形
```

また、同じ `資料番号 + 単字_見出し` に複数の異なる UCS 文字候補がある場合は自動置換せず、衝突レポートに出します。


## IDS表記のUCS変換と括弧除去

### 問題の発見

変換後のデータを確認すると、`漢語_見出し`・`漢語_出現形`列に次のような残存形が生じていました。

```
永無[𡏚]落
[𧹞]然有愧
```

元データでは`[⿰土虒]`のように、IDS表記が`[`と`]`で囲まれていました。スクリプトはIDS文字列そのものを置換対象としていたため、囲んでいる括弧はそのまま残ってしまったのです。

### 原因の整理

`apply_idc_ucs_replacements.py`の置換処理は、変換表に登録されているIDS文字列（`⿰土虒`など）を検索して置換します。元データに`[⿰土虒]`という形で入っていた場合、`⿰土虒`の部分は置換されますが、括弧`[`と`]`はそのまま残ります。結果として`[𡏚]`という中間状態が生じました。

### 対策の方針

対処方針として2点を整備しました。

**今後の新規変換への対応**として、`apply_idc_ucs_replacements.py`を修正し、`[⿰土虒]`・`【⿰土虒】`・`⿰土虒`の3パターンをすべて置換対象に加えました。これにより今後は`[𡏚]`のような中間状態が生じません。

**既存データの修正**として、別スクリプト`strip_ucs_brackets.py`を作成しました。

括弧除去にあたっては、単純に`[`と`]`で囲まれた文字列をすべて除去する方法は採りませんでした。DHSJRのデータには`[A]`・`[左]`・`[未詳]`のような注記的な括弧表記も存在するためです。誤って注記を消してしまうリスクを避けるため、**変換表に載っているUCS文字を囲む括弧のみ**を除去対象としました。

### 作成したスクリプト

`strip_ucs_brackets.py`の処理の流れは次のとおりです。

1. 変換表TSVからUCS文字の集合を読み込みます。
2. その文字セットだけにマッチする正規表現を生成します。
3. `漢語_見出し`・`漢語_出現形`列に対してのみ適用します。

変換表はヘッダなし4列形式（`資料番号`・`IDS`・`UCS16進`・`UCS文字`）を前提としています。

`strip_ucs_brackets.py` は、変換済みデータに残った [𡏚] や 【𡏚】 のような UCS文字を囲む括弧だけを外すスクリプトです。[左] や [未詳] などの注記括弧には触れません。

### 実行方法

dry-runで変更予定箇所を確認してから適用します。

オプションで指定するファイルの場所は適宜、自分の環境にあわせてください。

```bash
# 確認（dry-run）
python3 scripts/strip_ucs_brackets.py \
  --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
  --data-dir /home/ikeda/Hdic_data/DHSJR/data

# 適用
python3 scripts/strip_ucs_brackets.py \
  --map linked_out_dhsjr_all_cjkv-jp/unmatched_uniq_blocks_idc_with_ucs.tsv \
  --data-dir /home/ikeda/Hdic_data/DHSJR/data \
  --apply
```

適用後、括弧が残っていないことを確認します。

```bash
grep '𧹞\|𡏚\|𨢸' /home/ikeda/Hdic_data/DHSJR/data/*.tsv | grep '\['
```

何も出力されなければ除去完了です。

## おわりに

今回の作業で明らかになったのは、IDS→UCS変換の置換単位と元データの記述単位が一致していないことで中間状態が生じるという問題です。`apply_idc_ucs_replacements.py`への`[IDS]`・`【IDS】`パターン追加により、今後の変換ではこの問題は生じません。既存データについては`strip_ucs_brackets.py`による変換表ベースの括弧除去で対処しました。

## 次回(6)予告

本稿(5)では、`unmatched` 例の精査と DHSJR 側データの手当てに着手しました。`ids.txt` との照合で 93 件の IDS→UCS 変換を適用し、入力ミス（空白混入、【】括弧、平仮名混入など）の修正も一部行いました。しかし、(5) 冒頭の検討事項のうち、`CJK互換漢字` 4 例の `--itaiji-json` 用ペア整備や、`不也` のような `CJK統合漢字` ブロックの明白なエラーの系統的な整理は、いまだ手つかずです。`ids.txt` にもない IDC 表記や、`該当なし` ブロックに分類される記号・注記的な字種も、引き続き `unmatched` を占めています。

次回(6)では、まず DHSJR データ修正後に `gy_dhsjr_link.py` を DHSJR 全 74 文献に対して再実行し、(4) で得た `unmatched` 7,523 行（`multi` 103,586 行）からどれだけ改善するかを再計測することを予定します。あわせて、残る `unmatched` を異体字マップでさらに削れるか（`CJK互換漢字` など）を検討し、(4) で定量化した「`unmatched` 減少と `multi` 増加」のトレードオフについて、`multi` 行の具体例を精査します。(1) から課題として挙げていた `--sgy` オプションが、複数音候補の絞り込みにどこまで有効かも、可能な範囲で試してみる予定です。
