---
title: "類聚名義抄"
weight: 1
# date: 2022-01-09
#bookFlatSection: true
#bookToc: true
# bookHidden: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 類聚名義抄全文テキストデータベース

## はじめに

『類聚名義抄』は日本古辞書の雄編として名高い。
書名の読み方は「るいじゅみょうぎしょう」である。
源順撰『倭名類聚抄』の「類聚」と、空海撰『篆隷万象名義』の
「名義」とを採用して書名としたとされる。


ここでは、まず『類聚名義抄』とその諸本の概要を述べる。
次に『類聚名義抄』の完本として唯一の伝本である
観智院本について、その項目の構造を解説し、
その後、観智院本の本文入力方法の詳細を述べる。


なお、ここでの解説は、 池田証壽・劉冠偉・鄭門鎬・張馨方・李媛「観智院本『類聚名義抄』全文テキストデータベース―その構築方法と掲出項目数等の計量―」(『訓点語と訓点資料』144、2020)に述べたところと重複するところがあるが、筆頭著者の池田が、全面的な見直しをはかり、用語を整理し、その後の調査内容を大幅に追加して新たにまとめ直したものである。

## 内容

第1章から第5章までが**Core Documentation**（中核文書）であり、KRMの項目データモデル・入力規則・注釈方針に関する主要な参照文書である。第6章から第9章は、組版設定・進捗記録・事例研究などの補足資料である。

- [資料紹介](/docs/krm/01-introduction/)
- [公開データの概要](/docs/krm/02-data-overview/)
    - [krm_main](/docs/krm/02-data-overview/02-01-main/)
    - [krm_notes](/docs/krm/02-data-overview/02-02-notes/)
    - [krm_headword_chars](/docs/krm/02-data-overview/02-03-headword-chars/)
    - [krm_wakun](/docs/krm/02-data-overview/02-04-wakun/)　
    - [krm_pronunciations](/docs/krm/02-data-overview/02-06-pronunciations/)　
    - [krm_ndl](/docs/krm/02-data-overview/02-07-ndl/)　
- [項目データモデル](/docs/krm/03-entry-data-model/)
    - [項目データ構造](/docs/krm/03-entry-data-model/03-01-data-structure/)
    - [項目の種類](/docs/krm/03-entry-data-model/03-02-types-of-entries/)
    - [文字表記に関する概念](/docs/krm/03-entry-data-model/03-03-concepts-char/)
    - [項目データファイルの例](/docs/krm/03-entry-data-model/03-04-data-example/)
- [項目データ入力](/docs/krm/04-entry-input/)
    - [掲出字・項目配置とID体系](/docs/krm/04-entry-input/04-01-id/)
    - [文字の符号化と表現](/docs/krm/04-entry-input/04-02-char/)
    - [書写・表記・注記における問題と対応](/docs/krm/04-entry-input/04-03-handling/)
- [注釈作成の基本方針](/docs/krm/05-annotation-policy/)
    - [注釈作成の基本方針と分析対象](/docs/krm/05-annotation-policy/05-01-basic-policy/)
    - [掲出字数の算出](/docs/krm/05-annotation-policy/05-02-headword-count/)
    - [字体注の種類と記載形式](/docs/krm/05-annotation-policy/05-03-jitaichu-formats/)
    - [音注の種類と解読上の問題点](/docs/krm/05-annotation-policy/05-04-onchu-problems/)
    - [義注の種類と数量](/docs/krm/05-annotation-policy/05-05-gichu-quantity/)
    - [和訓注釈のための基礎資料](/docs/krm/05-annotation-policy/05-06-wakun-materials/)
    - [注釈記述の具体例](/docs/krm/05-annotation-policy/05-07-annotation-examples/)
- [翻刻・注釈の組版の設定](/docs/krm/06-typesetting/)
    - [花園明朝の設定](/docs/krm/06-typesetting/06-01-hanazono-mincho/)
    - [GlyphWikiの設定](/docs/krm/06-typesetting/06-02-glyphwiki/)
    - [sfkanbun.styの設定](/docs/krm/06-typesetting/06-03-sfkanbun-sty/)
    - [古辞書・訓点資料のためのLuaTeX組版備忘録](/docs/krm/06-typesetting/06-04-vscode-texlive/)
    - [オンラインツール](/docs/krm/06-typesetting/06-05-online-tools/)
- [進捗状況](/docs/krm/07-progress/)
- [事例研究](/docs/krm/08-case-studies/)
- [構築の経緯](/docs/krm/09-development-history/)

## 謝辞

観智院本『類聚名義抄』全文テキストデータベースの構築と公開は、天理図書館当局から特別に御許可を賜り推進しているものであり、天理図書館善本叢書の版元である八木書店各位にも格別の御配慮を賜っている。ここに記して感謝の意を表する。


This work was supported by JSPS KAKENHI Grant Numbers 25370506, 16H03422, 19H00526, 23K17500, 25K00466 and 26K21717.
