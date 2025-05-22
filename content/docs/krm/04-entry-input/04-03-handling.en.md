---
title: "Handling Issues in Transcription, Notation, and Annotation"
weight: 4
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

Under preparation.

# Handling Issues in Transcription, Notation, and Annotation

The *Myōgishō* is a dictionary of **`Hanzi (Chinese characters)`**. To accurately decipher its content and convert it into digital text, it is necessary to first understand the various characteristics visible in the original *Myōgishō* manuscripts and then to establish specific methods for data input and processing.

First, as the Myōgishō is an ancient manuscript, scribal errors are unavoidable.
Under Scribal Issues, we will address **`Miswritten Characters`** (誤字, *goji*), **`Omitted Characters`** (脱字, *datsuji*), **`Superfluous Characters`** (衍字, *enji*), and **`Correction Marks`** (訂正符号, *teisei fugō*).

Next, the *Myōgishō* employs sophisticated notational conventions for characters and words to convey diverse information related to the form, sound, and meaning of **`Hanzi (Chinese characters)`** accurately and efficiently. Under **Notational Conventions for Characters and Words**, we will discuss frequently used **`Abbreviated Characters`** (略字, *ryakuji*), **`Variant Characters` (*itaiji*)** (異体字), **`Iteration Marks`** (踊り字, *odoriji*), and **`Substitution Marks`** (代用符号, *daiyō fugō*). Although not numerous, examples of **`Compound Marks` (合符, *gōfu*)**—symbols used to connect characters to indicate they form a compound word—also exist and will be briefly introduced here. Since the nature of **`Substitution Marks`** and **`Compound Marks`** can be difficult to grasp, they will be explained in detail with examples in their respective dedicated sections.

Finally, various ingenious methods are also applied to information added beyond the main text of the *Myōgishō*, as well as to physical characteristics such as layout and variations in character size. Under **`Additional Notations and Layout Features`**, we will cover:

* **`Interlinear Notes`** (割注, *warichū*),
* variations in the size of characters within **`Original Glosses`** (注文文字の大小, *chūmon moji no daishō*),
* **`Small Character Annotations`** (小字注記, *shōji chūki*),
* **`Annotations from Variant Manuscripts`** (異本注記, *ihon chūki*),
* **`Source Attributions`** (出典注記, *shutten chūki*),
* **`Tone Marks` (*shōten*)** (声点),
* **`Morphosyntactic Glosses` (*wokototen*)** (ヲコト点),
* line breaks and spacing (改行・空白, *kaigyō/kūhaku*),
* **`Interpolated Glosses`** (補入注文, *honyū chūmon*),
* unannotated **`Entries`** (無注記, *muchūki*), and
* other noteworthy cases.

We will also explain how these are input and processed. The explanation of **`Tone Marks` (*shōten*)** will concurrently cover voiced sound symbols and nasal sound symbols."

While the primary focus of this explanation will be on issues common to the entire text of the *Myōgishō*, if there are problems specific to the constituent elements of an **`Entry`**—namely the **`Headword`**, **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, and **`Japanese Native Readings` (*wakun*)**—these will also be addressed according to their significance.
For example, "iteration marks" (踊り字, *odoriji*) are a common issue across various elements of an **`Entry`**, whereas "**`Tone Marks` (*shōten*)**" and "nasal sound symbols" (鼻音符号, *bionfugō*) are particularly problematic in the context of **`Phonetic Glosses`**.


In the published data, the transcription of **`Headwords`** is recorded in the `hanzi_entry` and `original_entry` columns of the `krm_main` file.
Similarly, the `hanzi_entry` and `original_entry` columns in the `krm_notes` file contain the same content as those in `krm_main`.
The `krm_wakun` file exclusively lists **`Japanese Native Reading` (*wakun*)** data in its `wakun_elements` column.

Furthermore, instances requiring particularly detailed explanation are described in the `remarks` column of the `krm_notes` file as **`Compiler's Remarks`**.

For more details on the overall structure of the published data and file formats, please refer to the [Overview of Public Data](/docs/krm/02-data-overview/).

