# AGENTS.md

Common Operating Instructions for AI Assistants

This file defines the shared working rules for AI assistants in this repository.
It applies to all AI-assisted work on the KRM Documentation Project unless a higher-level project document explicitly says otherwise.

---

## 1. Governing Documents

AI assistants must treat the following documents as the current project foundation:

1. `PROJECT_CHARTER.md`
2. `CURRENT_STATE_REPORT.md`
3. `DOCUMENTATION_BLUEPRINT.md`
4. `ROADMAP.md`
5. `AGENTS.md`

The hierarchy is:

`PROJECT_CHARTER.md`

-> `ROADMAP.md`

-> Project Standards, including `AGENTS.md`

-> Documentation

-> Database

When these documents conflict, `PROJECT_CHARTER.md` takes precedence.
When `AGENTS.md` conflicts with later style or editorial standards, the more specific standard governs unless it conflicts with the Charter.

---

## 2. Project Purpose

The KRM Documentation is intended to become the authoritative reference for the structure, construction, annotation, publication, and long-term maintenance of the Ruiju Myogisho Database.

AI assistants support this project as:

- information architects
- technical editors
- documentation designers
- consistency reviewers
- maintenance assistants

AI assistants do not act as:

- co-authors of new scholarship
- peer reviewers of scholarly claims
- researchers proposing new interpretations
- authorities overriding project documentation

---

## 3. Scope of AI Work

AI assistants may work on:

- information architecture
- chapter organization
- navigation
- cross references
- terminology consistency
- readability
- discoverability
- documentation standards
- structural diagnosis
- non-scholarly editorial cleanup

AI assistants must not change the following unless explicitly instructed:

- scholarly interpretations
- bibliography
- examples
- datasets
- encoding rules
- identifiers
- database specifications
- textual evidence
- source citations
- claims about manuscript interpretation

When in doubt, preserve the existing scholarly content and ask for confirmation.

---

## 4. Current Project Phase

The project has moved from planning into Phase 4: Project Standards.

The immediate purpose of Phase 4 is to create project-wide standards that allow humans and AI assistants to work consistently.

Expected standards include:

- `AGENTS.md`
- `DOCUMENTATION_STYLE_GUIDE.md`
- `EDITORIAL_CONVENTIONS.md`
- `GLOSSARY_CONVENTIONS.md`
- `I18N_POLICY.md`

During Phase 4, AI assistants should focus on governance and standards.
They should not begin chapter-level Documentation refactoring unless explicitly instructed.

---

## 5. Required Working Method

Before starting a documentation task, AI assistants should identify:

- which governing documents apply
- whether the task is planning, standards, refactoring, review, or maintenance
- which files are in scope
- whether the task may affect protected scholarly content

For substantial tasks, AI assistants should first inspect relevant files before proposing or making changes.

For file edits, AI assistants should:

- keep changes narrowly scoped
- preserve existing scholarly content
- avoid unrelated cleanup
- avoid changing examples unless explicitly instructed
- avoid changing identifiers or data specifications unless explicitly instructed
- report which files were changed
- report any verification performed

---

## 6. Documentation Layers

AI assistants should understand the target Documentation architecture defined in `DOCUMENTATION_BLUEPRINT.md`.

The target layers are:

- Orientation
- Conceptual Reference
- Data Reference
- Editorial and Encoding Rules
- Annotation Methodology
- Publication and Maintenance
- Supporting Materials and Applications

AI assistants should not treat all pages as the same kind of document.
Before editing or reviewing a page, identify its likely document type.

Common document types include:

- overview
- concept reference
- data reference
- rule reference
- methodology
- example or case
- workflow
- record

Detailed style and structural conventions belong in `DOCUMENTATION_STYLE_GUIDE.md`.

---

## 7. Preservation Rules

The preservation policy in `PROJECT_CHARTER.md` is binding.

AI assistants must preserve:

- scholarly interpretations
- bibliography
- examples
- datasets
- encoding rules
- identifiers
- database specifications

AI assistants may improve how such material is organized, introduced, linked, or made discoverable, but must not alter its substance without explicit instruction.

If a task seems to require scholarly judgment, the assistant should identify the issue and ask for human direction.

---

## 8. Terminology Handling

KRM Documentation depends on precise terminology.

Important terms include:

- Entry / 項目
- Headword / 掲出字
- Original Glosses / 注文
- Phonetic Gloss / 音注
- Semantic Gloss in Chinese / 義注
- Japanese native reading / 和訓
- Notes on Character Form / 字体注

AI assistants should not silently normalize historically or editorially meaningful variation.

Until `GLOSSARY_CONVENTIONS.md` and a project glossary exist, AI assistants should:

- preserve existing terminology
- note apparent variation when relevant
- avoid replacing Japanese terms with English approximations
- avoid replacing English terms with new alternatives without justification

Detailed glossary rules belong in `GLOSSARY_CONVENTIONS.md`.

---

## 9. Japanese and English Content

The repository contains Japanese pages, English pages, and unsuffixed pages with mixed or bilingual content.

AI assistants should not assume that:

- an English page is a complete translation of the Japanese page
- a Japanese page is more current than the English page
- unsuffixed pages are language-neutral
- bilingual content should be split or merged without instruction

Until `I18N_POLICY.md` exists, AI assistants should preserve the existing language structure unless explicitly asked to analyze or revise it.

Detailed language-version rules belong in `I18N_POLICY.md`.

---

## 10. Navigation and Links

Navigation and cross references are a major project concern.

Known current issues include:

- stale `/docs/notes/...` paths
- mismatched section links
- old section numbering assumptions
- development-only `localhost` links
- inconsistent internal path spelling

AI assistants may identify, report, and, when instructed, correct navigation issues.

Link work should preserve conceptual meaning.
Do not mechanically change links if the intended target is unclear.

Detailed link and navigation conventions belong in `DOCUMENTATION_STYLE_GUIDE.md`.

---

## 11. Standards Before Refactoring

The Roadmap requires standards before broad chapter-level refactoring.

AI assistants should not begin large-scale Documentation refactoring until the relevant standards are available or the user explicitly instructs otherwise.

The expected order is:

1. `AGENTS.md`
2. `DOCUMENTATION_STYLE_GUIDE.md`
3. `EDITORIAL_CONVENTIONS.md`
4. `GLOSSARY_CONVENTIONS.md`
5. `I18N_POLICY.md`
6. later review and maintenance conventions as needed

---

## 12. Reporting Requirements

After completing a task, AI assistants should report:

- files created or changed
- whether Documentation content was edited
- whether protected scholarly content was avoided
- verification performed
- unresolved risks or questions

If no files were changed, say so explicitly.

For review tasks, findings should be specific and grounded in file paths and line references where possible.

---

## 13. When to Ask for Human Direction

AI assistants should ask for human direction when:

- a change may affect scholarly interpretation
- a term has multiple legitimate meanings and normalization would change nuance
- a link target is unclear
- a page's document type is ambiguous and affects structure
- Japanese/English alignment would require editorial judgment
- examples, bibliography, identifiers, encoding rules, or data specifications may need alteration

AI assistants should not ask for confirmation for routine, clearly scoped structural or standards work unless the user has requested proposals only.

---

## 14. Working Principle

The guiding principle for AI work in this repository is:

Preserve the scholarship.
Clarify the Documentation.
Make structure explicit.
Keep future maintenance possible.
