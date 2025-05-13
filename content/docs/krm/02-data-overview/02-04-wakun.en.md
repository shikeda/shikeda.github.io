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

This data is derived by extracting wakun from the `KRM.tsv` file of the *Myōgishō* database, organizing variant forms of the wakun, and adjusting their correspondence with variant characters (itai-ji).

Collation and textual research related to wakun are documented in `krm_notes`, so they are omitted here.

In wakun, different readings may be written alongside the main reading as annotations.

For example, the wakun "マサル" (masaru) is assigned to the character "倍" (bai), but "su" is written in small katakana to the right of "ル" (ru) as an annotation. This indicates that the wakun "マス" (masu) is annotated in addition to "マサル" (masaru).

Since information from the JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) will be added to the wakun, it is necessary to accommodate cases where variant forms of wakun are written together.

The handling of variant characters involves cases where variant forms are indicated for the head character, and this data has been adjusted to account for them.

For example, the wakun "yatsukare" appears in the definition for the head characters "㒒/僕". The wakun "yatsukare" is a wakun for "僕" (boku) and is simultaneously a wakun for "㒒". The relationship between standard and variant forms such as "爲" and "為", or "來" and "来" is similar.

The JapanKnowledge version of the *Nihon Kokugo Daijiten* (Second Edition) has a "Notation" field that includes the kanji notations from the *Myōgishō*, so this adjustment is a measure to ensure correspondence with it.

To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_wakun.tsv` and `krm_wakun.json`."

The comparison of the new and old column names is as follows:

| New Column Name (v1.2.0) | Old Column Name (v1.1.97) |
|-------------------------|---------------|
| wakun_id                | KRID_wakun_no |
| definition_seq_id       | KRID_no       |
| kazama_entry_location   | KR2ID         |
| hanzi_entry             | Entry         |
| wakun_elements          | Def           |
| wakun_form              | Word_form     |
| wakun_standard_hanzi    | Wakun_Hanzi   |
| wakun_variant_in_hanzi  | Wakun_variant |
| variant_hanzi_for_wakun | Hanzi_variant |
| japan_knowledge_id      | JK_URL        |
| -           | Remarks       |


`Remarks` have been omitted and will be summarized in the following `krm_notes` file.

Next, the content of the column names will be explained.

| New Column Name (v1.2.0)      | Explanation        |
|-------------------------|------------------|
| wakun_id                | Wakun ID, extracted from kr_definition_sequence_id, containing only entries where the type of order is Japanese reading (wakun). Variant forms are appended with 'b', 'c', 'd'.  |
| definition_seq_id       | An identifier for each definition component, typically formed by appending a sequential suffix (e.g., _00, _01, _02) to the corresponding entry_id. The _00 suffix often denotes the main heading or an overall entry note, while _01, _02, etc., identify subsequent, ordered definition elements.   |
| kazama_entry_location   | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. |
| hanzi_entry             | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.         |
| wakun_elements          | Extracted Japanese reading (wakun) components from the full definition, one component per entry.  |
| wakun_form        | Form of the Japanese reading (wakun). Inflected words are in dictionary form, excluding particles. The particles 'no' and 'to' from 文選 readings are omitted. |
| wakun_standard_hanzi    | Standard wakun notation using standard kanji.      |
| wakun_variant_in_hanzi  | Variant form of wakun notation using standard Hanzi characters.      |
| variant_hanzi_for_wakun | Wakun notation using variant Hanzi characters (itai-ji).    |
| japan_knowledge_id      | The alphanumeric part of the JapanKnowledge URL for the corresponding entry in the Nihon Kokugo Daijiten 2nd Ed., starting from "20020" to the end, is recorded here if the wakun exists as a headword. If the wakun does not exist as a headword in the JapanKnowledge edition, null is entered.    |

