---
title: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(6)"
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
summary: "前回の連載(5)では、DHSJR側のunmatched例を精査し、IDS表記のUCS変換や一部の入力修正を行いました。今回の(6)では、--itaiji-json に指定する異体字JSONを整理し、修正後データに gy_dhsjr_link.py を再実行した結果を検討します。"
---


## はじめに

前回の
[宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(5)](/posts/sbgy-phonological-data-linking-to-hdic-and-dhsjr-5/)
では、`gy_dhsjr_link.py` が出力する `dhsjr_gy_unmatched.tsv` をもとに、
廣韻データに接続できなかった字を精査しました。

その過程で、DHSJR側の `単字_見出し` に含まれる入力ミスや、
`⿰土虒` のようなIDS表記を、すでにUnicodeに符号化されている文字
`𡏚` に置き換えられる例があることを確認しました。
これらはDHSJR側の個別TSVに反映しました。

今回は、修正後のDHSJRデータに対して `gy_dhsjr_link.py` を再実行し、
さらに `--itaiji-json` に指定する異体字JSONを追加した場合に、
`unmatched` と `multi` がどのように変化するかを確認します。

なお、この記事で扱う異体字JSONの一覧は、
[`--itaiji-json` 用JSONファイル目録](/posts/itaiji-json-inventory/)
として別に整理しました。各ファイルの由来や利用上の注意を確認したい場合は、
そちらも参照してください。

ここでいう `unmatched` は、DHSJR側の見出し字が廣韻データに見つからなかった行です。
一方、`multi` は、廣韻側に複数の音韻地位候補があり、一意に決められなかった行です。
異体字対応を増やすと `unmatched` は減りますが、同時に `multi` が増えることがあります。
この関係をどう読むかが、本稿の中心です。

## `--itaiji-json`とは何か

[`gy_dhsjr_link.py`](/downloads/scripts/gy_dhsjr_link.py) は、DHSJRの `単字_見出し` を `廣韻.csv` の `字頭` と照合します。
しかし、実際には同じ字種であっても、データごとに字体や符号位置が異なることがあります。

たとえば、DHSJR側に `内` があり、廣韻側には `內` がある場合、
そのままでは一致しません。このような関係を異体字ペアとして与えるためのオプションが
`--itaiji-json` です。

`--itaiji-json` では、次のようなJSONファイルを指定できます。

```json
[
  {
    "c1": "内",
    "c2": "內"
  }
]
```

この形式は、ここでは「c1/c2形式」または単に「ペア形式」と呼ぶことにします。
`c1` と `c2` というキー名は一般的なペア表現であり、特定の公開仕様に基づく名称ではありません。

重要なのは、`gy_dhsjr_link.py` が `c1` と `c2` の方向を固定的には扱わない点です。
ペアの中で、廣韻に収録されている側を正規化先として選びます。
したがって、廣韻に対応すると判断した字のペアを入れておけば、
どちらを `c1` に書くか、どちらを `c2` に書くかは、処理上の本質ではありません。

ただし、これは「何でも異体字として入れてよい」という意味ではありません。
ペアにした字が本当に同一字種として扱えるかどうかは、別途確認が必要です。

## これまでに作成した異体字JSON

作業を進めるうちに、`--itaiji-json` に指定できるJSONファイルが増えてきました。
主なものを整理すると次のようになります。

