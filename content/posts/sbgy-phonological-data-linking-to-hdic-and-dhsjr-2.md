---
title: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(2)"
date: 2026-06-27
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
categories:
  - デジタル人文学
  - 日本古辞書
summary: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(1)の続き。Pythonスクリプト gy_dhsjr_link.py により出力した未収録・異体字の扱いについて解説します。"
---


## はじめに

前回の
[宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(1)](/posts/sbgy-phonological-data-linking-to-hdic-and-dhsjr-1/)では、`廣韻.csv`をHDIC（KRM）やDHSJRの音注データに接続する基本手順を解説しました。今回は、未収録・異体字問題を扱います。


## 未収録字のファイル

[`gy_dhsjr_link.py`](/downloads/scripts/gy_dhsjr_link.py)、`廣韻.csv`、`30-048-02_RMK.tsv`を用意して次を実行します。（python3で動作しない場合はpythonで実行してください）

```
python3 gy_dhsjr_link.py \
  --dhsjr 30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --outdir ./linked_out/
```

処理は瞬時に終わって、次のように表示されます。

```
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
処理中: 30-048-02_RMK.tsv
  → linked_out/30-048-02_RMK_gy_linked.tsv (27978 行)
  → linked_out/dhsjr_gy_unmatched.tsv (5628 行)
  → linked_out/dhsjr_gy_multi.tsv (6522 行)
完了。
```

生成された`dhsjr_gy_unmatched.tsv`が未収録字のファイルですが、このファイルを通覧すると、`30-048-02_RMK.tsv`の`単字_見出し`に明白な誤りがあることに気が付きました。

`単字_見出し`は1文字であるべきですが、これが2文字となっているものが36件（蕎麥、相工など）、3文字のものが1件（蘡薁藤）、4文字のものが1件（ー（蝳））、合計43件です。

また、HDICで公開している`krm_pronunciations.tsv`を精査すると、`30-048-02_RMK.tsv`とのレコードの有無に相違がありました。これを整理することにしました。

`30-048-02_RMK.tsv`に対して、次を追加し、

```
30001	(行全体)	(行全体)	<HDIC側にのみ存在する行>	
30002	(行全体)	(行全体)	<HDIC側にのみ存在する行>	
30003	(行全体)	(行全体)	<HDIC側にのみ存在する行>	
30004	(行全体)	(行全体)	<HDIC側にのみ存在する行>	
```

次を削除することにしました。
```
8002	(行全体)	(行全体)		<HDIC側にのみ存在する行>
12852	(行全体)	(行全体)		<HDIC側にのみ存在する行>
```

パッチファイルは、次からダウンロードできます。

[diff_30-048-02_RMK_20260626_revised.patch](/downloads/patches/diff_30-048-02_RMK_20260626_revised.patch)


古いファイル（`30-048-02_RMK.tsv`）がある場所と同じディレクトリに`diff_30-048-02_RMK_20260626_revised.patch` を配置し、次のコマンドを実行します。

```bash
patch 30-048-02_RMK.tsv < diff_30-048-02_RMK_20260626_revised.patch
```


これで `30-048-02_RMK.tsv` の中身が直接書き換えられ、最新の状態にアップデートされます。

もし、元の古いファイルを上書きせずに、別名で最新版のファイルを生成したい場合は、`-o` オプションを使用します。

```bash
patch -o updated_30-048-02_RMK.tsv 30-048-02_RMK.tsv < diff_30-048-02_RMK_20260626_revised.patch
```

## `gy_dhsjr_link.py`を再実行

パッチを当てた上で`gy_dhsjr_link.py`を再実行します。

```bash
python3 gy_dhsjr_link.py  --dhsjr updated_30-048-02_RMK.tsv --gy 廣韻.csv --outdir ./linked_out20260626

廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
処理中: updated_30-048-02_RMK.tsv
  → linked_out20260626/updated_30-048-02_RMK_gy_linked.tsv (27985 行)
  → linked_out20260626/dhsjr_gy_unmatched.tsv (5595 行)
  → linked_out20260626/dhsjr_gy_multi.tsv (6543 行)
完了。
```

