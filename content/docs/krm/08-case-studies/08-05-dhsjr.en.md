---
title: "DHSJR Collaboration"
weight: 55
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# DHSJR Collaboration

This page is an English-language summary of a working record completed on June 19, 2025 (analysis begun February 16, 2025), documenting the process of preparing KRM data for collaboration with DHSJR (Database of Historical Sino-Japanese Readings). The full account, including detailed worked examples, is kept in the Japanese version, [DHSJRとの連携](/docs/krm/08-case-studies/08-05-dhsjr/); this page presents only a summary. For KRM's general treatment of **`Phonetic Glosses`**, see [Types of Phonetic Glosses and Decipherment Issues](/en/docs/krm/05-annotation-policy/05-04-onchu-problems/).

This summary reflects the state of the collaboration as of June 2025, when the underlying analysis was completed. The mapped data was subsequently published on September 10, 2025; see [krm_pronunciations](/en/docs/krm/02-data-overview/02-06-pronunciations/#collaboration-with-dhsjr) for the current status.

## 1. Overview of DHSJR and the Approach to Mapping KRM Data

* **Purpose of the DHSJR project**: DHSJR (Database of Historical Sino-Japanese Readings) is a project to make Sino-Japanese character and word readings, from the Heian–Kamakura periods through the present, cross-searchable based on annotations such as **`Kana glosses`**, **`Tone marks`**, and **`Fanqie spellings`**. It is led by Professor Katō Daikaku of Waseda University.
* **Including the *Myōgishō* and resource IDs**: The *Myōgishō* is not yet included in DHSJR. Work is underway to extract **`Phonetic Glosses`** from KRM's full-text data (`KRM.tsv` and `KRM_definitions.tsv`) and adapt them to DHSJR's format. Dedicated resource IDs have been reserved and organized for the *Myōgishō*'s several manuscripts (e.g., the Zushoryō manuscript: `30-048-01`; the Kanchi-in manuscript: `30-048-02`).
* **DHSJR's 23-column structure**: To load the data, each of DHSJR's 23 defined data columns (e.g., character headword, tone marks, kana glosses, fanqie, similar-sound notes, material location) was individually mapped to the corresponding KRM data items.

## 2. Designing Phonetic Gloss IDs and the Row-Splitting Rule for One-to-Many Relationships (the core of `krm_pronunciations`)

* **Basic ID design**: In principle, the **`Definition Sequence ID`** (`definition_seq_id`, formerly `KRID_no`), which identifies a component of a dictionary **`Entry`**, and the **`Phonetic Gloss ID`** (`pronunciation_id`, formerly `KRID_pron_no`) are mapped one to one.
* **Where one-to-many records arise**: When **`Kana glosses`**, **`Fanqie spellings`**, **`Similar sound notes`**, and **`Tone marks`** occur in combination within a single **`Definition`**, keeping everything on one row would obscure which character each **`Tone mark`** actually belongs to.
* **Adding suffix letters (b, c, …) and splitting rows**: Where a one-to-many relationship arises, suffixes `b`, `c`, `d`, … `n` are appended to the **`Definition Sequence ID`** to generate multiple **`Phonetic Gloss ID`**s, and the data is split across multiple rows (affecting roughly 500-690 cases).
* **Priority order for row splitting**:
  1. The **`Headword`**'s own direct **`Kana gloss`** and **`Tone mark`** (marked with a double circle "◎") take priority and are recorded on the same row.
  2. A **`Phonetic Gloss`** stated as part of the **`Definition`** is recorded as the **`Phonetic Gloss`** for the **`Headword`**, on a separate row.
  3. **`Kana glosses`** or **`Tone marks`** applied to the individual characters used within a **`Similar sound note`** or **`Fanqie spelling`** (**`Phonetic Gloss Character`**s) are recorded on yet another row, with the target-character field changed accordingly.

## 3. Data Conversion and Normalization Rules for Tone Marks and Kana Glosses

* **Replacing tone-mark symbols**: The romanized **`Tone mark`** symbols KRM uses internally (`L`/`F`/`H`/`R`/`T`/`S`/`V`) are converted in bulk to DHSJR's Japanese-language labels (平/平軽/上/去/入/入軽/濁). The underscore `_` marking the absence of a **`Tone mark`** (formerly the at-sign `@`, before the March 2025 specification change) is replaced with a full-width asterisk (＊).
* **Concatenating multiple kana glosses**: Where multiple **`Kana glosses`** exist, as in "シム／ニム", they are joined with a full-width slash (／).
* **Handling tone marks and nasal marks attached to a kana gloss**: Where a **`Tone mark`** or nasal-sound symbol (✓) is applied to the **`Kana gloss`** itself, that information is recorded inside full-width parentheses `（）` within the kana-gloss field — e.g., "和シヨ（＊平）" or "リヤウ（N＊＊）" — kept distinct from the **`Tone mark`** field used for **`Hanzi (Chinese characters)`**.
* **Preserving representation via special characters**: Specific characters inserted into a **`Kana gloss`** to mark a contracted or voiced sound — 火 for the contracted sound *kwa*, 所 for the contracted sound *sho*, 土 for a voiced sound — are retained as-is within the **`Kana gloss`**.

## 4. Detailed Processing Rules for Similar Sound Notes, Fanqie, and Reading-Type Markers

* **Separating tone marks within a fanqie spelling**: Where the final character of a **`Fanqie spelling`** (e.g., "曽" in "蘇曽反") itself carries a **`Tone mark`**, the **`Headword`**'s own row (e.g., "僧") records the fanqie with the tone-mark field left blank, and a separate row is created for the **`Phonetic Gloss Character`** record (e.g., "曽") giving its **`Tone mark`** (平軽).
* **Compound notations such as "二音" and "二反"**: Forms such as "二音", "二反", or "二切", where multiple **`Phonetic Glosses`** are listed together under one **`Headword`**, are for now **kept in their original notation** rather than mechanically decomposed, to avoid losing nuance or internal consistency.
* **Protecting reading-type markers and source citations**: **Reading-type markers** — the initial characters 和, 呉, 俗, 今, which indicate the nature of a reading — and **source citations** enclosed in double angle brackets (e.g., 《玉篇》《説文》) are essential scholarly information for interpreting a **`Phonetic Gloss`** and are retained in full in the data.
