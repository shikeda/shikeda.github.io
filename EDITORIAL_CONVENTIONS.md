# Editorial Conventions

Editing Authority and Boundaries for KRM Documentation

This document defines the editorial rules for KRM Documentation.
It applies to both human contributors and AI assistants.

Its purpose is to distinguish documentation editing from scholarly judgment, so that the Documentation can be clarified and maintained without silently changing scholarly content.

This document is governed by `PROJECT_CHARTER.md`.

---

## 1. Purpose and Scope

These conventions apply primarily to:

- `content/docs/krm/`
- project standards that govern KRM Documentation
- future documentation refactoring work

They define:

- what kinds of changes are ordinary documentation editing
- what kinds of changes require care
- what kinds of changes require confirmation
- what kinds of changes are prohibited unless explicitly instructed

These conventions do not define page style, glossary format, or language policy in detail.
Those topics belong to:

- `DOCUMENTATION_STYLE_GUIDE.md`
- `GLOSSARY_CONVENTIONS.md`
- `I18N_POLICY.md`

AI-specific behavior belongs to:

- `AGENTS.md`

---

## 2. Relationship to Other Standards

`PROJECT_CHARTER.md` is the highest-level governing document.
Its preservation policy is binding.

`AGENTS.md` defines how AI assistants should behave when applying these conventions.

`DOCUMENTATION_STYLE_GUIDE.md` defines how pages should be structured, written, and linked.

`GLOSSARY_CONVENTIONS.md` will define how terms are recorded and maintained.

`I18N_POLICY.md` will define how Japanese, English, and bilingual content are handled.

Future `REVIEW_CHECKLIST.md` may turn these conventions into review questions.
Future `MAINTENANCE_CONVENTIONS.md` may define periodic maintenance routines.
Those later documents should not replace the editorial boundaries defined here.

---

## 3. Core Editorial Principle

Documentation editing improves how existing knowledge is presented.
Scholarly judgment changes the knowledge itself.

Documentation editing may:

- clarify structure
- improve navigation
- organize existing explanations
- make assumptions explicit
- improve readability
- link related material
- distinguish document types

Scholarly judgment includes changes to:

- manuscript interpretation
- textual readings
- annotation judgments
- source evaluation
- examples as evidence
- bibliographic claims
- terminology concepts
- data specifications
- identifiers or encoding rules

Editors may reorganize, introduce, connect, and clarify existing content.
They must not silently change its scholarly substance.

---

## 4. Authority Levels

All documentation changes should be classified using four authority levels.

### Allowed

The change is within normal documentation editing.
It may be made without special confirmation.

### Allowed with Care

The change is probably editorial, but could affect meaning if done poorly.
It may be made when the editor can preserve the original meaning with confidence.

### Requires Confirmation

The change may affect scholarly content, terminology, data specifications, or interpretation.
It requires confirmation from the project owner or a scholarly editor with authority over the relevant area.

### Prohibited Unless Explicitly Instructed

The change must not be made unless the user or project owner explicitly instructs it.
This category includes changes that alter protected scholarly content.

---

## 5. Change Categories

Use the nature of the change, not only the object being edited, to classify authority.

### Structural Editing

Changes to organization, headings, section order, and page framing.

Usually:

- Allowed
- Allowed with Care for large reorganizations

Requires confirmation when the restructuring changes the apparent meaning, priority, or scope of scholarly content.

### Stylistic Editing

Changes to readability, grammar, paragraphing, and wording.

Usually:

- Allowed for ordinary explanatory prose
- Allowed with Care when wording is close to terminology, citation, translation, or interpretation

Requires confirmation when wording changes the meaning of a claim.

### Navigational Editing

Changes to internal links, section indexes, and cross references.

Usually:

- Allowed
- Allowed with Care when the intended target is uncertain

Requires confirmation when a link implies a scholarly relationship not already supported by the Documentation.

### Terminology Editing

Changes to terms, labels, translations, romanizations, or preferred forms.

Usually:

- Allowed with Care for local formatting or clearly established usage
- Requires Confirmation for preferred terms, concept boundaries, or bilingual equivalence

Prohibited unless explicitly instructed when the change alters a concept.

### Evidence and Example Handling

Changes to examples, transcriptions, cited passages, images, or evidence.

Usually:

- Allowed for surrounding explanation or presentation
- Requires Confirmation for changing selection, wording, interpretation, or evidentiary framing

Prohibited unless explicitly instructed when changing the content of the evidence itself.

### Data and Specification Handling

Changes to data-file names, column names, identifiers, encoding rules, schemas, or database relationships.

Usually:

- Requires Confirmation for explanatory changes that could affect interpretation
- Prohibited unless explicitly instructed for changes to the specification itself

---

## 6. Editorial Authority Matrix

