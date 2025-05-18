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

This section explains the criteria used to classify **`Entries`** in the *Ruiju Myōgishō* and describes the characteristics of each classification.

## Classification by Headword Form

**`Entries`** can be classified according to the form of their **`Headwords`**, i.e., whether they consist of a single **Chinese character** or multiple **Chinese characters**.

### Single Character Form and Multi-Character Form

**`Headwords`** can be in either a **Single Character Form** or a **Multi-Character Form**.

**Examples:**

  - Example of single character form: 人
  - Examples of multi-character form: 一人, 二人, 五人

Based on a tally from `krm_headword_chars.tsv` (latest version 1.2.1 as of May 12, 2025), out of a total of 32,607 **`Entries`** in the Kanchi-in manuscript, 24,692 **`Entries`** were in single character form, and 7,915 **`Entries`** were in multi-character form.

## Classification Based on Entry Content and Relationships

Besides the format of the **`Headword`**, the main criteria for classifying **`Entries`** include classification based on the content of the **`Entries`** and classification based on the relationships between **`Entries`**.

### Entries with Variant Characters Listed Together

When the **`Headword`** is in single-character form, this classification is often determined by **Form Classification Tags (*jitaichūki*)** within the **`Original Glosses`** (*chūmon*). However, an **`Entry`** can also be identified as containing variant character information based on its relationship with preceding and succeeding **`Entries`**, even without explicit **Form Classification Tags**.

Here, the term *jitaichūki* (字体注記, translated in this document primarily as "Form Classification Tag") directly refers to descriptive terms indicating the type or normative status of a character form, such as "正" (standard), "俗" (popular/vulgar), and "通" (common). This concept is comparable to what Nishihara Kazuyuki refers to as *jitaikihan* (字体規範) and Lee Kyeong Won calls "字級" (*zìjí*). In English, Nishihara's *jitaikihan* is close to a "Glyph Standard Label," and Lee's "字級" is similar to a "Form Classification Tag." For the purposes of this document, "Form Classification Tag" will be the primary English term used to convey a meaning similar to Lee's "字級" (correlating with the Japanese *jitaichūki*).

An **`Entry with Variant Character Information`** refers to **`Entries`** where multiple **`Headwords`** are listed together to indicate **`variant characters (*itaiji*)`**, or where **Form Classification Tags** such as "正" (standard) and "俗" (popular/vulgar) are provided within the **`Original Glosses`**.

**`Variant characters (*itaiji*)`** may be collated in consecutive **`Entries`** in single-character form, with **Form Classification Tags** provided in their **`Original Glosses`**. Alternatively, they may be included as variant forms within a single **`Entry`** in multi-character form, again with **Form Classification Tags** in the **`Original Glosses`**.

An **`Entry`** can also be identified as an **`Entry with Variant Character Information`** based on its relationship with preceding and succeeding **`Entries`**, even without explicit **Form Classification Tags**.

An **`Entry`** is determined to be an **`Entry with Variant Character Information`** based on the content of the **Form Classification Tags** (such as "正" standard and "俗" popular/vulgar) found in the **`Original Glosses`**, or by the relationship between the listed **`Headwords`**.

Currently, while we are unable to provide precise figures, our estimates suggest that out of the approximately 32,600 **`Entries`** in the Kanchi-in manuscript, around 14,000 are **`Entries with Variant Character Information`**. Among these, approximately 9,500 are expected to be in single-character form, and about 4,500 in multi-character form.

Next, we will explain this with specific examples.

**Examples**

