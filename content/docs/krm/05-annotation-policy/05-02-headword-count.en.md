---
title: "Calculation of Headword Count"
weight: 18
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Calculation of Headword Character Count

This section will explain issues such as **`Miswritten Characters`** (誤字, *goji*), **`Omitted Characters`** (脱字, *datsuji*), **`Superfluous Characters`** (衍字, *enji*), interpolations (補入, *honyū*), **`Embedded Characters`** (埋字, *umoji*; referring to entries incorporated within another entry), **`Substitution Marks`** (代用符号, *daiyō fugō*), and **`Iteration Marks`** (踊り字, *odoriji*). Following this discussion, it will proceed to calculate the *keishutsuji-sū* (掲出字数). The *keishutsuji-sū* refers to the total number of characters that constitute all **`Headwords`**.

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



### `Omitted Characters` (脱字, *datsuji*)

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
* `kazama_location`: K0200663
* `hanzi_entry`: 奚／［如］
* `original_entry`: 〇／〇
* `definition`: イカム（__L
* `remarks`: The character '如' is omitted. The Renjō-in manuscript has '奚如'. The Kōzan-ji manuscript does not use the substitution mark 'ー' but explicitly writes '如', and this entry is located near the latter half of the "女" (woman) radical section. This Kōzan-ji manuscript usage is considered to be an earlier example (Okada's research, p. 192).

### Superfluous Characters
## `Superfluous Characters` (*enji*)

Instances of **`Superfluous Characters`** (*enji*) in **`Headwords`** are rarely found.

**Example:**
* `kazama_location`: K0402481, `hanzi_entry`: ⿱赤廾, `definition`: サカユ　シツカナリ
* `kazama_location`: K0402482, `hanzi_entry`: 人, `definition`: （無） (Unannotated), `remarks`: Could this '人' be a superfluous character? Alternatively, the **`Headword`** might be a variant of '奕', and this '人' a miscopied iteration mark for the compound '奕奕'. The compound '奕奕' has examples in the *Shijing* (Book of Odes).

The reason for the presence of the character '人' in the second entry is unclear, and it is suspected to be a superfluous character.



## `Embedded Characters` (*umeji*) and the *Bunchūshiki* (Divided-Annotation Style)

**`Embedded Characters`** (*umeji*) refer to **`Entry`**-like segments that are incorporated within another main **`Entry`**.

**Example:**
* `kazama_location`: K0201261
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


### Characters in `Original Glosses` Written in Large Size

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

The number of **`Entries`** in the Kanchi-in manuscript of the *Ruiju Myōgishō* was published in: Ikeda Shoju, Liu Guanwei, Jun Munho, Zhang Xinfang, and Li Yuan, “Full-text Database of *Ruiju Myōgishō*, Kanchi-in MS : A Look at Development Methods and Calculating the Number of Headwords.” (*Kuntengo to Kuten Shiryō* 144, 2020). This paper classifies **`Entries`** by the number of characters in their **`Headwords`** and provides a detailed breakdown of these counts.

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

### *Butsujō* (仏上 – First "Buddha" Fascicle)

In the ***Butsujō*** (仏上) section, discrepancies in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) are found for the following two radical sections. The figures presented in the table below are from Ikeda et al. (2020):


| No. | Radical | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|---------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 001 | 人 (Man)  | 616    | 203    | 26     | 5      | 2      | 3       | 855            | 1,149        |
| 003 | 辵 (Walk) | 368    | 81     | 10     | 2      | 0      | 1       | 462            | 575          |

For the **"人" (Man) radical section** (人部, *jinbu*), the following instance, which should have been counted as two separate **`Entries`**, was mistakenly counted as a single **`Entry`**:

  * `kazama_location`: K01008341, `hanzi_entry`: 於／ー（何）, `definition`: 同
  * `kazama_location`: K01008343, `hanzi_entry`: 奈／ー（何）, `definition`: 同

This can be confirmed on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586891/10) in the National Diet Library Digital Collections.

In addition to this, there are the following four **`Entries`** where **`Omitted Characters`** in the **`Headword`** were supplied:

  * `kazama_location`: K01005131, `hanzi_entry`: 是／［以］
  * `kazama_location`: K01008421, `hanzi_entry`: 不／奈／［何］
  * `kazama_location`: K01031111, `hanzi_entry`: 将／為／［便］
  * `kazama_location`: K01035310, `hanzi_entry`: 奢／［侈］

The figures for the "人" (Man) radical section in Ikeda et al. (2020) need to be corrected for the number of **`Entries`** as follows. The corrected figures are shown in **bold**:

| No. | Radical | 1-char  | 2-char  | 3-char  | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|---------|--------:|--------:|--------:|-------:|-------:|--------:|---------------:|-------------:|
| 001 | 人 (Man)  | **614** | **205** | **28** | **4** | 2      | 3       | **856** | **1,153** |

For the **"辵" (Walk) radical section** (辵部, *Chaku-bu*), the following two **`Entries`** appear consecutively. Although they might seem like a single **`Entry`**, '迁' and '還' are distinct characters.

  * `kazama_location`: K01050412, `hanzi_entry`: 迁
  * `kazama_location`: K01050420, `hanzi_entry`: 還, `definition`: 音環(L)　カヘル-ス　メクル　マクラス　シリソク　マタ　ヤム　又音旋　和外ン

