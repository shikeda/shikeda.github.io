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

**`Abbreviated Characters`** (略字, *ryakuji*; also called 簡略字, *jiǎnlüèzì* in Chinese) found in the manuscript are generally normalized to their standard, common forms in the transcribed data.

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


### `Variant Characters (*itaiji*)` (異体字)

While care has been taken to input **`variant characters` (*itaiji*)** used as **`Headwords`** in a form that is faithful to, or closely approximates, their appearance in the original manuscript, the basic policy for **`variant characters` (*itaiji*)** appearing within the **`Original Glosses`** is to normalize them to their common or standard forms.

**Examples (Original form → Normalized form):**
* 𡰱 → 尼
* 凢 → 凡
* 𠩄 → 所
* 𢘻 → 悉
* 俻 → 備

### `Iteration Marks` (踊り字, *odoriji*)

For Kanji **`Iteration Marks`** (踊り字, *odoriji*; also known as 疊字符, *diézìfú* in Chinese), the mark "〻" (NINOMAETEN, U+303B) is used, while "々" (DITTO MARK, U+3005) is not.

For iteration marks in Katakana used for **`Japanese Native Readings` (*wakun*)**, the mark "ヽ" (KATAKANA ITERATION MARK, U+30FD) is used.

The marks "〱" (KUNOJITEN, U+3031), "〳" (KUNOJITEN WITH VOICED SOUND MARK, U+3033), and "〵" (KUNOJITEN WITH SEMI-VOICED SOUND MARK, U+3035) are not used; instead, the KATAKANA ITERATION MARK is repeated, such as "ヽヽ".

**Examples:**
* Example in a **`Headword`**: 曽／ー（祖）／〻（母）
* Example in a **`Japanese Native Reading` (*wakun*)**: 陽　アタヽカナリ
* Example in a **`Japanese Native Reading` (*wakun*)**: 倍　マスヽヽ



### `Substitution Marks` (代用符号, *daiyō fugō*)

The **`Substitution Mark`** (代用符号, *daiyō fugō*), appearing as '｜' in **`Headwords`** that are compound words (熟語, *jukugo*), is a symbol used when substituting for an annotated character (被注字, *hichūji*; also 被釋字, *hishakuji*; i.e., the target character of an annotation) or a previously listed **`Headword`**. In the data, this '｜' mark is input using 'ー' (CHOONPU - long vowel mark, U+30FC), and the actual character it represents is then input within full-width parentheses '（）'.

When the symbol '｜' is used within the **`Original Glosses`** to indicate the same character as the **`Headword`**, it is simply input as 'ー' (CHOONPU - long vowel mark, U+30FC), without an accompanying indication of the character it represents.

**Examples:**
* Examples in **`Headwords`**: 五／ー（人） (here 'ー' substitutes for '人'), ..., 真／人, 漁／ー（人）, 海／ー（人）
* Example in **`Original Glosses`**: 鄲 邯ー縣名 (For the **`Headword`** '鄲', the gloss "邯ー縣名" indicates that "邯ー" refers to "邯鄲", which is a county name.)


### `Compound Marks` (合符, *gōfu*)

A **`Compound Mark`** (合符, *gōfu*; also known as 連字符, *liánzìfú* in some contexts, though originally a vertical linking line in the manuscript) is represented in this dataset by a hyphen-minus ('-', U+002D). Examples of its use are relatively rare.

**Example:**
* **`Headword`**: 媊
    **`Original Glosses`** (excerpt): 箭(R)貲二音　又煎(L)音　太-白-星

In the **`Original Glosses`** for the **`Headword`** '媊', the notation "太-白-星" appears at the end. In this context, the hyphens function as **`Compound Marks`**, linking the characters '太', '白', and '星' to form the term "太白星" (*Tàibáixīng*), which refers to the planet Venus.



## `Additional Notations and Layout Features`

Finally, this section addresses various issues related to additional notations and layout features found in the *Myōgishō*.
If using the *Myōgishō* as a resource for the historical phonology or lexicology of Japanese, it is particularly important to carefully read the explanations regarding **`Tone Marks` (*shōten*)**, voiced sound marks (濁点, *dakuten*), and nasal sound symbols.

### **`Interlinear Notes`** (割注, *warichū*)