`dhsjr_gy_unmatched.tsv`は5628行から5595行となったので、未収録を33件減らすことができました。

`dhsjr_gy_multi.tsv`は6522行から6543行となったので、21件を追加できました。

# dhsjr_gy_unmatched.blocks.tsv Unicode ブロック別集計


`dhsjr_gy_multi.tsv`にUnicodeの16進数番号と、CJK統合漢字やCJK統合漢字拡張Aなどの文字ブロックを与えるPythonスクリプト[check_blocks.py](/downloads/scripts/check_blocks.py)を用意して次を実行しました。


```bash
python3 check_blocks.py dhsjr_gy_unmatched.tsv dhsjr_gy_unmatched.blocks.tsv
```

概要をまとめるPythonスクリプト[summarize_gy_unmatched_blocks.py](/downloads/scripts/summarize_gy_unmatched_blocks.py)を作成して、調査しました。


```bash
python3 summarize_gy_unmatched_blocks.py
```

結果は次のとおりです。

対象ファイル: `dhsjr_gy_unmatched.blocks.tsv`
- 総行数: 5,595 行
- ブロック種類: 11 種

## 集計表

| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大5件） |
|---------|-----:|-----:|--------------:|--------------|
| CJK統合漢字拡張B | 2,093 | 37.4% | 1,775 | `𡔟` U+2151F、`𠌃` U+20303、`𠉶` U+20276、`𠇺` U+201FA、`𢘋` U+2260B |
| CJK統合漢字 | 1,403 | 25.1% | 969 | `内` U+5185、`偣` U+5063、`傡` U+50A1、`仌` U+4ECC、`仅` U+4EC5 |
| IDC | 1,346 | 24.1% | 1,207 | `⿰亻胃` U+2FF0、`⿰亻盈` U+2FF0、`⿰亻𢙣` U+2FF0、`⿰亻箄` U+2FF0、`⿰亻忍` U+2FF0 |
| CJK統合漢字拡張A | 539 | 9.6% | 434 | `㐻` U+343B、`䋕` U+42D5、`㑊` U+344A、`㐺` U+343A、`䖺` U+45BA |
| CJK統合漢字拡張F | 94 | 1.7% | 80 | `𬿺` U+2CFFA、`𬾉` U+2CF89、`𭀂` U+2D002、`𬽢` U+2CF62、`𭀅` U+2D005 |
| CJK統合漢字拡張C | 49 | 0.9% | 43 | `𪝀` U+2A740、`𪜾` U+2A73E、`𪾼` U+2AFBC、`𪮧` U+2ABA7、`𪭧` U+2AB67 |
| CJK統合漢字拡張E | 32 | 0.6% | 28 | `𫣗` U+2B8D7、`𫪦` U+2BAA6、`𫾂` U+2BF82、`𬂡` U+2C0A1、`𬂶` U+2C0B6 |
| 該当なし | 31 | 0.6% | 1 | `〓` U+3013 |
| CJK統合漢字拡張G | 4 | 0.1% | 4 | `𰧫` U+309EB、`𰢚` U+3089A、`𰊊` U+3028A、`𰢟` U+3089F |
| CJK統合漢字拡張H | 3 | 0.1% | 3 | `𱖞` U+3159E、`𱹫` U+31E6B、`𱵒` U+31D52 |
| CJK統合漢字拡張D | 1 | 0.0% | 1 | `𫞳` U+2B7B3 |

## 補足

- **IDC**（Ideographic Description Characters）: 漢字構成記述文字（⿰⿱ など）。実字ではなく字形の構造を表す記号です。
- **該当なし**: Unicode ブロックに分類されない文字。例として `〓`（U+3013、欠損記号）が含まれます。
- 件数は行数ベースです。同一文字が複数の資料番号に登場する場合、行として重複カウントされます。

ここで注意されるのは、CJK統合漢字が1,403 件あり、その中に内（U+5185）が見える点です。つまり`廣韻.csv`は「內（U+5167）」を見出しとしているため、マッチしなかったわけです。

