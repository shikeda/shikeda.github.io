# Documentation Blueprint

Conceptual Architecture for the KRM Documentation

This Blueprint is a Phase 1 deliverable under `PROJECT_CHARTER.md`.
It defines the target conceptual information architecture for the KRM Documentation.

This document is not an implementation plan.
It is not a roadmap.
It does not prescribe file edits, migration steps, or chapter-by-chapter rewriting.

Its purpose is to define the architecture that future Documentation should follow.

---

## 1. Architectural Purpose

The KRM Documentation should function as the authoritative reference for the structure, construction, annotation, publication, and long-term maintenance of the Ruiju Myogisho Database.

Its target architecture should support two long-term goals:

- to document KRM clearly and sustainably
- to provide a reusable model for documenting historical lexical resources

The Documentation should therefore be organized as a reference system, not merely as a collection of pages.

The target architecture should make the following distinctions explicit:

- stable reference content
- conceptual explanation
- data specification
- editorial and annotation rules
- publication and maintenance workflow
- research applications
- project records

These categories may be connected, but they should not be conceptually conflated.

---

## 2. Document Layers

The target Documentation should be organized into layers.
Each layer has a distinct purpose and degree of stability.

### Layer 1: Orientation

Purpose:

- explain what KRM is
- identify the manuscript/resource being documented
- state the Documentation scope
- guide readers to the appropriate entry point

Primary audience:

- all users
- new readers
- researchers approaching KRM for the first time
- digital humanities users evaluating whether KRM is relevant

Expected content type:

- overview
- scope
- audience guide
- high-level resource description

This layer should answer:

- What is KRM?
- What does the Documentation cover?
- Which section should I read first?

### Layer 2: Conceptual Reference

Purpose:

- define the conceptual model of KRM
- explain the structure of entries
- define core scholarly and data concepts
- establish the terminology used across the Documentation

Primary audience:

- researchers
- data users
- editors
- developers
- AI/LLM users who need a stable semantic model

Expected content type:

- concept definitions
- diagrams
- model explanations
- relationships among entities

This layer should answer:

- What is an Entry?
- What is a Headword?
- What are Original Glosses?
- How are phonetic glosses, semantic glosses, wakun, and character-form notes related?

### Layer 3: Data Reference

Purpose:

- describe published data files
- explain columns and field meanings
- describe relationships among data files
- record version-sensitive data specifications

Primary audience:

- data users
- developers
- corpus linguists
- digital humanities users
- AI/LLM developers

Expected content type:

- file reference
- column reference
- ER diagrams
- format explanation
- version notes

This layer should answer:

- What files are published?
- What does each column mean?
- How do the files relate?
- Which parts of the data model are represented in each file?

### Layer 4: Editorial and Encoding Rules

Purpose:

- document rules for transcription, input, encoding, and representation
- explain how manuscript phenomena are represented in data
- preserve rules for identifiers, character representation, notation, and layout features

Primary audience:

- database maintainers
- editors
- data contributors
- technical users who need to interpret encoded phenomena

Expected content type:

- rule reference
- conventions
- edge cases
- examples
- controlled descriptions of editorial decisions

This layer should answer:

- How are IDs assigned?
- How are non-Unicode characters represented?
- How are variant characters, omitted characters, correction marks, tone marks, and supplementary notes handled?

### Layer 5: Annotation Methodology

Purpose:

- explain the principles and categories of annotation
- define the relationship between original text, commentary, and analytical judgment
- describe what annotation is intended to accomplish
- clarify how Compiler's Remarks and related annotation fields should be interpreted

Primary audience:

- researchers
- editors
- annotation maintainers
- advanced data users

Expected content type:

- annotation principles
- classification of annotation objects
- explanation of evidence types
- examples of annotation practice
- source-material orientation

This layer should answer:

- What kinds of annotations exist?
- What is the role of collation, source investigation, research history, lexical explanation, and additional commentary?
- Which phenomena require annotation?
- How should annotation evidence be understood?

### Layer 6: Publication and Maintenance

Purpose:

- explain how the Documentation and database are published and maintained
- distinguish stable data specifications from release-specific records
- document maintenance responsibilities and update patterns

