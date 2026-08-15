# Documentation Style Guide

Operational Style Standards for KRM Documentation

This guide defines how KRM Documentation pages should be structured, written, linked, and organized.
It is a practical day-to-day reference for documentation work.

This guide is governed by `PROJECT_CHARTER.md` and should be read together with:

- `AGENTS.md`
- `DOCUMENTATION_BLUEPRINT.md`
- `ROADMAP.md`
- future `EDITORIAL_CONVENTIONS.md`
- future `GLOSSARY_CONVENTIONS.md`
- future `I18N_POLICY.md`

---

## 1. Purpose and Scope

This Style Guide applies primarily to:

- `content/docs/krm/`

Its purpose is to make the Documentation:

- easier to navigate
- easier to maintain
- clearer for multiple audiences
- consistent across chapters
- aligned with the target architecture in `DOCUMENTATION_BLUEPRINT.md`

This guide covers:

- document layers
- document types
- page structure
- section index pages
- headings and titles
- navigation and cross references
- tables, lists, examples, and figures
- handling dense pages
- core and supporting material relationships
- basic front matter expectations

This guide does not define:

- what scholarly content may be changed
- how glossary entries are formally maintained
- how Japanese and English versions should be governed in detail
- AI behavior outside documentation style

Those topics belong to:

- `EDITORIAL_CONVENTIONS.md`
- `GLOSSARY_CONVENTIONS.md`
- `I18N_POLICY.md`
- `AGENTS.md`

---

## 2. Governing Principle

Every page should make its role clear.

A reader should be able to tell:

- what the page explains
- whether it is reference, rule, methodology, example, workflow, or record
- what knowledge is assumed
- where to go next

Prefer:

- clear structure over exhaustive explanation
- stable terminology over local variation
- self-contained pages over hidden dependencies
- explicit cross references over implied relationships
- examples that support definitions, not replace them

---

## 3. Documentation Layers

KRM Documentation should follow the layered architecture defined in `DOCUMENTATION_BLUEPRINT.md`.

The main layers are:

- Orientation
- Conceptual Reference
- Data Reference
- Editorial and Encoding Rules
- Annotation Methodology
- Publication and Maintenance
- Supporting Materials and Applications

Use these layers as a classification tool when creating or revising pages.

### Orientation

Use for pages that introduce KRM, define scope, identify the resource, or guide new readers.

Should include:

- what KRM is
- what the section covers
- who should read it
- where to go next

Should avoid:

- detailed data-file specifications
- long methodological discussions
- detailed case studies

### Conceptual Reference

Use for stable concepts and relationships.

Should include:

- definitions
- diagrams where useful
- relationships among concepts
- links to related data and rules

Should avoid:

- workflow instructions
- progress notes
- case-specific arguments as the only explanation of a concept

### Data Reference

Use for data files, fields, tables, and structured representations.

Should include:

- file purpose
- format
- column or field descriptions
- relationship to other files
- version-sensitive notes where needed

Should avoid:

- redefining core concepts locally when a concept page or glossary entry exists
- mixing data specification with extended research discussion

### Editorial and Encoding Rules

Use for rules about transcription, input, encoding, identifiers, and representation.

Should include:

- rule statements
- scope
- examples
- exceptions
- links to relevant data fields

Should avoid:

- altering protected scholarly interpretations
- making rules only implicit through examples

### Annotation Methodology

Use for annotation principles, evidence categories, and analytical boundaries.

Should include:

- annotation scope
- categories of annotation
- evidence types
- examples that demonstrate method

Should avoid:

- burying general methodology inside long examples
- presenting records or progress summaries as methodology

### Publication and Maintenance

Use for publication locations, update practices, and maintenance information.

Should include:

- where data or documentation is published
- what changes over time
- what is stable
- maintenance responsibilities where known

Should avoid:

- redefining data concepts
- mixing current status with normative rules without distinction

### Supporting Materials and Applications

Use for case studies, progress records, tool notes, and applied examples.

Should include:

- clear connection to relevant reference pages
- context for the use case or record
- indication when content is time-sensitive

Should avoid:

- being the only place where a core term, rule, or data structure is defined

---

## 4. Document Types

Every page should have a recognizable document type.

The main document types are:

- Overview
- Concept Reference
- Data Reference
- Rule Reference
- Methodology
- Example or Case
- Workflow
- Record

### Overview

Purpose:

- introduce a section or major topic
- guide readers to child pages

Recommended structure:

- short opening summary
- section scope
- reader guidance
- child-page list with brief descriptions
- related sections

### Concept Reference

Purpose:

- define a concept or relationship

Recommended structure:

- definition
- scope and boundaries
- related concepts
- examples, if useful
- links to data or rules

### Data Reference

Purpose:

- document a file, table, or field group

Recommended structure:

- file purpose
- format
- column or field table
- relationship to other files
- version notes
- related rules

### Rule Reference

Purpose:

- explain an editorial, input, encoding, or representation rule

Recommended structure:

- rule statement
- when the rule applies
- examples
- exceptions
- related data fields

### Methodology

Purpose:

- explain principles and analytical categories

Recommended structure:

- scope of method
- categories
- evidence used
- relationship to data and annotation fields
- examples

### Example or Case

Purpose:

- demonstrate a concept, rule, or method

Recommended structure:

- case context
- relevant data or passage
- explanation
- links back to the governing concept, rule, or methodology

### Workflow

Purpose:

- explain production, tool, publication, or maintenance procedures

Recommended structure:

- purpose
- prerequisites
- steps or workflow explanation
- outputs
- related reference pages

### Record

Purpose:

- preserve time-sensitive project state

Recommended structure:

- date or status context where relevant
- what is being recorded
- relationship to stable documentation

Records should not define core concepts or rules.

---

## 5. Page Structure

Each page should begin by telling the reader what the page is for.

Recommended baseline structure:

1. Title
2. Short opening paragraph
3. Scope or purpose
4. Main content
5. Examples, tables, or figures where needed
6. Related pages or next steps

For short pages, this structure can be lightweight.
For long pages, it should be explicit.

Avoid opening a page with:

- unexplained examples
- long historical detail before the page purpose
- lists of links without context
- temporary editorial notes

Each page should be understandable on its own, while still linking to related pages.

---

## 6. Section Index Pages

Section index pages are navigation guides.
They should not be only link lists.

Each `_index.*.md` page should ideally include:

- section purpose
- intended readers
- what the section contains
- recommended reading order
- child pages with one-line descriptions
- related sections

For example, an index page for a data-reference section should help readers understand:

- what data files are documented
- which file is the starting point
- how file-specific pages relate to the conceptual model

For supporting sections, the index should make the document status clear.
For example:

- progress records
- case studies
- workflow notes
- tools or typesetting support

---

## 7. Titles and Headings

Titles and headings should help readers scan the page.

General rules:

- The front matter `title` and H1 should describe the same topic.
- H1 should identify the page topic.
- H2 should mark major conceptual sections.
- H3 should be used for examples, subtypes, or local detail.
- Avoid making every paragraph a heading.
- Avoid vague headings such as `Notes`, `Details`, or `Other` unless the scope is clear.
- Avoid temporary headings that describe editing status rather than content.

For data pages:

- use file names such as `krm_main` or `krm_notes` when the page is a file reference
- use human-readable headings for field explanations

For concept pages:

- use stable terms in headings
- avoid introducing alternate terminology in headings unless the page explains that variation

Japanese/English heading alignment is governed in detail by `I18N_POLICY.md`.

---

## 8. Navigation and Cross References

Links should help readers understand relationships.

Use internal links for:

- prerequisite concepts
- related rules
- data-file representations
- examples
- glossary terms
- related sections

Do not introduce:

- stale `/docs/notes/...` paths
- development-only `localhost` links
- links to old section numbers
- links whose target is uncertain

When the intended target is unclear, flag the issue rather than guessing.

Cross references should be meaningful.
For example:

- a data field should link to the concept or rule that explains it
- an example should link back to the rule it illustrates
- a methodology page should link to representative examples
- a glossary entry should link to pages where the term is defined or operationally important

