---
bookCollapseSection: true
title: "Project Progress"
weight: 40
---

# Project Progress

This section is part of the **Project Records**, distinct from the normative Core
Documentation. It is a periodically updated snapshot of how far annotation work on
the Kanchi-in manuscript of the *Ruiju Myōgishō* has progressed.

**The detailed tables — broken down by the ten fascicles and by gloss type — are
maintained only in Japanese.** This page is an English summary of the current
figures. For the full breakdowns, see the Japanese version:
[進捗状況](/docs/krm/07-progress/).

## What is being tracked

For each **`Headword`** entry, the KRM data separates the components of its
**`Original Gloss`** (Jp. *chūmon*) into five kinds: **`Notes on Character Form`**
(*jitaichū*), **`Phonetic Glosses`** (*onchū*), **`Semantic Glosses in Chinese`**
(*gichū*), **`Japanese Native Readings`** (*wakun*), and a residual *Other*
category. Progress is recorded for the entries, for each gloss type, and — for the
*wakun* — for their linkage to the *Nihon Kokugo Daijiten* (2nd ed., via
JapanKnowledge).

## Current figures

From `krm_notes.tsv` v1.2.40 (2026-08-25) and `krm_wakun.tsv` v1.2.20
(2026-08-19).

### Entries and glosses

- **`Headword`** entries: **32,607**
- **`Original Gloss`** elements: **86,796** in total
  - Notes on Character Form: 13,359 (15.4%)
  - Phonetic Glosses: 24,148 (27.8%)
  - Semantic Glosses in Chinese: 12,658 (14.6%)
  - Japanese Native Readings (*wakun*): 35,378 (40.8%)
  - Other: 1,253 (1.4%)
- Entries and glosses together amount to roughly 119,400 recorded elements.
- Of the Phonetic Glosses, 4,463 (18.5%) carry **`Tone marks`**; of the *wakun*
  elements, 13,559 (38.3%) carry tone marks.

### Japanese Native Readings — linkage to the *Nihon Kokugo Daijiten*

Counted over 36,352 *wakun* elements, including juxtaposed variant readings:

- Matched to a dictionary headword: **30,467 (83.8%)**
- Checked and confirmed absent from the dictionary: **1,158 (3.2%)**
- Linkage resolved in total: **31,625 (87.0%)**; about 4,700 elements remain to be
  checked.
- Editorial notes (`remarks`) written: **19,505 (53.7%)**
- Variant *wakun* forms recorded: 2,007; variant-*kanji* notations for *wakun*:
  3,152

## Update policy

These figures are recomputed from the published data files whenever the
underlying data is updated; the change history is kept in `MAINTENANCE_LOG.md` in
the repository. Because the numbers are a work-in-progress snapshot, small
changes from one revision to the next reflect ongoing editorial corrections as
well as newly completed work.
