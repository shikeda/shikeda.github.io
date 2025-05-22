---
title: "Ruiju Myogisho"
weight: 2
# date: 2022-01-09
bookFlatSection: true
bookToc: true
# bookHidden: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

#  *Ruiju Myōgishō* (KRM): Full text Database of the Kanchiin Manuscript

## Introduction

The *Ruiju Myōgishō* is renowned as a masterpiece among old Japanese dictionaries. The book title is read as "ruiju myōgishō." It is said that the title was formed by taking "Ruiju" from Minamoto no Shitagō's Wamyō Ruijushō and "Myōgi" from Kūkai's *Tenrei Banshō Myeigi*.


Here, we will first describe the outline of the *Ruiju Myōgishō* and its various versions. Next, regarding the Kanchiin manuscript, which is the only extant complete manuscript of the *Ruiju Myōgishō*, we will explain the structure of its entries, and then describe the details of the input method for the text of the Kanchiin manuscript.


Note that while the explanation provided here overlaps in part with what is stated in the paper by Ikeda Shoju, Liu Guanwei, Jun Munho, Zhang Xinfang, and Li Yuan, “Full-text Database of *Ruiju Myogi-sho*, Kanchiin MS : A Look at Development Methods and Calculating the Number of Headwords." (*Kuntengo to Kuten Shiryō* 144, 2020), it has been completely overhauled and rewritten by the first author, Ikeda, who organized the terminology and substantially added subsequent research findings.



## Contents

- [Overview](./01-introduction/01-01-introduction/)
- [Overview of Public Data](./02-data-overview/)
    - [krm_main](./02-data-overview/02-01-main/)
    - [krm_notes](./02-data-overview/02-02-notes/)
    - [krm_headword_chars](./02-data-overview/02-03-headword_chars/)
    - [krm_wakun](./02-data-overview/02-04-wakun/)　
    - [krm_definitions](./02-data-overview/02-05-definitions/)　
    - [krm_pronunciations](./02-data-overview/02-06-pronunciations/)　
    - [krm_ndl](./02-data-overview/02-07-ndl/)　
- [Entry Data Model](./03-entry-data-model/)
    - [Entry Data Structure](./03-entry-data-model/03-01-data-structure/)
    - [Types of Entries](./03-entry-data-model/03-02-types-of-entries/)
    - [Concepts Related to Character Notation](./03-entry-data-model/03-03-concepts-char/)
    - [Publication and Updates of Entry Data Files](./03-entry-data-model/03-04-data-example/)
- [Item Data Entry](./04-entry-input/)
    - [Head Characters, Entry Structure, and ID System](./04-entry-input/04-01-id/)
    - [Character Encoding and Representation](./04-entry-input/04-02-char/)
    - [Problems and Handling in Writing, Notation, and Annotations](./04-entry-input/04-03-handling/)
- [Basic Principles for Creating Annotations/Commentary](./05-annotation-policy/)
    - [Basic Principles and Analytical Focus for Annotation Creation](./05-annotation-policy/05-01-basic-policy/)
    - [Calculation of Headword Count](./05-annotation-policy/05-02-headword-count/)
    - [Types and Descriptive Formats of Notes on Character Form](./05-annotation-policy/05-03-jitaichu-formats/)
    - [Types and Problems in Deciphering Phonetic Glosses](./05-annotation-policy/05-04-onchu-problems/)
    - [Types and Quantities of Semantic Glosses in Chinese](./05-annotation-policy/05-05-gichu-quantity/)
    - [Foundational Materials for Annotating Japanese Native Readings (*wakun*)](./05-annotation-policy/05-06-wakun-materials/)
    - [Specific Examples of Annotation Practice](./05-annotation-policy/05-07-annotation-examples/)
- [Typesetting Settings for Transcriptions and Annotations](./06-typesetting/)
    - [Hanazono Mincho Settings](./06-typesetting/06-01-hanazono-mincho/)
    - [GlyphWiki Settings](./06-typesetting/06-02-glyphwiki/)
    - [sfkanbun.sty Settings](./06-typesetting/06-03-sfkanbun-sty/)
    - [VS Code and TeX Live](./06-typesetting/06-04-vscode-texlive/)
    - [Online Tools](./06-typesetting/06-05-online-tools/)
- [Project Progress](./07-progress/)
- [Historical Research on Japanese: A Case Study of the KRM Manuscript](./08-case-studies/)

## Database Construction Process