This is a section where '迂', '迃', and '迁' appear in sequence, and it is considered to be an arrangement where **`Headwords`** with similar glyph forms are listed consecutively. The **`Entry`** for '迁' is treated as an unannotated **`Entry`**.

This can be confirmed on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586891/31) in the National Diet Library Digital Collections.

The discrepancy in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) is presumed to be due to differences in the method of counting this particular instance.


### *Butsuchū* (仏中 – Middle "Buddha" Fascicle)

In the ***Butsuchū*** section, discrepancies in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) are found for the following three radical sections. The figures presented in the table below are from Ikeda et al. (2020):


| No. | Radical  | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|----------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 014 | 口 (Mouth) | 858    | 146    | 17     | 9      | 4      | 1       | 1,035          | 1,274        |
| 018 | 日 (Sun)   | 450    | 96     | 7      | 2      | 1      | 0       | 556            | 676          |
| 020 | 肉 (Flesh) | 580    | 119    | 12     | 2      | 1      | 3       | 717            | 888          |

For the **"口" (Mouth) radical section** (口部, *kōbu*), there are three instances where the identification of **`Entries`** is problematic.

First, the following **`Entries`** for '吉' and '喆' are listed consecutively and might appear to be a single **`Entry`**:

  * `kazama_location`: K02047711, `hanzi_entry`: 吉
  * `kazama_location`: K02047712, `hanzi_entry`: 喆, `definition`: 知列反　サトル（HH\_）　アキラカナリ　シル　サカシ　シム

However, '吉' (*Guangyun*: "居質切" *jūzhì qiè*, Entering tone, *Zhi* (質) rhyme, character 吉) and '喆' (*Guangyun*: "陟列切" *zhìliè qiè*, Entering tone, *Xue* (薛) rhyme, character 哲) are distinct characters. The **`Entry`** for '吉' is an unannotated one.

Please refer to the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586892/27) in the National Diet Library Digital Collections.

Next, the **`Headwords`** '⿰口⿰木㬅' and '𠾺' are listed consecutively (following an **`Entry`** for '㘄') and might also appear to be a single **`Entry`** or part of the '㘄' **`Entry`**:

  * `kazama_location`: K02056421, `hanzi_entry`: 㘄, `definition`: 魯登反
  * `kazama_location`: K02056422, `hanzi_entry`: ⿰口⿰木㬅
  * `kazama_location`: K02056430, `hanzi_entry`: 𠾺, `definition`: 俗善字

However, '⿰口⿰木㬅' is graphically similar to '㘄', and it is presumed to have been listed for that reason. The **`Entry`** for '⿰口⿰木㬅' is likely an unannotated one.

Please refer to the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586892/32) in the National Diet Library Digital Collections.

The following is an example that could be interpreted as either one **`Entry`** or two, depending on the criteria for identification:

  * `kazama_location`: K02030211, `hanzi_entry`: 呴／吽／𤘘, `definition`: ◉呴吽𤘘「クチサキラ（HHHVHL）」　「或本ニハ已上五字カキツヽケタリ」 (In another manuscript, the preceding five characters are written consecutively)
  * `kazama_location`: K02030221, `hanzi_entry`: 吼／㖃, `definition`: 五正　呼厚反　イヒキ　ヨハフ　ホユ（LH）　ナク（HL）　和ク（L）

The **`Entry`** for '呴／吽／𤘘' has the note "或本ニハ已上五字カキツヽケタリ" (In another manuscript, the preceding five characters are written consecutively). At first glance, this makes it seem separate from the following **`Entry`** for '吼／㖃'. However, it could also be considered as a single, continuous **`Entry`**.

In Ikeda et al. (2020), these were treated as two separate **`Entries`**, prioritizing the format of their presentation in the manuscript.

Please refer to the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586892/19) in the National Diet Library Digital Collections.


### *Butsuge-hon* (仏下本 – Lower "Buddha" Fascicle, First Part)

In the ***Butsuge-hon*** section, discrepancies in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) are found for the following four radical sections. The figures presented in the table below are from Ikeda et al. (2020):

| No. | Radical      | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|--------------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 023 | 角 (Horn)    | 104    | 20     | 2      | 0      | 0      | 0       | 126            | 150          |
| 027 | 髟 (Hair)    | 127    | 28     | 5      | 2      | 3      | 0       | 165            | 221          |
| 028 | 手 (Hand)    | 886    | 219    | 37     | 3      | 2      | 1       | 1,148          | 1,465        |
| 029 | 木 (Tree)    | 1,044  | 243    | 40     | 5      | 0      | 1       | 1,333          | 1,676        |

For the **"角" (Horn) radical section** (角部, *kakubu*), the identification of **`Entries`** is problematic in the following instance:

* `kazama_location`: K03012511, `hanzi_entry`: ⿳或或角／𧥑, `definition`: (Unannotated)
* `kazama_location`: K03012520, `hanzi_entry`: 𧥑, `definition`: 音必　篳俗　羗人吹角
* `kazama_location`: K03012530, `hanzi_entry`: 觱, `definition`:俗　クスヌク


As some characters may not display correctly depending on the viewing environment, GlyphWiki images are used in the following explanation.