The basic form is *warichū sōgyō* (割注双行; meaning "small character definition in two lines," comparable to 雙行夾注, *shuāngháng jiāzhù* in Chinese contexts), which are transcribed from right to left according to their original appearance.
If an interlinear note extends to three lines, the part judged to be an addition is transcribed last.

### Variations in the Size of Characters within `Original Glosses`

There are rare instances where a character within the **`Original Glosses`** is mistakenly written in a large size, leading to potential confusion with a **`Headword`**.

**Example:**
* `hanzi_entry`: 憙
* `definition` (representing **`Original Glosses`**): 音喜（L-H）　又嬉　コノム（LLH）　喜「注也」　ネカフ (further glosses omitted)

In this example, following the **`Headword`** '憙', the **`Original Glosses`** provide a **`Phonetic Gloss`**, a **`Note on Character Form`** (implicitly, "又嬉" suggesting a variant or related form), and a **`Japanese Native Reading` (*wakun*)**. After these, the character '喜' is written in a large size, followed by other **`Japanese Native Readings` (*wakun*)** such as 'ネカフ'. To the right of the large character '喜', there is a note "注也" (*chū nari*; "this is a gloss/annotation"), indicating that '喜' itself functions as a **`Semantic Gloss in Chinese`** for the **`Headword`** '憙'.

### `Small Character Annotations` (小字注記, *shōji chūki*)

Annotations made using small characters are referred to as **`Small Character Annotations`** (小字注記, *shōji chūki*).
**`Small Character Annotations`** are frequently found in **`Notes on Character Form`** (字体注, *jitaichū*); these are specifically termed **`Small Character Notes on Character Form`** (小字字体注記, *shōji jitaichūki*).


There are instances where a **`Phonetic Gloss`** for a **`Hanzi (Chinese character)`** used within an **`Original Gloss`** is itself annotated in an interlinear style (割注形式, *warichū keishiki*); this is termed a **`Nested Interlinear Note`** (再割注, *saiwarichū*; or 再夾注, *zàijiāzhù* in Chinese; meaning "smaller character definition in two lines, reapplied").[^note1]

[^note1]: The term 再割注 (*saiwarichū*), or 再夾注 (*zàijiāzhù* in Chinese), implies a "re-application" of an interlinear-style gloss, often to a character already within a gloss.


Additionally, there are cases where a **`Semantic Gloss in Chinese`** is added in small characters directly below a **`Japanese Native Reading` (*wakun*)**; this is termed a **`Small Character Semantic Gloss for Wakun`** (小字和訓義注, *shōji wakun gichū*).

**`Small Character Annotations`** are transcribed by enclosing the relevant portion in full-width angle brackets (〈〉, U+3008 and U+3009).

**Examples:**
* Example of **`Small Character Notes on Character Form`**: 又鞘〈正〉 (Found in the **`Notes on Character Form`** for the **`Headword`** '削').
* Example of **`Nested Interlinear Note`**: 従夾〈公合〉成恰反 (For the **`Headword`** '陜', the second character '夾' of the *fanqie* spelling is further glossed with another *fanqie* spelling in small characters).
* Example of **`Small Character Semantic Gloss for Wakun`**: アク〈髪〉 (For the **`Headword`** '結', this note is attached to the **`Japanese Native Reading` (*wakun*)** 'アク' to distinguish it from homonyms (開く, 厭く, 挙ぐ) and to indicate the meaning of tying up 'hair' (髪)).

Cases where what should have been a **`Small Character Semantic Gloss for Wakun`** was mistakenly written in the same large size as the main **`Original Glosses`** are transcribed using 〈〉, and a note to this effect is made in the `remarks` column (as a **`Compiler's Remark`**).

The following examples are shown in the order of **`Headword`**, **`Japanese Native Reading` (*wakun*)** (including the erroneously large annotation transcribed within 〈〉), and **`Compiler's Remarks`**.

**Examples:**
* **`Headword`**: 展
    **`Japanese Native Reading` (*wakun*)**: ヒロク〈眉〉
    **`Compiler's Remarks`**: The annotation 〈眉〉 is written in a large size.
* **`Headword`**: 度
    **`Japanese Native Reading` (*wakun*)**: トコ〈床〉
    **`Compiler's Remarks`**: The semantic gloss is written in a large size.