こうした例は他にもあることが予想されます。マッチしなかったのは次のような例です。

```
倶  5036
偸  5078
値	5024
渉	6E09
卧	5367
畒	7552
伇	4F07
徳	5FB3
呉	5449
赱	8D71
黄	9EC4
説	8AAC
歳	6B73
間	9593
（他略）
```

##  単漢字異体字データテーブル

「內」と「内」とのような、異体字を対照したデータテーブルは、人間文化研究機構（NIHU）がNIHUデータカタログとして公開している「[単漢字異体字データテーブル](https://bridge.nihu.jp/accumulateddata_detail/18045149)」があります。これは、高田智和, 盛思超, 山田太造の三氏の作成により、利用ライセンス　CC BYで公開されています。作成日2012-01-01、登録日2022-12-02、最終更新日2026-02-20です。

CSV、TSV、XLSXの3形式で公開されていますが、ここではTSV形式の`異体漢字対応テーブル111220版_TSV221111.txt`を利用してみます。

冒頭の若干例を次に示します。

```tsv
整理番号        異体1   Unicode1        異体2   Unicode2        異体3   Unicode3        異体4   Unicode4
03473   㑇      3447    㑳      3473
0361A   㘎      360E    㘚      361A
0396E   㤘      3918    㥮      396E
```

## `gy_dhsjr_link.py`の異体字正規化オプション

`gy_dhsjr_link.py`には、異体字正規化オプションを用意しています。

>--itaiji は異体字TSV（NIHUテーブル等）のパス。複数ファイルをカンマ区切りで指定可能。
>--itaiji-json は異体字JSON（{"字A":"字B"} や {"字A":["字B","字C"]}、
>または [{"c1":"字A","c2":"字B"}] 形式のペアリスト）のパス。
>「新字・旧字」のような方向の区別は不要で、廣韻に収録されている側が
>自動的に正規化先として選ばれる。
>異体字正規化を行う場合、元の字形を GY_正規化前 列に記録する。

### 異体字TSVで実行

次を実行してみます。

```python
python3 gy_dhsjr_link.py \
  --dhsjr 30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji 異体漢字対応テーブル111220版_TSV221111.txt \
  --outdir ./linked_out_itaiji_nihu/
```

結果は次のとおりです。

```
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
異体字マップを構築中…
  [itaiji] NIHUテーブル読み込み: 異体漢字対応テーブル111220版_TSV221111.txt
  異体字マップ件数: 2128
処理中: 30-048-02_RMK.tsv
  → linked_out_itaiji_nihu/30-048-02_RMK_gy_linked.tsv (27978 行)
  → linked_out_itaiji_nihu/dhsjr_gy_unmatched.tsv (5480 行)
  → linked_out_itaiji_nihu/dhsjr_gy_multi.tsv (6557 行)
完了。
```

修正した`30-048-02_RMK.tsv`での結果と比べると、`dhsjr_gy_unmatched.tsv`は5595行から5480行となったので、未収録を15件減らすことができました。

`dhsjr_gy_multi.tsv`は6543行から6557行となったので、14件を追加できました。

### 異体字JSONで実行

`gy_sbgy_link.py`の`--itaiji-josn`オプションは次の三つの形式に対応しています。

### `--itaiji-json` の3形式（同一データでの書き分け）

俞↔兪、倐↔倏、値↔值のペアを例に、3形式すべてで同じ内容を表現する場合は次のようになります。

**形式1：`{"字A": "字B"}`（1対1のペア）**

```json
{
  "俞": "兪",
  "倐": "倏",
  "値": "值"
}
```

**形式2：`{"字A": ["字B", "字C", ...]}`（1対多も書けるリスト形式）**

```json
{
  "俞": ["兪"],
  "倐": ["倏"],
  "値": ["值"]
}
```

1対多の例（1つの字に複数の異体字がある場合）：

```json
{
  "俞": ["兪", "兪", "𠓻"]
}
```

**形式3：`[{"c1": "字A", "c2": "字B"}, ...]`（ペアのリスト形式）**

```json
[
  {"c1": "俞", "c2": "兪"},
  {"c1": "倐", "c2": "倏"},
  {"c1": "値", "c2": "值"}
]
```

補足すると、3形式とも、キー・値（または `c1`・`c2`）のどちらが先に書かれているかは判定に影響しません。`俞` と `兪` のどちらを先に書いても、最終的に廣韻に収録されている方が正規化先として選ばれます。

どの形式を選ぶかは作業のしやすさで決めて構いません。手作業で1件ずつ確認しながら追加するなら形式3（ペアのリスト）が見通しやすく、既存の辞書データから一括変換するなら形式1・2がコードで扱いやすいでしょう。

### KRM対応の異体字リスト

`dhsjr_gy_unmatched.tsv`を通覧して、UnicodeのCJK統合漢字で、異体字のペアありそうな例をピックアップしました。

KRMのCJK統合漢字内異体字ペア [itaiji_krm_unverified_20260626.json](/downloads/data/itaiji_krm_unverified_20260626.json)

このファイルを`gy_dhsjr_link.py`のオプションに指定して、実行結果は次のとおりです。

```bash
python3 gy_dhsjr_link.py  \
  --dhsjr updated_30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji-json itaiji_krm_unverified_20260626.json \
  --outdir ./linked_out/
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_krm_unverified_20260626.json
  異体字マップ件数: 45
処理中: updated_30-048-02_RMK.tsv
  → linked_out/updated_30-048-02_RMK_gy_linked.tsv (27985 行)
  → linked_out/dhsjr_gy_unmatched.tsv (5500 行)
  → linked_out/dhsjr_gy_multi.tsv (6559 行)
完了。
```

次に、廣韻と照合して、同字であることを確認したデータが`krm_notes.tsv`に多数記載されているので、それらを抽出整理した異体字リストを作成しました。

廣韻と同字確認済み異体字ペア[itaiji_krm_gy_attested.json](/downloads/data/itaiji_krm_gy_attested.json)

このファイルを`gy_dhsjr_link.py`のオプションに指定して、実行結果は次のとおりです。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr updated_30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji-json itaiji_krm_gy_attested.json \
  --outdir ./linked_out
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_krm_gy_attested.json
  異体字マップ件数: 1365
処理中: updated_30-048-02_RMK.tsv
  → linked_out/updated_30-048-02_RMK_gy_linked.tsv (27985 行)
  → linked_out/dhsjr_gy_unmatched.tsv (4058 行)
  → linked_out/dhsjr_gy_multi.tsv (7047 行)
完了。
```

次の二つを同時にすることもできます。

- KRMのCJK統合漢字内異体字ペア[itaiji_krm_unverified_20260626.json](/downloads/data/itaiji_krm_unverified_20260626.json)
- 廣韻と同字確認済み異体字ペア[itaiji_krm_gy_attested.json](/downloads/data/itaiji_krm_gy_attested.json)


実行結果は以下のとおりです。


```bash
python3 gy_dhsjr_link.py \
  --dhsjr updated_30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji-json itaiji_krm_unverified_20260626.json, itaiji_krm_gy_attested.json \
  --outdir ./linked_out
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_krm_unverified_20260626.json
  [itaiji] JSON読み込み: itaiji_krm_gy_attested.json
  異体字マップ件数: 1395
処理中: updated_30-048-02_RMK.tsv
  → linked_out/updated_30-048-02_RMK_gy_linked.tsv (27985 行)
  → linked_out/dhsjr_gy_unmatched.tsv (3989 行)
  → linked_out/dhsjr_gy_multi.tsv (7061 行)
完了。
```

さらに`異体漢字対応テーブル111220版_TSV221111.txt`も追加して指定してみます。


```bash
python3 gy_dhsjr_link.py \
  --dhsjr updated_30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji 異体漢字対応テーブル111220版_TSV221111.txt \
  --itaiji-json itaiji_krm_unv
erified_20260626.json, itaiji_krm_gy_attested.json \
  --outdir ./linked_out
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19586
異体字マップを構築中…
  [itaiji] NIHUテーブル読み込み: 異体漢字対応テーブル111220版_TSV221111.txt
  [itaiji] JSON読み込み: itaiji_krm_unverified_20260626.json
  [itaiji] JSON読み込み: itaiji_krm_gy_attested.json
  異体字マップ件数: 3501
処理中: updated_30-048-02_RMK.tsv
  → linked_out/updated_30-048-02_RMK_gy_linked.tsv (27985 行)
  → linked_out/dhsjr_gy_unmatched.tsv (3868 行)
  → linked_out/dhsjr_gy_multi.tsv (7092 行)
完了。
```

## 異体字オプション別の実行結果（処理行数の比較）

ここでは、前述した `gy_dhsjr_link.py` の実行結果を、**照合成功**（`*_gy_linked.tsv` の行数＝廣韻に接続できた行数）を中心に整理しました。入力はいずれも `updated_30-048-02_RMK.tsv` です。

| # | 異体字データ | マップ件数 | 照合成功 | 未収録 | 複数候補 | 未収録の削減※ |
|:-:|-------------|----------:|--------:|------:|--------:|-------------:|
| 0 | （なし・参照） | — | **27,985** | 5,595 | 6,543 | — |
| 1 | `itaiji_krm_unverified_20260626.json` | 45 | **27,985** | 5,500 | 6,559 | −95 |
| 2 | `itaiji_krm_gy_attested.json` | 1,365 | **27,985** | 4,058 | 7,047 | −1,537 |
| 3 | 上記2 JSON を併用 | 1,395 | **27,985** | 3,989 | 7,061 | −1,606 |
| 4 | NIHU TSV ＋ 上記2 JSON | 3,501 | **27,985** | 3,868 | 7,092 | −1,727 |

※ 未収録の削減は、#0（異体字なし）の 5,595 行との差です。

**読み方**

- **照合成功**（27,985 行）は4回とも変わりません。異体字正規化によって新たに一意に結び付いた行は、このデータセットでは増えませんでした。
- 異体字マップを増やすと、**未収録が減り**（最大 1,727 行削減）、**複数候補が増えます**（最大 +549 行）。未収録だった字が異体字経由で廣韻にヒットしますが、音韻地位が一意に定まらず複数候補側に振り分けられたと解釈できます。
- 効果が最も大きいのは `itaiji_krm_gy_attested.json`（#2）です。#1 の未検証ペア（45 件）の追加効果は小さく（未収録 −95）、#3・#4 は NIHU テーブル併用でさらに未収録を 121〜1,727 行削減します。


## おわりに

本稿(2)では、`gy_dhsjr_link.py`の異体字処理のためのオプションである
`--itaiji`と`--itaiji-json`の使い方を解説し、TSV形式の異体字データ、JSON形式の異体字データを使った結果を報告しました。

(1)で、観智院本類聚名義抄（30-048-02_RMK.tsv、27,978行）に適用した結果の概略は次のとおりでした。

| 状況 | 行数 | 比率 |
|---|---:|---:|
| 一意 | 15,828 | 56.6% |
| 複数音 | 6,522 | 23.3% |
| 未収録 | 5,628 | 20.1% |

今回、修正した観智院本類聚名義抄のデータ（updated_30-048-02_RMK.tsv、27,985行）に適用した結果の概略は次のとおりとなります。ここではNIHUのTSVファイルに自作のJSONファイル二つを適用した結果を示します。未収録は6.3%ほど減らすことに成功しました。

| 状況 | 行数 | 比率 |
|---|---:|---:|
| 一意 | 17,025 | 60.8% |
| 複数音 | 7,092 | 25.3% |
| 未収録 | 3,868 | 13.8% |


## 次回(3)予告

(1)と(2)では、`廣韻.csv`をベースに作業を進めてきましたが、(3)では、これに`sbgy.xml`を加えて、未収録字としたものがどこまで処理できるかを検討します。
