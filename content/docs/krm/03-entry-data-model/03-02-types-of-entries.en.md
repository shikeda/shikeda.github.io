---
title: "Types of Entries"
weight: 5
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---


# Types of Entries

This section explains the criteria used to classify entries in the *Ruiju Myōgishō* and describes the characteristics of each classification.



## Classification by Headword Form

Entries can be classified according to the form of their headwords, i.e., whether they consist of a single character or multiple characters.

### Single Character Form and Multi-character Form

Headwords can be in either a **Single Character Form** or a **Multi-Character Form**.

**Examples:**
- Example of single character form: 人
- Examples of multi-character form: 一人, 二人, 五人

Based on a tally from `krm_headword_chars.tsv` (latest version 1.2.1 as of May 12, 2025), out of a total of 32,607 entries in the Kanchi-in manuscript, 24,692 entries were in single character form, and 7,915 entries were in multi-character form.

## Classification Based on Entry Content and Relationships

Besides the format of the headword, the main criteria for classifying entries include classification based on the content of the entries and classification based on the relationships between entries.

### Entries with Variant Characters Listed Together

When the headword is in single-character form, it is judged based on the Notes on Character Form (*jitaichūki*) in the Original Glosses (*chūmon*). However, entries can also be judged as variant character entries based on their relationship with preceding and succeeding entries, even without Notes on Character Form.

Here, "Notes on Character Form (*jitaichūki*)" directly refers to terms indicating the types and standards of character forms, such as "正" (standard), "俗" (vulgar), and "通" (common). This concept is equivalent to Nishihara Kazuyuki's "*jitaikihan* (glyph standard label)" and Lee Kyeong Won's "字級 (zìjí) (form classification tag)." Nishihara's "*jitaikihan*" is close to a Glyph Standard Label, and Lee's "字級" is similar to a Form Classification Tag. In this document, we will primarily use "Form Classification Tag" in English to convey a meaning similar to Mr. Lee's "字級," while using "*jitaichūki*" (or "字体注" when contextually appropriate) in Japanese.


**Entry with Variant Character Information** refers to entries where headwords are listed together to indicate variant characters, or where Form Classification Tags such as "正" (standard) and "俗" (vulgar) are provided within the Original Glosses.

Variant characters may be collated in consecutive entries in single-character form, with Form Classification Tags such as "正" (standard) and "俗" (vulgar) provided in their Original Glosses. Alternatively, they may be included as variant forms within a single entry in multi-character form, again with Form Classification Tags in the Original Glosses.

An entry can also be identified as an Entry with Variant Character Information based on its relationship with preceding and succeeding entries, even without explicit Form Classification Tags.

An entry is determined to be an Entry with Variant Character Information based on the content of the Form Classification Tags such as "正" (standard) and "俗" (vulgar) found in the Original Glosses, or the relationship between the listed headwords.

Certainly. Here's the English translation of that section:

Currently, while we are unable to provide precise figures, our estimates suggest that out of the approximately 32,600 entries in the Kanchi-in manuscript, around 14,000 are Entries with Variant Character Information. Among these, approximately 9,500 are expected to be in single-character form, and about 4,500 in multi-character form.

Next, we will explain this with specific examples.

**Examples**

