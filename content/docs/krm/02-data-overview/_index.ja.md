---
bookCollapseSection: true
weight: 2
title: "公開データの概要"
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 公開データの概要

## はじめに

このデータベースは、観智院本類聚名義抄（略称KRM）の全文をテキストデータベース化し、所在情報、本文校勘、出典考証などを行ったものであり、
平安時代漢字字書総合データベース（略称HDIC）を構成する漢字字書データベースのひとつである。

観智院本類聚名義抄は、十二世紀に成立した漢字の字書であり、真言宗の僧侶によって編纂された。
アクセントを示した和訓、詳細な漢字音の注記、異体字の注記を大量に収録することから、日本語史研究の
重要資料とされてきた。また、反切、意義注、字体注の漢文注記は、中国語学の資料としても注目されている。

2022年3月から公開していたが、2025年3月に、仕様の変更を行い、詳細な説明を施して改訂版を公開するものである。

## データファイル一覧

[https://github.com/shikeda/krm](https://github.com/shikeda/krm/)
で公開している観智院本類聚名義抄のデータは次のとおりである。
一部公開準備中のものを含む。

- [krm_main](./02-01-main/): 基本データ。掲出字、注文全文、所在などに関する情報を含む。TSVファイルとJSONファイルを公開。
- [krm_notes](./02-02-notes/): 注釈データ。掲出字、字体注、音注、意義注、和訓、その他に分類し、校勘と出典考証を行ったもの。TSVファイルとJSONファイルを公開。
- [krm_headword_chars](./02-03-krm-headword-chars/): すべての掲出字に関する詳細情報。風間版所在、天理版所在、画像ファイル名など。
- [krm_wakun](./02-04-wakun/): 和訓データ。和訓の異形、漢字の異体字、『日本国語大辞典第二版』の表記欄との対応に関する情報を含む。TSVファイルとJSONファイルを公開。
- [krm_definitions](./02-05-definitions/): 注文を字体注、音注、意義注、和訓、その他に分類したもの。TSVファイルを公開。公開済みの[KRM_definitions.tsv](https://github.com/shikeda/HDIC/KRM_definitions.tsv)に同じ。
- [krm_pronunciations](./02-06-pronunciations/): 音注に関してDHSJRとの連携をとるためのデータ（準備中）。
- [krm_ndl](./02-07-ndl/): 国会図書館デジタルコレクションへのリンク。TSVファイルを公開。公開済みの[KRM_ndl.tsv](https://github.com/shikeda/HDIC/KRM_ndl.tsv)に同じ。

2025年3月に大幅な仕様変更を行った。従来の公開ファイルは、
KRMを付していたが、仕様変更後のファイルは、krmを付すことに
した。

## 仕様変更

仕様変更の要点は次のとおりである。

- 仮名和訓の無声点を示す“@”を“_”に変更
- 濁音の声点を示す“"”を半角英字“V”に変更
- 有声点を示す半角()を全角（）に変更
- 誤字の訂正案を示す半角()を全角〔〕に変更
- 脱字を示す半角[]を全角［］に変更

仕様変更後のファイルは[https://github.com/shikeda/krm](https://github.com/shikeda/krm/)で公開した。

## ER図

次のER図は、krm_main、krm_notes、krm_wakun の三つのテーブル間の関係を示したものである。

![ER diagram.](/images/krmer.drawio.png)

なお、krm_notes.json は入れ子構造を持つデータであり、各レコードは複数の定義（definitions）の配列を内部に含んでいる。
この詳細な構造については、[別ページ](./02-02-notes)にて説明する。


![ER_notes図](/images/krm_notes_er.drawio.png)


## 共通情報

公開データのバージョン情報、作成者および著作権情報などの詳細は
次のGitHubリポジトリの `README_jp.md`ファイルに記してある。

[https://github.com/shikeda/krm](https://github.com/shikeda/krm/)

## 謝辞

観智院本類聚名義抄の解読テキストの公開について、御許可を賜った
天理図書館ならびに八木書店に感謝申し上げる。


この研究は日本学術振興会科学研究費補助金（課題番号16H03422、 19H00526、23K17500、25K00466）の成果の一部である。記して感謝の意を表す。
