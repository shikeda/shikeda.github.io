# Glossary Conventions

Terminology Management Standards for KRM Documentation

This document defines how terminology is recorded, referenced, and maintained in KRM Documentation.
It applies to both human contributors and AI assistants.

The Glossary is not a place to invent new meanings.
It is a control and reference layer for recording term status, evidence, variants, relationships, and source pages.

This document is governed by `PROJECT_CHARTER.md` and follows the editorial authority model in `EDITORIAL_CONVENTIONS.md`.

---

## 1. Purpose and Scope

These conventions apply to terminology work across KRM Documentation, primarily under:

- `content/docs/krm/`

They define:

- how terms should be recorded
- how term status should be represented
- how variants and unresolved differences should be preserved
- how glossary entries should relate to reference pages
- which terminology actions require confirmation

These conventions do not define:

- full page style
- page translation policy
- AI behavior outside terminology work
- periodic maintenance schedules
- review checklist details

Those topics belong to:

- `DOCUMENTATION_STYLE_GUIDE.md`
- `I18N_POLICY.md`
- `AGENTS.md`
- future `MAINTENANCE_CONVENTIONS.md`
- future `REVIEW_CHECKLIST.md`

---

## 2. Relationship to Other Standards

`PROJECT_CHARTER.md` provides the highest-level preservation policy.
Terminology work must not silently change scholarly interpretation, examples, datasets, encoding rules, identifiers, or database specifications.

`AGENTS.md` defines AI behavior.
AI assistants may collect, record, and flag terminology information, but must not decide preferred terms, official translations, or deprecated terms without confirmation.

`DOCUMENTATION_STYLE_GUIDE.md` defines how glossary pages and cross references should be presented as documentation.

`EDITORIAL_CONVENTIONS.md` defines editorial authority levels.
This document applies those levels specifically to terminology work.

`I18N_POLICY.md` will define Japanese/English page and translation policy.
This document records term correspondences, but does not govern full page translation or language-version operation.

Future `REVIEW_CHECKLIST.md` may check whether glossary entries follow these conventions.
Future `MAINTENANCE_CONVENTIONS.md` may define periodic terminology review and update routines.

---

## 3. Core Principle

Glossary management records terminology evidence.
Scholarly judgment determines the meaning, authority, and conceptual boundaries of terms.

The Glossary may record:

- existing terms
- source pages
- definition sources
- variants
- historical usage
- source-specific usage
- provisional translations
- unresolved conflicts
- related terms
- related data fields

The Glossary must not silently decide:

- new definitions
- preferred terms
- official English terms
- deprecated terms
- concept boundaries
- which conflicting definition is correct

---

## 4. Descriptive and Normative Functions

The Glossary has both descriptive and normative functions.
These must be kept distinct.

### Descriptive Function

The descriptive function records how terminology is already used.

It may include:

- terms found in existing pages
- variants found in different pages
- definitions already present in the Documentation
- source-specific usage
- historical usage
- provisional translation candidates
- unresolved differences

Descriptive records do not make a term preferred.

### Normative Function

The normative function records approved terminology decisions.

It may include:

- preferred terms
- accepted variants
- deprecated terms
- official English terms
- approved definitions

Normative status requires confirmation from the project owner or a scholarly editor with authority over the relevant area.
For technical terminology limited to data-field naming or schema-related usage, confirmation may come from an authorized technical maintainer.

Preferred terms and official English terms must not be decided by mechanically counting existing usage.

---

## 5. Terminology Status System

Glossary entries and individual term forms may carry status.

Status may apply to:

- the entry as a whole
- a Japanese form
- an English form
- a reading
- a romanization
- a variant
- a translation candidate
- a deprecated form

When the status does not apply to the whole entry, state which form or field it applies to.

### Core Status Values

Use the following status values.

`preferred`

The approved standard term for project use.
Requires confirmation.

`accepted variant`

A permitted variant that may be used in defined contexts.
Requires confirmation unless the acceptance is already explicit in a governing or reference document.

`provisional`

A recorded term, definition summary, translation, or relation that has not been approved.
Use this status actively when evidence exists but authority has not been established.

`source-specific`