The transcription of the **`Original Glosses`** is recorded in the `definition` column of the `krm_main` public data file.
In the `krm_notes` file, the constituent elements of the **`Original Glosses`**—namely **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings` (*wakun*)**, and **`Other`** information—are categorized and recorded in the `definition_elements` column.


## Scribal Issues

This section addresses issues such as **`Miswritten Characters`** (誤字, *goji*), **`Omitted Characters`** (脱字, *datsuji*), **`Superfluous Characters`** (衍字, *enji*), and **`Correction Marks`** (訂正符号, *teisei fugō*).

### `Miswritten Characters` (誤字, *goji*)

When a **`Headword`** is clearly a **`Miswritten Character`** (誤字, *goji*), the collated (corrected) form is recorded in the `hanzi_entry` column, and the original manuscript form is recorded in the `original_entry` column. The basis for the collation is provided in the `remarks` column of the `krm_notes` file (for details on `krm_notes`, please refer to the relevant section in the [Overview of Public Data](/docs/krm/02-data-overview/)).

**Examples (Original Japanese remarks):**
- `hanzi_entry`: 向／後, `original_entry`: 〇／ー（彴）, `remarks`: 掲出字は「向後」とすべきを誤る。岡田研究193-194頁に「ー」使用は高山寺本が適切との指摘あり。
- `hanzi_entry`: 姡, `original_entry`: 活, `remarks`: 掲出字は誤写。高山寺本・蓮成院本・西念寺本「姡」に作るにより改める。

As illustrated by the preceding examples, the `remarks` in the `krm_notes` file are originally written in Japanese. English translations of these specific `remarks` are provided below for reference.

**English Translations of `remarks` examples:**

* **For `hanzi_entry` '向／後':**
    Erroneous **`Headword`**; should be '向後'. Okada (pp. 193-194) notes the use of 'ー' is appropriate for the Kōzan-ji ms.
* **For `hanzi_entry` '姡':**
    Miscopied **`Headword`**. Corrected to '姡' per Kōsan-ji, Renshō-in, & Sainen-ji mss.

### `Omitted Characters` (脱字, *datsuji*)

When a character is clearly omitted from a **`Headword`**, the presumed omitted character is indicated by enclosing it in full-width square brackets "［］". If further explanation is necessary, it is provided separately (e.g., in the **`Compiler's Remarks`**).

**Examples:**
1.  将／［指］
2.  叔／［母］

In Example 1, the **`Headword`** is found in the "手" (hand) radical section, and it is evident from the context that the character '指' is missing.

In Example 2, the **`Headword`** is found in the "女" (woman) radical section. Given the presence of the character '母' in preceding and succeeding **`Entries`**, its omission here is clear.

If it is clear that a character has been omitted, but the specific missing character is unknown, it is indicated by a full-width underscore within full-width square brackets, like "［＿］".

The following example illustrates a case where either the first or second character of a *fanqie* spelling was clearly omitted, but the specific missing character is unknown.

**Example:**
* 𤎥 ［＿］覽反

In this example, the **`Original Glosses`** for '𤎥' show "覽反".
According to the *Guangyun*, '𤎥' has readings *chùzhān qiè* (處占切; level tone, 鹽韻, for the character 䪜) or *tǔgǎn qiè* (吐敢切; rising tone, 敢韻, for the character 𦵹). Since '覽' has the *Guangyun* reading *gǎnlú qiè* (敢盧切; rising tone, 敢韻), it is clear that the first character of the *fanqie* spelling is missing.
Therefore, it is transcribed as "［＿］覽反".

### `Superfluous Characters` (衍字, *enji*)

Cases of **`Superfluous Characters`** (衍字, *enji*) are noted in the `remarks` column of the `krm_notes.tsv` file.