### `Annotations from Variant Manuscripts` (異本注記, *ihon chūki*)

**`Annotations from Variant Manuscripts`** (異本注記, *ihon chūki*) can pertain to either the **`Headword`** or the **`Original Glosses`**.

**`Annotations from Variant Manuscripts`** pertaining to a **`Headword`** are indicated by a preceding '▲' (U+25B2 BLACK UP-POINTING TRIANGLE) followed by the content of the annotation enclosed in Japanese quotation marks 「」.

**`Annotations from Variant Manuscripts`** pertaining to the **`Original Glosses`** are enclosed in full-width parentheses（）, U+FF08 and U+FF09. They are shown in the format: *original character(s) in the gloss* - *annotation from the variant manuscript*.

The symbol representing an "annotation from a variant manuscript" itself (異本注記) is often the Katakana character 'イ' (which might be a part of the '他' character in '他本', *tahon*, meaning "other manuscript," or simply represent '異').

**Examples:**
* **`Annotation from Variant Manuscripts`** (for a **`Headword`**): ▲𦫿「艾」
* **`Annotation from Variant Manuscripts`** (for a **`Headword`**): ▲捺「⿰扌柰イ」
* **`Annotation from Variant Manuscripts`** (for **`Original Glosses`**): 責猛（猛-⿰亻孟イ）二音

### `Source Attributions` (出典注記, *shutten chūki*)

Book titles or personal names indicating a source are enclosed in double angle brackets (《》, U+300A and U+300B).

**Examples:**
1.  Example of a personal name: 齔 《王右軍》作 (Here, 《王右軍》 *Ō Ugun* [Wang Youjun] indicates the person who created or used this form/reading).
2.  Example of a personal name: 𡫸 ◇《弘法大師》又云 (Here, ◇ indicates a note in literary Chinese placed to the right of the **`Headword`**, and 《弘法大師》 *Kōbō Daishi* is the cited person).
3.  Example of a book title: 它 可見《類音决》 (Here, 《類音决》 *Ruionketsu* is the cited book title, meaning "can be seen in the *Ruionketsu*").
4.  Example of a book title: 𭘬 《大日經疏》云丁也反 (Here, 《大日經疏》 *Dainichikyōsho* is the cited book title, followed by a *fanqie* spelling).

In example 2, the '◇' mark indicates that this is an annotation in literary Chinese placed to the right of the **`Headword`**.



### `Tone Marks (*shōten*)` (声点)

Since **`Tone Marks` (*shōten*)** are a feature of great interest to users of the *Myōgishō* data, they are explained in detail here.

In the published data, the transcription of the **`Original Glosses`** is recorded in the `definition_elements` column of the `krm_notes` file. By loading `krm_notes.tsv` into a spreadsheet program like Excel and filtering the `definition_type_name` column for "**`Phonetic Gloss`**" or "**`Japanese Native Reading` (*wakun*)**", users can extract the relevant information.

**Types of `Tone Marks` (*shōten*)**

**`Tone Marks` (*shōten*)** are indicated by the abbreviations shown in parentheses: Ping/Even (L), Shang/Rising (H), Qu/Departing (R), Ru/Entering (S), Ping-Qing/Even-Light (F), and Ru-Qing/Entering-Light (T). The identification of light tones (軽声, *keishō*) is provisional.

If the position of a **`Tone Mark` (*shōten*)** is difficult to determine, a question mark "?" is added to indicate this uncertainty.

Voiced sound marks and nasal sound symbols are often displayed concurrently with **`Tone Marks` (*shōten*)**, so they are explained next.

**Voiced Sounds (濁音, *dakuon*)**

The voiced sound mark (濁音符号, *dakuon fugō*), indicated by double dots (゛) in the original, is represented by the English letter 'V' (U+0056) in the data.

**Nasal Sound Symbols (鼻音符号, *bion fugō*)**

The nasal sound symbol (鼻音符号, *bion fugō*;  also 鼻音符, *bíyīnfú* in Chinese) is represented by "(N)" in the data. In the manuscript, nasal sound symbols appear in forms such as ✓, v, レ, or 」. If it is necessary to refer to the specific shape of a nasal sound symbol, the check mark '✓' (U+2713) is used for explanatory purposes.

**Multiple `Tone Marks` (*shōten*)**