A term or form used in a specific source, page, dataset, field, or scholarly context.
It should not be automatically generalized across the Documentation.

`historical`

A term or form used in earlier documentation, earlier specifications, older scholarship, or historical explanation.
Historical usage should be preserved when relevant.

`deprecated`

A term or form that should generally not be used in new project prose.
Requires confirmation.
Deprecated terms may still appear in quotations, historical explanations, examples, or source-specific contexts.

`unresolved`

A term, definition, translation, or relationship where multiple uses or interpretations exist and no decision has been made.
Use this status instead of forcing premature consistency.

### Optional Labels

Optional labels may be used when helpful:

- `translation-candidate`
- `needs-review`
- `data-field`
- `schema-related`
- `annotation-category`
- `manuscript-term`
- `page-local`

Optional labels should clarify context.
They should not replace the core status values.

---

## 6. Term Entry Fields

Glossary entries should remain usable as a reference layer.
Do not overload them with full scholarly discussion.

### Required Fields

Each glossary entry should include:

- `term_id`
- `status`
- `short definition`
- `source pages`
- `definition source`
- `notes`

### Conditional Fields

Include these when applicable:

- `Japanese term`
- `English term`
- `reading`
- `romanization`
- `variants`
- `historical forms`
- `deprecated forms`
- `source-specific usage`
- `provisional translations`
- `unresolved issues`
- `related terms`
- `related data fields`
- `related reference pages`
- `approval status`
- `approved by`
- `last reviewed`

Japanese, English, reading, and romanization fields are conditional.
They should be recorded when they are relevant and supported by source pages or editorial decision.

### Source Pages and Definition Source

`source pages` identify where the term is used.

`definition source` identifies where the definition or explanation comes from.

These fields are central.
A glossary entry without source evidence should normally be treated as `provisional`.

---

## 7. Japanese, English, Reading, and Romanization

Japanese and English terminology should be linked, not forced into one-to-one equivalence.

Allowed relationships include:

- one Japanese term with multiple English renderings
- one English term corresponding to multiple Japanese terms
- a Japanese term with no approved English term
- an English label used provisionally
- a romanization used only as a reading aid
- a source-specific English rendering

Romanization is a reference aid.
It does not replace the Japanese term.

An English term may be recorded as a provisional translation.
It becomes an official English term only after confirmation.

Full language-version policy belongs to `I18N_POLICY.md`.

---

## 8. Recording Variation and Conflict

Do not automatically normalize terminology variation.
Record it first.

When multiple forms or definitions appear, classify the difference where possible:

- spelling or orthographic variation
- reading variation
- romanization variation
- translation variation
- historical usage
- source-specific usage
- page-local usage
- context-dependent usage
- conceptual difference
- unresolved inconsistency

If the difference affects meaning or concept boundaries, classify the issue as `unresolved` and seek confirmation before standardizing.

Variation is part of the documentation evidence.
It should be preserved unless an authorized decision resolves it.

---

## 9. Glossary and Reference Pages

The Glossary should not be the only place where complex concepts are explained.

Responsibilities:

| Document type | Responsibility |
| --- | --- |
| Glossary Entry | Short definition, status, variants, source pages, related terms, and links |
| Concept Reference | Full conceptual explanation and relationships |
| Data Reference | File, field, and structured data meaning |
| Rule Reference | Operational editorial, input, encoding, or representation rule |
| Methodology | Analytical principles and evidence categories |

Glossary entries should point readers to the appropriate full explanation.
They should not replace that explanation.

---

## 10. Editing and Approval Authority

Terminology work follows the four authority levels in `EDITORIAL_CONVENTIONS.md`.

### Allowed

The following are normally allowed:

- record a term found in an existing page
- add source page references
- add definition source references
- mark a new entry as `provisional`
- mark an unresolved difference as `unresolved`
- record variants as observed usage
- improve formatting without changing meaning

### Allowed with Care

The following are allowed when meaning is preserved:

- summarize an existing definition
- group observed variants
- add related terms
- add related data fields
- identify source-specific usage
- record a provisional translation as provisional

### Requires Confirmation

The following require confirmation from the project owner or an authorized scholarly editor:

- assign `preferred` status
- assign `accepted variant` status
- assign `deprecated` status
- approve an official English term
- approve a definition as project-standard
- resolve an `unresolved` conflict
- change a term's conceptual boundary
- change the relationship between Japanese and English terms when meaning is affected

An authorized technical maintainer may confirm terminology decisions only when the decision is limited to data-field naming, schema-related terminology, or technical metadata.

### Prohibited Unless Explicitly Instructed

The following must not be done without explicit instruction:

- invent a new definition
- replace existing terminology across pages for consistency alone
- treat a provisional translation as official
- treat a source-specific term as a project-wide term
- erase meaningful variation
- alter quotations, transcriptions, identifiers, data fields, or specifications for terminology normalization

---

## 11. Adding, Revising, and Deprecating Terms

New glossary entries should normally begin as `provisional` unless they record an already approved term.

When adding a term:

- record the source pages
- identify the definition source
- use conditional language when status is uncertain
- record variants without choosing among them
- use `unresolved` for conflicts

When revising a term:

- preserve prior evidence
- distinguish formatting changes from meaning changes
- update related references when needed
- seek confirmation for status or definition changes

When deprecating a term:

- confirmation is required
- the historical or source-specific use should still be recorded
- related pages should not be rewritten mechanically

Recurring review schedules belong to future `MAINTENANCE_CONVENTIONS.md`.

---

## 12. Cross References

Glossary entries should support navigation across the Documentation.

Useful references include:

- source pages where the term is used
- definition source pages
- full Concept Reference pages
- related Data Reference pages
- related Rule Reference pages
- related Methodology pages
- related data fields
- unresolved conflict locations

Cross references should show why a page is related.
Do not add links only because two pages contain the same word.

Link style and page presentation should follow `DOCUMENTATION_STYLE_GUIDE.md`.

---

## 13. Minimal Template

Use the minimal template when recording a term quickly or when evidence is limited.

```markdown
## [Term Label]

term_id:
status:
short definition:
source pages:
definition source:
notes:
```

If the term is not approved, use `provisional` or `unresolved`.

---

## 14. Standard Template

Use the standard template for stable or frequently referenced terms.

```markdown
## [Term Label]

term_id:
status:

Japanese term:
English term:
reading:
romanization:

short definition:
definition source:
source pages:

variants:
historical forms:
deprecated forms:
source-specific usage:
provisional translations:
unresolved issues:

related terms:
related data fields:
related reference pages:

approval status:
approved by:
last reviewed:

notes:
```

Fields that do not apply may be omitted.
Do not fill fields by guessing.

---

## 15. Provisional Entry Skeleton

Use this skeleton when a term has been observed but not yet reviewed.
This is a neutral example and does not define a real KRM term.

```markdown
## [Observed Term]

term_id: [to be assigned]
status: provisional

Japanese term: [record if present in source]
English term: [record if present in source]
reading: [record if present or established]
romanization: [record if present or established]

short definition: [brief summary of existing source wording, or "not yet defined"]
definition source: [page or section where definition appears, if any]
source pages:
- [path or page reference]

variants:
- [observed variant, with source if known]

provisional translations:
- [translation candidate, if explicitly provisional]

unresolved issues:
- [question or conflict to be reviewed]

related terms:
- [related term, if known]

related data fields:
- [field name, if relevant]

notes:
- This entry records observed usage only.
- No preferred term or official translation has been approved.
```

---

## 16. Boundaries

This document defines terminology management standards.

It does not:

- create a glossary
- decide preferred KRM terms
- approve English translations
- resolve terminology conflicts
- define full translation policy
- define maintenance schedules
- provide a full review checklist

Use:

- `EDITORIAL_CONVENTIONS.md` for editorial authority boundaries
- `DOCUMENTATION_STYLE_GUIDE.md` for glossary page structure and links
- `I18N_POLICY.md` for language-version policy
- future `REVIEW_CHECKLIST.md` for acceptance checks
- future `MAINTENANCE_CONVENTIONS.md` for periodic terminology review

---

## 17. Summary Rule

Record terminology evidence before standardizing terminology.

Use `provisional` and `unresolved` to preserve uncertainty.
Do not convert observed usage into preferred terminology without authorized confirmation.
