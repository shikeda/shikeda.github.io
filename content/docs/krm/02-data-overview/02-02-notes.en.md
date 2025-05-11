---
title: "krm_notes"
weight: 12
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# krm_notes

A new file, `krm_notes.tsv`, has been created, containing detailed annotation information added to the `KRM_def.tsv` file.

This is available in both TSV and JSON formats. To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_notes.tsv` and `krm_notes.json`.

Considering `krm_notes.tsv` as the new file and `KRM_definitions.tsv` as the old file, the comparison of their column names is as follows:

| New Column Name (v1.2.6) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |

Furthermore, we decided to incorporate the contents of `KRM.tsv` into `krm_notes`. Comparing the column names of both will result in the following.

| New Column Name (v1.2.6) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id        | KRID_n                    |
| tenri_location    | KR_Tenri_p                      |
| volume_name            | KR_vol_name                      |
| radical_name      | KR_radical                        |
| volume_radical_index     | KR_vol_radical                |
| original_entry     | Entry_original                   |


As mentioned earlier, the internal structure of `krm_notes` has the following nested format.


![ER_notes diagram](/images/krm_notes_er.drawio.png)

Next, the content of the column names will be explained.


| New Column Name (v1.2.6) | English Explanation              |
|--------------------------|---------------------------|
| entry_id                 |A heading item ID formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.  |
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.|
| tenri_location           |An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.   |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.          |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.         |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used.  |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.           |
| definition_type_code     | 3-digit numeric code representing the definition type.   |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.  |
| remarks                  | Editor's notes providing additional context or information.      |

