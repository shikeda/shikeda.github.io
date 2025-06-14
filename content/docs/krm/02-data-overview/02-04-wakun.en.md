---
title: "krm_wakun"
weight: 14
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# krm_wakun

## Overview and file formats

This data file is derived by extracting **`Japanese Native Readings (*wakun*)`** from the `KRM.tsv` file (an older version of `krm_main`) of the *Myōgishō* database, organizing variant forms of these **`wakun`**, and adjusting their correspondence with **`variant characters (*itaiji*)`**.

Collation notes and source investigations related to **`wakun`** are documented in the `krm_notes` file (which contains data for **`Compiler's Remarks`**), so they are omitted here.

In some **`wakun`** entries, different phonetic readings are presented side-by-side as annotations.
For example, the **`wakun`** "マサル" (masaru) is assigned to the **`Hanzi (Chinese character)`** "倍" (bai), but "ス" (su) is written in small katakana to the right of "ル" (ru) as an additional note. This indicates that the **`wakun`** "マス" (masu) is also noted in addition to "マサル" (masaru).

Since information from the JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) will be added to the **`wakun`** data, it is necessary to accommodate cases where variant forms of **`wakun`** are presented together.

The correspondence with **`variant characters (*itaiji*)`** has been adjusted because **`Headwords`** in the *Myōgishō* sometimes indicate such variants.
For example, the **`wakun`** "ヤツカレ" (yatsukare) appears in the **`Definition (Original Glosses)`** for the **`Headword(s)`** "㒒／僕". The **`wakun`** "ヤツカレ" is a **`Japanese Native Reading`** for "僕" (boku) and simultaneously for "㒒". The relationship between standard and variant forms such as "爲" and "為", or "來" and "来" is handled similarly.

The JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) has a "Notation" (表記) field that includes **`Hanzi (Chinese character)`** notations from the *Myōgishō*; this adjustment is a measure to ensure correspondence with that resource.

To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_wakun.tsv` and `krm_wakun.json`.


## Column name comparison

The comparison of the new and old column names is as follows:

| New Column Name (v1.2.0) | Old Column Name (v1.1.97) |
|-------------------------|---------------|
| wakun_id                | KRID_wakun_no |
| definition_seq_id       | KRID_no       |
| kazama_location   | KR2ID         |
| hanzi_entry             | Entry         |
| wakun_elements          | Def           |
| wakun_form              | Word_form     |
| wakun_standard_hanzi    | Wakun_Hanzi   |
| wakun_variant_in_hanzi  | Wakun_variant |
| variant_hanzi_for_wakun | Hanzi_variant |
| japan_knowledge_id      | JK_URL        |
| -                       | Remarks       |

`Remarks` have been omitted as this type of information is now consolidated in the `krm_notes` file (data for **`Compiler's Remarks`**).


## Description of each column


Next, the content of the column names will be explained.

| New Column Name (v1.2.0)   | English Explanation (Final Revised)                                                                                                                                                                                                                                                           |
| :------------------------- | :-------------------------------------------------- |
| wakun_id                   | An ID for each **`Japanese Native Reading (*wakun*)`**. This is derived from `definition_seq_id` by extracting only those elements where the type (from `definition_type_name` in `krm_notes`) is **`Japanese Native Reading (*wakun*)`**. Suffixes 'b', 'c', 'd' are appended for variant forms. |
| definition_seq_id        | An identifier for each component of the **`Definition (Original Glosses)`** or for the **`Headword`** itself within an **`Entry`**. It is formed by appending a sequential suffix (e.g., "_00" for the **`Headword`** or overall **`Entry`** note, "_01", "_02" for subsequent elements of the **`Definition (Original Glosses)`** in order of appearance) to the 5-digit numeric part of the `entry_id`. (This ID links to records in `krm_notes`). |
| kazama_location    | ID including location information (Kazama edition: K, Book/volume, page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple **`Entries`** in a column. "Book(volume)" represents the volume number, "page(xxx)" the page number, "line(y)" the line number, and "column(zz)" the column number. |
| hanzi_entry              | The collated **`Headword`** (using **`Hanzi (Chinese characters)`**) to which this **`Japanese Native Reading (*wakun*)`** pertains. Principally Kangxi Dictionary forms, though Unicode-representable new forms (common-use, popular variants) may be retained.                                |
| wakun_elements           | Extracted elements of **`Japanese Native Readings (*wakun*)`** from the full **`Definition (Original Glosses)`**. Each record typically corresponds to one such element.                                                                                                            |
| wakun_form               | The lexical form of the **`Japanese Native Reading (*wakun*)`**. Inflected words are generally given in their dictionary (citation) form, excluding grammatical particles. The particles 'no' and 'to' from *Monzen* (文選) style readings are omitted.                                     |
| wakun_standard_hanzi     | Notation of the **`Japanese Native Reading (*wakun*)`** using standard **`Hanzi (Chinese characters)`**.        |
| wakun_variant_in_hanzi   | Notation of a variant form of the **`Japanese Native Reading (*wakun*)`** using standard **`Hanzi (Chinese characters)`**.    |
| variant_hanzi_for_wakun  | Notation of the **`Japanese Native Reading (*wakun*)`** using **`variant characters (*itaiji*)`** of **`Hanzi (Chinese characters)`**.     |
| japan_knowledge_id       | If this **`Japanese Native Reading (*wakun*)`** exists as a headword in the JapanKnowledge version of the *Nihon Kokugo Daijiten* (2nd Ed.), the alphanumeric part of its URL (from "20020" to the end) is recorded here. If it does not exist as a headword, "null" is entered.           |

