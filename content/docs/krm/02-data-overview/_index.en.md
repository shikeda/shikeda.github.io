---
bookCollapseSection: true
weight: 2
title: "Overview of Published Data"
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---


# Overview of Published Data

## Introduction

This database is a full-text digitization of the Kanchi-in manuscript of the Ruiju Myogisho (abbreviated as KRM), incorporating location information, textual collation, source studies, and more. It is one of the **Hanzi** dictionary databases comprising the **Integrated Database of Hanzi Dictionaries in Early Japan** (abbreviated as HDIC). **The terms 'kanji' and 'hanzi' are explained later.**

The Kanchi-in manuscript of the Ruiju Myogisho is a **Hanzi** dictionary compiled in the twelfth century by a Shingon Buddhist monk. It has been regarded as an important resource for Japanese historical linguistics research due to its extensive collection of *wakun* indicating accent, detailed annotations on **Hanzi** pronunciations, and annotations on variant characters. Furthermore, its Chinese annotations on **fanqie**, meanings, and glyph forms have also garnered attention as materials for Chinese linguistics.

It was first published in March 2022, and in March 2025, a revised edition with specification changes and detailed explanations will be released.


## Kanji and Hanzi

To bridge the gap between 'Kanji' and 'Hanzi,' and to facilitate international academic discourse, the following supplementary explanation may be useful:

Dictionaries of Chinese characters compiled in Japan during the Heian period are invaluable resources not only for the study of Japanese linguistics but also for the study of Chinese linguistics. To promote international accessibility, we propose using the term 'Hanzi.' Researchers specializing in Japanese studies may, without any issue, read this term as 'Kanji.' This approach aims to respect the linguistic diversity and academic traditions of both fields, while encouraging broader scholarly exchange.

This explanation aims to provide clarity and respect for both terminologies, ensuring that researchers from different backgrounds can engage with the material without linguistic barriers.

For these reasons, 'hanzi' is used for the column names of the public data, while 'kanji' is used in the explanatory text.

## Data Files

### List and Brief Description

The data from the Kanchi-in manuscript of the Ruiju Myogisho, published at [https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2), is as follows. This includes some files that are currently being prepared for public release.

- [krm_main](./02-01-main/): Basic data. Includes information about head characters, full definitions, locations, etc. TSV and JSON files are available.
- [krm_notes](./02-02-notes): Annotation data. Categorized into head characters, glyph annotations, pronunciation annotations, meaning annotations, *wakun*, and others, with collation and source studies. TSV and JSON files are available.
- [krm_headword_chars](./02-03-headword-chars/): Detailed information about all head characters. Includes location in the Kazama edition, location in the Tenri edition, image file names, etc. Currently under preparation for release.
- [krm_wakun](./02-04-wakun/): *Wakun* data. Includes information about variant forms of *wakun*, variant forms of hanzi (*itai-ji*), and correspondence with the "Notation" field of the *Nihon Kokugo Daijiten* (Second Edition). TSV and JSON files are available.
- [krm_definitions](./02-05-definitions/): Definitions categorized into glyph annotations, pronunciation annotations, meaning annotations, *wakun*, and others. TSV file available. Same as the already published [KRM_definitions.tsv](https://github.com/shikeda/HDIC/KRM_definitions.tsv).
- [krm_pronunciations](./02-06-pronunciations/): Data for linking with DHSJR regarding pronunciation annotations (under preparation).
- [krm_ndl](./02-07-ndl/): Links to the National Diet Library Digital Collections. TSV file available. Same as the already published [KRM_ndl.tsv](https://github.com/shikeda/HDIC/KRM_ndl.tsv).


### Specification Change

A significant specification change was implemented in March 2025. Previously, the published files were prefixed with "KRM," but the files following this specification change will be prefixed with "krm."

The files incorporating the specification changes have been placed in the "v1.2" folder. Please note that this is a temporary arrangement.

Here are the key points of the specification change:

- The at mark "@", which indicates that kana wakun does not have tone marks, has been changed to an underscore "_".
- The double quotation mark """, which indicates that voiced sound wakun has tone marks, has been changed to a half-width English letter "V".
- The half-width parentheses "()", which indicate the presence of tone marks, have been changed to full-width parentheses "（）".
- The half-width parentheses "()" indicating a correction proposal for a typo have been changed to full-width square brackets "〔〕".
- The half-width square brackets "[]", which indicate missing characters, have been changed to full-width square brackets "［］".

### ER Diagram

The following ER diagram shows the relationship between the three tables: krm_main, krm_notes, and krm_wakun.

![ER diagram.](/images/krmer.drawio.png)

Moreover, krm_notes.json has a nested structure as shown in the following diagram.

![ER_notes diagram](/images/krm_notes_er.drawio.png)

## Common Information

For details including the version of the released data, author information, and copyright notices, please refer to the `README.md` file in the following GitHub repository.


[https://github.com/shikeda/HDIC/tree/master/v1.2/README.md](https://github.com/shikeda/HDIC/tree/master/v1.2/README.md)


## Acknowledgments

We would like to express our gratitude to Tenri Central Library and Yagi Bookstore for granting permission to publish the decipherment text of the Kanchi-in manuscript of the Ruiju Myogisho.  

This research is partly supported by JSPS KAKENHI Grant Numbers 16H03422, 19H00526, 23K17500 and 25K00466. We gratefully acknowledge this support.