The **`Headword`** of the first **`Entry`** (K03012511 in the previous example, with `hanzi_entry`: ⿳或或角／𧥑) is composed of the glyphs ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012511.50px.png) and ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012512.50px.png). The **`Headword`** of the second **`Entry`** (K03012520, with `hanzi_entry`: 𧥑) is the glyph ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012520.50px.png). 
These three glyphs appear consecutively in the manuscript. 
A slight space is observed between the first glyph and the second glyph (both part of K0301251's **`Headword`**). A clear space, equivalent to one character width, is found between the second glyph (the end of K03012511's **`Headword`**) and the third glyph (the **`Headword`** of K03012520). If we represent the slight space with '\_' and the one-character space with '\_\_', the sequence appears as:

![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012511.50px.png) \_ ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012512.50px.png) \_\_ ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012520.50px.png)

The calculated number of **`Entries`** can vary depending on whether these three visually consecutive **`Headword`** glyphs are counted as one, two, or three separate **`Entries`**.
In Ikeda et al. (2020), this sequence was counted as two **`Entries`**. This determination was based on the clear space between the second glyph (the last character of the first **`Entry`**'s **`Headword`**) and the third glyph (the **`Headword`** of the second **`Entry`**), and the fact that the first **`Entry`** (K0301251, '⿳或或角／𧥑') is unannotated.

Please refer to the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586893/10) in the National Diet Library Digital Collections.

Incidentally, this section in the Kanchi-in manuscript of the *Myōgishō* bears a strong resemblance to **`Entries`** found in Volume 4 of the *Longkan Shoujian/Shoujing* (龍龕手鏡), under the "角" (horn) radical.

  * `location`: Lb1690102, `hanzi_entry`: ⿳或旦角／⿳或或角, `definition`: 二俗。 (Two popular forms.)
  * `location`: Lb1690104, `hanzi_entry`: ⿳咸咸角／𧥑, `definition`: 二古。 (Two old forms.)
  * `location`: Lb1690106, `hanzi_entry`: 觱, `definition`: 今。音必。羗人吹角以驚与也。今作篳ー篥樂噐也。下又音佛。ー理也。五。 (Current form. Pronunciation *bì*. Horn blown by the Qiang people to startle game. Now written as 篳ー篥 (*bìlì*), a musical instrument. The second character also has the pronunciation *fó* (佛). The 'ー' indicates a principle/type. Five (notes/entries).)

The **`Headword`** for entry `Lb1690104` in the *Longkan Shoujian/Shoujing* is  ![⿳咸咸角](https://glyphwiki.org/glyph/zihai-144813.50px.png) ![𧥑](https://glyphwiki.org/glyph/hdic_hkrm-03012512.50px.png).


For the **"髟" (Hair) radical section** (髟部, *Hyōbu*), the identification of **`Entries`** is problematic in the following instance:

* `kazama_location`: K03036311
* `hanzi_entry`: ⿰镸及／■／⿰镸用／⿰镸少
* `definition` (representing **`Original Glosses`**): 未詳 (Unknown) 「⿰镸⿱右王⿰镸宀圭〈私入〉」
* `remarks` (**`Compiler's Remark`**): Ikeda's note: The string "⿰镸⿱右王⿰镸宀圭〈私入〉" is written in red ink. It is considered an **`Embedded Item`** (埋字, *umoji*). It is not counted as a separate **`Entry`** in this context.

The total number of **`Entries`** changes depending on whether the string "⿰镸⿱右王⿰镸宀圭〈私入〉" (found within the **`Original Glosses`** of the above **`Entry`**) is counted as a separate **`Entry`** itself.
In Ikeda et al. (2020), this string was not included in the **`Entry`** count for the "髟" (Hair) radical section.

Please refer to the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586893/22) in the National Diet Library Digital Collections.

For the **"手" (Hand) radical section** (手部, *Shu-bu*), the identification of **`Entries`** is problematic in the following instance:

* `kazama_location`: K03061721, `hanzi_entry`: ⿰扌水, `definition`: スクフ
* `kazama_location`: K03061722, `hanzi_entry`: 捏, `definition`: 二奴結反　下又音張　舉也　刾也　又勅貞反

Because the **`Original Glosses`** for `K03061722` '捏' begin with the character '二' (two), the **`Entries`** for '⿰扌水' and '捏' were initially treated as a single unit in the database. However, it was later decided to separate them. Nonetheless, questionable points remain regarding the content of the text. This instance can be seen on page 74 of the facsimile edition of the *Hōbodai-in manuscript*.

For the Kanchi-in manuscript, please refer to the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586893/34) in the National Diet Library Digital Collections.

The following are two **`Entries`** where **`Omitted Characters`** in the **`Headword`** were supplied:

* `kazama_location`: K03039530, `hanzi_entry`: 将／［指］
* `kazama_location`: K03047140, `hanzi_entry`: 磬／［控］

The figures for the "手" (Hand) radical section in Ikeda et al. (2020) are corrected as follows. The corrected figures are shown in **bold**. For the "6 or more characters" category, there is one **`Entry`** which consists of 8 characters:

| No. | Radical    | 1-char | 2-char  | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|------------|-------:|--------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 028 | 手 (Hand)  | 886    | **220** | 37     | 3      | 2      | 1       | **1,149** | **1,467** |


