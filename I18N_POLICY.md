# I18N Policy

Language Version Policy for KRM Documentation

This document defines language coverage, language-version relationships, translation status, difference tracking, and translation authority for KRM Documentation.
It applies to both human contributors and AI assistants.

This is not a translation style guide.
It is a project-wide policy for deciding which documents should exist in which languages, how language versions relate, and how translation or language adjustment should be governed.

This document is governed by `PROJECT_CHARTER.md` and follows the authority model in `EDITORIAL_CONVENTIONS.md`.

---

## 1. Purpose and Scope

This policy applies primarily to:

- `content/docs/krm/`
- `content/posts/`
- project standards that govern KRM Documentation

It defines:

- which document types should be bilingual
- which document types may be language-specific
- how Japanese and English pages correspond
- how missing, partial, legacy, or unresolved language states are recorded
- how differences between language versions are classified
- who may approve translation or language alignment decisions

This policy does not decide:

- preferred English terms
- official translations of individual terms
- readings
- romanizations
- glossary entry status

Those belong to `GLOSSARY_CONVENTIONS.md`.

---

## 2. Relationship to Other Standards

`PROJECT_CHARTER.md` is the highest-level governing document.
Its preservation policy applies to all translation and language-version work.

`AGENTS.md` defines AI behavior.
AI assistants must not silently resolve language differences, approve translations, or treat one language version as automatically authoritative.

`DOCUMENTATION_STYLE_GUIDE.md` defines page structure, headings, links, and document types.
This policy defines language coverage and language-version relationships.

`EDITORIAL_CONVENTIONS.md` defines editing authority.
Translation or language alignment that affects scholarly content, terminology concepts, data specifications, examples, citations, identifiers, or encoding rules must follow its confirmation rules.

`GLOSSARY_CONVENTIONS.md` defines how preferred terms, official English terms, provisional translations, readings, and romanizations are recorded.
This policy may refer to those categories, but does not approve them.

Future `REVIEW_CHECKLIST.md` may check whether language versions follow this policy.
Future `MAINTENANCE_CONVENTIONS.md` may define periodic language-version review and synchronization procedures.

---

## 3. Core I18N Principles

Language coverage is determined by document role.
Not every page requires full bilingual synchronization.

Core reference documentation should be bilingual where feasible.
Case studies and blog posts may be Japanese-only by policy.

Parallel Japanese and English pages are corresponding documentation pages, not necessarily literal translations.
They should share page purpose, major information, and basic structure, but may differ in explanation style and reader support.

No language version is automatically authoritative.
Japanese may be the drafting starting point in many cases, but this does not mean that the Japanese page is always latest, most accurate, or more authoritative than the English page.
The English page is not automatically a subordinate translation.

Differences should be recorded before they are resolved.
Do not automatically merge, overwrite, or synchronize language versions.

Translation must not change scholarship.
Language adjustment must preserve scholarly content, citations, transcriptions, examples, identifiers, data specifications, and encoding rules.

---

## 4. Audience

Japanese and English pages are not mechanical replacements for one another.
They are corresponding versions shaped for their primary audiences.

### Japanese

Primary audience:

- project members
- Japanese researchers
- researchers and contributors who work directly with Japanese source materials
- editors and maintainers responsible for detailed scholarly and technical documentation

Japanese pages may provide fuller specialist, source-oriented, or project-internal detail where appropriate.

### English

Primary audience:

- international researchers
- external collaborators
- researchers who need access to KRM concepts, data structures, methods, and editorial rules through English
- technical users who may not read detailed Japanese scholarly discussion

English pages may provide additional background explanation where useful for international or technical readers.

### Permitted Audience Adaptation

Audience differences may justify:

- additional background explanation in English
- more detailed specialist or source-oriented explanation in Japanese
- adjusted explanation order
- different amounts of examples or supplementary explanation
- links to different supporting pages, when the core reference relationship is preserved

Audience adaptation must not change:

- core concepts
- data specifications
- identifiers
- encoding rules
- annotation judgments
- manuscript interpretation
- scholarly claims

---

## 5. Language Coverage by Document Type

Language requirements follow document type and documentation layer.

| Document area or type | Language coverage | Notes |
| --- | --- | --- |
| Orientation | Bilingual required | Core entry points should be available in Japanese and English. |
| Concept Reference | Bilingual required | Core concepts should be accessible in both languages. |
| Data Reference | Bilingual required | File, field, and data-structure meanings should be available in both languages. |
| Rule Reference | Bilingual required | Editorial, input, encoding, and representation rules should be available in both languages. |
| Core Annotation Methodology | Bilingual required or recommended | Core method should be bilingual; highly detailed examples may be language-specific. |
| Glossary / terminology control | Bilingual required for core terms | Individual term decisions are governed by `GLOSSARY_CONVENTIONS.md`. |
| Publication and Maintenance | Bilingual recommended | Stable publication and maintenance information should be accessible in English where relevant. |
| Workflow and tool notes | Language-specific or bilingual recommended | Depends on audience and stability. |
| Records and progress pages | Language-specific allowed | Records do not automatically require translation. |
| Case studies | Japanese-only by policy | English summaries or guides may be added, but full translation is not required. |
| Blog posts | Japanese-only by policy | Blogs are not synchronized bilingual documentation. |

