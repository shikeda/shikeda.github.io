---
title: 項目データ入力
weight: 4
bookToc: true
---

# 項目データの入力

観智院本類聚名義抄(KRM)の項目データの入力方法を解説する。

項目は掲出字と注文とからなる。
ここでは掲出字の入力と注文の入力とに共通する事項を説明する。


## Unicodeによる符号化

**説明**

UnicodeのバージョンによりCJK統合漢字の数は異なる。
HDICプロジェクトとしては2014年にスタートしており、
当初、基本に据えたのは2015年のUnicode 8.0.0であり、
使用できる漢字の数は、
CJK統合漢字とCJK統合漢字拡張A-Eの80,358字である。
その後も拡張が続いており、90,000字を超えるところまで
きている。ただ、Unicodeに収録されても、実際に画面に表示したり、
印刷したりして使えるようになるのは時間がかかるようである。JCK統合漢字
拡張Eまでを可能な限り利用し、拡張F以降は、備考欄などに注記するにとどめている。


Unicodeによっても入力できない例は、当面、漢字の部品を組み合せて示すIDS漢字構成記述文字列（Ideographic Description Sequence, 表意文字描述序列）により入力する。これをIDS入力と呼ぶ。
IDSは12字(⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻)のIDC漢字構成記述文字(Ideographic Description Character)を使用して示される。
IDSのデータは守岡知彦がCHISEで構築・公開しているものを利用・参照している。

IDSでも表現できない文字は■（黒い四角, U+25A0）を入力する。
虫損・判読不能の説明も参照されたい。

IDSで表現しにくい区別は近い字形とβ、γ等とを組み合せて記述することもある。
これをβ入力と呼ぶ。


**入力例**

    IDS入力の例：⿰亻胃
    βの例：正β(匸の中にヽが横に二つの字体)



## GlyphWikiの利用

**説明**

上地宏一氏のGlyphWikiで原文に
近似した明朝体の字形を表示するために
GlyphWiki（上地宏一氏）を利用する。

次にはmarkdownの記法で示す。

**入力例**

```markdown
![正β](https://glyphwiki.org/glyph/hdic_hkrm-01075140.png)
```

とすると、次のように表示される。

![正β](https://glyphwiki.org/glyph/hdic_hkrm-01075140.png)

これでは文字サイズが大きいので、小さいサイズを使う場合には

```markdown
![正β](https://glyphwiki.org/glyph/hdic_hkrm-01075140.50px.png)
```
とすれば、次のように表示される。

![正β](https://glyphwiki.org/glyph/hdic_hkrm-01075140.50px.png)


-------------
## 虫損・判読不能

**説明**

虫損（insect holes）で判読できない字や点画が複雑すぎてIDSの表現が困難な字を
「■」（黒い四角, U+25A0）として入力する。
虫損が一部で判読可能な字は「□(某)」のように示す。

**入力例**

-------------
## 複字形式の掲出字

**説明**

複字形式の掲出字の異体字併記と熟語は、掲出字を「／」（全角スラッシュ, U+FF0F）で区切って入力する。


**入力例**

    異体字併記：翛／倐／倏／翛β
    熟語：一／人

## 脱字

**説明**

脱字（omitted character, 脫字）であることが明らかな掲出字は、
「［］」（全角の角括弧）に入れて示す。

**入力例**

    将／[指]


## 誤字

**説明**
誤字（miswritten character, 誤字）であることが明らかな掲出字は、
校訂済みの字体をEntryに、原文の字体をEntry_originalに示し、備考欄に校訂の根拠を示す。

**入力例**

    Entry   Entry_original  Remarks
    向／後  〇／ー（彴）    掲出字は「向後」とすべきを誤る。岡田研究193-194頁に「ー」使用は高山寺本が適切との指摘あり。



## 符号
### 省略符号

**説明**
熟語の掲出字に見える省略符号（omission mark）「｜」は、
被注字（annotated headword, 被釋字）或いは前掲する掲出字を代用する時に使用される符号で、
「ー」（長音符, U+30FC）を用いて入力し、その後の「（）」（全角括弧）内に該当字を入力する。

**入力例**

    五／ー（人）

### 踊り字

**説明**

複字形式の掲出字に使われる踊り字（repetition mark, 疊字符）は
「〻」（二の字点, U+303B）を用いることとし、「々」（同の字点, U+3005）を用いない。

**入力例**

    曽／ー（祖）／〻（母）


### 本文訂正の符号

**説明**

転倒符（reverse mark, 顛倒符）を施して複字形式の掲出字の順序を正したり、見消符（deletion mark, 抹消符）を施して正しい掲出字を傍書（side note, 旁記）したり、補入符（interpolation mark, 補入符）を用いて掲出項目の順序を正したりすることがある。これらは正しい内容に修正して本文を入力する。

次の入力例では、注ごとに詳しい説明を施している。
項目データでは、どの箇所を訂正したのか、分かりにくいので、
注文の種類ごとに分割したデータとして、公開する予定である。

**入力例**

    Entry   Def Remarks
    儻／儻  コヒネカハクハ  西端誤写諸例54頁③文字のいれかわり818。高山寺本「コネヒカハクハ」の「ヒ」の右肩に転倒符あり、文字のいれかわりの誤りは解消済み（草川昇「類聚名義抄和訓小考」29頁）。


### 掲出字に施された声点等の注記

**説明**

掲出字に施された声点・仮名字音、傍訓、漢文注記、異本注記は、「掲出字補注」とし、それぞれ◎、⦿、◇、▲を付して示す。



## 複字形式の掲出字ID

**説明**

複字形式の掲出字IDは一番目の掲出字IDを代表として示し、
二番目以降の掲出字IDは公開するTSV形式のデータでは省略する。

掲出項目「AB」の「A」の掲出字IDがK08084411、「B」の掲出字IDがK08084412とすると、
公開するTSV形式のデータでは「A」の掲出字IDのK08084411だけ表示している。

