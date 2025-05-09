---
bookCollapseSection: true
weight: 2
title: 公開データの概要
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 公開データの概要

[https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC)
で公開している観智院本類聚名義抄のデータについて、その概要を解説する。

- [krm_main](/docs/notes/krm/02-data-overview/02-01-main/)
- [krm_notes](/docs/notes/krm/02-data-overview/02-02-notes/)
- [krm_headword_chars](/docs/notes/krm/02-data-overview/02-03-headword_chars/)
- [krm_wakun](/docs/notes/krm/02-data-overview/02-04-wakun/)　
- [krm_definitions](/docs/notes/krm/02-data-overview/02-05-definitions/)　
- [krm_pronunciations](/docs/notes/krm/02-data-overview/02-06-pronunciations/)　
- [krm_ndl](/docs/notes/krm/02-data-overview/02-07-ndl/)　

2025年3月に大幅な仕様変更を行った。従来の公開ファイルは、
KRMを付していたが、仕様変更後のファイルは、krmを付すことに
した。

仕様変更後のファイルはv1.2のフォルダーに置いた。これは一時的なものである。

仕様変更の要点は次のとおりである。

- 仮名和訓の無声点を示す“@”を“_”に変更
- 濁音の声点を示す“"”を半角英字“V”に変更
- 有声点を示す半角()を全角（）に変更
- 誤字の訂正案を示す半角()を全角〔〕に変更
- 脱字を示す半角[]を全角［］に変更

`krm_main`、`krm_notes`、`krm_wakun` の三つのテーブルの関係を図示すれば
次のようになる。

![ER diagram](/images/krmer.drawio.png)


さらに `krm_notes.json` は次に図示するような入れ子構造を持っている。

![ER_notes図](/images/krm_notes_er.drawio.png)