For the **"木" (Tree) radical section** (木部, *Mokubu*), the identification of **`Entries`** is problematic in the following instance:

* `kazama_location`: K03102341, `hanzi_entry`: 小／ー（櫃）／膳／ー（櫃）, `definition`: アケノヒツ（HH\_\_\_）

According to the *Nihon Kokugo Daijiten* (*Nikkoku*), there are examples of '小櫃' (*kobitsu*) in the *Wamyō Ruijushō* (*Wamyōshō*), and '膳櫃' (*omono hitsu*) in the *Engi Shiki*. As it is preferable to treat these as separate **`Entries`**, the KRM data has been corrected as follows:

* `kazama_location`: K03102341, `hanzi_entry`: 小／ー（櫃）, `definition`: (Unannotated)
* `kazama_location`: K03102343, `hanzi_entry`: 膳／ー（櫃）, `definition`: アケノヒツ（HH___）

Please refer to the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586893/55) in the National Diet Library Digital Collections.

As a result of this correction, the number of **`Entries`** in the "木" (Tree) radical section now matches the count in Sakai (1967). The corrected figures are shown in **bold**:

| No. | Radical    | 1-char | 2-char  | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|------------|-------:|--------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 029 | 木 (Tree)  | 1,044  | **245** | 40     | **4** | 0      | 1       | **1,334** | 1,676        |


### *Butsuge-matsu* (仏下末 – Lower "Buddha" Fascicle, Last Part)

In the ***Butsuge-matsu*** section, discrepancies in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) are found for the following radical section. The figures presented in the table below are from Ikeda et al. (2020):

| No. | Radical    | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|------------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 039 | 火 (Fire)  | 407    | 91     | 11     | 1      | 1      | 2       | 513            | 648          |

For the **"火" (Fire) radical section** (火部, *Kabu*), Sakai (1967) counts 512 **`Entries`**, resulting in a difference of one **`Entry`** when compared to the count of 513 in Ikeda et al. (2020). There are three instances where the method of counting **`Entries`** is problematic. The discrepancy with Sakai (1967) is thought to arise from differences in calculating the count in one or more of these instances.

* `kazama_location`: K04038132, `hanzi_entry`: 𤊹, `definition`: (Unannotated)
* `kazama_location`: K04038141, `hanzi_entry`: 㶿／⿰火⿳朩冖子／⿰火⿱十子, `definition`: 三俗勃字　音悖　サカリ

After the **`Headword`** '𤊹' in **`Entry`** `K04038132`, there is a slight space. In Ikeda et al. (2020), this was counted as an unannotated **`Entry`**.

The original text for this section can be referred to on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586894/23) in the National Diet Library Digital Collections.




* `kazama_location`: K04041732, `hanzi_entry`: 焭, `definition`: (Unannotated)
* `kazama_location`: K04041741, `hanzi_entry`: ⿱⿱⿰火火冖凡／煢, `definition` (corrected from `defifnition`): 俗通正　音瓊　ヒトリ　𠎽〈古〉　惸〈古〉　ヒトリアルヤモメ（HHL__HHH）　ヤモメ（HHH）

The **`Original Glosses`** for **`Headword`** '⿱⿱⿰火火冖凡／煢' (K04041741) begin with the **`Form Classification Tag`** "俗通正" (*zoku tsū sei*). This might suggest that '焭' (K04041732) and '⿱⿱⿰火火冖凡／煢' were originally intended as a single **`Entry`**. However, the blank space following '焭' (K04041732) is distinct. Considering this, and given that there are instances where a **`Form Classification Tag`** can refer to a preceding **`Entry`**, Ikeda et al. (2020) counted '焭' (K04041732) as a separate, unannotated **`Entry`**.

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586894/24) in the National Diet Library Digital Collections.

* `kazama_location`: K04052540, `hanzi_entry`: ⿱亦火, `definition`: 餘石反　盛也　カヽヤク　⿱赤火　ウレフ　ユク　和ヤク, `remarks` (**`Compiler's Remark`**): The string '⿱赤火' can be interpreted as either an **`Embedded Item`** (*umeji*) or as a note on a **`variant character` (*itaiji*)**.

This case is as explained in the `remarks` column. The string '⿱赤火' is written in a slightly larger size, and if considered an **`Embedded Item`**, it would increase the **`Entry`** count by one. However, since **Masamune's Kanji Index** (正宗漢字索引, *Masamune Kanji Sakuin*) does not list '⿱赤火' as a separate **`Headword`**, it was treated as an annotation concerning a **`variant character` (*itaiji*)** within the **`Original Glosses`**.

The original text for this section can be referred to on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586894/30) in the National Diet Library Digital Collections.

### *Hōjō* (法上 – First “Dharma” Fascicle)


For the **"水" (Water) radical section** (水部, *Sui-bu*), attention should be paid to the following four **`Entries`**, which are associated with the note "此クタリ二水ノトコロニアリ" (These items are in the place of 冫 [*nisui*, the ice radical]):