When multiple **`Tone Marks` (*shōten*)** are present, they are listed in the following order: Ping/Even (L) → Ping-Qing/Even-Light (F) → Shang/Rising (H) → Qu/Departing (R) → Ru-Qing/Entering-Light (T) → Ru/Entering (S). They are separated by a hyphen-minus ('-', U+002D).


**Types of `Phonetic Glosses`**

There are three types of **`Phonetic Glosses`**:
* **`Fanqie spellings`** (反切, *hansetsu* or *fanqie*),
* **`Similar sound notes`** (類音注, *ruion-chū*; annotations indicating similar pronunciations by character), and
* **`Kana glosses`** (仮名音注, *kana-onchū*; phonetic annotations in kana).

**`Tone marks` (*shōten*)** and voiced sound indications using double-dot **`Tone marks` (*shōten*)** (i.e., *dakuten* represented via *shōten* placement) can be applied to **`Fanqie spellings`**, **`Similar sound notes`**, and **`Kana glosses`**.
Nasal sound symbols are applied to **`Kana glosses`**.

**Types of `Japanese Native Readings` (*wakun*)**

**`Japanese Native Readings` (*wakun*)** are generally written in Katakana.

The only exception is for '木賊' (*tokusa*), where the *Man'yōgana* '度久佐' (*tokusa*) is used; this instance does not have **`Tone marks` (*shōten*)** applied.

**`Japanese Native Readings` (*wakun*)** can have **`Tone marks` (*shōten*)** and voiced sound indications (using double-dot *shōten*) applied.
There is one recognized, though not entirely certain, instance of a nasal sound symbol being applied to a **`Japanese Native Reading` (*wakun*)** (a nasal sound symbol on 'ナ' in the *wakun* 'ナラフ' for the character '儔').


**Input and Processing Methods for `Tone Marks` (*shōten*), Voiced Sound Marks, and Nasal Sound Symbols**

**`Tone Marks` (*shōten*)** and voiced sound indications (using double-dot *shōten*) are applied to **`Hanzi (Chinese characters)`** or to **`Japanese Native Readings` (*wakun*)** written in Katakana.
Nasal sound symbols are applied to **`Phonetic Glosses`** in Katakana (i.e., **`Kana glosses`**) or to **`Japanese Native Readings` (*wakun*)** in Katakana.

For **`Fanqie spellings`** (反切, *hansetsu*), which consist of an initial character (反切上字, *hansetsu jōji*) and a final character (反切下字, *hansetsu kaji*), any applied **`Tone Marks` (*shōten*)** are converted to their corresponding symbols (e.g., L, H) and enclosed in full-width parentheses（）.

**`Similar sound notes`** (類音注, *ruion-chū*) are also enclosed in full-width parentheses（）.

**`Kana glosses`** (仮名音注, *kana-onchū*), when written in small characters around *fanqie* spellings or similar sound notes, are enclosed in Japanese quotation marks 「」. However, if a **`Kana gloss`** is explicitly prefixed with "呉" (*Go*, for Go-on) or "和" (*Wa*, for Wa-on) within the main text of the **`Original Glosses`**, the quotation marks 「」 are omitted.

For **`Phonetic Glosses`**, **`Tone Marks` (*shōten*)**, voiced sound marks, and nasal sound symbols are recorded on a per-**`Hanzi (Chinese character)`** basis (i.e., for each single character). For **`Japanese Native Readings` (*wakun*)**, these marks are recorded for the entire word or phrase.

**Partial Application of `Tone Marks` (*shōten*)**

If **`Tone Marks` (*shōten*)** are applied to only a part of a **`Japanese Native Reading` (*wakun*)**, the parts without **`Tone Marks` (*shōten*)** are indicated by a half-width underscore ('_', U+005F). (This typically means **`Hanzi (Chinese characters)`** are treated one by one, while a *wakun* is treated as a whole unit for tone marking, with underscores for unmarked morae/syllables if only part of it is marked).

**Examples:**
1.  偵 勅令（R）反
2.  使 所里（H）所使（H）二反
3.  㒓 達（S）音
4.  僆 輦（H）練（R）二音
5.  偶 音藕（HV）「コウ」
6.  侮 音武（L-HV）「フ」「ム（H）」
7.  拱 呉音恐（L）
8.  捉 呉冊（S） サク（_L）
9.  類 和ルイ（_L）
10. 形 和キヤウ（N\_H-N）

