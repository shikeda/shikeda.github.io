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

## Overview and file formats

**`Headwords`** in the *Myōgishō* can consist of single **Chinese characters** or multiple **Chinese characters** (multi-character compounds). The `krm_headword_chars` data file provides a list of all **constituent characters that form these `Headwords`** from the *Myōgishō*. The characters are ordered according to the sequence of **`Entries`** (items) in the *Myōgishō* and then by the order of appearance of characters within each **`Headword`**.

In the *Myōgishō* database, the primary data file `krm_main`, the `krm_notes` file (containing data for **`Compiler's Remarks`**), and the `krm_wakun` file (**`Japanese Native Reading (*wakun*)`** data) are all structured on an **`Entry`**-by-**`Entry`** basis. Consequently, for **`Headwords`** composed of multiple **Chinese characters**, any character subsequent to the first cannot be directly referenced from these particular data files.

To search for **`Headwords`** from the *Myōgishō* character by character, display their original manuscript images, or perform analyses at the individual **Chinese character** level, a complete list of all constituent characters of the **`Headwords`**, including those from the second character onwards in multi-character compounds, is necessary.

The `krm_headword_chars` data file was created for this purpose. This data is provided in TSV and JSON formats. Each row (or record) corresponds to a single constituent character of a **`Headword`** and includes information such as: the sequential ID of the **`Headword`** (single or multi-character) in the *Myōgishō* to which the constituent character belongs (`hanzi_id`); the ID of the *Myōgishō* **`Entry`** to which this character's **`Headword`** belongs (`entry_id`); the order of the character within its **`Headword`** (`character_order`); the character itself (`constituent_char`); the file name of the individually cropped image for the character (`img_file_name`); and location information for that character in both the Kazama and Tenri editions (`kazama_location_id`, `tenri_location_id`). This enables information access at the individual character level while allowing linkage with **`Entry`**-based data files such as `krm_main`.

## Description of each column

The column names and their descriptions for `krm_headword_chars` are as follows:

| Column Name          | English Explanation      |
| :------------------- | :------------------------------------------------------ |
| hanzi_id             | A sequential ID assigned to each **`Headword`** (whether single or multi-character) in the order of its appearance in the *Myōgishō*. It consists of a 5-digit numeric ID starting with 'S'.   |
| entry_id             | The ID of the **`Entry`** (from `krm_main`) to which the **`Headword`** (containing this constituent character) belongs. This ID is a 5-digit numeric value starting with 'F'. For some newly added **`Entries`**, a 'b' suffix is appended.      |
| constituent_char     | The constituent **Chinese character** itself. Abbreviation marks (ー) and iteration marks (〻) are converted to the actual characters they represent. Collated **Chinese characters** are, in principle, Kangxi Dictionary forms; the handling of Unicode new character forms (common-use forms, popular variants) is specified separately. For detailed collation notes, refer to `krm_notes` (for **`Compiler's Remarks`** on collation).       |
| character_order      | Indicates the numerical order of appearance of the character within its **`Headword`**.     |
| kazama_location_id   | An ID indicating the location of this constituent character in the Kazama Edition: K + Volume (2 digits) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).  |
| tenri_location_id    | An ID indicating the location of this constituent character in the Tenri Edition: T + Volume (a/b/c) + Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character Order in Segment (1 digit).   |
| img_file_name        | File name of the image for the constituent **`Headword`** character (including the .jpg extension). The main part of the file name consists of a 7-digit number for images from Volume 1 to Volume 9, and an 8-digit number for images from Volume 10. For 7-digit numbers, the first digit indicates the volume number; for 8-digit numbers, the first two digits indicate Volume 10. The last 6 digits are based on the order of appearance, assigned according to a unique internal rule. Detailed documentation for this naming convention is not available as the work was completed over two decades ago. Null if no image is available. |