Primary audience:

- project maintainers
- technical editors
- future AI assistants
- data users who need to understand release state

Expected content type:

- publication workflow
- maintenance policy
- version notes
- release-state explanation

This layer should answer:

- Where is the data published?
- How are updates recorded?
- What maintenance responsibilities exist?
- Which information is stable and which is release-specific?

### Layer 7: Supporting Materials and Applications

Purpose:

- provide research case studies, examples, applied analyses, progress summaries, and auxiliary tools
- demonstrate how KRM can be used
- preserve useful but non-core material without confusing it with stable reference content

Primary audience:

- researchers
- advanced users
- students
- readers interested in applied use

Expected content type:

- case studies
- progress records
- tool notes
- typesetting notes
- applied research examples

This layer should answer:

- How has KRM been used?
- What research questions can KRM support?
- What auxiliary workflows help produce or use KRM?

---

## 3. Document Types

The target architecture should classify every page by document type.
Document type should determine structure, expected content, and navigation behavior.

### Overview

An Overview page introduces a major area.
It should define scope, audience, and the relationship between child pages.

Examples of suitable locations:

- KRM landing page
- section index pages

### Concept Reference

A Concept Reference page defines entities, relationships, and intellectual categories.
It should prioritize stable definitions over procedural detail.

Typical subjects:

- Entry
- Headword
- Original Glosses
- wakun
- phonetic glosses
- character-form notes
- manuscript and data-model relationships

### Data Reference

A Data Reference page describes a data file, table, field group, or structured representation.
It should be precise, stable, and easy to scan.

Typical subjects:

- `krm_main`
- `krm_notes`
- `krm_headword_chars`
- `krm_wakun`
- `krm_pronunciations`
- `krm_ndl`

### Rule Reference

A Rule Reference page documents editorial, encoding, or input rules.
It should distinguish general principles from special cases.

Typical subjects:

- ID rules
- character representation
- transcription conventions
- notation handling
- layout features

### Methodology

A Methodology page explains why and how annotation or interpretation is structured.
It should describe principles, evidence categories, and analytical boundaries.

Typical subjects:

- annotation policy
- annotation targets
- source investigation
- collation
- use of previous research

### Example or Case

An Example or Case page demonstrates a concept, rule, or method through concrete material.
It should be connected to the relevant reference page, but should not be the only location where the rule is defined.

Typical subjects:

- annotation examples
- wakun case studies
- DHSJR collaboration examples

### Workflow

A Workflow page explains how publication, maintenance, typesetting, or tool use is performed.
It should be separated from conceptual reference unless the workflow is necessary to understand the data itself.

Typical subjects:

- publication workflow
- maintenance procedure
- typesetting setup
- tool usage

### Record

A Record page preserves time-sensitive information.
It should be identifiable as a record rather than a stable rule.

Typical subjects:

- progress status
- release notes
- update history

---

## 4. Chapter Relationships

The target chapter model should be based on conceptual dependency.
Readers should be able to move from broad context to precise reference without circular dependence.

The ideal relationship is:

1. Orientation
2. Conceptual Model
3. Data Reference
4. Editorial and Encoding Rules
5. Annotation Methodology
6. Publication and Maintenance
7. Supporting Materials and Applications

The Conceptual Model should precede Data Reference because readers need stable concepts before interpreting fields and files.

The Data Reference should precede detailed Editorial and Encoding Rules because users should first know what data exists and then learn how specific phenomena are encoded.

Editorial and Encoding Rules should precede Annotation Methodology when the reader's goal is data interpretation.
Annotation Methodology may precede Editorial and Encoding Rules when the reader's goal is scholarly understanding.
The navigation model should support both paths.

Publication and Maintenance should be downstream from data and editorial reference.
It should describe how the resource is kept stable over time, not redefine the concepts themselves.

Supporting Materials and Applications should depend on the reference layers.
They should illustrate or apply the core Documentation, not serve as the primary source for definitions or rules.

---

## 5. Navigation Model

The target navigation model should support multiple reader paths while preserving one stable conceptual hierarchy.

### Primary Navigation

Primary navigation should expose the main layers:

- Start Here
- Concepts
- Data
- Rules
- Annotation
- Publication and Maintenance
- Examples and Applications
- Glossary

This model gives users a predictable path from orientation to reference to application.

### Section Navigation

Each major section should have an index page that explains:

- what the section covers
- who should read it
- which concepts are prerequisites
- which child pages are included
- how the section relates to other sections

Section index pages should be navigational documents, not merely lists.

### Cross References

Cross references should express conceptual relationships.
They should not merely compensate for missing hierarchy.

Core cross-reference patterns:

- Concept Reference -> Data Reference
- Data Reference -> Rule Reference
- Rule Reference -> Concept Reference
- Annotation Methodology -> Examples
- Examples -> relevant Concept, Data, Rule, and Methodology pages
- Glossary -> all pages where the term is defined or operationally important

### Reader Paths

The target architecture should support at least four reader paths.

Researcher path:

1. Orientation
2. Concepts
3. Annotation Methodology
4. Examples and Applications

Data-user path:

1. Orientation
2. Concepts
3. Data Reference
4. Editorial and Encoding Rules

Maintainer path:

1. Concepts
2. Data Reference
3. Editorial and Encoding Rules
4. Publication and Maintenance

AI/LLM developer path:

1. Orientation
2. Glossary
3. Concepts
4. Data Reference
5. Rules

---

## 6. Glossary Placement

The target architecture should include a central Glossary as a first-class reference layer.

The Glossary should not replace conceptual pages.
It should provide stable term entries and link outward to fuller explanations.

Each glossary entry should ideally include:

- preferred term
- Japanese term
- English term
- reading or romanization where useful
- definition
- related terms
- relevant data fields
- relevant Documentation pages
- notes on variation or ambiguity

The Glossary should cover at least these term groups:

- entry structure terms
- annotation terms
- character-form terms
- input and encoding terms
- manuscript/source terms
- data-file and column terms
- publication and maintenance terms

Terminology should flow from the Glossary into all other layers.
Individual pages may introduce local explanations, but the Glossary should remain the stable point of reference.

Terms with legitimate variation should be documented as variation, not silently normalized.
For example, the distinction and relationship between `注文`, `ちゅうもん`, `ちゅうぶん`, and `Original Glosses` should be visible to readers.

---

## 7. Audience Model

The target architecture should support a layered audience model.
Different readers need different entry points, but they should share the same conceptual foundation.

### Primary Audience

Primary users are specialists in:

- Historical Japanese Lexicography
- Historical Japanese
- Kanji Studies

They need:

- manuscript context
- terminology precision
- annotation methodology
- evidence and examples

### Secondary Audience

Secondary users include:

- Digital Humanities researchers
- Corpus Linguistics researchers
- Text Encoding users

They need:

- data model explanation
- file and field reference
- encoding rules
- reproducible interpretation of data values

### Emerging Audience

Emerging users include:

- AI/LLM developers
- digital library developers
- historical lexical resource developers

They need:

- stable terminology
- explicit data semantics
- clear relationships among concepts, files, and fields
- machine-readable or machine-interpretable consistency where possible

### Maintainer Audience

Maintainers include:

- project editors
- technical editors
- future AI assistants
- publication maintainers

They need:

- project-wide rules
- stable terminology
- maintenance conventions
- publication and update expectations

The architecture should avoid creating separate conceptual systems for each audience.
Instead, it should provide different paths through a shared reference structure.

---

## 8. Information Flow

The ideal information flow should move from stable concepts to specific data and then to applied use.

Core flow:

1. Resource identity
2. Conceptual model
3. Data representation
4. Editorial and encoding rules
5. Annotation methodology
6. Publication and maintenance
7. Examples and applications

This flow should make implicit knowledge explicit.
Readers should not need to infer core definitions from examples or progress notes.

Definitions should appear before dependent explanations.
Rules should appear before exceptions.
Examples should illustrate rules rather than carry the burden of defining them.
Records should preserve historical or project state without becoming normative reference pages.

The flow between layers should be directional but not rigid.
Advanced users should be able to enter through Data Reference or Glossary pages and navigate backward to concepts when needed.

---

