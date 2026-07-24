# Current State Report

Phase 1: Current State Analysis

This report is a formal Phase 1 deliverable under `PROJECT_CHARTER.md`.
It records observations, analysis, and diagnosis of the current KRM Documentation.
It does not edit or revise the Documentation itself.

Primary scope:

- `content/docs/krm/`
- supporting static assets under `static/images/`

Out of scope for this report:

- scholarly revision
- rewriting of Documentation pages
- changes to bibliography, examples, datasets, identifiers, encoding rules, or database specifications
- detailed implementation planning

---

## 1. Executive Summary

The KRM Documentation already contains a substantial body of reference material for the Ruiju Myogisho Database.
It documents the database overview, entry data model, input rules, annotation policy, typesetting environment, progress records, and case studies.

The current state is best understood as a rich but uneven documentation corpus.
Its strongest assets are the presence of domain-specific explanations, data-file descriptions, conceptual definitions, and detailed examples.
Its main weakness is not lack of content, but insufficient information architecture.

The Documentation currently mixes several document types at the same structural level:

- reference documentation
- data specifications
- editorial/input rules
- annotation methodology
- technical setup notes
- progress reports
- research-oriented case studies

Internal navigation is functional in broad outline, but inconsistent in detail.
Several links point to older or mismatched paths, including `/docs/notes/...`, `/docs/krm/06-progress/`, and `/docs/krm/07-case-studies/`.

Japanese and English versions exist for much of the core Documentation, but the bilingual structure is not yet conceptually stable.
Some English files contain substantial Japanese text, and some later sections use unsuffixed Markdown files containing both Japanese and English.

The Documentation is therefore ready for a Documentation Blueprint, but the Blueprint should be based on a clear distinction between core reference documentation, supporting workflow documentation, and research/application materials.

---

## 2. Repository Overview

The repository root contains the project-level governance document:

- `PROJECT_CHARTER.md`

The KRM Documentation is located under:

- `content/docs/krm/`

The current KRM Documentation is divided into eight top-level directories:

- `content/docs/krm/01-introduction/`
- `content/docs/krm/02-data-overview/`
- `content/docs/krm/03-entry-data-model/`
- `content/docs/krm/04-entry-input/`
- `content/docs/krm/05-annotation-policy/`
- `content/docs/krm/06-typesetting/`
- `content/docs/krm/07-progress/`
- `content/docs/krm/08-case-studies/`

Static visual assets relevant to the Documentation are located under:

- `static/images/`

Observed image assets include:

- `static/images/krm-item-sample1.png`
- `static/images/krm-item-structure.png`
- `static/images/krmer.drawio.png`
- `static/images/krm_notes_er.drawio.png`
- `static/images/item-excel-sample.png`
- `static/images/gy_dhsjr_link_workflow.svg`
- `static/images/frequency_of_updates202505.png`

The image inventory is small and focused.
It mainly supports data model explanation, ER diagrams, sample data views, and workflow visualization.

---

## 3. Documentation Inventory

The KRM Documentation currently contains 83 Markdown files under `content/docs/krm/`.

Observed language/file pattern:

- 34 English files using `.en.md`
- 34 Japanese files using `.ja.md`
- 15 files without language suffix

Top-level section file counts:

- `01-introduction/`: 4 files
- `02-data-overview/`: 16 files
- `03-entry-data-model/`: 10 files
- `04-entry-input/`: 8 files
- `05-annotation-policy/`: 16 files
- `06-typesetting/`: 12 files
- `07-progress/`: 8 files
- `08-case-studies/`: 7 files

The main KRM landing pages are:

- `content/docs/krm/_index.ja.md`
- `content/docs/krm/_index.en.md`

Core section index pages include:

- `content/docs/krm/01-introduction/_index.ja.md`
- `content/docs/krm/01-introduction/_index.en.md`
- `content/docs/krm/02-data-overview/_index.ja.md`
- `content/docs/krm/02-data-overview/_index.en.md`
- `content/docs/krm/03-entry-data-model/_index.ja.md`
- `content/docs/krm/03-entry-data-model/_index.en.md`
- `content/docs/krm/04-entry-input/_index.ja.md`
- `content/docs/krm/04-entry-input/_index.en.md`
- `content/docs/krm/05-annotation-policy/_index.ja.md`
- `content/docs/krm/05-annotation-policy/_index.en.md`
- `content/docs/krm/06-typesetting/_index.ja.md`
- `content/docs/krm/06-typesetting/_index.en.md`
- `content/docs/krm/07-progress/_index.md`
- `content/docs/krm/08-case-studies/_index.md`