1.  Example with **Form Classification Tags**: 槎査　上通下正
2.  Example with **Form Classification Tags**: 㔽卣　今正
3.  Example without **Form Classification Tags**: 若𠰥　音弱（SV）「シヤク」　モシ（RL）　…
4.  Example without **Form Classification Tags**: 政⿰正攴 之盛反　マツリコト（HHHH\_） …
5.  Example with Partially Missing **Form Classification Tags**: ![㲻](https://glyphwiki.org/glyph/hdic_hkrm-01007840.50px.png) 溺字　キヨシ（LL\_）　タヽヨフ  ![㲻](https://glyphwiki.org/glyph/hdic_hkrm-01008110.50px.png)（無）

In Example 1, from the **`Original Glosses`** "上通下正," it is stated that the **`Headword`** "槎" is "通" (common) and "査" is "正" (standard), indicating that "槎" and "査" are listed together as **`Headwords`** in a **`variant character (*itaiji*)`** relationship.

Similarly, in Example 2, from the **`Original Glosses`** "今正," it is stated that the **`Headword`** "㔽" is "今" (current/present form) and "卣" is "正" (standard), allowing us to identify this as an **`Entry with Variant Character Information`**.

Examples 3 and 4 are cases where no **Form Classification Tags** are visible in the **`Original Glosses`**. In Example 3, the difference between "若" and "𠰥" is a minimal variation between "艹" (grass radical) and "䒑" (grass head). Similarly, in Example 4, the difference between "政" and "⿰正攴" is a slight variation between "攵" (knock radical) and "攴" (tap/rap radical). In both cases, it is clear that they are in a **`variant character (*itaiji*)`** relationship.

In Example 5, while  has the note "溺字" (indicating, as per the Guangyun, that 㲻 is an ancient form of 溺 'drowning' ["古作㲻"]), the subsequent **`Entry`**  lacks **`Original Glosses`**. This example involves "㲻" and its **`variant character (*itaiji*)`**, so [GlyphWiki](https://glyphwiki.org/) is used to display them to clarify their difference.

### Idiom Entries

An **`Idiom Entry`** (熟語項目) is one where the **`Headword`** is in multi-character form and constitutes an idiom. While an **`Entry`** is clearly an **`Idiom Entry`** if there is an explanation of the **`Headword`** as an idiom in the **`Original Glosses`**, it is also considered an **`Idiom Entry`** even when there is no such explanation and **`Phonetic Glosses`** and **`Semantic Glosses in Chinese`** are provided for each character of the **`Headword`**.

Currently, while precise figures are not available, the estimated numbers for **`Idiom Entries`** are as follows:

Out of the approximately 32,600 **`Entries`** in the Kanchi-in manuscript, around 14,000 are **`Entries with Variant Character Information`**, meaning that approximately 18,600 **`Entries`** are not **`Entries with Variant Character Information`**. Among these approximately 18,600 **`Entries`**, about 15,000 are in single-character form, and 3,500 are in multi-character form. These multi-character form **`Entries`** are projected to be **`Idiom Entries`**. The remaining approximately 100 **`Entries`** are those for which the **`Entry`** type cannot be determined based on their content.

Next, we will provide specific examples.

**Examples**

1.  凡ー（俗） タヽヒト（LLV__）　ワロ人（LL_）
2.  苾蒭　上蒲（L）「ホ」結（S）反　古馝字　香草也　カウハシ　又毗必反　下音鶵　草之惣名　クサ　\*カラクサ　ワラ
3.  齟齬　上慈呂（H）反　嚼　ナヤマシ（LL__）
4.  菡萏　上胡感反　下徒感反　ーー〔菡萏〕　ハチスノハナ

In Example 1, for the idiom "凡俗," the **`Japanese Native Readings (*wakun*)`** "タヽヒト" (*tatabito*) and "ワロ人" (*warobito*) are listed.

In Example 2, for the idiom "苾蒭," **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, and **`Japanese Native Readings (*wakun*)`** are provided for both the first character "苾" and the second character "蒭."

In Example 3, for the idiom "齟齬," a **`Phonetic Gloss`**, a **`Semantic Gloss in Chinese`**, and a **`Japanese Native Reading (*wakun*)`** are provided for the first character "齟."

In Example 4, for the idiom "菡萏," **`Phonetic Glosses`** are provided for both the first character "菡" and the second character "萏," followed by the **`Japanese Native Reading (*wakun*)`** "ハチスノハナ" (*hachisunohana* - lotus flower) for the idiom "菡萏."

### Basic Entries and Extended Entries

Based on the format of the **`Original Glosses`**, **`Headword`** **`Entries`** are divided into **`Basic Entries`**, in which all information regarding the "form" (形), "sound" (音), and "meaning" (義) of the **`Headword`** is recorded, and **`Extended Entries`**, which are all other **`Entries`**.

"Form" is represented by the **`Headword`** itself and **Form Classification Tags**, "sound" by **`Phonetic Glosses`**, and "meaning" by **`Semantic Glosses in Chinese`** and **`Japanese Native Readings (*wakun*)`**.

**`Basic Entries`** can be either in single-character or multi-character form. **`Extended Entries`** are, in terms of format, considered to follow **`Basic Entries`**.

In terms of content, **`Extended Entries`** include those in which only a part of the "form," "sound," or "meaning" of the **`Headword`** is recorded. However, even **`Entries`** without **`Original Glosses`** or with "**`unknown`**" (未詳) noted in the **`Original Glosses`** are included as **`Extended Entries`** if some kind of relationship is recognized between them and the preceding or succeeding **`Entries`**.

Currently, while precise figures are not available, our estimates suggest that out of the approximately 32,600 **`Entries`** in the Kanchi-in manuscript, around 15,100 are expected to be **`Basic Entries`** and approximately 17,000 are projected to be **`Extended Entries`**. The remaining approximately 500 **`Entries`** have weak relationships with other **`Entries`** and are presumed to have been arranged temporarily or for convenience.

Next, we will provide specific examples.

**Examples**

  - **`Basic Entry`**: 人　音仁（LV）「ニン」　ヒト（HL）　ワレ（LL）　サネ　マホル　ユク
  - **`Extended Entry`**: 一人　ヒトリ（LH_）
  - **`Extended Entry`**: 二人　フタリ（HHL）

### Independent Entries and Serial Entries

**`Headword`** **`Entries`** are divided, based on whether a **`Basic Entry`** has **`Extended Entries`**, into **`Independent Entries`**, which consist only of a **`Basic Entry`** without any **`Extended Entries`**, and **`Serial Entries`**, which consist of both a **`Basic Entry`** and one or more **`Extended Entries`**. Within a **`Serial Entry`**, the **`Basic Entry`** is sometimes referred to as the **`Chief Entry`**, and the **`Extended Entries`** as **`Sub Entries`**.

The number of **`Independent Entries`** and **`Serial Entries`** has not yet been calculated.

**`Independent Entries`** are exemplified by the following:

**Examples**

  - 仕　音士　ツカフ（HHL）　ツカマツル（HL\_\_\_）　ミヤツカヘ　ツモム
  - 任　音壬（LV）「シム」「ニム」　タヘタリ（LR\_\_、ヘ-フ）　…

Although "仕" (to serve) and "任" (to entrust) have similar graphic forms, they are distinct **Chinese characters**, and each functions as a **`Basic Entry`** with its own **`Phonetic Glosses`** and **`Japanese Native Readings (*wakun*)`**. However, no **`variant characters (*itaiji*)`** of "仕" or compound words containing "仕" are found. Similarly, no related **`variant characters (*itaiji*)`** or compound words are found for "任."

**`Serial Entries`** are exemplified by "人" (person) as the **`Basic Entry`** and "一人" (one person), "二人" (two people) as the **`Extended Entries`**, as shown in the examples for **`Basic Entries`** and **`Extended Entries`**. "人" is the **`Chief Entry`**, and "一人" and "二人" are the **`Sub Entries`**.