* `kazama_location`: K05033810, `hanzi_entry`: ■, `definition`: 「此クタリ二水ノトコロニアリ」　フチ(LH)
    *(Compiler's Note for K0503381: An **`Interpolation Mark`** appears immediately before this. This note indicates that these four **`Entries`** on this line should be moved to the "冫" (*nisui*) radical section. See Sakai, *Jijun* [Character Order], p. 33.)*
* `kazama_location`: K05033820, `hanzi_entry`: 减, `definition`: 俗減字　オトス（LLH）　ヘク（LHV）　ヘス　和ケム
* `kazama_location`: K05033830, `hanzi_entry`: 冸, `definition`: ソヽク
* `kazama_location`: K05033840, `hanzi_entry`: ⿰冫⿰关⺉, `definition`: フカシ

These four **`Entries`** have been assigned to the "冫" (*nisui*) radical section for the purpose of calculating **`Entry`** counts.

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586895/20) in the National Diet Library Digital Collections.

Sakai (1967) calculated 1,322 **`Entries`** for the "水" (Water) radical section, while Ikeda et al. (2020) calculated 1,321 **`Entries`**, resulting in a difference of one **`Entry`**. Upon review, the following **`Entry`** is a potential source of this counting discrepancy:

* `kazama_location`: K05001310, `hanzi_entry`: 水, `definition` (representing **`Original Glosses`**): 尸癸反　ミツ（HHV）　カハ　月ー（水）　ツキノサハリ　和スイ（LH）

The string '月ー（水）' (moon-[substituting for] water; referring to menstruation, 月水 *gessui*) is a compound word. If this were treated as an **`Embedded Item` (*umeji*)** and counted as a separate **`Entry`**, the **`Entry`** counts of Sakai (1967) and Ikeda et al. (2020) for this radical section would become identical. However, the subsequent part of the **`Original Glosses`**, "和スイ（LH）" (a *Wa-on* pronunciation for '水'), pertains to the main **`Headword`** '水'. Identifying an embedded **`Entry`** in a way that interrupts the glosses for the main **`Headword`** is problematic. Therefore, this **`Entry`** (for '水') is maintained as a single **`Entry`** as per Ikeda et al. (2020).

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586895/4) in the National Diet Library Digital Collections.



For the **"足" (Foot) radical section** (足部, *Sokubu*), Sakai (1967) counts 494 **`Entries`**, while Ikeda et al. (2020) count 493 **`Entries`**, a difference of one **`Entry`**. The following instance is likely related to this discrepancy:

* `kazama_location`: K05076311, `hanzi_entry`: 踟／ー（蹰）, `definition` (representing **`Original Glosses`**): 上馳(L)　又智音　或躊字　タチヤスラフ　オソシ, `remarks` (**`Compiler's Remark`**): Ikeda's note: "躊字" (the characters '躊' and '字') is written in a large size. It is considered part of the **`Original Glosses`**.

As noted in the `remarks` (the **`Compiler's Remark`**), one might consider counting "躊字" (the characters '躊' and '字' found in the gloss above) as a separate **`Entry`**. However, the character '躊' is itself listed as the **`Headword`** of the very next **`Entry`**:

* `kazama_location`: K05076330, `hanzi_entry`: 躊, `definition` (representing **`Original Glosses`**): 音儔　タチモトホル　タチヤスラフ（LH____）

Therefore, rather than considering '躊' to be a duplicated **`Headword`** (or "躊字" to be an independent embedded **`Entry`**), it is considered more appropriate to interpret "躊字" in the first instance as characters within the **`Original Glosses`** that were simply written in a large size.

The original text for this section can be referred to on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586895/42) in the National Diet Library Digital Collections.


### *Hōchū* (法中 – Middle "Dharma" Fascicle)

In the ***Hōchū*** section, discrepancies in **`Entry`** counts between Sakai (1967) and Ikeda et al. (2020) are found for the following three radical sections. The figures presented in the table below are from Ikeda et al. (2020):

| No. | Radical     | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|-------------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 051 | 石 (Stone)  | 308    | 57     | 5      | 3      | 0      | 3       | 376            | 472          |
| 052 | 玉 (Jade)   | 294    | 76     | 8      | 1      | 3      | 1       | 383            | 496          |
| 057 | 心 (Heart)  | 730    | 161    | 13     | 1      | 2      | 1       | 908            | 1,111        |

For the **"石" (Stone) radical section** (石部, *Sekibu*), Sakai (1967) counts 375 **`Entries`**, while Ikeda et al. (2020) initially counted 376 **`Entries`**, a difference of one **`Entry`**. This discrepancy is likely related to the following instance:

* `kazama_location`: K06001320, `hanzi_entry`: ⿸𠂋帀, `definition` (representing **`Original Glosses`**): 古　△在下

In the **`Original Gloss`** "△在下", the '△' symbol is written in a slightly larger size, which was misidentified as a separate **`Headword`** (contributing to the initial count of 376 by Ikeda et al.).

Additionally, an **`Entry`** where an **`Omitted Character`** in the **`Headword`** was supplied is the following:

* `kazama_location`: K06012741, `hanzi_entry`: 桃／花／［石］, `definition`: 此間音タウクヱシヤク（LHHHLLL）

The **`Entry`** count and total headword character count for the "石" (Stone) radical section are corrected as follows:

| No. | Radical     | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|-------------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 051 | 石 (Stone)  | 307    | 56     | 6      | 3      | 0      | 4       | 375            | 472          |