The first six sections generally use Japanese/English pairs.
The last two sections are mostly unsuffixed and appear to function as bilingual or Japanese-centered content.

---

## 4. Information Architecture

The current structure is numerically ordered and broadly intelligible.
The sequence moves from general introduction to data overview, data model, input rules, annotation policy, typesetting, progress, and case studies.

This order has a plausible learning path:

1. What the resource is
2. What data files exist
3. What the data model means
4. How data is input
5. How annotation is created
6. How transcription and annotation may be typeset
7. What progress has been made
8. How the data can support research cases

However, the current hierarchy does not clearly separate reference layers.
For example:

- `02-data-overview/` functions as data-file reference.
- `03-entry-data-model/` functions as conceptual reference.
- `04-entry-input/` functions as editorial/input rules.
- `05-annotation-policy/` mixes methodology, counts, examples, and source materials.
- `06-typesetting/` functions partly as production workflow notes.
- `07-progress/` functions as project status records.
- `08-case-studies/` functions as research/application content.

This creates ambiguity about what belongs to the stable core reference and what belongs to supporting or evolving material.

The strongest conceptual center is currently spread across:

- `content/docs/krm/02-data-overview/`
- `content/docs/krm/03-entry-data-model/`
- `content/docs/krm/04-entry-input/`
- `content/docs/krm/05-annotation-policy/`

These sections together define the database, its data files, its concepts, its input rules, and its annotation methodology.

The current top-level architecture is therefore usable, but not yet fully aligned with a long-term reference documentation model.

---

## 5. Navigation and Cross References

The Documentation includes explicit content lists on major index pages.
Examples:

- `content/docs/krm/_index.ja.md`
- `content/docs/krm/_index.en.md`
- `content/docs/krm/02-data-overview/_index.ja.md`
- `content/docs/krm/05-annotation-policy/_index.ja.md`
- `content/docs/krm/06-typesetting/_index.en.md`

This is a strength: readers are not dependent only on automatically generated side navigation.

However, several cross-reference problems were observed.

Path mismatches in the Japanese KRM landing page:

- `content/docs/krm/_index.ja.md` links to `/docs/krm/06-progress/`, while the actual directory is `content/docs/krm/07-progress/`.
- `content/docs/krm/_index.ja.md` links to `/docs/krm/07-case-studies/`, while the actual directory is `content/docs/krm/08-case-studies/`.

Path mismatch in the English KRM landing page:

- `content/docs/krm/_index.en.md` links to `./02-data-overview/02-03-headword_chars/`, while the actual file path uses `02-03-headword-chars`.

Old or non-current documentation paths remain in several pages:

- `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md`
- `content/docs/krm/04-entry-input/_index.ja.md`
- `content/docs/krm/04-entry-input/04-03-handling.ja.md`
- `content/docs/krm/07-progress/_index.md`
- `content/docs/krm/07-progress/1.md`
- `content/docs/krm/07-progress/2.md`

Examples include paths under:

- `/docs/notes/krm/`
- `/docs/notes/krm-main/`
- `/docs/notes/krm_main/contens/`

A localhost URL was also observed:

- `http://localhost:1313/docs/notes/krm-main/notes-input/`

These cross-reference issues suggest that the Documentation has undergone structural migration, but not all internal references were normalized afterward.

---

## 6. Terminology

The Documentation contains valuable terminology definitions.

The most important terminology explanation is in:

- `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md`
- `content/docs/krm/03-entry-data-model/03-01-data-structure.en.md`

This section defines or discusses core concepts such as:

- Entry / 項目
- Headword / 掲出字
- Original Glosses / 注文
- Phonetic Gloss / 音注
- Semantic Gloss in Chinese / 義注
- Japanese native reading / 和訓
- Notes on Character Form / 字体注
- Other / その他

The Documentation also explains terms related to character representation:

- `content/docs/krm/03-entry-data-model/03-03-concepts-char.ja.md`
- `content/docs/krm/03-entry-data-model/03-03-concepts-char.en.md`

These include:

- 書体
- 字体
- 字形
- 異体字
- 形近字

Input-related terminology is concentrated in:

- `content/docs/krm/04-entry-input/04-03-handling.ja.md`
- `content/docs/krm/04-entry-input/04-03-handling.en.md`