1.  Example with Form Classification Tags: 槎査　上通下正
2.  Example with Form Classification Tags: 㔽卣　今正
3.  Example without Form Classification Tags: 若𠰥　音弱（SV）「シヤク」　モシ（RL）　…
4.  Example without Form Classification Tags: 政⿰正攴 之盛反　マツリコト（HHHH\_） …
5.  Example with Partially Missing Form Classification Tags: ![㲻](https://glyphwiki.org/glyph/hdic_hkrm-01007840.50px.png) 溺字　キヨシ（LL\_）　タヽヨフ  ![㲻](https://glyphwiki.org/glyph/hdic_hkrm-01008110.50px.png)（無）


In Example 1, from the Original Glosses "上通下正," it is stated that the headword "槎" is "通" (common) and "査" is "正" (standard), indicating that "槎" and "査" are listed together as headwords in a variant character relationship.

Similarly, in Example 2, from the Original Glosses "今正," it is stated that the headword "㔽" is "今" (current/present form) and "卣" is "正" (standard), allowing us to identify this as an Entry with Variant Character Information.

Examples 3 and 4 are cases where no Form Classification Tags are visible in the Original Glosses. In Example 3, the difference between "若" and "𠰥" is a minimal variation between "艹" (grass radical) and "䒑" (grass head). Similarly, in Example 4, the difference between "政" and "⿰正攴" is a slight variation between "攵" (knock radical) and "攴" (tap/rap radical). In both cases, it is clear that they are in a variant character relationship.

In Example 5, while  has the note "溺字" (drowning character), the subsequent entry  lacks Original Glosses. This example involves "㲻" and its variant character, so [GlyphWiki](https://glyphwiki.org/) is used to display them to clarify their difference.


### Idiom Entries

An **Idiom Entry** (熟語項目) is one where the headword is in multi-character form and constitutes an idiom. While an entry is clearly an Idiom Entry if there is an explanation of the headword as an idiom in the Original Glosses, it is also considered an Idiom Entry even when there is no such explanation and phonetic and semantic glosses are provided for each character of the headword.


Currently, while precise figures are not available, the estimated numbers for idiom entries are as follows:

Out of the approximately 32,600 entries in the Kanchi-in manuscript, around 14,000 are Entries with Variant Character Information, meaning that approximately 18,600 entries are not Entries with Variant Character Information. Among these approximately 18,600 entries, about 15,000 are in single-character form, and 3,500 are in multi-character form. These multi-character form entries are projected to be idiom entries. The remaining approximately 100 entries are those for which the item type cannot be determined based on their content.

Next, we will provide specific examples.

**Examples**

1.  凡ー（俗） タヽヒト（LLV__）　ワロ人（LL_）
2.  苾蒭　上蒲（L）「ホ」結（S）反　古馝字　香草也　カウハシ　又毗必反　下音鶵　草之惣名　クサ　*カラクサ　ワラ
3.  齟齬　上慈呂（H）反　嚼　ナヤマシ（LL__）
4.  菡萏　上胡感反　下徒感反　ーー〔菡萏〕　ハチスノハナ

In Example 1, for the idiom "凡俗," the Japanese native readings "タヽヒト" (tatabito) and "ワロ人" (warobito) are listed.

In Example 2, for the idiom "苾蒭," phonetic glosses, semantic glosses, and Japanese native readings are provided for both the first character "苾" and the second character "蒭."

In Example 3, for the idiom "齟齬," a phonetic gloss, a semantic gloss, and a Japanese native reading are provided for the first character "齟."

In Example 4, for the idiom "菡萏," phonetic glosses are provided for both the first character "菡" and the second character "萏," followed by the Japanese native reading "ハチスノハナ" (hachisunohana - lotus flower) for the idiom "菡萏."


### Basic Entries and Extended Entries

Based on the format of the Original Glosses, headword entries are divided into **Basic Entries**, in which all information regarding the "form," "sound," and "meaning" of the headword is recorded, and **Extended Entries**, which are all other entries.

"Form" is represented by the headword itself and Form Classification Tags, "sound" by Phonetic Glosses, and "meaning" by Semantic Glosses and Japanese native readings.

Basic entries can be either in single-character or multi-character form. Extended Entries are, in terms of format, considered to follow basic entries.

In terms of content, extended entries include those in which only a part of the "form," "sound," or "meaning" of the headword is recorded. However, even entries without Original Glosses or with "未詳" (unknown) noted in the Original Glosses are included as extended entries if some kind of relationship is recognized between them and the preceding or succeeding entries.

Currently, while precise figures are not available, our estimates suggest that out of the approximately 32,600 entries in the Kanchi-in manuscript, around 15,100 are expected to be basic entries and approximately 17,000 are projected to be extended entries. The remaining approximately 500 entries have weak relationships with other entries and are presumed to have been arranged temporarily or for convenience.


Next, we will provide specific examples.

**Examples**

- Basic Entry: 人　音仁（LV）「ニン」　ヒト（HL）　ワレ（LL）　サネ　マホル　ユク
- Extended Entry: 一人　ヒトリ（LH_）
- Extended Entry: 二人　フタリ（HHL）


### Independent Entries and Serial Entries

Headword entries are divided, based on whether a basic entry has extended entries, into **Independent Entries**, which consist only of a basic entry without any extended entries, and **Serial Entries**, which consist of both a basic entry and one or more extended entries. Within a serial entry, the basic entry is sometimes referred to as the **Chief Entry**, and the extended entries as **Sub Entries**.

The number of independent entries and serial entries has not yet been calculated.

Independent entries are exemplified by the following:

**Examples**
- 仕　音士　ツカフ（HHL）　ツカマツル（HL___）　ミヤツカヘ　ツモム
- 任　音壬（LV）「シム」「ニム」　タヘタリ（LR__、ヘ-フ）　…


Although "仕" (to serve) and "任" (to entrust) have similar graphic forms, they are distinct characters, and each functions as a basic entry with its own phonetic glosses and Japanese native readings. However, no variant characters of "仕" or compound words containing "仕" are found. Similarly, no related variant characters or compound words are found for "任."

Serial entries are exemplified by "人" (person) as the basic entry and "一人" (one person), "二人" (two people) as the extended entries, as shown in the examples for basic and extended entries. "人" is the chief entry, and "一人" and "二人" are the sub entries.