For the **"玉" (Jade) radical section** (玉部, *Gyokubu*), Sakai (1967) counts 384 **`Entries`**, while Ikeda et al. (2020) count 383 **`Entries`**, a difference of one **`Entry`**. The following **`Entry`** is likely related to this discrepancy:

* `kazama_location`: K06013430, `hanzi_entry`: 玊, `definition` (representing **`Original Glosses`**): 音夙（T）「シク」　又栗（T）「リク」　又欣救反　琢「ミカク」玉を工也, `remarks` (**`Compiler's Remark`**): Ikeda's note: '栗' is an error for '粟'. The red ink mark on '玉' might be an `Morphosyntactic Glosses` (*wokototen*, ヲコト点) for 'を' (*wo*). '工也' is written in small characters in the manuscript, but it has been transcribed in large characters here because the *Guangyun* has the semantic gloss '琢玉工' (jade-carving artisan).

There is a possibility of treating '琢玉' (jade carving), which appears in the gloss as '琢「ミカク」玉を', as an **`Embedded Item` (*umeji*)**. However, since '琢' is listed as a separate **`Headword`** elsewhere, it is likely appropriate to consider '琢玉' as part of the **`Original Glosses`** for '玊'.

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586896/10) in the National Diet Library Digital Collections.

For the **"心" (Heart) radical section** (心部, *Shinbu*), Sakai (1967) counts 909 **`Entries`**, while Ikeda et al. (2020) count 908 **`Entries`**, a difference of one **`Entry`**. The following **`Entry`** is likely related to this discrepancy:

* `kazama_location`: K06084521, `hanzi_entry`: 㥶, `definition` (representing **`Original Glosses`**): 「注」⿺⻎偘古　「注」⿱保言𠐨〈籀〉, `remarks` (**`Compiler's Remark`**): Ikeda's note: Although '⿺⻎偘古' and '⿱保言𠐨' are written in large characters, each is accompanied by the character '注' (annotation), indicating they are part of the **`Original Glosses`**.

Since '⿺⻎偘古' and '⿱保言𠐨' are written in large characters, there is a possibility of counting them as **`Headwords`**. However, they are not characters that would typically be assigned to the "心" (Heart) radical section, and furthermore, they are explicitly marked with '注' (annotation). Therefore, it is unlikely that Ikeda et al. (2020) miscounted by including these as separate **`Entries`** (implying the discrepancy may originate from Sakai's count or another unclarified instance).

The original text for this section can be referred to on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586896/46) in the National Diet Library Digital Collections.

For the **"糸" (Silk) radical section** (糸部, *Shibu*), there is no difference in the number of **`Entries`** between Sakai (1967) and Ikeda et al. (2020). However, a correction is made to the character count of the **`Headword`** in the following **`Entry`**:

* `kazama_location`: K06121611, `hanzi_entry`: 罘／䋄, `definition`: ノアミ

This corrects a previous misidentification where the **`Headword`** was mistakenly interpreted as '四／不／䋄'. As a result of this correction to the headword's character composition, the breakdown of **`Entry`** counts by headword length and the total headword character count for this section are as follows (the total number of **`Entries`**, 736, remains unchanged):

| No. | Radical    | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|------------|-------:|-------:|-------:|-------:|-------:|--------:|---------------:|-------------:|
| 059 | 糸 (Silk)  | 631    | 94     | 8      | 3      | 0      | 0       | 736            | 855          |


### *Hōge* (法下 – Lower "Dharma" Fascicle)

In the *Hōge*, discrepancies in Entry counts between Sakai (1967) and Ikeda et al. (2020) are found for the following four radical sections. The figures presented in the table below are from Ikeda et al. (2020):

| No. | Radical    | 1-char | 2-char | 3-char | 4-char | 5-char | 6+ char | No. of Entries | No. of Chars |
|-----|---|------:|------:|-----:|----:|----:|------:|------:|---:|
| 066 | 勹 | 29   | 4   | 0   | 0  | 0  | 0  | 33   | 37   |
| 068 | 雨 | 177  | 43  | 6   | 1  | 1  | 0  | 228  | 290  |
| 075 | 疒 | 234  | 138  | 23  | 1  | 1  | 2  | 399  | 603  |
| 080 | 寸 | 18   | 21   | 0   | 0  | 0  | 0  | 39   | 60   |

For the **"勹" (Wrap) radical section** (勹部, *Hōbu*), the following instance is problematic:

* `kazama_location`: K07057620, `hanzi_entry`: 匑, `definition` (representing **`Original Glosses`**): 音⿺麦羽　又穹　ー𠤂　謹敬皃, `remarks` (**`Compiler's Remark`**): Ikeda's note: Although 'ー𠤂' is written in a slightly larger size, it is considered part of the **`Original Glosses`**.
* `kazama_location`: K07057640, `hanzi_entry`: 𠤂, `definition` (representing **`Original Glosses`**): 音躬

In the **`Original Glosses`** for '匑' (`K07057620`), the 'ー' in 'ー𠤂' is a **`Substitution Mark`**. Thus, 'ー𠤂' represents '匑𠤂', and its semantic meaning is given as '謹敬皃' (*jǐnjìngmào*; "appearance of being reverent and respectful"). **Masamune's Kanji Index** lists 'ー（匑）𠤂' as an **`Entry`**.