Stable definitions, rules, data specifications, and encoding explanations should not exist only in language-specific case studies or blog posts.
If such information appears there, it should be recorded as a candidate for Core Documentation.

---

## 6. Page Language Status

Use page language status to describe the expected language coverage of a page.

| Status | Meaning |
| --- | --- |
| `bilingual-required` | Japanese and English corresponding pages are required by policy. |
| `bilingual-recommended` | Japanese and English versions are desirable, but phased development is acceptable. |
| `language-specific` | The page may be complete in one language by policy. |
| `translation-pending` | Translation is expected but not yet available. |
| `alignment-review-needed` | Language versions exist, but their relationship needs review. |
| `legacy` | The page may reflect an earlier language or file-structure convention. |
| `unresolved` | The language status is not yet determined. |

Do not infer status mechanically from filename alone.
For example, an unsuffixed `.md` file is not automatically language-neutral, Japanese-only, legacy, or unresolved.
It must be evaluated in context.

---

## 7. Supplementary Language Availability

Supplementary language availability is separate from page language status.

A page may be Japanese-only by policy and still provide limited English support.

For example:

```text
Page language status:
Japanese-only by policy

Supplementary availability:
English summary available
```

Possible supplementary availability values include:

| Supplementary status | Meaning |
| --- | --- |
| `English summary available` | A short English summary exists. |
| `English guide available` | English guidance for navigation or use exists. |
| `English navigation available` | English links or navigation notes exist. |
| `Japanese summary available` | A short Japanese summary exists for primarily English content. |
| `no supplementary version` | No supplementary language support exists. |
| `supplementary status unresolved` | Supplementary status has not been classified. |

Supplementary status should not be over-required.
It is useful when documenting language support, not a mandatory metadata burden for every page.

Adding an English summary to a case study or blog post does not make the page `bilingual-required`.
It also does not make the section subject to full Japanese/English synchronization.

---

## 8. File Naming and Language Suffixes

Current observed patterns include:

- `.ja.md`
- `.en.md`
- unsuffixed `.md`

These patterns must be interpreted conservatively.
Existing unsuffixed files should not be mechanically classified as legacy, Japanese-only, bilingual, or language-neutral.

### Current Structure

The current file structure should be preserved unless a specific refactoring task is approved.
Existing suffix patterns are part of the current documentation state.
They should not be treated as errors by default.

### Future Naming Direction

For new Core Documentation pages:

- use `.ja.md` for Japanese pages
- use `.en.md` for English pages
- create corresponding versions when the page is `bilingual-required`

For case studies and posts:

- unsuffixed Japanese-oriented operation is acceptable
- existing suffixless pages should not be treated as incomplete solely because they lack `.ja.md`
- English summaries or guides may be added without changing the section's basic language policy

File naming policy does not decide which language version is authoritative.

---

## 9. Relationship Between Japanese and English Pages

Corresponding Japanese and English pages should share:

- page purpose
- document type
- core subject
- major information
- basic structure where practical
- compatible data specifications and rule statements
- links to equivalent or functionally similar reference pages

They do not need to be:

- sentence-by-sentence translations
- identical in length
- identical in explanation order
- identical in examples or background explanation

Allowed differences include:

- English background explanation for international readers
- fuller Japanese specialist detail
- different explanatory order
- different supporting examples
- reader-specific navigation

Not allowed without confirmation:

- conflicting data specifications
- conflicting identifier explanations
- conflicting encoding rules
- conflicting annotation categories
- changed scholarly interpretation
- changed manuscript readings or examples

---

## 10. Managing Differences Between Language Versions

Record and classify differences before resolving them.

| Difference category | Meaning |
| --- | --- |
| `expression difference` | Same meaning expressed differently. |
| `supplementary difference` | One version has additional explanation that does not conflict. |
| `update-timing difference` | One version appears to reflect a newer or older update. |
| `substantive inconsistency` | Versions may conflict in meaning or factual content. |
| `scholarly nuance difference` | Translation or wording may affect scholarly interpretation. |
| `reader-adaptation difference` | Difference appears intentional for audience needs. |
| `unresolved difference` | Difference exists but has not been classified. |

Audience adaptation is acceptable.
Contradiction in major information is not.

When a difference affects scholarly content, terminology concepts, data specifications, identifiers, examples, citations, or encoding rules, classify it as requiring confirmation.

Do not automatically change one language version because the other has changed.

---

## 11. Translation and Language Adjustment Authority

Translation and language adjustment follow the four authority levels in `EDITORIAL_CONVENTIONS.md`.