Examples 1 and 2 are **`Fanqie spellings`**. Examples 3 and 4 are **`Similar sound notes`**. Examples 5 and 6 are **`Similar sound notes`** accompanied by **`Kana glosses`**.

Examples 7 and 8 are *Go-on* (呉音) readings; example 7 is a **`Similar sound note`**, while example 8 is a **`Similar sound note`** accompanied by a **`Kana gloss`**.

Examples 9 and 10 are *Wa-on* (和音) readings; example 9 has **`Tone Marks` (*shōten*)** recorded, while example 10 has both **`Tone Marks` (*shōten*)** and nasal sound symbols.


"Regarding **`Tone Marks` (*shōten*)**, while distinguishing between those written in red ink (朱点, *shuten* – also referred to by some specialists as **`Vermilion Glosses`**) and those written in black ink (墨点, *bokuten*) is important, this distinction has not been made in the current data input. We anticipate detailed verification by specialists in historical Japanese phonology."


### `Morphosyntactic Glosses (*wokototen*)` (ヲコト点)

No definitive examples of **`Morphosyntactic Glosses` (*wokototen*)** have been confirmed in the manuscript at this time.
Should any definitive examples be identified, they will be transcribed using Hiragana.
。
This may be an example of a *wokototen*.

- `kazama_location`: K0601343, `hanzi_entry`: 玊, `definition`: 音夙（T）「シク」　又栗（T）「リク」　又欣救反　琢「ミカク」玉を工也, `remarks`: Ikeda's note: The character '栗' is a mistake for '粟'. The vermilion dot on the character '玉' may be the *wokototen* mark for 'wo (を)'. Although '工也' is written in small characters, it has been transcribed in large characters because the *Guangyun* provides an explanatory note for the meaning '琢玉工' (a jade craftsman).

### Line Breaks and Spacing (改行・空白, *kaigyō/kūhaku*)

Line breaks as they appear in the original manuscript are not explicitly represented in the transcribed data. Spacing in the data reflects the results of interpretation rather than an exact reproduction of the original manuscript's spacing.

### `Interpolated Glosses` (補入注文, *honyū chūmon*)

**`Interpolated Glosses`** (補入注文, *honyū chūmon*) are inserted at positions deemed appropriate based on textual analysis.

### Unannotated `Entries` (無注記, *muchūki*)

When an **`Entry`** has no **`Original Glosses`**, this is indicated by "（無）" (using full-width parentheses).


### `Supplementary Headword Annotations` (掲出字補注, *keishutsuji hochū*)

Annotations applied directly to a **`Headword`** are referred to as **`Supplementary Headword Annotations`** (掲出字補注, *keishutsuji hochū*).
These include **`Tone marks` (*shōten*)** and Katakana phonetic annotations directly applied to the **`Headword`** to indicate Sino-Japanese readings; side-line *kun* readings (傍訓, *bōkun*) and *kaeriten* marks (返点, *kaeriten*) directly applied to the **`Headword`** to indicate Japanese native readings and reading order; and annotations from variant manuscripts found at the end of the **`Original Glosses`** (but pertaining to the **`Headword`**).
These will be explained together here.

**`Tone Marks` (*shōten*) and Katakana Phonetic Annotations for `Headwords`**

**`Tone marks` (*shōten*)** and Katakana phonetic script applied to a **`Headword`** to indicate its Sino-Japanese reading are transcribed at the beginning of the **`Original Glosses`**. They are preceded by a double circle (◎, U+25CE) and the annotated character (被注字, *hichūji*), followed immediately by the annotation. **`Tone marks` (*shōten*)** are represented by their abbreviations within full-width parentheses （）, and Katakana phonetic script is enclosed in Japanese quotation marks 「」.

**Side-Line *Kun* Readings, *Kaeriten* Marks, and Other Annotations for `Headwords`**