| Documentation element | Allowed | Allowed with Care | Requires Confirmation | Prohibited Unless Explicitly Instructed |
| --- | --- | --- | --- | --- |
| Page title and H1 | Align title and H1 when meaning is unchanged | Clarify a vague title using existing page scope | Rename a page in a way that changes its scope or classification | Rename a page to assert a new scholarly interpretation |
| Headings | Improve heading clarity, fix hierarchy, remove duplicate heading levels | Rename headings near technical or scholarly terminology | Change headings that redefine categories or analytical scope | Replace established category names with new concepts |
| Opening summaries | Add a brief page-purpose statement based on existing content | Summarize a dense page without changing emphasis | Add a summary that interprets evidence or prioritizes scholarly claims | Present a new conclusion not already supported by the page |
| Section order | Move sections to improve readability when meaning is unaffected | Reorder dense sections while preserving conceptual dependency | Reorder material in a way that changes argumentative sequence | Reorder evidence to support a new interpretation |
| Paragraphing | Split long paragraphs, remove accidental repetition, improve flow | Rewrite dense prose near technical or scholarly claims | Condense prose where nuance may be lost | Remove qualifications or uncertainty from scholarly claims |
| Ordinary typos | Correct clear typographical errors in ordinary prose | Correct words near technical terms when meaning is obvious | Correct a possible error in a scholarly term, transcription, title, citation, or data value | Silently change readings, cited text, identifiers, or encoded values |
| Internal links | Fix stale links when the intended target is clear | Replace old paths when several plausible targets exist | Add links that imply a new conceptual or scholarly relationship | Link evidence to a claim in a way that changes interpretation |
| External links | Fix formatting or add access notes without changing citation meaning | Mark a link as broken or updated when clearly verified | Replace a cited source URL with a different source | Remove or substitute bibliographic evidence |
| Section index pages | Add child-page descriptions and reading guidance | Reclassify a child page by document type | Move a page between conceptual categories | Reframe a research page as normative reference without review |
| Tables | Reformat tables for readability without changing values | Convert prose to a table when all values are preserved | Rename columns or labels with possible semantic impact | Change table values, counts, data fields, or specifications |
| Examples | Improve surrounding explanation or formatting | Add labels that identify what an example illustrates | Change which examples are used or how they are interpreted | Change example text, transcription, reading, or evidentiary content |
| Figures and images | Improve captions or references when meaning is unchanged | Reposition figures to support page structure | Replace an image or diagram that carries scholarly or data-model meaning | Alter image content or diagram semantics |
| Bibliography | Reformat bibliography without changing entries | Normalize punctuation or ordering if bibliographic meaning is preserved | Correct author, title, date, publication data, or citation scope | Remove, replace, or reinterpret bibliographic evidence |
| Citations and quoted text | Improve citation placement or surrounding prose | Adjust citation formatting | Change quotation, citation target, or evidentiary relation | Alter quoted/cited text without explicit instruction |
| Terminology | Preserve existing terms and mark variation for glossary review | Align local wording with established project terminology | Choose or change preferred terms, translations, readings, or romanizations | Redefine concepts or erase meaningful variation |
| Japanese/English alignment | Note mismatch or preserve current structure | Make minor language improvements that do not change meaning | Harmonize content between Japanese and English pages | Assume one language version overrides the other |
| File names and paths | Reference existing paths accurately | Propose path changes as part of architecture work | Rename files or directories | Change paths in ways that break published URLs without instruction |
| Front matter | Correct metadata formatting when meaning is unchanged | Align title or weight with existing structure | Change ordering that affects navigation meaning | Hide, remove, or repurpose pages without instruction |
| Data file names | Format names such as `krm_main` consistently | Clarify prose around existing file names | Change explanation of what a file represents | Rename or redefine data files |
| Column names | Format existing column names consistently | Clarify surrounding prose without changing meaning | Change a column explanation | Rename, remove, merge, or reinterpret columns |
| Identifiers | Format identifiers consistently | Explain identifier examples using existing rules | Correct a suspected identifier error | Change identifier values or ID rules |
| Encoding rules | Link to or organize existing encoding explanations | Clarify prose if the rule is unchanged | Restate a rule where ambiguity exists | Change the rule or encoded representation |
| Annotation categories | Improve navigation to existing category explanations | Clarify wording using existing definitions | Change category boundaries or labels | Reclassify annotation types |
| Manuscript readings | Improve surrounding explanation without touching the reading | Flag possible ambiguity | Correct or reinterpret a reading | Change transcription or reading |
| Progress records | Clarify that a page is a record | Add context without changing status | Update status or counts | Rewrite historical records as current facts without review |

---

## 7. Allowed Editing

The following changes are normally allowed:

- fixing broken internal links when the intended target is clear
- improving heading hierarchy without changing meaning
- adding short page-purpose introductions based on existing content
- improving section index navigation
- splitting long paragraphs for readability
- fixing clear typos in ordinary prose
- formatting Markdown tables, lists, and code blocks
- adding links to already established related pages
- clarifying whether a page is reference, example, workflow, or record