| Authority level | Translation and language work |
| --- | --- |
| Allowed | Record page language status, record corresponding page existence, fix clear ordinary prose issues, preserve existing language structure. |
| Allowed with Care | Improve readability, adjust explanation order, add short summaries or navigation notes, draft translations as provisional content. |
| Requires Confirmation | Approve Core Documentation translations, resolve substantive differences, approve wording affecting scholarly content, align data or rule statements, translate protected technical or scholarly material. |
| Prohibited Unless Explicitly Instructed | Change quotations, transcriptions, kanbun, wakun, identifiers, data values, data specifications, encoding rules, or scholarly interpretation for translation convenience. |

Requires Confirmation means confirmation from the project owner or a scholarly editor with authority over the relevant area.
An authorized technical maintainer may confirm language decisions only when the issue is limited to technical labels, data-field naming, schema-related terminology, or technical metadata.

AI or machine translation may be used as a draft tool.
Such output is provisional and not authoritative until reviewed.
It must not determine scholarly meaning or create official terminology.

---

## 12. Protected Content in Translation

The following require special care and must not be silently translated, normalized, or adjusted:

- quotations
- manuscript transcriptions
- kanbun
- wakun
- source titles
- personal names
- bibliography
- citations
- identifiers
- data values
- file names
- column names
- encoding rules
- database specifications
- manuscript readings
- annotation judgments

If translation may change the meaning of protected content, seek confirmation before editing.

---

## 13. Japanese Terms, English Terms, Reading, and Romanization

English pages may retain Japanese terms when the Japanese term is conceptually important.
Japanese pages may include English terms where useful for data reference, terminology alignment, or international readability.

Reading and romanization may be used as reader aids.
They do not replace the Japanese term.

An English rendering may be:

- explanatory
- provisional
- source-specific
- official

Only `GLOSSARY_CONVENTIONS.md` governs whether an English term is preferred, official, provisional, deprecated, or unresolved.
Do not decide official English terms in this policy or in ordinary translation work.

---

## 14. Case Studies

`content/docs/krm/08-case-studies/` is Japanese-only by policy unless explicitly reclassified.

Default status:

```text
Page language status:
Japanese-only by policy
```

This does not mean unfinished.
It does not mean translation pending.

Optional supplementary elements may include:

- short English summary
- English navigation note
- related bilingual Core Documentation links
- English terminology references

A full English translation is not required.

If an individual case study receives an English version, this does not automatically change the language policy of `08-case-studies/` as a whole.
The section remains language-specific by policy unless the project explicitly changes that policy.

---

## 15. Blog Posts

`content/posts/` is Japanese-only by policy unless explicitly reclassified.

Blog posts are not part of Japanese/English synchronization work.

English summaries or English guidance may be added to individual posts where useful.
This does not make the blog bilingual content as a whole.

Blog posts must not be the only location for stable:

- definitions
- editorial rules
- data specifications
- encoding rules
- identifier rules
- annotation methodology

If a blog post contains information that should be reused as stable documentation, record it as a candidate for Core Documentation.

---

## 16. Stable Information in Language-Specific Content

Language-specific content may contain valuable observations, examples, or exploratory notes.
However, stable reference information should live in Core Documentation.

When stable information appears in a case study or blog post:

- do not automatically rewrite the case study or post
- identify the stable information
- record the relevant source page
- propose or track it as a candidate for Core Documentation
- preserve the original context

Moving or rewriting such information may require confirmation under `EDITORIAL_CONVENTIONS.md`.

---

## 17. Metadata and Tracking

Language state and correspondence may be tracked through:

- front matter fields
- a language-status inventory
- page-to-page correspondence tables
- issue records
- review notes

This policy does not require a specific implementation yet.

Useful tracking information includes:

- page language status
- supplementary language availability
- corresponding page path
- difference category
- review status
- reviewer or approver
- last reviewed date
- unresolved questions

Detailed review and maintenance processes belong to future `REVIEW_CHECKLIST.md` and `MAINTENANCE_CONVENTIONS.md`.

---

## 18. Boundaries

This policy defines language operation and language-version governance.

It does not:

- translate existing pages
- classify every existing unsuffixed page
- decide official English terms
- decide romanization
- create a bilingual maintenance schedule
- provide a full acceptance checklist

Use:

- `DOCUMENTATION_STYLE_GUIDE.md` for page structure and linking style
- `EDITORIAL_CONVENTIONS.md` for authority boundaries
- `GLOSSARY_CONVENTIONS.md` for term status, official translations, readings, and romanization
- future `REVIEW_CHECKLIST.md` for acceptance checks
- future `MAINTENANCE_CONVENTIONS.md` for recurring language review

---

## 19. Summary Rules

Core reference documentation should be bilingual where feasible.

Case studies and blog posts may be Japanese-only by policy.

English summaries may support language-specific pages without making them bilingual-required.

Japanese and English pages are corresponding documentation versions, not automatic source and translation.

Differences should be recorded before they are resolved.

Translation must not change scholarly content, evidence, identifiers, data specifications, or encoding rules.
