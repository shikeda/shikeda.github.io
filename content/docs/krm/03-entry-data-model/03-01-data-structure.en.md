---
title: "Entry Data Structure"
weight: 4
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Entry Data Structure


This section explains the structure and format of entries in the Kanchi-in manuscript of the *Ruiju Myōgishō* (hereinafter *Myōgishō*).

It begins by defining key terms (and related concepts) such as **Headword** (掲出字, *keishutsuji*) and **Original Glosses** (注文, *chūmon*). Next, an example of an actual entry is presented as an image (a facsimile). The structure of this entry is then illustrated in an abstract and diagrammatic form. Finally, a transcription of the entry shown in the image is provided.

Regarding the Japanese reading of "注文," although we have adopted "*chūmon*," it may also be read as "*chūbun*" to explicitly indicate that it refers to annotations on characters or words.

## Structure of Entries

### Explanation of Terms

The following explains the terms used to describe the constituent elements of entries in the *Myōgishō*.

The terminology herein is defined from a philological viewpoint, which may occasionally result in variations from the column names used in the data or terms in other sections.

An **Entry** consists of a **Headword** and **Original Glosses**.

A **Headword** (掲出字) is also referred to as *midashi*, *midashiji*, *hyōji*, or *hyōshutsushi*. In Chinese, it is called *zìtóu* (字頭).

**Original Glosses** consist of the following components: **Phonetic Gloss** (音注, *onchū*), **Semantic Gloss in Chinese** (義注, *gichū*), **Japanese native reading** (和訓, *wakun*), **Notes on Character Form** (字体注, *jitaichū*), and **Other**.

A **Phonetic Gloss** is provided through methods such as *fanqie* spelling (反切), similar pronunciation annotation by character (類音注), pronunciation annotation by kana (片仮名音注), *shōten* (声点, tone marks), and other notations.

A **Semantic Gloss in Chinese** is also sometimes referred to as *gichū* (義注, semantic gloss) or *kanbun imichū* (漢文意味注, semantic gloss in Chinese). Unless it causes misunderstanding, it is often simply referred to as **Semantic Gloss** (義注).

A **Japanese native reading** (*wakun*) refers to *kun'yomi* (native Japanese readings of Chinese characters) and is also sometimes called *wakunchū* (Japanese native reading glosses). It is generally written in Katakana. For example, 'mono' may be written with the abbreviated character '牜' (a variant of 物), and 'koto' may use the ligature 'ヿ'. There is one instance where *Man'yōgana* is used (e.g., '度久佐' for '木賊').

**Notes on Character Form** are indicated using terms such as '正' (standard) or '俗' (popular).

There are semantic glosses in Chinese, Katakana, etc., written around the headword; these can be termed **Supplementary Headword Annotations** (掲出字補注 *Keishutsuji Hochū*). These have been classified into Phonetic Glosses, Japanese native readings (*wakun*), etc., according to their content. In the process of data conversion, measures were taken to clearly identify them as Supplementary Headword Annotations (see "Supplementary Headword Annotations" under "Issues and Treatments in Transcription, Notation, and Annotation" in the "Entry Data Input" section).

**Other** includes items marked as **unknown** (未詳), **notes on textual transmission** (伝写上の注記), and cases where the type of gloss could not be determined.


### Examples of Entries (Images)



The following presents facsimile reproductions of entries from the *Myōgishō* as specific examples, including '功', '加復', 'ー之', and '助' (along with its variant characters).

{{< figure src="/images/krm-item-sample1.png" alt="entry structure" width="500px" >}}


### Diagram of Entry Structure


The following is a diagram illustrating the structure of an entry that contains all elements of a **Headword** and its **Original Glosses**.

{{< mermaid title="Entry Structure" >}}
graph TB
    A(Entry)
    A--->B(Headword)
    A--->C(Original Glosses)
    C--->D(Notes on Character Form)
    C--->E(Phonetic Gloss)
    C--->F(Semantic Gloss in Chinese)
    C--->G(Japanese native reading)
    C--->H(Other)
{{< /mermaid >}}

### Example of an Entry (Transcription)

Next, we present transcriptions of the examples shown in the images of sample entries.

First, let's consider "功," an entry that includes the basic elements.

**Example**

```text
功　音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟
```

  - Headword: 功
  - Elements of the glosses:
      - Phonetic gloss: 音工（L-R）「コウ（\_N）」「クウ（\_N）」
      - Semantic gloss: 續也　事也　成也
      - Japanese native reading: タシカニ（LHLH）
      - Note on character form: 𭃄歟

This structure should clearly illustrate the relationship between the headword and the elements of the glosses.
However, a detailed explanation of this entry's content would require considerable text.
The Japanese quotation marks (*kagi-kakko*) 「」 enclose supplementary notes, and the symbols shown in parentheses () are Romanized representations of tone marks and nasal sound symbols.
For further details, please see "[Handling Issues in Transcription, Notation, and Annotation](/docs/krm/04-entry-input/04-03-handling/)" within "[Entry Data Input](/docs/krm/04-entry-input/)"; such details are omitted here.


Similar to the example of "功," "加復" and "ー之" can be transcribed as follows.

**Example**
```text
加復　シカノミナラス  
ー之　同
```
- Headword: 加復
- Elements of the glosses:
    - Japanese native reading: シカノミナラス
- Headword: ー（加）之
- Elements of the glosses:
    - Japanese native reading: 同（i.e., same as above: シカノミナラス）

Since the "ー" in "ー之" is a notation substituting for "加," which is used in the preceding headword, it is here written as the headword "ー（加）之."

Lastly, "助" and its variant characters are shown as follows.

**Example**
```text
⿰目力	鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）  
𦔳助	今正
```
- Headword: ⿰目力
- Elements of the glosses:
    - Phonetic gloss: 鉏據反
    - Japanese native reading: タスク（LL_）　マサル（HH_）　ハサム
    - Phonetic gloss: 和自ヨ（_L）
- Headword: 𦔳助
- Elements of the glosses:
    - Note on character form: 今正

Explaining the content of the glosses for "加復," "ー之," and for "助" and its variant characters would require considerable text, so it is omitted here.

