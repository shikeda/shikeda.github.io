---
title: "注釈データ入力の詳細"
# 掲出字と注文の分類
weight: 16
# bookFlatSection: false
# bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# 注釈作成の基本方針

名義抄の注釈には、
校勘、出典考証、研究史整理、語釈、余説などが含まれる。それぞれの内容を解説すれば、次のとおりである。

- 校勘：諸本本文・逸文との校異を示し比較考証し、伝写上の誤りを正して本来の本文を再構成する。
- 出典考証：引用原典を探索してその引用法の分析し、直接引用・間接引用（孫引き）の別も明らかにする。
- 研究史整理：諸先学による見解を要約紹介する。
- 語釈：語義、音韻、表記に関する語学的分析を行う。
- 余説：注釈者の考察である。当該の項目の分析から判明した事項を詳細に述べる。

注釈は、簡潔明瞭であることが理想であるが、その前段階として、注釈に必要な材料を可能な限り集めることが
必要であり、その準備が整った後に、収集した材料を取捨選択する作業に入ることができる。

現在までに収集した材料は、データベース作成者による注釈（`Compiler's Remarks`）として
`krm_notes`の`remarks`カラムに記載している。

ここでは、まず項目を掲出字と注文各種に分類し、それらの数量を示す。
その上で、掲出字の種類と注文の種類毎に注釈の作成の重要度を検討し、分析対象を和訓と
音注に絞ることを述べて、**注釈作成の基本方針と分析対象**を明確にする。


次に、誤字、脱字、衍字などの具体例をあげて解説し、それらの情報を
データベース作成者による注釈（`Compiler's Remarks`）にどのように記載したかを
紹介し、**掲出字数の算出**を行う。

**字体注**は、その**種類と記載形式**を整理して、字体注の内容・形式を明確化することで、
データベース作成者による注釈（`Compiler's Remarks`）での言及を最小限にする。

**義注**は、その**種類と数量**を示し、片仮名と誤認された義注の例を紹介する。

**和訓**は、先行研究が数多いので、その一覧とデータベース作成者による注釈（`Compiler's Remarks`）で用いる
略称を整理し、**和訓注釈のための基礎資料**を紹介する。

最後に、観智院本類聚名義抄の仏上62頁を**注釈記述の具体例**として、
データベース作成者による注釈（`Compiler's Remarks`）の内容を紹介する。
そこでは、GlyphWikiの利用により、漢字字形の微妙な差を注釈で説明できることを示す。

- [注釈作成の基本方針と分析対象](./05-01-basic-policy/)
- [掲出字数の算出](./05-02-headword-count/)
- [字体注の種類と記載形式](./05-03-jitaichu-formats/)
- [音注の種類と解読上の問題点 ](./05-04-onchu-problems/)
- [義注の種類と数量](./05-05-gichu-quantity/)
- [和訓注釈のための基礎資料](./05-06-wakun-materials/)
- [注釈記述の具体例](./05-07-annotation-examples/)