## 9. Target Conceptual Structure

The target Documentation should be conceptually organized as follows.
The names below describe architectural roles, not required directory names.

### Start Here

Role:

- orient readers
- define scope
- explain KRM's position within HDIC and historical Japanese lexicography
- direct users to reader paths

Contains:

- project/resource overview
- scope and non-goals
- audience guide
- documentation map

### Concepts

Role:

- define the intellectual and data model of KRM

Contains:

- entry structure
- headword and original gloss model
- manuscript/source relationships
- character-form concepts
- annotation object types

### Data Reference

Role:

- document the published data files and their relationships

Contains:

- data file list
- file-specific reference pages
- column definitions
- field relationships
- ER diagrams
- version-sensitive specification notes

### Editorial Rules

Role:

- document how manuscript content is represented in data

Contains:

- ID system
- transcription principles
- character encoding and representation
- notation handling
- layout and supplementary note handling
- special cases

### Annotation Methodology

Role:

- document the principles and analytical categories behind annotation

Contains:

- annotation scope
- annotation categories
- evidence types
- source investigation principles
- treatment of uncertainty
- examples linked to rule and concept pages

### Publication and Maintenance

Role:

- explain how KRM is published, updated, and maintained

Contains:

- publication locations
- update model
- maintenance responsibilities
- version and release explanation
- long-term preservation concerns

### Glossary

Role:

- provide the authoritative terminology layer

Contains:

- stable term entries
- Japanese/English correspondence
- readings and romanizations
- cross references
- ambiguity notes

### Examples and Applications

Role:

- demonstrate use of KRM without redefining core rules

Contains:

- case studies
- applied research examples
- tool-assisted workflows
- explanatory examples

### Records

Role:

- preserve time-sensitive project state

Contains:

- progress records
- update summaries
- status notes

---

## 10. Relationship to Current Documentation

The target architecture can absorb the current Documentation without changing its scholarly substance.

Current sections map conceptually as follows:

- `01-introduction/` belongs mainly to Start Here and Concepts.
- `02-data-overview/` belongs mainly to Data Reference.
- `03-entry-data-model/` belongs mainly to Concepts, with some links to Data Reference.
- `04-entry-input/` belongs mainly to Editorial Rules.
- `05-annotation-policy/` belongs mainly to Annotation Methodology, with some Example and Glossary material.
- `06-typesetting/` belongs mainly to Publication, Workflow, or Supporting Materials.
- `07-progress/` belongs mainly to Records.
- `08-case-studies/` belongs mainly to Examples and Applications.

This mapping is conceptual only.
It does not prescribe a migration strategy or file layout.

---

## 11. Design Principles

The target architecture should follow these principles.

### Clarity Before Coverage

Each section should make its purpose clear before adding detail.
Completeness should not obscure the reader's ability to understand the structure.

### Stable Concepts Before Local Detail

Core definitions should be established in conceptual and glossary layers before being reused in data, rules, or examples.

### Self-Contained Pages

Each reference page should state its scope and key assumptions.
Readers should not need to reconstruct basic context from several other pages before understanding the page.

### Explicit Cross References

Cross references should show meaningful dependency:

- definition
- rule
- data representation
- example
- related term

### Separation of Stable and Time-Sensitive Content

Stable reference material should be clearly separated from progress records, temporary notes, and release-state information.

### International Readability

Japanese and English documentation should share the same conceptual architecture.
Language versions may differ in wording, but not in the underlying model.

### Scholarly Preservation

The architecture should preserve scholarly precision.
It should clarify and organize existing knowledge without replacing scholarly judgment or altering evidence.

---

## 12. Blueprint Outcome

The target KRM Documentation should become a layered reference system.

At maturity, a reader should be able to:

- understand what KRM is
- learn the core concepts
- find the meaning of any major term
- understand each published data file
- interpret identifiers, symbols, and encoding conventions
- understand the principles behind annotation
- distinguish stable reference from examples, progress records, and workflow notes
- move between Japanese and English content without losing the conceptual structure

This Blueprint defines the conceptual architecture required for that outcome.
Future planning documents may translate this architecture into priorities, milestones, and implementation strategy.
