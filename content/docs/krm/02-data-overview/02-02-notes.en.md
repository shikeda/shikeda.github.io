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

## Overview and file formats

A new file, `krm_notes.tsv`, has been created, containing detailed annotation information added to the `KRM_definitions.tsv` file.

This is available in both TSV and JSON formats. To explicitly indicate that these are the filenames after the specification change in March 2025, lowercase "krm" was used instead of uppercase "KRM," resulting in the names `krm_notes.tsv` and `krm_notes.json`.

## Column name comparison

This section compares the column names in the new `krm_notes.tsv` (v1.2.6) with those in the previous files it replaces or incorporates data from.

### Comparison with KRM_definitions.tsv (v1.1.55)

The following table shows the correspondence between columns primarily related to definition details derived from the previous definitions file:

| New Column Name (krm_notes v1.2.6) | Old Column Name (KRM_definitions v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                       |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks                  | Remarks                    |

### Incorporation of KRM.tsv (v1.1.347) content

The new `krm_notes.tsv` also incorporates information previously stored in `KRM.tsv`. The corresponding column names are compared below:

| New Column Name (krm_notes v1.2.6) | Old Column Name (KRM v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| original_entry           | Entry_original             |


## Data Structure: ER Diagram and JSON Implementation



The JSON representation of `krm_notes` utilizes a nested format, as detailed below.

![ER_notes diagram](/images/krm_notes_er.drawio.png)


In the **ER diagram**, the `krm_notes` table is shown as a child table linked to `krm_main` (as detailed in the [krm_main section](./02-01-main)) by `entry_id`. However, in the **actual JSON data**, the equivalent of the `krm_notes` table is not flat: instead, it is implemented as a **nested array of objects** under the key `"definitions"` within each top-level record (referred to as a `krm_main` conceptual record).

Each object inside the `definitions` array corresponds to a definition note and contains the following fields:

* `definition_seq_id`
* `definition_elements`
* `definition_type_code`
* `definition_type_name`
* `remarks`

This structure can be conceptually represented in the ER diagram as follows:

* The **`krm_main` table** has a **one-to-many relationship** with a conceptual `definitions` or `notes` table.
* In the JSON representation, the **definitions are embedded as an array of objects** within each `krm_main` object, rather than being stored in a separate flat table.

### Example JSON:

```
{
  "entry_id": "F00001",
  ...
  "definitions": [
    {
      "definition_seq_id": "F00001_01",
      "definition_elements": "音仁（LV）「ニン」",
      "definition_type_code": 215,
      "definition_type_name": "音注声点有_類音注等",
      "remarks": "広韻「如鄰切」..."
    },
    ...
  ]
}
```
## Description of each column

Next, the content of the column names will be explained.


| New Column Name (v1.2.6) | English Explanation              |
|--------------------------|---------------------------|
| entry_id                 |A heading item ID formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.  |
| definition_seq_id        | An identifier for each definition component, typically formed by appending a sequential suffix (e.g., _00, _01, _02) to the corresponding entry_id. The _00 suffix often denotes the main heading or an overall entry note, while _01, _02, etc., identify subsequent, ordered definition elements.         |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.|
| tenri_location           |An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.  |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.   |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.          |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.         |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used.  |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per definition record (i.e., per object in the definitions array in JSON).  |
| definition_type_code     | 3-digit numeric code representing the definition type.   |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, Japanese readings (*wakun*), and others.  |
| remarks                  | Editor's notes providing additional context or information.      |