*Side-line *kun* readings* (傍訓, *bōkun*) and *kaeriten* marks applied to a **`Headword`** to indicate its Japanese native reading and reading order are transcribed immediately following the annotated character, preceded by a bullseye mark (⦿, U+29BF) and the annotated character, and enclosed in 「」.
Annotations in literary Chinese (such as **`Fanqie spellings`**, **`Semantic Glosses in Chinese`**, **`Notes on Character Form`**, or **`Source Attributions`**) applied to a **`Headword`** are transcribed immediately following the annotated character, preceded by a lozenge/diamond mark (◇, U+25C7) and the annotated character, and enclosed in 「」.
**`Annotations from Variant Manuscripts`** applied to a **`Headword`** are transcribed immediately following the annotated character, preceded by a black up-pointing triangle (▲, U+25B2) and the annotated character, and enclosed in 「」.

**`Annotations from Variant Manuscripts` at the End of `Original Glosses`**

**`Annotations from Variant Manuscripts`** pertaining to the **`Headword`** but added at the end of the **`Original Glosses`** are indicated by a preceding '▲' at the end of the glosses, with the content of the annotation enclosed in 「」.

**Order of Transcription**

If it is necessary to transcribe multiple types of **`Supplementary Headword Annotations`** for a single **`Headword`**, they are recorded in the following order: ◎ Sino-Japanese reading information, ⦿ Japanese native reading information / reading order marks, ◇ Annotations in literary Chinese, ▲ Annotations from variant manuscripts.

**Examples:**
* ◎純「ト（L）ン（H）」
* ⦿虱「キサヽ」
* ◇⿱惟乃「手歟」
* ▲⿲骨石辛「𩪧イ」


### Other Noteworthy Cases

**Decipherment Notes (判読注, *handoku-chū*)**

A compiler's decipherment note (解讀注記, *jiědú zhùjì* in Chinese) may be indicated by enclosing it in parentheses ().

**Example:**
* ⿰阝⿱𠂉夕 オチイル（L___、ホを見消してチ）
    *(This `hanzi_entry` (⿰阝⿱𠂉夕) is followed by its `Japanese Native Reading (*wakun*)` 'オチイル' with `Tone Marks` and a decipherment note "ホを見消してチ" [meaning "'ホ' is deleted and replaced by 'チ'"].)*

For this example, the following content would be recorded in the `remarks` column (as a **`Compiler's Remark`**):

> Masamune's Index, under 'オホ（-ヒ）チイル', notes: "'ホ（-ヒ）' is a mark indicating 'ホ' was deleted. Should it be 'オチイル'?" Kusakawa's *Wakun Shūsei* records 'オホ' and 'チイル' separately. Mochizuki's *Wakun Shūsei* records 'オチイル'. Ikeda's note: Follow Masamune and Mochizuki.

**`Fanqie` Spellings within `Headwords`**

If a **`Fanqie spelling`** is inserted within a **`Multi-Character Form Headword`** (typically an idiom/compound), a forward slash '/' (half-width slash) is used to indicate the separation.

**Example:**
* 𣚊ー（棗） 人充　/　ノナツメ（_HHH）

In this example, which shows the **`Headword`** followed by its **`Original Glosses`**, the **`Fanqie spelling`** "人充" is written directly beneath '𣚊' (the first part of the **`Headword`** '𣚊ー（棗）').

**`Japanese Native Readings` (*wakun*) Attached to `Hanzi (Chinese characters)` within `Original Glosses`**

Small Katakana characters (representing **`Japanese Native Readings` (*wakun*)**) attached to a **`Hanzi (Chinese character)`** within the **`Original Glosses`** are transcribed as is, enclosed in Japanese quotation marks 「」. If such a *wakun* is written in even smaller characters (小字, *shōji*), it is enclosed in full-width angle brackets 〈〉. Examples of the latter are rare.

**Examples:**
1.  琢「ミカク」玉工也
2.  圏〈ヲリ〉
3.  ー「タヘ」「平歟」趹「ハシル」追「ヲオフ」蹤「ニクルヲ」

Example 1 is seen within the **`Original Glosses`** for the **`Headword`** '玊'; the **`Japanese Native Reading` (*wakun*)** 'ミカク' is attached to the right side of the character '琢'.

Example 2 is seen within the **`Original Glosses`** for the **`Headword`** '檻'; the **`Japanese Native Reading` (*wakun*)** is attached below '圏' in small characters.

Example 3 is seen within the **`Original Glosses`** for the **`Headword`** '要'. It shows example sentences (or phrases) and their **`Japanese Native Readings` (*wakun*)**.