The *Ruiju Myōgishō* of the Kanchiin manuscript is an old handwritten manuscript, and because it contains an extremely large number of difficult characters, we proceeded with database construction using the following steps.

**Step 1:** Scan the facsimile edition and cut out each listed character to create an image database of the *Ruiju Myōgishō* of the Kanchiin manuscript. The image files of the listed characters are named according to the location of the listed character. This image file name will later be used as the listed character ID.


**Step 2:** Add the location information to the existing *Tenrei Banshō Meigi* database by referring to the "Kanji Index" included in Atsuo Masamune's *Ruiju Myōgishō Volume 2* (Kazama Shobō, 1955). Input the location information from the "Kanji Index" into the *Tenrei Banshō Meigi* data rearranged in the order of the *Dai Kanwa Jiten* index numbers compiled by Tetsuji Morohashi. Then, rearrange it according to the order of locations in the Kanchiin manuscript, collate it with the text of the Kanchiin manuscript, and add the page numbers and character order of the Kanchiin manuscript that are not found in the "Kanji Index."

**Step 3:** Take in various information included in the *Tenrei Banshō Meigi* database (*Dai Kanwa Jiten* index numbers, Unicode numbers, kanji characters, location information in the *Tenrei Banshō Meigi*) and the corresponding location information of the *Ruiju Myōgishō* Kanchiin manuscript created in Step 2, into the *Ruiju Myōgishō* Kanchiin manuscript image database (created in Step 1) to create an input database for the *Ruiju Myōgishō* Kanchiin manuscript text.

**Step 4:** While referring to the facsimile edition of the *Ruiju Myōgishō* Kanchiin manuscript (Tenri Library Rare Books Series, Japanese Books Section, Volumes 32-34) and the *Ruiju Myōgishō* Kanchiin manuscript image database, add the text information for the listed characters and their explanations ("chūmon/chūbun") to the input database for the *Ruiju Myōgishō* Kanchiin manuscript text created in Step 3.

**Step 5:** Integrate the *Ruiju Myōgishō* Kanchiin manuscript image database and the *Ruiju Myōgishō* Kanchiin manuscript text database to form the *Ruiju Myōgishō* Kanchiin manuscript database. Then, check and revise the text content using the newly published color facsimile edition of the *Ruiju Myōgishō* Kanchiin manuscript (New Tenri Library Rare Books Series, Volumes 9-11). When checking the text content, also distinguish between compound word entries and variant character entries in the listed items, and distinguish between font annotations, pronunciation annotations, meaning annotations, and Japanese glosses in the explanations, and add this information.

**Step 6:** Publish the completed *Ruiju Myōgishō* Kanchiin manuscript database on the internet and provide a search service.


## Online Information Provision

HDIC's online information provision consists of three parts: the main site, the search screen, and the text data. The main site is available at the following URL and summarizes the overview of the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC) (in Japanese, Chinese, and English), a list of research results, links to related sites, etc.
[https://hdic.jp](https://hdic.jp)

The search screen is available at the following URL, where you can use the HDIC Viewer to search the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC). The HDIC Viewer is maintained and managed by [Liu Guanwei](https://researchmap.jp/liuguanwei?lang=en) and allows searches not only on personal computers but also on smartphones.
[https://viewer.hdic.jp](https://viewer.hdic.jp)

We would like to express our gratitude to [Tomohiko Morioka](https://researchmap.jp/morioka-tomohiko?lang=en) for his technical support in maintaining and managing the hdic.jp website.

The text data is available at the following URL, where we publish the text files created by the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC). 

We preserve records of data revisions and provide the latest versions of the full-text databases for the Song Dynasty edition of the *Yupian*, the Kosanji manuscript of the *Tenrei Banshō Meigi*, and the Tenji manuscript of the *Shinsen Jikyō*.

[https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC)


The *Ruiju Myōgishō* of the Kanchiin manuscript underwent a specification change in March 2025, and the latest version of its full-text database is available at the following URL:

[https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2)

Please note that the above URLs are subject to change in the future.
Maintaining and managing the constructed data is a significant challenge.

## Acknowledgements

The construction and publication of the full-text database of the *Ruiju Myōgishō* of the Kanchiin manuscript are being carried out with special permission from the authorities of Tenri Library, and we have also received exceptional consideration from Yagi Shoten, the publisher of the Tenri Library Rare Books Series. We hereby express our gratitude for this.

This work was supported by JSPS KAKENHI Grant Numbers 16H03422, 19H00526, 23K17500 and 25K00466.
