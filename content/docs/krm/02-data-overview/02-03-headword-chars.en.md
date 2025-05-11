---
title: "krm_headword_chars"
weight: 13
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# krm_headword_chars



Headwords in the *Myōgishō* can consist of single characters or multiple characters (multi-character compounds). The `krm_headword_chars` data file lists all headwords from the *Myōgishō*, ordered according to the sequence of items in the *Myōgishō* and by the order of appearance of characters within each item.

In the *Myōgishō* database, the primary data file `krm_main`, as well as the annotation data `krm_notes` and the *wakun* data `krm_wakun`, are all structured on an item-by-item basis. Consequently, for headwords composed of multiple characters, any character subsequent to the first cannot be directly referenced from these particular data files.


To search for headwords from the *Myōgishō* character by character, display their original manuscript images, or perform analyses at the individual character level, a complete list of all headword characters, including those from the second character onwards in multi-character compounds, is necessary.

The `krm_headword_chars` data file was created for this purpose. This data is provided in TSV and JSON formats. Each row (or entry) corresponds to a single headword character and includes information such as: the sequential ID of the headword (single or multi-character) in the *Myōgishō* to which the character belongs (`hanzi_id`), the ID of the *Myōgishō* item to which this character's headword belongs (`entry_id`), the order of the character within its headword entry (`character_order`), the character itself (`constituent_char`), the file name of the individually cropped image for the character (`img_file_name`), and location information for that character in both the Kazama and Tenri editions (`kazama_location_id`, `tenri_location_id`). This enables information access at the individual character level while allowing linkage with item-based data files such as `krm_main`.

The column names and their descriptions for `krm_headword_chars` are as follows:


| Column Name    | English Explanation     |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| hanzi_id           | A sequential ID assigned to each headword (single or multi-character) in the order of its appearance in the Myōgishō. It consists of a 5-digit numeric ID starting with 'S'.              |
| entry_id           | A heading item ID (from krm_main) to which this character's headword belongs, formed by a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.          |
| constituent_char   | The constituent character itself. Abbreviation marks (ー) and iteration marks (〻) are converted to the actual characters they represent. Collated characters are, in principle, Kangxi Dictionary forms; the handling of Unicode new character forms (common-use forms, popular variants) is specified separately. For detailed collation notes, refer to krm_notes.               |
| character_order    | Indicates the numerical order of appearance of the character within its headword entry.       |
| kazama_location_id | An ID indicating the location of this character in the Kazama Edition: K + Volume (2 digits) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).            |
| tenri_location_id  | An ID indicating the location of this character in the Tenri Edition: T + Volume (a/b/c) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).          |
| img_file_name      | File name of the headword character image (including the .jpg extension). The main part of the file name consists of a 7-digit number for images from Volume 1 to Volume 9, and an 8-digit number for images from Volume 10. For 7-digit numbers, the first digit indicates the volume number; for 8-digit numbers, the first two digits indicate Volume 10. The last 6 digits are based on the order of appearance, assigned according to a unique internal rule. Detailed documentation for this naming convention is not available as the work was completed over two decades ago. Null if no image is available. |