| ファイル名 | 件数 | 内容 |
|---|---:|---|
| [`itaiji_gy_compare.json`](/downloads/data/itaiji_gy_compare.json) | 870 | `廣韻.csv` と `sbgy.xml` の字頭差分から作成 |
| [`itaiji_jisx0213.json`](/downloads/data/itaiji_jisx0213.json) | 1,320 | CJKVI `jisx0213-variants.txt` 由来 |
| [`itaiji_cjkv_simplified-variants.json`](/downloads/data/itaiji_cjkv_simplified-variants.json) | 16,786 | CJKV系の簡体字・異体字対応 |
| [`itaiji_jp-old.json`](/downloads/data/itaiji_jp-old.json) | 1,093 | 日本語新旧字体対応 |
| [`itaiji_krm_gy_attested.json`](/downloads/data/itaiji_krm_gy_attested.json) | 1,618 | KRM側で廣韻同字確認済みとみなしたペア |
| [`itaiji_krm_unverified_20260626.json`](/downloads/data/itaiji_krm_unverified_20260626.json) | 60 | KRM未検証ペア |
| [`gy_kakko_itaiji.json`](/downloads/data/gy_kakko_itaiji.json) | 238 | 廣韻字頭の `主字〈異体字〉` 表記から作成 |
| [`checked_unmatched_chars_in_cjkvi_variant.json`](/downloads/data/checked_unmatched_chars_in_cjkvi_variant.json) | 4,002 | CJKVI variants 系データで確認した候補 |

これらはすべて同じ性格のデータではありません。
`itaiji_gy_compare.json` や `itaiji_jisx0213.json` は比較的説明しやすい由来を持っています。
一方、`checked_unmatched_chars_in_cjkvi_variant.json` は、未照合字をCJKVI variants系データに照らして作った候補であり、
そのまま「確定した異体字対応」とみなすには慎重さが必要です。

このため、当面はこれらを一つの巨大なJSONに統合せず、
由来別のファイルとして管理する方針にしています。
どのファイルを足したときに、どれだけ `unmatched` が減り、
どれだけ `multi` が増えるかを追跡できるようにするためです。

## 廣韻字頭の `主字〈異体字〉` 表記

今回追加したJSONの一つに、`gy_kakko_itaiji.json` があります。

`廣韻.csv` の `字頭` には、次のような表記があります。

```text
爼〈俎〉
䭾〈馱〉
皷〈鼓〉
```

これは、人間が読むには「爼と俎は関連する字である」と分かります。
しかし、プログラムから見ると、`爼〈俎〉` は一つの文字列です。
DHSJR側に `爼` や `俎` が単独で出てきても、
`爼〈俎〉` というキーとは一致しません。

そこで、`廣韻.csv` の `主字〈異体字〉` 形式を走査し、
主字と括弧内字をペアにしたJSONを作成しました。
最終的には次のような形式です。

```json
[
  {
    "c1": "俎",
    "c2": "爼"
  }
]
```

このファイルが `gy_kakko_itaiji.json` です。
238ペア、重複なしのペアリストとして作成しました。

このJSONは、廣韻側の字頭欄に埋め込まれた異体字情報を、
`gy_dhsjr_link.py` が利用できる形に取り出したものと言えます。

## CJKVI variants から候補を作る

次に、残った `unmatched` のうち、IDC表記や記号を除いた漢字だけを取り出し、
CJKVI variants 系データに含まれるかどうかを調べました。

まず、`dhsjr_gy_unmatched.tsv` にUnicodeブロック情報を付与し、
重複を整理した上で、IDC・記号類を除いた文字リストを作ります。

```bash
sort -u dhsjr_gy_unmatched.blocks.tsv > unmatched_uniq.tsv

awk -F'\t' '$2 !~/[⿰-⿿_□■〓シデ々]/ {print $2}' unmatched_uniq.tsv |
sort -u > unmatched_char.tsv
```

この `unmatched_char.tsv` を、
`~/codex/cjkvi-variants/` 配下の各種 variant ファイルに照合しました。
ただし、簡体字対応をそのまま入れると、対応範囲が広くなりすぎる可能性があります。
そこで、今回はファイル名に `variant` を含み、`simpl` を含まないものに絞りました。

```bash
python3 check_unmatched_chars_in_cjkvi.py |
grep 'variant' |
grep -v 'simpl' > checked_unmatched_chars_in_cjkvi_variant.tsv
```

その後、候補を `c1/c2` 形式のJSONに変換し、
`checked_unmatched_chars_in_cjkvi_variant.json` を作成しました。

このファイルは4002件あります。
数が多く効果も大きいのですが、候補性の強いデータです。
したがって、これは「確定版の異体字表」というより、
残る `unmatched` をさらに調べるための作業用リストと見るべきでしょう。

