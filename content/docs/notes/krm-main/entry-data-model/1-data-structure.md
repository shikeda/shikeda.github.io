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
以前に英訳した用語を再検討し、それらを（）内のように改めた。

**項目** (Entry) は**掲出字** (Headword) と**注文** (Original Glosses) からなる。

掲出字は、見出し、見出字、標字、標出字とも呼ばれる。中国語では字頭と呼ぶ。

注文は、**音注** (Phonetic Gloss) 、**漢文義注** (Semantic Gloss in Chinese)、
**和訓** (Japanese native reading)、
**字体注** (Notes on Character Form) 、**その他** (Other) からなる。

漢文義注は、義注、漢文意味注ということもある。
誤解を生じない限り、単に**義注**とすることが多い。

和訓は、訓読みのことであり、和訓注ということもある。

掲出字の周囲に施された漢文義注、片仮名などがあり、これらは**掲出字補注**と呼ぶことができる。
これらはその内容に応じて、音注、和訓等に分類した。データ化に際しては、
掲出字補注であることが明白となるような措置をとった（詳細後述）。

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

>功　音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟

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
その詳細は[注文データ入力の詳細](/docs/notes/krm_main/def_input/)を参照してもらうこととして、
ここでは省略する。

「功」の例と同様に、「加復」と「ー之」は次のように翻刻できる。

>加復　シカノミナラス
>ー之　同

- 掲出字：加復
- 注文の要素
    - 和訓：シカノミナラス
- 掲出字：ー（加）之
- 注文の要素
    - 和訓：同（シカノミナラス）

「ー之」の「ー」は直前の掲出字に用いられる「加」を代用した表記であるので、
掲出字「ー（加）之」と記載してみた。

最後に「助」とその異体字は次のように示される。

>⿰目力	鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）  
>𦔳助	今正

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

 
# Entry Data Structure

Here, we explain the **entry structure** and **entry format** of the Kanchi-in manuscript *Ruiju Myōgishō* (hereafter abbreviated as *Myōgishō*).

First, we define key terms (concepts) such as **Headword** and **Original Glosses**. Next, we present a **visual example** of an actual entry example. Then, we provide a diagram illustrating its structure. Finally, we show the transcribed data corresponding to the example entry shown in the image.

## Entry Structure

### Terminology

The terminology used to describe the elements composing an entry in the *Myōgishō* is explained below.
We have reconsidered previously translated English terms and revised them as shown below in parentheses.

An **Entry** consists of a **Headword** and the **Original Glosses**.

**Headword** is also referred to in Japanese as *midashi*, *midashiji*, *hyōji*, or *hyōshutsuji*. In Chinese, the corresponding term is *zìtóu* (字頭).

The **Original Glosses** comprise: **Phonetic Gloss**, **Semantic Gloss in Chinese**, ***Wakun*** (Japanese native reading), **Note on Character Form**, and **Other**.

**Semantic Gloss in Chinese** is sometimes also referred to as *Gichū* or *Kanbun Imichū*. Provided there is no risk of ambiguity, it is often simply referred to as ***Gichū***.

***Wakun*** refers to *kun'yomi* (Japanese native readings) and may sometimes be called ***Wakunchū***.

There are semantic glosses (in Chinese), katakana phonetic notations, etc., written around the headword; these can be termed **Supplementary Headword Annotations** (掲出字補注 *Keishutsuji Hochū*). According to their content, these were classified into the main categories such as **Phonetic Gloss** or ***Wakun***. During data creation, measures were taken to clearly identify these as Supplementary Headword Annotations (details to follow).

The **Other** category includes items such as: those marked '**unclear**' (未詳 *mishō*), **notes related to textual transmission** (scribal notes), and glosses whose type could not be determined.

### Example Entry (Image)

Below, we present visual representations of three example entries from the Myōgishō: '加復', 'ー之', '助' and its variant forms, and '功'.

{{< figure src="/images/krm-item-sample1.png" alt="entry structure" width="500px" >}}


### Entry Structure Diagram

The diagram below illustrates the structure of a complete entry, featuring all components associated with the Headword and the Original Glosses.

{{< mermaid title="Entry Structure" >}}
graph TB
    A(Main Item)--->B(Headword)
    A-->C("Original Gloss")
    C-->D("Note on Character Form")
    C-->E(Phonetic Gloss)
    C-->F("Semantic Gloss (in Chinese)")
    C-->G("Wakun (Japanese native reading)")
    C-->H(Other)
{{< /mermaid >}}

### Example Entry (Transcription)

First, let's consider the entry for '功', which includes the basic components.

> 功　音工 (L-R)「コウ (\_N)」「クウ (\_N)」　續也　事也　成也　タシカニ (LHLH)　𭃄歟

  * **Headword:** 功
  * **Elements of Original Glosses:**
      * **Phonetic Gloss:** 音工 (L-R)「コウ (\_N)」「クウ (\_N)」
      * **Semantic Gloss:** 續也　事也　成也
      * ***Wakun*:** タシカニ (LHLH)
      * **Note on Character Form:** 𭃄歟

Presented this way, the relationship between the **Headword** and the elements of the **Original Glosses** should be clear.
However, explaining the content of this entry in detail would be lengthy.
The brackets「 」indicate supplementary notes, and the symbols shown within parentheses ( ) are Roman letter representations of the original tone marks and nasal sound symbols.
Detailed explanations are omitted here; please refer to [Details of Original Gloss Data Input](https://www.google.com/search?q=/docs/notes/krm_main/def_input/) for further information.


Similar to the example for '功', the entries for '加復' and 'ー之' can be transcribed as follows:

> 加復　シカノミナラス
> ー之　同

* **Headword:** 加復
* **Elements of Original Glosses:**
    * ***Wakun*:** シカノミナラス
* **Headword:** ー(加)之
* **Elements of Original Glosses:**
    * ***Wakun*:** 同 (Same as above: シカノミナラス)

Since the 'ー' in 'ー之' is a notation substituting for '加' from the preceding headword, we have represented this headword in the breakdown as 'ー(加)之'.


Finally, the entry for '助' and its variant form(s) is shown as follows:

> ⿰目力    鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）  
> 𦔳助     今正

* **Headword:** ⿰目力
* **Elements of Original Glosses:**
    * **Phonetic Gloss:** 鉏據反
    * ***Wakun*:** タスク (LL_), マサル (HH_), ハサム
    * **Phonetic Gloss:** 和自ヨ (_L)
* **Headword:** 𦔳助
* **Elements of Original Glosses:**
    * **Note on Character Form:** 今正

A detailed explanation of the content of the original glosses for '加復', 'ー之', and '助' and its variant form(s) would require considerable space and is therefore omitted here.

## Entry Format

