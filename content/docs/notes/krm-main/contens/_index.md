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
で公開している観智院本類聚名義抄のデータについて、その概要を
解説する。

- [krm_main](/docs/notes/krm-main/contens/1_main/)
- [krm_notes](/docs/notes/krm-main/contens/2_notes/)　
- [krm_wakun](/docs/notes/krm-main/contens/3_wakun/)　
- [krm_definitions](/docs/notes/krm-main/contens/4_definitions/)　
- [krm_pronunciations](/docs/notes/krm-main/contens/5_pronunciations/)　
- [krm_ndl](/docs/notes/krm-main/contens/6_ndl/)　

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

krm_main、krm_notes、krm_wakunの三つのテーブルの関係を図示すれば
次のようになる。

![ER図](/images/krmer.drawio.png)