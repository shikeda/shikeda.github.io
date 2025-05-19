---
title: "krm_wakun"
weight: 14
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# krm_wakun

## 概要とファイル形式

これは、名義抄デーベースの `KRM.tsv` から和訓を抜き出して、
和訓の異形を整理し、異体字との対応を調整したデータである。

和訓に関する校勘と出典考証は `krm_notes` に記載したので省略している。

和訓には、異なる読み方を傍書して併記する場合がある。

たとえば「倍」に「マサル」という和訓を付すが、「ル」の右に小さい片仮名で「ス」を傍書する。
これは「マサル」に加えて「マス」という和訓を注記したものである。

和訓にはジャパンナレッジ版『日本国語大辞典第二版』の情報を追加するので、
和訓の異形を併記する場合に対応する必要がある。

異体字との対応は、掲出字に異体字を示すことがあり、これを調整したものである。

たとえば、「ヤツカレ」という和訓は、掲出字「㒒／僕」の注文に見える。
和訓「ヤツカレ」は、「僕」に対する和訓であると同時に「㒒」に対する和訓となっている。
「爲」と「為」、「來」と「来」との関係も同様である。

ジャパンナレッジ版『日本国語大辞典第二版』には「表記」欄があり、名義抄の
漢字表記を収録しているので、これとの対応をとるための措置である。

2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字の KRM ではなく小文字の krm を用いて
`krm_wakun.tsv` と `krm_wakun.json`という名称とした。

## カラム名対照

新旧のカラム名を対照すれば次のようになる。

| New Column Name (v1.2.0) | Old Column Name (v1.1.97) |
|-------------------------|---------------|
| wakun_id                | KRID_wakun_no |
| definition_seq_id       | KRID_no       |
| kazama_entry_location   | KR2ID         |
| hanzi_entry             | Entry         |
| wakun_elements          | Def           |
| wakun_form              | Word_form     |
| wakun_standard_hanzi    | Wakun_Hanzi   |
| wakun_variant_in_hanzi  | Wakun_variant |
| variant_hanzi_for_wakun | Hanzi_variant |
| japan_knowledge_id      | JK_URL        |
| -           | Remarks       |

`Remarks` は `krm_notes` にまとめることとして、省略した。

## 各カラムの説明

次に、カラム名の内容を説明する。

| New Column Name (v1.2.0)           | Japanese Explanation            |
|-------------------------|-------------|
| wakun_id                | 和訓ID。kr_definition_sequence_idから、注文の種類が和訓のものだけを取り出したもの。変異形を追加したものには末尾にb, c, dを付した。        |
| definition_seq_id        | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。 |
| kazama_entry_location   | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| hanzi_entry                | 原文の漢字を校訂したもの。康熙字典体とするのを原則としたが、Unicodeで入力できる新字体（通用字体、俗字体）を残すこともある。                            |
| wakun_elements          | 注文の全文から、和訓の要素を一つずつ抜き出したもの。             |
| wakun_form           | 和訓の語形。活用のあるものは、助詞助動詞を除いて終止形とする。文選読みの「の」「と」は省略する。            |
| wakun_standard_hanzi         | 標準的な漢字による和訓表記。                            |
| wakun_variant_in_hanzi | 標準的な漢字による和訓の異形の表記。                |
| variant_hanzi_for_wakun    | 異体字による和訓の表記。                           |
| japan_knowledge_id      | ジャパンナレッジ版『日本国語大辞典第二版』にこの和訓が見出しとして存在する場合に、そのURLの後半、20020から末尾までの英数字を記載する。見出しとして存在しない場合は null と入力する。  |
