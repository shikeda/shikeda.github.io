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



## `Embedded Characters` (*umoji*) and the *Bunchūshiki* (Divided-Annotation Style)

**`Embedded Characters`** (*umoji*) refer to **`Entry`**-like segments that are incorporated within another main **`Entry`**.

**Example:**
* `kazama_location`: K0201261
* `hanzi_entry`: 娜
* `definition` (representing **`Original Glosses`**): 乃可（H）反　マヽハヽ　タヲヤカナリ　婀ー　ヨキカホ　ナマメク
* `remarks` (**`Compiler's Remark`**): Could the segment "婀ー　ヨキカホ　ナマメク" be an embedded item/entry?

These embedded segments can either be considered equivalent to a separate **`Entry`** or interpreted as an explanation of a compound word provided within the **`Original Glosses`** of the main **`Entry`**.

The method of embedding glosses for a multi-character compound within the **`Original Glosses`** of a single (often the first) character of that compound is termed the "**`Divided-Annotation Style`**" (分註式, *Bunchūshiki*). In contrast, the method of presenting such information as an independent **`Entry`** following the main single-character **`Entry`** is called the "**`Independent-Entry Style`**" (独立式, *Dokuritsushiki*) (Okada Yoshio, *Ruiju Myōgishō no Kenkyū* [A Study of the *Ruiju Myōgishō*], p. 313 ff.).

While these annotation styles are important indicators for studying the relationships between different manuscripts and the sequential ordering of **`Entries`**, they will not be discussed further in this section.

