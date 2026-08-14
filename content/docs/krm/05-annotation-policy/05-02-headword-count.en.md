---
title: "Calculation of Headword Character Count"
weight: 18
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Calculation of Headword Character Count

This page is detailed reference data supporting the policy set out in [Basic Principles and Analytical Focus for Annotation Creation](./05-01-basic-policy/). For definitions of the character-form terms used below (Miswritten Characters, Omitted Characters, Superfluous Characters, etc.), see [Handling Issues in Transcription, Notation, and Annotation](/en/docs/krm/04-entry-input/04-03-handling/).

This section will explain issues such as **`Miswritten Characters`** (誤字, *goji*), **`Omitted Characters`** (脱字, *datsuji*), **`Superfluous Characters`** (衍字, *enji*), interpolations (補入, *honyū*), **`Embedded Items`** (埋字, *umeji*; referring to entries incorporated within another entry), **`Substitution Marks`** (代用符号, *daiyō fugō*), and **`Iteration Marks`** (踊り字, *odoriji*). Following this discussion, it will proceed to calculate the *keishutsuji-sū* (掲出字数). The *keishutsuji-sū* refers to the total number of characters that constitute all **`Headwords`**.

Then, based on the results of this *keishutsuji-sū* calculation, the number of **`Entries`** (*keishutsu kōmoku-sū*, 掲出項目数) will also be calculated. The number of **`Entries`** will be aggregated according to the number of characters constituting their **`Headwords`** (e.g., **`Entries`** with single-character **`Headwords`**, **`Entries`** with two-character **`Headwords`**, and so on).

Finally, a list will be provided showing the *keishutsuji-sū* (total headword character count) and the number of **`Entries`** (*keishutsu kōmoku-sū*) for each of the 120 radical sections of the *Myōgishō*. In this listing, our calculated number of **`Entries`** will be compared with the entry count calculated by Sakai Kenji, and any discrepancies between our calculations and his will also be explained.

## `Miswritten Characters` (*goji*)

Below are some examples of **`Miswritten Characters`** (誤字, *goji*) found in **`Headwords`**.

The examples are presented by extracting relevant portions from `krm_main.tsv` and adding the content of the `remarks` column from `krm_notes.tsv`. For ease of reference, the Kazama Edition location is also shown as `kazama_location`. For instance, `K02008840` indicates an appearance in Volume 2 (仏中, *Butsuchū*), Page 8, Line 8, Segment 4 (the explanation for the last digit, which represents character order within the segment, is omitted here).

The first example is relatively straightforward.

**Example:**
* `kazama_location`: K02008840
* `hanzi_entry`: 姡
* `original_entry`: 活
* `definition`: 今
* `remarks`: The **`Headword`** is a scribal error. It has been corrected to '姡' based on the Kōzan-ji, Renshō-in, and Sainen-ji manuscripts, all of which have '姡'.

This example is a **`Headword`** from the "女" (woman) radical section. Since other manuscripts (異本, *ihon*) have the character '姡' (with the "女" woman radical), it is clear that there is a scribal error in the Kanchi-in manuscript.


The following is an example where it is difficult to determine whether the **`Headword`** is a **`Miswritten Character`**.

**Example:**

  * `kazama_location`: K01045610
  * `hanzi_entry`: 迷
  * `original_entry`: 〇
  * `definition`: 俗悉字　私逸反
  * `remarks`: Is the **`Headword`** '迷' a glyph form that evolved from '⿺辶半', a **`variant character` (*itaiji*)** of '悉'?

In this example, the **`Headword`** '迷' has the **`Note on Character Form`** "俗悉字" (*zoku Shitsu ji*; "popular form of 悉") in its **`Original Glosses`**, indicating it is treated as a 'popular' form of '悉'. However, '迷' and '悉' are distinct characters, and to connect them, a scribal error must be assumed. It is presumed that this form arose from writing the '心' (heart) component at the bottom of '悉' in a way that resembles '辶' (motion radical). This is an example where a **`variant character` (*itaiji*)** of '悉' appears to have been conflated with, or graphically evolved towards, the character '迷'.