Examples are shown below in the order of **`Headword`** (`hanzi_entry`), relevant part of the **`Original Glosses`** (`definition_elements` from `krm_notes` or context from `krm_main`'s `definition`), and **`Compiler's Remarks`** (`remarks`).

**Examples:**
* **`Headword`** (`hanzi_entry`): 胳
    **`Original Glosses`** (excerpt from `definition` / `definition_elements`): 又俗音腋也
    **`Compiler's Remarks`** (`remarks`): The character '也' in "又俗音腋也" is superfluous.
* **`Headword`** (`hanzi_entry`): 眺
    **`Original Glosses`** (excerpt from `definition` / `definition_elements`): *ヒカヽメ
    **`Compiler's Remarks`** (`remarks`): The *Shinsen Jikyō* has "又比加目". The 'ヽ' mark here is possibly a superfluous character, but this remains questionable (存疑, *zongi*).

### `Correction Marks` (訂正符号, *teisei fugō*)

The marks used for corrections in the main text include **`Transposition Marks`** (転倒符, *tentōfu*), **`Deletion Marks`** (見消符, *misekechifu*), and **`Interpolation Marks`** (補入符, *honyūfu*).

* **`Transposition Marks`** (転倒符, *tentōfu*; also called 顛倒符, *tentōfu*)[^1] are used to correct the order of characters within a **`Multi-Character Form Headword`**.
* **`Deletion Marks`** (見消符, *misekechifu*; also called 抹消符, *masshōfu*)[^2] often indicate that the correct **`Headword`** is provided as a side note  (e.g., 傍記 or 傍書).
* **`Interpolation Marks`** (補入符, *honyūfu*)[^3] are used to correct the order of **`Entries`**.

When inputting the main text data, the text is entered in its corrected form as indicated by these correction marks, and the details of such corrections are recorded in the `remarks` column (which forms part of the **`Compiler's Remarks`**).

In the input examples that follow, detailed explanations are provided for each instance of correction or annotation. This explanatory content constitutes the **`Compiler's Remarks`** and is recorded in the `remarks` column of the `krm_notes` file.

**Example 1:**
* **`hanzi_entry`**: 儻／儻
* **`definition_elements`**: コヒネカハクハ
* **`remarks`**: Nishihata, *Gosha Shorei* (Examples of Scribal Errors), p. 54, item ③ "moji no irekawari" (character transposition) no. 818. Kusakawa Noboru ("Ruiju Myōgishō Wakun Shōkō," p. 29) notes that the Kōzan-ji manuscript has a **`Transposition Mark`** on the upper right of 'ヒ' in "コネヒカハクハ," indicating the character transposition error (as pointed out by Nishihata for the Kanchi-in manuscript) had already been resolved.

**Example 2:**
* **`hanzi_entry`**: 拻
* **`definition_elements`**: 不定「ウシヽ歟」相撃
* **`remarks`**: Masamune's Index, under 'ウシヽ', notes: "Is 'ウシヽ' an error for 'ホシヽ', or was the cursive form of '完' misread as 'ホシヽ'? It is a lexical error." Under 'フ', it states: "Could this be the character '不', explained in the *Jikyō* dictionary as '音灰不言相撃' (pronunciation *hai*, unspoken, mutual strike)? This requires further research." Kusakawa's *Wakun Shūsei* records 'ウシヽ' (treating it as a *wakun*). Ikeda's note: In the original text "フ定相撃", there is a red **`Deletion Mark`** to the left of '定', and 'ウシヽ歟' ("perhaps ウシヽ?") is written to its right in red. This is likely an editorial note (*ango*) added due to misidentifying a **`Hanzi (Chinese character)`** as kana.

**Example 3:**
* **`hanzi_entry`**: ⿸𠂋帀
* **`definition_elements`**: △在下
* **`remarks`**: Although '△' is written in a large size similar to a **`Headword`**, it is not a **`Headword`** itself but should be regarded as an **`Interpolation Mark`**.

## Notational Conventions for Characters and Words


This section discusses frequently used **`Abbreviated Characters`** (略字, *ryakuji*), **`Variant Characters` (*itaiji*)** (異体字), **`Iteration Marks`** (踊り字, *odoriji*), **`Substitution Marks`** (代用符号, *daiyō fugō*), and **`Compound Marks` (合符, *gōfu*)**.

### **`Abbreviated Characters`** (略字, *ryakuji*)

**`Abbreviated Characters`** (略字, *ryakuji*; also called 簡略字, *kanryakuji*) found in the manuscript are generally normalized to their standard, common forms in the transcribed data.

**Examples:**
(The left side shows the abbreviated form found in the manuscript, and the right side shows the normalized character used in the data.)
1.  亠 → 音 (*on*)
2.  ﹅ → 也 (*nari*, *ya*)
3.  彳 → 従 (*jū*, *shitagau*)
4.  扌 → 於 (*o*, *okeru*)
5.  乂 → 反 (*han*; as in *fanqie* 反切)
6.  禾 → 和 (*wa*; as in *Wa-on* 和音, an older layer of Sino-Japanese pronunciation)
7.  谷 → 俗 (*zoku*) (but see note below)
8.  牜 → 物 (*butsu*, *mono*)
9.  类 → 類 (*rui*)
10. 欤 → 歟 (*yo*, *ka*)

Among these, examples 1 through 4 are illustrated in the prefatory notes (凡例, *hanrei*) of the *Myōgishō* in a section explaining "注中多略用片" (meaning "in the glosses, abbreviated forms, often single components of characters [like radicals or katakana], are frequently used").

Example 1 (亠 for 音 'sound/pronunciation'), Example 5 (乂 for 反 'reversal', used in **`fanqie`** spellings), and Example 6 (禾 for 和 'harmony/Japanese', used to denote **`Go-on`** (和音, *Wa-on*) pronunciations) are frequently used in **`Phonetic Glosses`**.

Example 7 (谷 for 俗) is frequently used in **`Notes on Character Form`** (to mean 'popular/vulgar' form), and example 8 (牜 for 物) is frequently used in **`Japanese Native Readings` (*wakun*)**.
However, '谷' can also be used with its inherent meaning ("valley"). In such cases, it is transcribed as '谷' and not normalized to '俗'. 
For instance, **`Headwords`** containing '谷' as a component are listed under the '八' (eight) radical section (八部, hachibu) of the Kanchi-in manuscript.
The **`Entry`** for '豅', for example, has its semantic meaning given in the original text as "大長谷" (large long valley), so '谷' is retained as is.

Example 9 (类 for 類) is used in **`Entries`** derived from category names in the *Wamyō Ruijushō* (倭名類聚抄), such as "草類" (types of grasses) and "苔類" (types of mosses).

Example 10 (欤 for 歟) is used in notes expressing doubt or questioning the correctness of characters or phrases (these are considered types of editorial notes or *ango*).

