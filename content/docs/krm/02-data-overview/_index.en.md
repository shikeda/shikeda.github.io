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

This database is a full-text digitization of the Kanchi-in manuscript of the *Ruiju Myōgishō* (abbreviated as KRM), incorporating location information, textual collation, source studies, and more. It is one of the **Hanzi** dictionary databases comprising the **Integrated Database of Hanzi Dictionaries in Early Japan** (abbreviated as HDIC). **The terms 'kanji' and 'hanzi' are explained later.**

The Kanchi-in manuscript of the *Ruiju Myōgishō* is a **Hanzi (Chinese character)** dictionary compiled in the twelfth century by a Shingon Buddhist monk. It has long been regarded as an important resource for research in Japanese historical linguistics due to its extensive collection of:

* **`Japanese Native Readings` (*wakun*)** that indicate accent (often with **`Tone marks`**),
* detailed **`Phonetic Glosses`** on the pronunciation of **Hanzi (Chinese characters)**, and
* comprehensive **`Notes on Character Form`**, including information on **`variant characters` (*itaiji*)**.

Furthermore, its annotations written in literary Chinese—which include **`fanqie` spellings**, **`Semantic Glosses in Chinese`** (explaining meanings), and **`Notes on Character Form`** (detailing glyph forms)—have also garnered attention as valuable materials for the study of Chinese linguistics.

It was first published in March 2022, and in March 2025, a revised edition with specification changes and detailed explanations will be released.


## Kanji and Hanzi

To bridge the gap between 'Kanji' and 'Hanzi,' and to facilitate international academic discourse, the following supplementary explanation may be useful:

Dictionaries of Chinese characters compiled in Japan during the Heian period are invaluable resources not only for the study of Japanese linguistics but also for the study of Chinese linguistics. To promote international accessibility, we propose using the term 'Hanzi.' Researchers specializing in Japanese studies may, without any issue, read this term as 'Kanji.' This approach aims to respect the linguistic diversity and academic traditions of both fields, while encouraging broader scholarly exchange.

This explanation aims to provide clarity and respect for both terminologies, ensuring that researchers from different backgrounds can engage with the material without linguistic barriers.

For these reasons, 'hanzi' is used for the column names of the public data, while 'kanji' is used in the explanatory text.


## List of Data Files

The data for the Kanchi-in manuscript of the *Ruiju Myōgishō*, available at [https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2), is as follows. This list includes some files that are currently under preparation for public release.

  * **[krm\_main](./02-01-main/)**: Basic data. Includes information on **`Headwords`**, the full text of **`Definition (Original Glosses)`**, locations, etc. TSV and JSON files are available.
  * **[krm\_notes](./02-02-notes/)**: Data for the **`Compiler's Remarks`**. This comprises analyses of **`Headwords`**, **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings` (*wakun*)**, and **Other** elements from the *Myōgishō*, including results of textual collation and source investigation. TSV and JSON files are available.
  * **[krm\_headword\_chars](./02-03-headword-chars/)**: Detailed information about all **`Headwords`**. Includes location in the Kazama edition, location in the Tenri edition, image file names, etc.
  * **[krm\_wakun](./02-04-wakun/)**: **`Japanese Native Reading` (*wakun*)** data. Includes information about variant forms of *wakun*, variant forms of **Hanzi (Chinese characters) (*itaiji*)**, and correspondence with the "Notation" field of the *Nihon Kokugo Daijiten* (Second Edition). TSV and JSON files are available.
  * **[krm\_definitions](./02-05-definitions/)**: Data from the **`Definition (Original Glosses)`** of the *Myōgishō*, categorized into its constituent elements: **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings` (*wakun*)**, and **Other** elements. TSV file available. This is the same as the previously published [KRM\_definitions.tsv](https://github.com/shikeda/HDIC/KRM_definitions.tsv).
  * **[krm\_pronunciations](./02-06-pronunciations/)**: Data to facilitate linkage with the DHSJR regarding **`Phonetic Glosses`** (under preparation).
  * **[krm\_ndl](./02-07-ndl/)**: Links to the National Diet Library Digital Collections. TSV file available. This is the same as the previously published [KRM\_ndl.tsv](https://github.com/shikeda/HDIC/KRM_ndl.tsv).

A major revision of the data specifications was implemented in March 2025. Previously, published files were prefixed with "KRM" (uppercase). Files released after this revision are prefixed with "krm" (lowercase).

## Specification Change

Files incorporating these specification changes have been placed in the "v1.2" folder. Please note that this is a temporary arrangement.

The key points of these specification changes are as follows:

* The at mark "@", used to indicate that a *kana wakun* (a `Japanese Native Reading` written in kana) does not have **`Tone marks`**, has been changed to an underscore "_".
* The double quotation mark """, used to indicate that a *wakun* for a voiced sound is accompanied by **`Tone marks`**, has been changed to the half-width English letter "V".
* Half-width parentheses "()", used to indicate the presence of **`Tone marks`**, have been changed to full-width parentheses "（）".
* Half-width parentheses "()", used to indicate a proposed correction for a typographical error, have been changed to full-width square brackets "〔〕".
* Half-width square brackets "[]", used to indicate missing characters, have been changed to full-width square brackets "［］".


### ER Diagram

The following ER diagram shows the relationship between the three tables: `krm_main`, `krm_notes`, and `krm_wakun`.

![ER diagram.](/images/krmer.drawio.png)

Please note that the `krm_notes.json` file has a nested structure: each record contains an array of definitions rather than a flat list of rows. For more details on the internal structure of `krm_notes.json`, see the [dedicated page](./02-02-notes/).

![ER_notes diagram](/images/krm_notes_er.drawio.png)

## Common Information

For details including the version of the released data, author information, and copyright notices, please refer to the `README.md` file in the following GitHub repository.


[https://github.com/shikeda/HDIC/tree/master/v1.2/README.md](https://github.com/shikeda/HDIC/tree/master/v1.2/README.md)


## Acknowledgments

We would like to express our gratitude to Tenri Central Library and Yagi Bookstore for granting permission to publish the decipherment text of the Kanchi-in manuscript of the Ruiju Myogisho.  

This research is partly supported by JSPS KAKENHI Grant Numbers 16H03422, 19H00526, 23K17500 and 25K00466. We gratefully acknowledge this support.
