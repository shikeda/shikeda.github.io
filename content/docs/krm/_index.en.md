---
title: "KRM Documentation"
weight: 1
# date: 2022-01-09
# bookFlatSection: true
# bookToc: true
# bookHidden: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# KRM Documentation

*Scholarly and Technical Documentation for the KRM Database*

## About This Documentation

**KRM Documentation** is the official scholarly and technical reference documentation for the KRM Database — the full-text database of the Kanchi-in manuscript of the *Ruijū Myōgishō*. It documents the source manuscript, the published data files, the entry data model, data entry conventions, annotation policy, the typesetting environment, project progress, and related case studies.

This documentation is intended for readers working with the KRM data directly — researchers in Japanese historical linguistics, lexicography, and digital humanities — as well as readers who want to understand how the KRM Database was built and is maintained.

- **Author:** Shōju Ikeda, Professor Emeritus, Hokkaido University
- **Documentation Version:** 0.9 (draft; Version 1.0 planned on completion of this reorganization)
- **Publication Date:** *draft — to be finalized at Version 1.0*
- **Last Updated:** *draft — to be finalized at Version 1.0*
- **Project Website:** [https://shikeda.github.io/](https://shikeda.github.io/)
- **Documentation Website:** [https://shikeda.github.io/docs/krm/](https://shikeda.github.io/docs/krm/)
- **Documentation License:** [CC BY-SA 4.0](https://github.com/shikeda/krm/blob/main/LICENSE)
- **Suggested Citation:** *(draft — finalized at Version 1.0)* Ikeda, Shōju. *KRM Documentation*. Version 0.9. [https://shikeda.github.io/docs/krm/](https://shikeda.github.io/docs/krm/).
- **Relationship:** KRM Documentation documents the KRM Database, which is distributed through GitHub and Zenodo (see [Resource Documented](#resource-documented) below).

Note that while the explanation in this documentation overlaps in part with what is stated in the paper by Shōju Ikeda, Liu Guanwei, Jung Munho, Zhang Xinfang, and Li Yuan, “Full-text Database of *Ruijū Myōgishō*, Kanchi-in MS : A Look at Development Methods and Calculating the Number of Headwords." (*Kuntengo to Kuten Shiryō* 144, 2020), it has been completely overhauled and rewritten by the first author, Ikeda, who organized the terminology and substantially added subsequent research findings.

## Resource Documented

This documentation describes **KRM: Database of the Kanchi-in Manuscript of the *Ruijū Myōgishō*** (KRM) — a full-text digitization of the Kanchi-in manuscript, together with location data, textual collation, and source studies. KRM is not only a dataset: its repository also includes processing scripts and a local search web application.

- **Repository:** [https://github.com/shikeda/krm](https://github.com/shikeda/krm)
- **KRM Data Version:** v1.2.6
- **KRM Dataset DOI:** [10.5281/zenodo.15481563](https://doi.org/10.5281/zenodo.15481563)
- **Data Citation:** Ikeda, Shōju. (2025). *KRM: Database of the Kanchi-in Manuscript of the Ruijū Myōgishō*. Version v1.2.6. Zenodo. [https://doi.org/10.5281/zenodo.15481563](https://doi.org/10.5281/zenodo.15481563).
- **KRM Data License:** [CC BY-SA 4.0](https://github.com/shikeda/krm/blob/main/LICENSE)
- **Software License:** [MIT License](https://github.com/shikeda/krm/blob/main/scripts/LICENSE) (applies to `scripts/` and `webapp/`)

**Repository Contents:**

| Path | Contents |
| --- | --- |
| `krm_*.tsv`, `krm_*.json` | Published KRM data files (headwords, definitions, notes, readings, etc.) |
| `scripts/` | Python utility scripts for data conversion and maintenance (MIT License) |
| `webapp/` | A local full-text search application (Next.js; MIT License) |
| `docs/` | Repository documentation (distinct from this Documentation site) |
| `examples/`, `images/`, `diff/` | Supporting examples, images, and change-tracking material |

## Relationship to the HDIC Project

KRM is one of the Hanzi dictionary databases that make up the **Integrated Database of Hanzi Dictionaries in Early Japan (HDIC)**. For an introduction to the HDIC Project as a whole — its background, its other constituent databases, and the HDIC Viewer search tool — see the [HDIC Project home page](/en/).

## About the Ruijū Myōgishō

The KRM Database is based on the Kanchi-in manuscript of the *Ruijū Myōgishō* (類聚名義抄), a twelfth-century Sino-Japanese character dictionary compiled by a Shingon Buddhist monk. The Kanchi-in manuscript is the only complete extant witness to the work's revised-compilation lineage, and is a valuable resource for research in the history of the Japanese lexicon, the historical phonology of Sino-Japanese character readings, and the history of Chinese character forms as used in Japan.

For a full description see [Chapter 1: Overview of the *Ruijū Myōgishō*](./01-introduction/).

## How This Documentation Is Organized

This documentation is organized into the following chapters:

1. **[Overview of the *Ruijū Myōgishō*](./01-introduction/)** — the source manuscript: its textual traditions, compiler, date, significance, and structure.
2. **[Overview of Published Data](./02-data-overview/)** — the KRM data files and their structure.
3. **[Entry Data Model](./03-entry-data-model/)** — the conceptual model behind KRM entries.
4. **[Input of Entry Data](./04-entry-input/)** — headwords, IDs, character encoding, and transcription conventions.
5. **[Basic Policy for Annotation Creation](./05-annotation-policy/)** — annotation policy and methodology, with worked examples.
6. **[Typesetting Configuration](./06-typesetting/)** — the typesetting environment for transcriptions and annotations.
7. **[Project Progress](/docs/krm/07-progress/)** — development records (Japanese only).
8. **[Case Studies](/docs/krm/08-case-studies/)** — applied research examples (Japanese only).
9. **[Development History](./09-development-history/)** — how the KRM Database was constructed.

Use the navigation sidebar to move between chapters and pages.

## Acknowledgements

The construction and publication of the full-text database of the *Ruijū Myōgishō* of the Kanchi-in manuscript are being carried out with special permission from the authorities of Tenri Library, and we have also received exceptional consideration from Yagi Shoten, the publisher of the Tenri Library Rare Books Series. We hereby express our gratitude for this.

This work was supported by JSPS KAKENHI Grant Numbers 25370506, 16H03422, 19H00526, 23K17500, 25K00466 and 26K21717.