## 再実行コマンド

以上を踏まえ、今回は次のように `gy_dhsjr_link.py` を実行しました。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr-dir ~/Hdic_data/DHSJR/data \
  --gy 廣韻.csv \
  --itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_unverified_20260626.json,gy_kakko_itaiji.json,checked_unmatched_chars_in_cjkvi_variant.json \
  --outdir ./linked_out_dhsjr_all_cjkv-jp4
```

`--dhsjr-dir` には、DHSJRの個別TSVが入ったディレクトリを指定します。
結合済みの `DHSJR_data_all.tsv` ではなく、
`~/Hdic_data/DHSJR/data` 配下の個別TSVを対象にしている点が重要です。

実行時には次のように表示されました。

```text
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  [itaiji] JSON読み込み: itaiji_cjkv_simplified-variants.json
  [itaiji] JSON読み込み: itaiji_jp-old.json
  [itaiji] JSON読み込み: itaiji_krm_unverified_20260626.json
  [itaiji] JSON読み込み: gy_kakko_itaiji.json
  [itaiji] JSON読み込み: checked_unmatched_chars_in_cjkvi_variant.json
  異体字マップ件数: 9563
```

ここでの「異体字マップ件数」は、JSONファイルに含まれる行数の単純合計ではありません。
廣韻側に実際に接続できる形に正規化された後のマップ件数です。

## 実行結果

最終的な出力は次のとおりです。

```text
→ linked_out_dhsjr_all_cjkv-jp4/dhsjr_gy_unmatched.tsv (3480 行)
→ linked_out_dhsjr_all_cjkv-jp4/dhsjr_gy_multi.tsv (104847 行)
完了。
```

連載(4)で得た最終条件では、`unmatched` は7523行、`multi` は103586行でした。
今回の再実行結果と比べると、次のようになります。

| 条件 | `unmatched` | `multi` |
|---|---:|---:|
| (4) 最終条件 | 7,523 | 103,586 |
| 今回 | 3,480 | 104,847 |
| 差分 | **−4,043** | **+1,261** |

`unmatched` は4043行減りました。
一方で、`multi` は1261行増えました。

これは、異体字JSONを追加することで、これまで廣韻に接続できなかった字が、
何らかの廣韻字頭に接続できるようになったことを示します。
ただし、その接続先が複数の音韻地位を持つ場合、一意照合ではなく `multi` に入ります。

したがって、`multi` の増加は単純な悪化ではありません。
むしろ、これまで「未収録」として見えていなかった問題が、
「複数候補の中からどれを選ぶか」という、次の段階の問題として見えるようになったと考えるべきです。

## baselineから見た変化

連載(4)では、異体字マップを指定しない baseline の結果を次のように示しました。

| 条件 | `unmatched` | `multi` |
|---|---:|---:|
| baseline | 22,012 | 98,047 |
| (4) 最終条件 | 7,523 | 103,586 |

今回の結果を加えると、次のようになります。

| 条件 | `unmatched` | baseline比 | `multi` | baseline比 |
|---|---:|---:|---:|---:|
| baseline | 22,012 | — | 98,047 | — |
| (4) 最終条件 | 7,523 | −14,489 | 103,586 | +5,539 |
| 今回 | 3,480 | **−18,532** | 104,847 | **+6,800** |

baselineから見ると、`unmatched` は22,012行から3,480行まで減りました。
これは18,532行の減少で、約84%の削減です。

一方、`multi` は98,047行から104,847行へ増えました。
差分は6,800行です。

この数字は、異体字対応によって接続できる字が大幅に増える一方で、
その分、音韻地位の候補を精査すべき行も増えることを示しています。

## `unmatched` と `multi` をどう読むか

ここで注意したいのは、`unmatched` の減少だけを成果と見ないことです。

たとえば、あるDHSJR見出し字が異体字マップによって廣韻のある字に接続されたとします。
その字が廣韻で一つの音しか持たなければ、一意照合になります。
しかし、廣韻に複数の音が登録されていれば、`multi` になります。

つまり、異体字マップを追加した結果は、おおまかに次の二つに分かれます。

1. `unmatched` から一意照合へ移る
2. `unmatched` から `multi` へ移る

前者はそのまま照合精度の改善と言えます。
後者は、未収録だった字が候補付きで拾えるようになった状態です。
これは未解決ではありますが、情報量は増えています。

人文学のデータ処理では、このような「完全自動で決まらないが、候補が見えるようになる」段階が重要です。
人間が確認すべき対象を絞り込めるからです。

## 広い異体字マップの危うさ

今回もっとも注意が必要なのは、
`checked_unmatched_chars_in_cjkvi_variant.json` の扱いです。

このファイルは、CJKVI variants 系データを使って、未照合字に関連しそうな字を拾ったものです。
4002件と件数が多く、`unmatched` を大きく減らす力があります。

しかし、対応範囲が広いということは、過剰に結び付ける危険もあるということです。
同じ「variant」とされる関係でも、音韻接続のために使ってよい関係かどうかは別問題です。

今回の結果は、候補発見としては有用です。
ただし、最終的な研究データとして採用するには、
`dhsjr_gy_multi.tsv` や `dhsjr_gy_unmatched.tsv` の具体例を確認し、
どの対応が妥当かを吟味する必要があります。

特に、CJKV系の異体字表や簡体字表は、対応関係が一対一とは限りません。
文字コード上の関連字であっても、音韻史の接続先として常に適切とは限らない点に注意が必要です。

## KRMはなお難しい

今回の処理により、DHSJR全体の `unmatched` は大きく減りました。
しかし、類聚名義抄（KRM）に関係する資料では、依然として難しい例が残ります。

KRMには、Unicode拡張漢字、IDS表記、俗字、廣韻にそのまま見えない字形が多く含まれます。
これは単純な異体字マップだけで解決できる問題ではありません。

異体字JSONによる処理は、あくまで「廣韻にある字と結び付けられるもの」を拾う方法です。
廣韻に対応字がない、あるいは字形の認定自体が難しい場合には、
別の検討が必要になります。

## 今後の課題

今回の結果を踏まえると、次の作業が必要です。

1. `checked_unmatched_chars_in_cjkvi_variant.json` の4002候補を精査する。
2. `gy_kakko_itaiji.json` の238ペアについて、廣韻字頭の併記情報として妥当か確認する。
3. `dhsjr_gy_multi.tsv` の具体例を見て、異体字マップ追加による `multi` 増加の中身を分類する。
4. `unmatched` に残った3480行を、Unicode拡張字・IDS表記・廣韻未収録字・入力上の問題に分けて確認する。
5. 声点情報や `--sgy` オプションを使って、`multi` の候補をさらに絞り込めるか検討する。

特に重要なのは、`multi` の精査です。
これまでは `unmatched` を減らすことを主な目標にしてきました。
しかし、ここまで未収録が減ってくると、次は「複数候補のうち、どれが実際の音注に合うのか」を見る段階になります。

## おわりに

本稿では、DHSJR側の修正後データに対して、
`--itaiji-json` に指定する異体字JSONを追加しながら `gy_dhsjr_link.py` を再実行しました。

その結果、`unmatched` は連載(4)の7523行から3480行へ、さらに4043行減少しました。
baselineから見ると、22,012行あった `unmatched` は3,480行まで減り、
約84%を削減できたことになります。

一方で、`multi` は104,847行まで増加しました。
これは、異体字マップを広げるほど、未収録だった字が候補付きで拾えるようになる反面、
音韻地位を一意に決める作業が次の課題として前面に出てくることを意味します。

つまり、作業は「照合できるかどうか」から、
「照合候補のうち、どれが妥当か」へ移りつつあります。

次回は、`dhsjr_gy_multi.tsv` の具体例を見ながら、
異体字マップによって増えた複数候補をどう評価するかを検討したいと思います。