The character '匑' appears in the *Guangyun* with the gloss "謹敬之皃。又音穹。" (Appearance of being reverent and respectful. Also pronounced *qióng* [穹]) under the Level tone (平声), *Dong* (東) rhyme, *xiaoyun* '弓' (*gōng*): *jūróng qiè* (居戎切); and also as "謹敬之皃" (Appearance of being reverent and respectful) under the Level tone, *Dong* rhyme, *xiaoyun* '穹' (*qióng*): *qùgōng qiè* (去宫切) [Departing tone reading for 穹]. The **`Phonetic Gloss`** "音⿺麦羽" found in the *Myōgishō* is questionable. However, the accompanying "又穹" (also *qióng*) can be seen as indicating a pronunciation from the Level tone, *Dong* rhyme. Furthermore, '匑' is found in the *Banshō Meigi* (万象名義) with "丘陸反。謹敬皃" and in the Song edition of the *Yupian* (宋本玉篇) with "丘六切。又丘弓切。匑𠤊謹敬皃". Since '丘陸反' (*qiūlù fǎn*) and '丘六切' (*qiūliù qiè*) correspond to the Entering tone (入声), *Wu* (屋) rhyme, and *Xi* (溪) initial, they are likely scribal errors for '麴󠄀' (yeast/leaven), which has the *fanqie* spelling "驅匊切" (*qūdī qiè*) in the *Guangyun*.

The next **`Entry`**, `K07057640` for '𠤂', has the **`Phonetic Gloss`** "音躬" (pronounced as '躬'). While '𠤂' is not found in the *Guangyun*, the character '躬' (*gōng*) cited in the gloss is listed in the *Guangyun* with the *fanqie* "居戎切" (*jūróng qiè*; Level tone, *Dong* rhyme, *xiaoyun* '弓'), making it homophonous with '匑'. Although '𠤂' is not found in the *Banshō Meigi*, the Song edition of the *Yupian*, or the *Guangyun*, it does appear in the *Jiyun* (集韻) under the entry for "𠤂匔" with the gloss "謹敬也或作匔" (Reverent and respectful; also written as 匔) under the Level tone, *Dong* rhyme, *xiaoyun* '窮' (*qióng*): *qúgōng qiè* (渠弓切).

Based on the above, it is difficult to consider 'ー（匑）𠤂' in the Kanchi-in manuscript as a compound word; it is more likely a co-listing of **`variant characters` (*itaiji*)**.

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586897/32) in the National Diet Library Digital Collections.


For the **"雨" (Rain) radical section** (雨部, *Ubu*), Sakai (1967) counts 226 **`Entries`**, while Ikeda et al. (2020) count 228 **`Entries`**, a difference of two **`Entries`**. The following example illustrates an instance where the identification of **`Entries`** is problematic:

* `kazama_location`: K07067330, `hanzi_entry`: 霆, `definition` (representing **`Original Glosses`**): 定（R）亭（L）挺（H）三音　霹靂　イナヒカリ（\_\_LVHL）　イカツチ（H\_HV\_）, `remarks` (**`Compiler's Remark`**): Ikeda's note: '霹靂' is a **`Semantic Gloss in Chinese`**.

The characters '霹靂' (*Hekireki*; thunderclap) are written in a slightly larger size. Furthermore, while this **`Entry`** for '霆' occupies the space of two cells (or blocks; 2格, *nikaku*), the segment '霹靂　イナヒカリ（\_\_LVHL）' is written in the second cell, suggesting it could potentially have been a separate **`Headword`** (and thus a distinct **`Entry`**). However, since '霹靂' is listed as a **`Headword`** elsewhere in the *Myōgishō*, and considering its content in this instance, it was judged appropriate to treat it as a phrase within the **`Original Glosses`** for '霆'.

The original text for this section can be referred to on the left side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586897/37) in the National Diet Library Digital Collections.

Another problematic instance is the following example. Related preceding and succeeding **`Entries`** are also shown for context:

  * `kazama_location`: K07068530, `hanzi_entry`: 雹, `definition`: 歩角反　アラレ（HHH）　和ハク　ハウ
  * `kazama_location`: K07068541, `hanzi_entry`: 𩅟, `definition`: 或
  * `kazama_location`: K07068542, `hanzi_entry`: 雹, `definition`: (Unannotated)
  * `kazama_location`: K07068611, `hanzi_entry`: 𩂁／䨔／⿱𩅒田, `definition`: 俗

The third **`Entry`**, `K07068542` with **`Headword`** '雹', appears at the end of its line and might seem continuous with the next **`Entry`** on the following line, `K07068611` with **`Headword`** '𩂁／䨔／⿱𩅒田'. There is a slight blank space below '雹' (`K07068542`). Furthermore, although the **`Headwords`** of the first **`Entry`** (`K07068530`) and the third **`Entry`** (`K07068542`) are both transcribed as '雹', in the original manuscript, the lower part of the latter ('雹' in `K07068542`) is written in a form resembling '⿱冖巳'. It is thought that a blank space was intentionally left below it to accommodate some form of **`Note on Character Form`**.