Prefer section-level links when the exact subsection is unstable.
Use subsection links when the heading is stable and important.

---

## 9. Tables, Lists, Examples, and Figures

Use the format that best fits the information.

Use tables for:

- column descriptions
- field comparisons
- file inventories
- structured mappings
- counts or classifications

Use lists for:

- short enumerations
- reading paths
- categories
- requirements

Use code blocks for:

- TSV examples
- JSON examples
- command examples
- transcription samples

Use figures or diagrams for:

- entity relationships
- entry structure
- workflows
- visual examples that cannot be explained clearly in prose

Examples should illustrate a definition, rule, or method.
They should not be the only place where that definition, rule, or method appears.

Do not alter example content unless explicitly instructed.
Rules for protected examples belong to `EDITORIAL_CONVENTIONS.md`.

---

## 10. Tone and Readability

KRM Documentation should read as reference documentation.

Prefer:

- direct statements
- explicit scope
- stable terminology
- short paragraphs
- clear transitions
- evidence-oriented wording

Avoid:

- conversational filler
- unexplained assumptions
- temporary implementation notes in stable pages
- unnecessary repetition
- overlong paragraphs
- claims that go beyond the documented evidence

The tone should support international readability while preserving scholarly precision.
Detailed Japanese/English language policy belongs to `I18N_POLICY.md`.

---

## 11. Handling Dense Pages

Dense pages should be clarified before they are rewritten.

When a page contains several content types, identify them first.
Common mixed types include:

- definition
- rule
- example
- evidence
- methodology
- record
- workflow note

For dense pages:

- add or preserve clear section structure
- make the page purpose explicit
- distinguish general rules from examples
- preserve examples and evidence
- avoid changing scholarly interpretation
- avoid splitting or moving material without a specific task

Dense pages in annotation or data-model sections may contain protected scholarly content.
Before changing substance, consult `EDITORIAL_CONVENTIONS.md`.

---

## 12. Core and Supporting Materials

Core reference pages should be the primary source for:

- concepts
- data file meanings
- editorial rules
- annotation methodology
- terminology

Supporting materials may include:

- case studies
- progress pages
- typesetting notes
- tool notes
- applied research examples

Supporting materials should link to core reference pages when they use core concepts or rules.
They should not become the only place where a term or rule is explained.

Progress pages should be treated as records.
Case studies should be treated as examples or applications.
Typesetting and tool pages should be treated as workflow or supporting material unless they define a necessary publication rule.

---

## 13. Front Matter and Metadata

Front matter should support navigation and page identity.

Expected fields include:

- `title`
- `weight` where ordering matters

General rules:

- `title` should match the page role.
- `weight` should support the intended reading order.
- commented-out metadata should be minimized unless there is a reason to preserve it.
- page title, H1, and navigation label should not contradict each other.

Author and publication-date metadata may be retained for pages that originated as independently published articles, research notes, or case studies. They are not required for Core Reference pages or section index pages.

Language-specific metadata and filename policy belong to `I18N_POLICY.md`.

---

## 14. Style Review Checklist

Before accepting a documentation style change, check:

- Is the page type clear?
- Does the opening explain the page purpose?
- Are headings useful and proportional?
- Are links current and meaningful?
- Are examples supporting the rule or concept?
- Is stable reference content separated from records or workflow notes?
- Is terminology preserved or flagged for glossary review?
- Has protected scholarly content been preserved?
- Are language-version issues deferred to `I18N_POLICY.md` when needed?

A fuller review checklist may be created later as a separate project standard.

---

## 15. Boundaries

This Style Guide defines how Documentation should be structured and written.

It does not define all project standards.

Use:

- `AGENTS.md` for AI assistant behavior
- `EDITORIAL_CONVENTIONS.md` for editorial authority and protected content
- `GLOSSARY_CONVENTIONS.md` for glossary entry structure and terminology maintenance
- `I18N_POLICY.md` for Japanese/English documentation policy
- future review or maintenance standards for acceptance checks and long-term upkeep

When a style question overlaps with scholarly content, preservation rules take precedence.