The hypothesized process of change from '悉' to '迷' can be illustrated as follows:


![悉](https://glyphwiki.org/glyph/u6089.50px.png)  →
![𢘻](https://glyphwiki.org/glyph/u2263b.50px.png)  → 
![𭜧](https://glyphwiki.org/glyph/u2d727-j.50px.png)  → 
![𨒃](https://glyphwiki.org/glyph/u28483-g.50px.png)  → 
![迷](https://glyphwiki.org/glyph/u8ff7.50px.png) 
 
According to GlyphWiki, an example of  ![𨒃](https://glyphwiki.org/glyph/u28483-g.50px.png) (𨒃, U+28483) can be found in [*Yínánzì Kǎoshì Yǔ Yánjiū* (疑難字考釋與研究, Philological Studies and Research on Difficult and Problematic Characters)].



## `Omitted Characters` (脱字, *datsuji*)

**`Omitted Characters`** (*datsuji*) in **`Headwords`**, which have been detailed elsewhere, are handled as follows: when a character is clearly omitted from a **`Headword`**, the presumed omitted character is indicated by enclosing it in full-width square brackets "［］".

**Example:**
```
是／［以］
不／奈／［何］
将／為／［便］
嘻／［囉］
奢／［侈］
奚／［如］
```

An example of the corresponding annotation is shown below:

**Example:**
* `kazama_location`: K02006630
* `hanzi_entry`: 奚／［如］
* `original_entry`: 〇／〇
* `definition`: イカム（__L
* `remarks`: The character '如' is omitted. The Renjō-in manuscript has '奚如'. The Kōzan-ji manuscript does not use the substitution mark 'ー' but explicitly writes '如', and this entry is located near the latter half of the "女" (woman) radical section. This Kōzan-ji manuscript usage is considered to be an earlier example (Okada's research, p. 192).

## `Superfluous Characters` (*enji*)

Instances of **`Superfluous Characters`** (*enji*) in **`Headwords`** are rarely found.

**Example:**
* `kazama_location`: K04024810, `hanzi_entry`: ⿱赤廾, `definition`: サカユ　シツカナリ
* `kazama_location`: K04024820, `hanzi_entry`: 人, `definition`: （無） (Unannotated), `remarks`: Could this '人' be a superfluous character? Alternatively, the **`Headword`** might be a variant of '奕', and this '人' a miscopied iteration mark for the compound '奕奕'. The compound '奕奕' has examples in the *Shijing* (Book of Odes).

The reason for the presence of the character '人' in the second entry is unclear, and it is suspected to be a superfluous character.



## `Embedded Characters` (*umeji*) and the *Bunchūshiki* (Divided-Annotation Style)

**`Embedded Characters`** (*umeji*) refer to **`Entry`**-like segments that are incorporated within another main **`Entry`**.

**Example:**
* `kazama_location`: K02012610
* `hanzi_entry`: 娜
* `definition` (representing **`Original Glosses`**): 乃可（H）反　マヽハヽ　タヲヤカナリ　婀ー　ヨキカホ　ナマメク
* `remarks` (**`Compiler's Remark`**): Could the segment "婀ー　ヨキカホ　ナマメク" be an embedded item/entry?

These embedded segments can either be considered equivalent to a separate **`Entry`** or interpreted as an explanation of a compound word provided within the **`Original Glosses`** of the main **`Entry`**.

The method of embedding glosses for a multi-character compound within the **`Original Glosses`** of a single (often the first) character of that compound is termed the "**`Divided-Annotation Style`**" (分註式, *Bunchūshiki*). In contrast, the method of presenting such information as an independent **`Entry`** following the main single-character **`Entry`** is called the "**`Independent-Entry Style`**" (独立式, *Dokuritsushiki*) (Okada Yoshio, *Ruiju Myōgishō no Kenkyū* [A Study of the *Ruiju Myōgishō*], p. 313 ff.).

While these annotation styles are important indicators for studying the relationships between different manuscripts and the sequential ordering of **`Entries`**, they will not be discussed further in this section.

## `Substitution Marks` (代用符号, *daiyō fugō*) using '｜' (transcribed as 'ー')

When the same **`Headword`** as in the preceding **`Entry`** is used, the vertical line '丨' (U+4E28) is sometimes employed in the original manuscript to substitute for it. In this database, for better readability in horizontal text, this '丨' is represented by 'ー' (CHOONPU - long vowel mark, U+30FC), followed by the actual **`Headword`** it represents, enclosed in parentheses.

While the **`Substitution Mark`** 'ー' (representing the original '丨') almost always refers to the **`Headword`** of the immediately preceding **`Entry`**, users should be aware that in very rare cases, it may refer to the **`Headword`** of an **`Entry`** that is not directly adjacent, skipping over one or more intervening **`Entries`**.

The following example illustrates a case where 'ー' refers to a **`Headword`** that is considerably distant.


**Example:**
* `kazama_location`: K01038411, `hanzi_entry`: 以／後, `definition`: ノチ
* `kazama_location`: K01038420, `hanzi_entry`: 㣭, `definition`: 字公（L）反　數也
* `kazama_location`: K01038430, `hanzi_entry`: 𢓈, `definition`: 音旬之去声　トヽム　メクル　アマネシ
* `kazama_location`: K01038510, `hanzi_entry`: 徇, `definition`: 同　トナフ　*アハネシ（L___）　シタカフ（__HV_）　*イトナム
* `kazama_location`: K01038530, `hanzi_entry`: 彴, `definition`: 止「已」約反　シタフ
* `kazama_location`: K01038541, `hanzi_entry`: 已／ー, `definition`: 同
* `kazama_location`: K01038611, `hanzi_entry`: 向／ー, `definition`: ユクサキ（HH__）　ユクスヱ, `remarks`: Erroneous **`Headword`**; should be '向後'. Okada's research (pp. 193-194) notes that the use of 'ー' is appropriate for the Kōzan-ji manuscript.

Regarding the last two **`Headwords`** in the example ('已／ー' and '向／ー'), if one were to straightforwardly interpret the substitution mark 'ー' as referring to the immediately preceding **`Headword`** ('彴' from `K01038530`), they would become '已／ー (substituting 彴)' and '向／ー (substituting 彴)'. However, this interpretation does not make sense in context. As Okada Yoshio has pointed out, the **`Headword`** '向／ー' in this section should actually be '向後'. Consequently, the preceding **`Headword`** '已／ー' should then be interpreted as '已／後'.

In other words, it is hypothesized that this section originally had the **`Entries`** with **`Headwords`** '以／後', '已／後', and '向／後' listed in sequence. Subsequently, the **`Entries`** listed above from the second one (`K01038420`, **`Headword`** '㣭') through the fifth one (`K01038530`, **`Headword`** '彴') are presumed to have been inserted into this original sequence.


## `Iteration Marks` (踊り字, *odoriji*) using '〻'

**`Iteration Marks`** (踊り字, *odoriji*) are also known as repetition marks (繰り返し符号, *kurikaeshi fugō*) or similar terms.
Although the iteration mark '々' (U+3005) is commonly used for **`Hanzi (Chinese characters)`** today, this database employs '〻' (U+303B).
In the Kanchi-in manuscript, the '〻' mark is typically used for the second and subsequent characters in the **`Headword`** of an **`Entry`** for a compound word (熟語項目, *jukugo kōmoku*), as shown in the examples below.

**Examples:**
* `kazama_location`: K01059441, `hanzi_entry`: ー（迢）／〻（迢）, `definition`: トホノカナリ
* `kazama_location`: K02021731, `hanzi_entry`: 曽／ー（祖）／〻（母）, `definition`: オホオハ（LHLHV）
* `kazama_location`: K06036711, `hanzi_entry`: 郁／〻（郁）, `definition`: マタラカナリ（LLVHL__）


## Characters in `Original Glosses` Written in Large Size

There are instances where characters within the **`Original Glosses`** are written in a large size, similar to **`Headwords`**, which can lead to confusion.

**Example 1:**
* `kazama_location`: K02051210
* `hanzi_entry`: 𠰍
* `definition`: 音主　呼鷄
* `remarks` (**`Compiler's Remark`**): In both the Kōzan-ji and Renjō-in manuscripts, the part corresponding to '呼鷄' is rendered as 'ー〻呼鷄' (where 'ー〻' likely indicates iteration or continuation from a preceding entry, followed by '呼鷄'). The Kanchi-in manuscript, however, writes '呼鷄' in a large size.

This is an example from the "口" (mouth) radical section. While the Kanchi-in manuscript writes '呼鷄' in a large size, both the Kōzan-ji and Renjō-in manuscripts have 'ー〻呼鷄', suggesting that '呼鷄' in the Kanchi-in manuscript should be considered as characters within the **`Original Glosses`** (rather than a separate **`Headword`**).

**Example 2:**
* `kazama_location`: K06100620
* `hanzi_entry`: 憙
* `definition`: 音喜（H-L）　又嬉　コノム（LLH）　喜「注也」　ネカフ　ツクス　ヨロコフ（LLH_）　ヒロシ（LL_）
* `remarks` (**`Compiler's Remark`**): Within the **`Original Glosses`**, the character '喜' is written in a large size; '注也' ("this is a gloss") is written to its left in red ink.

This example is from the "心" (heart) radical section. Here, the character '喜' is written in a large size, making it appear like a **`Headword`**. However, the annotation '注也' (*chū nari*; "this is a gloss") to its left explicitly indicates that '喜' is a character within the **`Original Glosses`** and not a **`Headword`**.

## Number of `Entries`

### Number of `Entries` and Total Headword Character Count

The number of **`Entries`** in the Kanchi-in manuscript of the *Ruiju Myōgishō* was published in: Ikeda Shoju, Liu Guanwei, Jung Munho, Zhang Xinfang, and Li Yuan, “Full-text Database of *Ruiju Myōgishō*, Kanchi-in MS : A Look at Development Methods and Calculating the Number of Headwords.” (*Kuntengo to Kuten Shiryō* 144, 2020). This paper classifies **`Entries`** by the number of characters in their **`Headwords`** and provides a detailed breakdown of these counts.

For example, a table row such as:

| No. | Radical[^1] | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|---------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 001 | 人 (Man)  | 616    | 203    | 26     | 5      | 2      | 3       | 855            | 1,149        |

[^1]:In this table and those that follow, the term "部" (Radical) is used. This is a revision from "篇" (*hen*), which the author (Ikeda) had previously employed in papers and other publications.

indicates that in the "人" (man) radical section (人部, *jinbu*), there are 616 **`Entries`** whose **`Headwords`** are in **`Single Character Form`** (1 character). **`Headwords`** with two or more characters are in **`Multi-Character Form`**; in this section, there are 203 **`Entries`** with two-character **`Headwords`**, 26 with three-character, 5 with four-character, 2 with five-character, and 3 with six-or-more-character **`Headwords`**. The total number of **`Entries`** for this radical section is 855.
The breakdown for the "6+ char" (6字以上) category is: 2 **`Entries`** with six-character **`Headwords`** and 1 **`Entry`** with a seven-character **`Headword`**.
Therefore, the total number of characters (*jisū*, 字数; i.e., the sum of characters in all **`Headwords`** for this section) is calculated as 1,149 using the following formula:

```
616 (representing 616 x 1) + (203 x 2) + (26 x 3) + (5 x 4) + (2 x 5) + (2 x 6) + (1 x 7) = 1,149
```

### Verification of `Entry` Counts

The verification of **`Entry`** counts was primarily focused on radical sections where discrepancies were found with the figures presented in Sakai Kenji's "Ruiju Myōgishō no Jijun to Bushu Hairetsu" (Character Order and Radical Arrangement in the *Ruiju Myōgishō*), published in *Honpō Jishoshi Ronsō* (Collected Papers on the History of Dictionaries in Japan), edited by Yamada Tadao (Tokyo: Sanseidō, 1967), pp. 191–258.

As a result, discrepancies were identified in the following 25 radical sections. The "Difference" column indicates cases where the count in Ikeda et al. (2020) is less than that in Sakai (1967) with a negative number (e.g., -1), and where it is greater with a positive number (e.g., +1). 
Counts determined to be correct as a result of this verification are shown in **bold**. Sections shown with non-bolded figures signify that, even if the counts from the two sources differ, a conclusion was pending or not reached in the current verification.


| No. | Radical      | Sakai (1967) | Ikeda et al. (2020) | Diff. |
|-----|--------------|------:|-----------:|------:|
| 001 | 人 (Man)       | **856** | 855       | -1    |
| 003 | 辵 (Walk)    | 463   | **462** | -1    |
| 014 | 口 (Mouth)   | 1,034 | **1,035** | +1    |
| 018 | 日 (Sun)     | 557   | **556** | -1    |
| 020 | 肉 (Flesh)   | 718   | **717** | -1    |
| 023 | 角 (Horn)    | 127   | **126** | -1    |
| 027 | 髟 (Hair)    | 166   | **165** | -1    |
| 029 | 木 (Tree)    | 1,334 | **1,333** | -1    |
| 039 | 火 (Fire)    | 512   | 513       | +1    |
| 041 | 水 (Water)   | 1,322 | 1,321     | -1    |
| 044 | 足 (Foot)    | 494   | **493** | -1    |
| 051 | 石 (Stone)   | **375** | 376       | +1    | 
| 052 | 玉 (Jade)    | 384   | **383** | -1    |
| 057 | 心 (Heart)   | 909   | **908** | -1    |
| 066 | 勹 (Wrap)    | 34    | **33** | -1    |
| 068 | 雨 (Rain)    | 226   | **228** | +2    |
| 075 | 疒 (Sickness)| 400   | **399** | -1    |
| 080 | 寸 (Inch)    | 41    | **39** | -2    |
| 087 | 食 (Eat)     | 214   | **213** | -1    |
| 095 | 弓 (Bow)     | 102   | **101** | -1    |
| 111 | 鳥 (Bird)    | 532   | 533       | +1    |
| 113 | 魚 (Fish)    | 378   | **379** | +1    |
| 114 | 虫 (Insect)  | 665   | 664       | -1    |
| 117 | 鬼 (Ghost)   | **74** | 75        | +1    |
| 120 | 雑 (Misc.)   | 1,500 | **1,501** | +1    |

For the following radical sections, the counts in Sakai (1967) and Ikeda et al. (2020) were initially the same, but verification revealed a need for correction:

| No. | Radical    | Sakai (1967) & Ikeda et al. (2020) - Initial | Ikeda et al. (2020) - Revised | Diff. (from initial) |
|-----|--------------|-----------------------------:|-----------------------:|---------------------:|
| 028 | 手 (Hand)    | 1,148                        | **1,149** | +1                   |
| 086 | 毛 (Fur)     | 104                          | **103** | -1                   |

Many of these discrepancies relate to differences in how **`Entries`** are identified and counted. Therefore, the following sections will specifically explain the discrepancies with the **`Entry`** counts presented in Sakai (1967). Finally, a list of **`Entry`** counts for each radical section, based on the revised figures, will be provided.


See [Entry and Headword Counts by Radical Section](../05-02b-headword-count-by-fascicle/) for the detailed radical-by-radical breakdown.