This includes:

- 誤字
- 脱字
- 衍字
- 訂正符号
- 略字
- 踊り字
- 代用符号
- 合符
- 割注
- 小字注記
- 異本注記
- 出典注記
- 声点
- ヲコト点

The terminology base is therefore strong.
The main issue is distribution.
Terms are defined locally, but there is no observed central glossary or terminology index under `content/docs/krm/`.

There are also signs of terminology variation across pages.
For example, `注文` is explained as being read as both `ちゅうもん` and `ちゅうぶん` in `03-01-data-structure.ja.md`.
This is valuable scholarly context, but it also increases the need for a stable terminology layer.

---

## 7. Internationalization (Japanese / English)

The Documentation has substantial bilingual coverage in sections `01` through `06`.
Most files in these sections have `.ja.md` and `.en.md` counterparts.

Examples:

- `content/docs/krm/02-data-overview/02-01-main.ja.md`
- `content/docs/krm/02-data-overview/02-01-main.en.md`
- `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md`
- `content/docs/krm/03-entry-data-model/03-01-data-structure.en.md`
- `content/docs/krm/04-entry-input/04-03-handling.ja.md`
- `content/docs/krm/04-entry-input/04-03-handling.en.md`

However, the bilingual model is not yet stable.

Observed issues:

- Some `.en.md` files contain substantial Japanese text.
- Some unsuffixed files contain both Japanese and English.
- English and Japanese pages often differ significantly in length.
- Some English pages appear to be expanded explanations rather than direct counterparts.
- Some Japanese pages are concise while English versions are much longer.

Examples of major length imbalance:

- `content/docs/krm/01-introduction/01-01-introduction.en.md`
- `content/docs/krm/01-introduction/01-01-introduction.ja.md`
- `content/docs/krm/04-entry-input/04-01-id.en.md`
- `content/docs/krm/04-entry-input/04-01-id.ja.md`
- `content/docs/krm/05-annotation-policy/05-02-headword-count.en.md`
- `content/docs/krm/05-annotation-policy/05-02-headword-count.ja.md`

Examples of English files with notable Japanese content:

- `content/docs/krm/05-annotation-policy/05-03-jitaichu-formats.en.md`
- `content/docs/krm/05-annotation-policy/05-07-annotation-examples.en.md`
- `content/docs/krm/05-annotation-policy/05-06-wakun-materials.en.md`

Section `08-case-studies/_index.md` contains both Japanese and English content in a single unsuffixed file.
It also includes meta-text such as `Note on Terminology`, which reads as translation/editorial commentary rather than stable reference documentation.

The current internationalization state is therefore partially implemented but not yet governed by a clear policy.

---

## 8. Documentation Types

Several documentation types are present.

Reference overview:

- `content/docs/krm/_index.ja.md`
- `content/docs/krm/_index.en.md`
- `content/docs/krm/01-introduction/`

Data-file reference:

- `content/docs/krm/02-data-overview/02-01-main.*.md`
- `content/docs/krm/02-data-overview/02-02-notes.*.md`
- `content/docs/krm/02-data-overview/02-03-headword-chars.*.md`
- `content/docs/krm/02-data-overview/02-04-wakun.*.md`
- `content/docs/krm/02-data-overview/02-05-definitions.*.md`
- `content/docs/krm/02-data-overview/02-06-pronunciations.*.md`
- `content/docs/krm/02-data-overview/02-07-ndl.*.md`

Conceptual model:

- `content/docs/krm/03-entry-data-model/03-01-data-structure.*.md`
- `content/docs/krm/03-entry-data-model/03-02-types-of-entries.*.md`
- `content/docs/krm/03-entry-data-model/03-03-concepts-char.*.md`

Data publication/example material:

- `content/docs/krm/03-entry-data-model/03-04-data-example.*.md`

Input and transcription rules:

- `content/docs/krm/04-entry-input/04-01-id.*.md`
- `content/docs/krm/04-entry-input/04-02-char.*.md`
- `content/docs/krm/04-entry-input/04-03-handling.*.md`

Annotation methodology:

- `content/docs/krm/05-annotation-policy/`

Typesetting and production setup:

- `content/docs/krm/06-typesetting/`

Progress records:

- `content/docs/krm/07-progress/`

Research/application case studies:

- `content/docs/krm/08-case-studies/`