Allowed edits must still preserve scholarly content.

---

## 8. Editing Allowed with Care

The following changes are allowed only when the editor can preserve meaning with confidence:

- rewriting dense prose near technical explanation
- converting prose into tables
- moving examples closer to related rules
- adding explanatory labels to examples
- reordering sections within a page
- normalizing visible formatting of terms
- updating external-link status notes
- clarifying page scope when the scope is already evident

When meaning may change, move the change to Requires Confirmation.

---

## 9. Changes Requiring Confirmation

Requires Confirmation means confirmation from the project owner or a scholarly editor with authority over the relevant area.

The following changes require confirmation:

- changing a preferred term
- changing a Japanese/English term correspondence
- changing the conceptual scope of a term
- changing the explanation of a data file or column
- changing the interpretation of an example
- changing which examples are used
- correcting a possible error in a transcription, citation, title, name, date, identifier, or data value
- harmonizing Japanese and English pages when the versions differ in substance
- changing annotation category descriptions
- updating progress status or numerical counts
- changing bibliography metadata
- replacing external scholarly sources

When confirmation is needed, preserve the original wording and record the issue clearly.

---

## 10. Prohibited Changes Without Explicit Instruction

The following changes are prohibited unless explicitly instructed:

- changing scholarly interpretations
- changing manuscript readings
- changing transcriptions
- changing examples as evidence
- changing bibliography entries
- changing citation content
- changing datasets
- changing identifiers
- changing encoding rules
- changing database specifications
- changing column names or data-file semantics
- changing annotation judgments
- removing evidence or qualifications
- presenting new research conclusions

These restrictions apply even when the proposed change appears likely to be correct.

---

## 11. Examples, Evidence, Bibliography, and Citations

Examples, evidence, bibliography, and citations are protected content.

Editors may improve:

- placement
- captions
- surrounding explanation
- link formatting
- table formatting
- readability around the material

Editors must not silently change:

- the text of an example
- a cited passage
- a transcription
- a bibliographic entry
- a source relationship
- the interpretation attached to evidence

If an apparent error appears in protected material, record it as an issue requiring confirmation.
Do not correct it as an ordinary typo.

---

## 12. Ordinary Typos vs Protected Errors

Clear typographical errors in ordinary explanatory prose may be corrected.

Examples of ordinary prose include:

- navigation descriptions
- page-purpose summaries
- non-technical transitional sentences
- repeated words caused by editing

Possible errors are not ordinary typos when they occur in:

- scholarly terms
- manuscript transcriptions
- quotations
- bibliographic entries
- personal names
- source titles
- dates
- identifiers
- file names
- column names
- encoded values
- data specifications
- annotation labels

In those cases, treat the issue as Requires Confirmation unless explicit instruction has been given.

---

## 13. Terminology

Terminology should be preserved unless there is a clear project standard.

Editors may:

- preserve local terminology
- identify variation
- link to relevant terminology explanations
- flag candidates for glossary review

Editors should not:

- silently replace established Japanese terms
- invent English equivalents
- remove meaningful variation
- change the conceptual boundary of a term

Detailed glossary entry rules belong to `GLOSSARY_CONVENTIONS.md`.

---

## 14. Japanese and English Differences

Japanese and English pages should not be assumed to be exact equivalents.

Editors may:

- identify differences
- improve structure within one language version
- preserve existing language status
- flag alignment issues

Editors should not:

- silently harmonize Japanese and English content
- assume either language version is authoritative by default
- translate protected scholarly content without instruction
- remove bilingual material solely for consistency

Detailed language policy belongs to `I18N_POLICY.md`.

---

## 15. Data and Specifications

Data and specification material must be handled conservatively.

Protected items include:

- data file names
- column names
- identifiers
- encoding rules
- schema explanations
- version-sensitive specifications
- database relationships
- field meanings

Editors may improve presentation around these items.
They must not change the meaning of the specification.

If a specification appears outdated or inconsistent, flag the issue for confirmation.

---

## 16. Uncertainty and Escalation

When uncertain, do not rewrite.

Use this order:

1. Preserve the original content.
2. Identify the affected file or section.
3. State the uncertainty.
4. Classify the issue as Requires Confirmation.
5. Ask the project owner or relevant scholarly editor for direction.

Do not resolve uncertainty by choosing the wording that seems most likely.

---

## 17. Relationship to Review and Maintenance

This document defines editorial authority and boundaries.

It does not provide a full acceptance checklist.
That belongs to a future `REVIEW_CHECKLIST.md`.

It does not define recurring maintenance schedules or procedures.
That belongs to a future `MAINTENANCE_CONVENTIONS.md`.

Review and maintenance documents should apply these conventions rather than duplicate them.

---

## 18. Summary Rule

If a change improves presentation without changing scholarly substance, it is usually documentation editing.

If a change affects interpretation, evidence, terminology concepts, data specifications, identifiers, or encoded representation, it requires confirmation or explicit instruction.
