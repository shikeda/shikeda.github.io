---
title: "原典に見られる問題への対応"
weight: 4
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 原典に見られる問題への対応


## 原典に見られる問題への対応
### 虫損・判読不能

虫損（insect holes）で判読できない字や点画が複雑すぎてIDSの表現が困難な字を
「■」（黒い四角, U+25A0）として入力する。
虫損が一部で判読可能な字は「□(某)」のように示す。

次に入力例を示す。()内に補足説明を加える（以下同）。

**例:**  
-    再β／再γ	■／■ (右側のoriginal_entryに見える字形は「再」の異体字であるが、IDSの再現が困難。左側のentryにβ方式で関連字を示す)

ここに説明した「判読不能」を示す「■」の符号は、物理的に判読できない場合である。
点画が複雑すぎて、関連字を求め難く技術的に表現できない場合にも「■」の符号が
用いられる。
技術的に表現できない場合の詳細は[文字の符号化と表現](/docs/notes/krm-main/item-input/#文字の符号化と表現)セクションを参照。


### 脱字

脱字（omitted character, 脫字）であることが明らかな掲出字は、
「［］」（全角の角括弧）に入れて示す。

**例:**  
- 将／［指］ (手部の掲出字であり、文脈から「指」の脱字は明白)


### 誤字

誤字（miswritten character, 誤字）であることが明らかな掲出字は、
校訂済みの字体をentryに、原文の字体をoriginal_entryに示し、
krm_notesのremarksに校訂の根拠を示す
（krm_notesの詳細は[公開データの概要](/docs/notes/krm-main/contens/2-notes/)の当該項目を参照）

entry、original_entry、remarksの順に例示する。

**例:**  
-    向／後  〇／ー（彴）    掲出字は「向後」とすべきを誤る。岡田研究193-194頁に「ー」使用は高山寺本が適切との指摘あり。

