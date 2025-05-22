---
bookCollapseSection: true
title: "Input of Entry Data"
weight: 4
bookToc: true
---

# Input of Entry Data


This document explains how to input **`Entry`** data for the Kanchiin manuscript of the *Ruiju Myōgishō*. Hereinafter, the Kanchiin manuscript of the *Ruiju Myōgishō* will be referred to as *"Myōgishō"* or "KRM."

An **`Entry`** consists of a **`Headword`** and **`Original Glosses`**. This section focuses on matters common to the input of **`Headwords`** and **`Original Glosses`** for the main **`Entry`** data of the *"Myōgishō"* (e.g., `krm_main.tsv`).

Among the input rules explained in this document, those concerning **character representation methods** (such as for characters outside of Unicode, special symbols, etc.) may also apply to other published data, including `krm_notes` (the file containing data for **`Compiler's Remarks`**). For details on the overall structure and file formats of the published data, please refer to the [Overview of Public Data](../krm/02-data-overview/). 

The published data primarily uses TSV format, but some data is also available in JSON format for better readability.

First, we will explain the **`Headwords`, `Entry` Structure, and ID System**. The ID system for KRM data is complex, so users are advised to read this section carefully.
Next, we will discuss **Character Encoding and Representation** using Unicode. We will also explain the handling of characters that cannot be represented by Unicode, as multiple methods are used in combination.
Finally, we will organize **scribal issues** such as misspellings and omissions; **notation formats for characters and words** like abbreviation marks and iteration marks; and **additional notes and layout** features such as interlinear notes and small character annotations. We will then summarize the **Handling of Issues in Transcription, Notation, and Annotation**.


- [Headwords, Entry Structure, and ID System](./04-01-id/)
- [Character Encoding and Representation](./04-02-char/)
- [Handling Issues in Transcription, Notation, and Annotation](./04-03-handling/)