However, the **`Headword`** of the last listed **`Entry`**, '𩂁／䨔／⿱𩅒田' (`K07068611`), consists of **`variant characters` (*itaiji*)** of '雹', as can be seen in the following examples from Volume 2 of the *Longkan Shoujian/Shoujing* (龍龕手鑑), under the "雨" (Rain) radical. Therefore, it is also conceivable that '雹' (`K07068542`) and '𩂁／䨔／⿱𩅒田' (`K07068611`) originally constituted a single **`Entry`**.

  * `location`: Ls52b0802, `hanzi_entry`: 䨔𩂁𩅒, `definition`: 三俗。 (Three popular forms.)
  * `location`: Ls52b0805, `hanzi_entry`: 𩄉𩅟𩇌, `definition`: 三古。 (Three old forms.)
  * `location`: Ls52b0808, `hanzi_entry`: 雹, `definition`: 正。蒲各反。雨冰也。七。 (Standard form. *Fanqie*: 蒲各反 (*pú gè fǎn*). Means 'rain and ice' (hail). Seven (notes/entries).)

A comparison of the **`Headword`** characters from the Kanchi-in manuscript and the *Longkan Shoujian/Shoujing* is shown below. Only **`Notes on Character Form`** (字体注, *jitaichū*) are indicated; **`Phonetic Glosses`** and **`Japanese Native Readings` (*wakun*)** are omitted. A slash '/' indicates a conceptual line break (for aligning the Kanchi-in sequence). Arabic numerals represent the order of appearance in the Kanchi-in manuscript; 'x' marks characters from the *Longkan Shoujian/Shoujing* list not found in the Kanchi-in manuscript's corresponding sequence, and parentheses () are used for characters that are similar but not identical.

(Kanchi-in Manuscript)
1![雹](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068530.50px.png)……
2![𩅟](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068541.50px.png)或
3![雹](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068542.50px.png) 　/
4![𩂁](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068611.50px.png)
5![䨔](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068612.50px.png)
6![⿱𩅒田](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068613.50px.png)俗

(*Longkan Shoujian/Shoujing*)
5![䨔](https://glyphwiki.org/glyph/u4a14.50px.png)
4![𩂁](https://glyphwiki.org/glyph/u29081.50px.png)
(6)![𩅒](https://glyphwiki.org/glyph/u29152.50px.png)三俗
x![𩄉](https://glyphwiki.org/glyph/u29109.50px.png)
2![𩅟](https://glyphwiki.org/glyph/u2915f.50px.png)
x![𩇌](https://glyphwiki.org/glyph/u291cc.50px.png)三古
1![雹](https://glyphwiki.org/glyph/u96f9.50px.png)正　…

The Kanchi-in manuscript sequence involves 6 character forms (or groups), while the *Longkan Shoujian/Shoujing* list shows 7 relevant character forms here. Their order of description does not directly match.
The characters marked with 'x', namely  ![𩄉](https://glyphwiki.org/glyph/u29109.50px.png) and ![𩇌](https://glyphwiki.org/glyph/u291cc.50px.png), from the *Longkan Shoujian/Shoujing* list are not found in the corresponding Kanchi-in manuscript sequence.
Character 3 , ![雹](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068542.50px.png), and character 6, ![⿱𩅒田](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068613.50px.png), from the Kanchi-in manuscript do not have direct identical counterparts in this *Longkan Shoujian/Shoujing* list.
However, character 6 from the Kanchi-in manuscript, ![⿱𩅒田](https://glyphwiki.org/glyph/hdic-tanki10_hkrm-07068613.50px.png), is similar to character (6), ![𩅒](https://glyphwiki.org/glyph/u29152.50px.png), from the *Longkan Shoujian/Shoujing*.

It is presumed that the exemplar of a dictionary like the *Longkan Shoujian/Shoujing* that was consulted by the compiler(s) of the revised Kanchi-in manuscript of the *Ruiju Myōgishō* may have had questionable points or textual corruptions.

The original text for this section in the Kanchi-in manuscript can be referred to on the right side of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586897/38) in the National Diet Library Digital Collections.

The original text for the relevant section in the *Longkan Shoujian/Shoujing* can be referred to on the right side of the [corresponding page](https://www.google.com/search?q=https://dl.ndl.go.jp/info:ndljp/pid/1126592/132) in the National Diet Library Digital Collections.



For the **"疒" (Sickness) radical section** (疒部, *Daibu*), Sakai (1967) counts 400 **`Entries`**, while Ikeda et al. (2020) count 399 **`Entries`**, a difference of one **`Entry`**. The identification of **`Entries`** is problematic in the following instance:

* `kazama_location`: K07125841, `hanzi_entry`: 𤻿／⿸疒既, `definition` (representing **`Original Glosses`**): 俗通　古界反　⿱⿰白旡月　正䐴　𦝫, `remarks` (**`Compiler's Remark`**): Ikeda's note: The string '⿱⿰白旡月' is an example of characters from the **`Original Glosses`** being written in a large size.

Although the string '⿱⿰白旡月' is written in a large size and might appear to be a **`Headword`**, it does not contain the '疒' radical component. Therefore, it is not appropriate to classify it as a **`Headword`** belonging to the "疒" (Sickness) radical section.

The original text for this section in the Kanchi-in manuscript can be referred to on the upper right of the [corresponding page](https://dl.ndl.go.jp/info:ndljp/pid/2586897/67) in the National Diet Library Digital Collections.

