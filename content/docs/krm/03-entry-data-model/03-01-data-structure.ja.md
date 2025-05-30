---
title: "項目データ構造"
weight: 4
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 項目データ構造

ここでは、観智院本『類聚名義抄』（以下、名義抄と略）
の項目の構造と項目の形式を取り上げて解説する。

まず、掲出字・注文等の用語（概念）を定義し、
次に実際の項目の例を画像（模写）として掲げ、
その項目の構造を抽象化・図式化して示し、
最後に画像として示した項目の翻刻データを示す。


## 項目の構造

### 用語の説明

名義抄の項目を構成する要素を表現するための用語を次に説明する。

このセクションで括弧内に示した英訳の用語は
文献学的な観点から定義されており、そのためデータで使用されるカラム名や他のセクションの用語とは時折バリエーションが生じることがある。


**項目** (Entry) は**掲出字** (Headword) と**注文** (Original Glosses) からなる。

なお、「注文」の日本語の読み方は、「ちゅうもん」とすることが多いが、
文字や語の注釈であることを明示するために「ちゅうぶん」とすることもある。

掲出字は、見出し、見出字、標字、標出字とも呼ばれる。中国語では**字頭**と呼ぶ。

注文は、**音注** (Phonetic Gloss) 、**漢文義注** (Semantic Gloss in Chinese)、
**和訓** (Japanese native reading)、
**字体注** (Notes on Character Form) 、**その他** (Other) からなる。

音注は、反切、類音注、仮名音注、声点、その他の注記により施される。

漢文義注は、義注、漢文意味注ということもある。
誤解を生じない限り、単に**義注**とすることが多い。

和訓は、訓読みのことであり、和訓注ということもある。
片仮名により記される。「モノ」は「物」の略字「牜」、「コト」は合字「ヿ」を用いることがある。
万葉仮名を用いる例が1例ある（「木賊」に「度久佐」）。

字体注は、「正」「俗」等の字体規範を表す用語により注記される。

掲出字の周囲に施された漢文義注、片仮名などがあり、これらは**掲出字補注**と呼ぶことができる。
これらはその内容に応じて、音注、和訓等に分類した。データ化に際しては、
掲出字補注であることが明白となるような措置をとった
（「項目データ入力」セクションの「書写・表記・注記における問題と対応」の「掲出字補注」を参照）。

その他は、「**未詳**」とするもの、**伝写上の注記**、注文の種類が判断できないものなどである。



### 項目の例（画像）

次は、名義抄の具体例として、「加復」と「ー之」、「助」とその異体字、「功」の三つの
項目を模写して示したものである。

{{< figure src="/images/krm-item-sample1.png" alt="entry structure" width="500px" >}}


### 項目の構造の図示

次は、掲出字と注文のすべての要素が揃った項目の構造を図示したものである。

{{< mermaid title="Entry Structure" >}}
graph TB
    A(項目)
    A--->B(掲出字)
    A--->C(注文)
    C--->D(字体注)
    C--->E(音注)
    C--->F(義注)
    C--->G(和訓)
    C--->H(その他)
{{< /mermaid >}}


### 項目の例（翻刻）

次に、項目の例（画像）に挙げた三つの例を翻刻したものを示す。

まず、基本的な要素を備えた「功」を取り上げる。

**例**
```text
功　音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟
```
- 掲出字：功
- 注文の要素
    - 音注：音工（L-R）「コウ（_N）」「クウ（_N）」
    - 義注：續也　事也　成也
    - 和訓：タシカニ（LHLH）
    - 字体注：𭃄歟

このようにすると、掲出字と注文の要素との関係が分かりやすいであろう。
ただし、この項目の内容を詳細に説明するには多くの字数が必要である。
鍵括弧「」は補足的注記であり、
丸括弧()の中に示した符号は、声点と鼻音符号をローマ字に置き換えたものである。
その詳細は[項目データ入力](/docs/notes/krm/04-entry-input/)の
[書写・表記・注記における問題と対応](/docs/notes/krm/04-entry-input/04-03-handling/)を参照してもらうこととして、
ここでは省略する。

「功」の例と同様に、「加復」と「ー之」は次のように翻刻できる。

**例**
~~~text
加復　シカノミナラス  
ー之　同
~~~
- 掲出字：加復
- 注文の要素
    - 和訓：シカノミナラス
- 掲出字：ー（加）之
- 注文の要素
    - 和訓：同（シカノミナラス）

「ー之」の「ー」は直前の掲出字に用いられる「加」を代用した表記であるので、
掲出字「ー（加）之」と記載してみた。

最後に「助」とその異体字は次のように示される。

**例**
```text
⿰目力	鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）  
𦔳助	今正
```
- 掲出字：⿰目力
- 注文の要素
    - 音注：鉏據反
    - 和訓：タスク（LL_）　マサル（HH_）　ハサム
    - 音注：和自ヨ（_L）
- 掲出字：𦔳助
- 注文の要素
    - 字体注：今正

「加復」と「ー之」、「助」とその異体字の注文内容の解説は
多くの字数を必要とするので、ここでは割愛する。