The presence of these types is a strength.
The weakness is that document type boundaries are not explicit in the navigation or hierarchy.

---

## 9. Strengths

The Documentation contains deep domain-specific material that cannot be reconstructed from generic documentation patterns.

Major strengths:

- Clear top-level directory organization under `content/docs/krm/`.
- Strong coverage of published data files under `02-data-overview/`.
- Core conceptual explanation of Entry, Headword, and Original Glosses under `03-entry-data-model/`.
- Detailed input and notation handling rules under `04-entry-input/`.
- Substantial annotation methodology under `05-annotation-policy/`.
- Existing bilingual infrastructure for much of the core material.
- Explicit index pages for major sections.
- Use of diagrams and images for structural explanation.
- Preservation of scholarly detail, examples, and evidence.

The Documentation already has enough substance to support a long-term reference documentation system.

---

## 10. Weaknesses

The main weaknesses are architectural and editorial rather than scholarly.

Observed weaknesses:

- Core reference, workflow notes, progress records, and research case studies appear at the same top-level depth.
- Several links point to old or incorrect paths.
- Some section numbers in links no longer match actual directory numbers.
- There is no observed central glossary.
- Japanese and English versions do not consistently behave as parallel versions.
- Some English files contain untranslated or partially translated Japanese text.
- Some unsuffixed files mix Japanese and English content.
- Page length and granularity vary widely.
- Some titles and headings differ in scope or wording between Japanese and English.
- Some pages include temporary, conversational, or tool-specific wording.

These weaknesses affect discoverability, maintainability, and reader confidence.

---

## 11. Technical Debt

The Documentation has accumulated structural and editorial technical debt.

Observed technical debt includes:

- Stale links to `/docs/notes/...`.
- Broken or likely broken links caused by directory renumbering.
- Mismatched path spelling, such as `headword_chars` vs `headword-chars`.
- A `localhost` reference in `content/docs/krm/07-progress/1.md`.
- Legacy or transitional page titles, such as `注釈データ入力の詳細` in the front matter of `05-annotation-policy/_index.ja.md`, while the page heading is `注釈作成の基本方針`.
- Mixed language strategy across `.ja.md`, `.en.md`, and unsuffixed `.md` files.
- Large pages that combine conceptual explanation, examples, counts, and detailed notes.
- External links marked as broken in some typesetting/tool pages.

This debt does not invalidate the Documentation.
It indicates that the project has evolved faster than its documentation architecture.

---

## 12. Key Findings

1. The Documentation is content-rich but architecture-light.

2. The current top-level structure is understandable, but it does not yet clearly separate stable reference content from progress records, technical setup notes, and research case studies.

3. The strongest reference core is distributed across `02-data-overview/`, `03-entry-data-model/`, `04-entry-input/`, and `05-annotation-policy/`.

4. The terminology base is strong, especially in `03-entry-data-model/03-01-data-structure.*.md` and `04-entry-input/04-03-handling.*.md`, but terminology is not centralized.

5. Internal navigation needs architectural review because several links preserve older paths or mismatched section numbering.

6. Bilingual documentation exists, but internationalization is not governed by a consistent document model.

7. Section `05-annotation-policy/` is highly valuable but structurally dense.
It includes policy, examples, counts, materials, and detailed annotation cases.

8. Section `06-typesetting/` is useful but has a different document type from the core KRM reference.

9. Section `07-progress/` appears to preserve project status information and old navigation assumptions.

10. Section `08-case-studies/` is valuable as applied research material, but it should be distinguished from core database reference documentation in later planning.

---

## 13. Roadmap Implications

The later Documentation Blueprint and `ROADMAP.md` should treat the current Documentation as a mature content base requiring architectural consolidation.

Implications for later phases:

- A future Blueprint should define the core reference layer before chapter-level refactoring begins.
- Navigation and cross-reference normalization should be treated as architectural work, not merely link cleanup.
- Terminology should be handled as a project-wide concern.
- Internationalization needs an explicit policy for Japanese pages, English pages, and bilingual/unsuffixed pages.
- Document types should be classified before deciding where each existing section belongs.
- `07-progress/` and `08-case-studies/` should be evaluated as supporting documentation rather than assumed to be part of the same reference layer as data model and input rules.
- Long, dense pages should be diagnosed for information structure before any rewriting is attempted.

These implications are diagnostic only.
They are intended to inform the subsequent Documentation Blueprint and Roadmap Design phases.
