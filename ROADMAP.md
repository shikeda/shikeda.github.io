# KRM Documentation Roadmap

Implementation Strategy for the KRM Documentation

This Roadmap is governed by `PROJECT_CHARTER.md`.
It translates the findings of `CURRENT_STATE_REPORT.md` and the target architecture of `DOCUMENTATION_BLUEPRINT.md` into a practical implementation strategy.

This document does not revise scholarly content.
It does not prescribe changes to bibliography, examples, datasets, encoding rules, identifiers, or database specifications.
Its focus is information architecture, navigation, terminology, cross references, maintainability, and documentation workflow.

---

## 1. Roadmap Purpose

The purpose of this Roadmap is to guide the KRM Documentation from its current content-rich but uneven state toward a stable reference documentation system.

The implementation strategy should preserve existing scholarly substance while improving:

- conceptual structure
- navigation
- terminology consistency
- document type separation
- Japanese/English documentation governance
- maintainability
- readiness for long-term documentation work

The Roadmap should be treated as subordinate to `PROJECT_CHARTER.md` and as the practical companion to `DOCUMENTATION_BLUEPRINT.md`.

---

## 2. Strategic Priorities

### Priority 1: Stabilize the Documentation Architecture

The first priority is to make the target conceptual architecture operational.
The Documentation should distinguish stable reference content from supporting materials, progress records, workflow notes, and research applications.

Affected conceptual areas:

- Orientation
- Concepts
- Data Reference
- Editorial Rules
- Annotation Methodology
- Publication and Maintenance
- Glossary
- Examples and Applications
- Records

Expected result:

- every major page has a clear role within the Documentation system
- section index pages explain purpose and relationships
- readers can identify whether a page is reference, rule, methodology, example, workflow, or record

### Priority 2: Normalize Navigation and Cross References

Broken, stale, or structurally misleading links should be addressed early because they affect user confidence and all later refactoring.

Known problem areas:

- stale `/docs/notes/...` paths
- mismatched progress and case-study links
- `headword_chars` vs `headword-chars`
- `localhost` references
- old section numbering assumptions

Expected result:

- internal links reflect the current KRM Documentation structure
- cross references express conceptual relationships rather than old migration paths
- section index pages provide reliable navigation

### Priority 3: Establish a Terminology Layer

A central glossary or terminology layer is necessary before broad chapter refactoring.
The existing Documentation already contains strong local definitions, but they are distributed.

Core source areas:

- `content/docs/krm/03-entry-data-model/03-01-data-structure.*.md`
- `content/docs/krm/03-entry-data-model/03-03-concepts-char.*.md`
- `content/docs/krm/04-entry-input/04-03-handling.*.md`
- `content/docs/krm/05-annotation-policy/`

Expected result:

- preferred terms and accepted variants are visible
- Japanese and English terminology correspondences are explicit
- later editing can reuse stable terms without redefining them locally

### Priority 4: Clarify Japanese/English Documentation Policy

The current bilingual structure is useful but inconsistent.
Before large-scale rewriting, the project should define how Japanese pages, English pages, and bilingual unsuffixed pages should relate.

Expected result:

- language versions share the same conceptual architecture
- pages have clear language status
- translation/editorial notes are distinguished from stable documentation
- English pages are not assumed to be exact translations unless explicitly intended

### Priority 5: Refactor Dense Core Sections Carefully

The most valuable and structurally dense areas should be refactored only after architecture, navigation, terminology, and language policy are stable.

Key sections:

- `content/docs/krm/02-data-overview/`
- `content/docs/krm/03-entry-data-model/`
- `content/docs/krm/04-entry-input/`
- `content/docs/krm/05-annotation-policy/`

Expected result:

- core reference pages become easier to scan and maintain
- examples support rules instead of carrying core definitions
- long pages are structured around reader tasks and document type

---

## 3. Dependencies

The implementation order should respect the following dependencies.

### Governance Before Editing

Any major architectural decision must be consistent with `PROJECT_CHARTER.md`.
If the project philosophy changes, the Charter should be revised first.

### Blueprint Before Refactoring

`DOCUMENTATION_BLUEPRINT.md` defines the target architecture.
Chapter-level refactoring should follow the Blueprint rather than reinvent the structure locally.

### Terminology Before Broad Rewriting

Terminology should be stabilized before extensive page edits.
Otherwise, refactoring may reproduce local inconsistencies.

### Navigation Before Deep Content Work

Broken and stale links should be normalized before or alongside structural work.
Reliable navigation makes later review possible.

### Language Policy Before Bilingual Refactoring

Japanese/English alignment should not be handled page by page without a policy.
The project should first decide how language counterparts are expected to behave.

### Document Type Classification Before Page Movement

Pages should be classified by type before deciding whether they belong in the core reference layer, supporting materials, records, or examples.

---

## 4. Milestones

### Milestone 1: Planning Foundation

Goal:

- establish the project planning foundation below `PROJECT_CHARTER.md`

Inputs:

- `PROJECT_CHARTER.md`
- `CURRENT_STATE_REPORT.md`
- `DOCUMENTATION_BLUEPRINT.md`
- `ROADMAP.md`

Deliverables:

- accepted Roadmap
- agreed interpretation of document layers and document types
- confirmation that future edits should preserve scholarly content

Success criteria:

- Roadmap is consistent with the Charter
- Roadmap clearly separates implementation planning from scholarly revision
- Roadmap can guide later project standards and chapter refactoring

### Milestone 2: Project Standards

Goal:

- create standards that allow humans and AI assistants to edit consistently

Likely deliverables:

- `AGENTS.md`
- `CLAUDE.md`
- editorial conventions
- documentation style guide
- link and cross-reference conventions
- language-version conventions
- glossary conventions

Dependencies:

- Milestone 1
- accepted document type model
- accepted terminology strategy

Success criteria:

- future contributors know what they may and may not change
- document type expectations are explicit
- link, heading, glossary, and bilingual conventions are defined

### Milestone 3: Navigation Stabilization

Goal:

- make the current Documentation navigable and internally coherent

Scope:

- stale internal links
- old `/docs/notes/...` references
- mismatched section links
- section index pages
- cross-reference conventions

Dependencies:

- Milestone 2 standards, or at least provisional link conventions

Success criteria:

- known stale links are resolved or documented
- section index pages guide readers reliably
- current paths and conceptual navigation are aligned

### Milestone 4: Glossary and Terminology Baseline

Goal:

- establish a central terminology reference

Scope:

- entry structure terms
- annotation terms
- character-form terms
- input and encoding terms
- manuscript/source terms
- data-file and column terms

Dependencies:

- Milestone 2 standards
- review of terminology-bearing pages

Success criteria:

- core terms have stable entries
- Japanese and English correspondences are explicit
- known variations are documented rather than hidden
- pages can link to central terminology entries

### Milestone 5: Core Reference Refactoring

Goal:

- align the stable core Documentation with the Blueprint layers

Primary sections:

- `02-data-overview/`
- `03-entry-data-model/`
- `04-entry-input/`
- `05-annotation-policy/`

Dependencies:

- Milestone 3 navigation stabilization
- Milestone 4 glossary baseline
- language-version policy

Success criteria:

- each core section has a clear document type
- data reference, concept reference, rule reference, and methodology content are distinguishable
- dense pages have clearer internal structure
- examples are connected to the rules or concepts they illustrate

### Milestone 6: Supporting Materials Classification

Goal:

- distinguish supporting materials from the stable reference core

Primary sections:

- `06-typesetting/`
- `07-progress/`
- `08-case-studies/`

Dependencies:

- document type standards
- navigation model

Success criteria:

- progress records are recognizable as records
- case studies are linked as applications, not primary definitions
- typesetting/tool pages are classified as workflow or supporting material
- readers can tell which pages are normative reference and which are contextual support

### Milestone 7: Long-Term Maintenance Model

Goal:

- make the Documentation sustainable over time

Scope:

- maintenance procedures
- periodic terminology review
- link checking
- release/update documentation
- rules for adding new pages
- preservation of scholarly integrity

Dependencies:

- stable standards
- stable navigation
- glossary baseline

Success criteria:

- future changes can be evaluated against explicit standards
- terminology drift can be detected
- new Documentation can be added without disrupting architecture
- maintenance work does not alter scholarly content unintentionally

---

## 5. Quick Wins

Quick wins are low-risk changes that improve reliability without requiring deep scholarly review.
They should still follow project standards and avoid altering scholarly content.

High-value quick wins:

- identify and list stale internal links
- normalize obvious broken internal paths
- remove or replace development-only `localhost` references
- align section index links with actual directories
- document known external links marked as broken
- classify existing pages by document type in an inventory
- identify `.en.md` pages that contain substantial Japanese text
- identify unsuffixed pages that mix Japanese and English
- collect candidate glossary terms from core terminology pages

These tasks are good early implementation work because they improve maintainability and reviewability without changing the underlying scholarship.

---

## 6. Long-Term Refactoring Tasks

Long-term refactoring should proceed after standards, navigation, and terminology are stable.
The following tasks are structural and editorial, not scholarly.

### Core Section Refactoring

Refactor core sections so that each page has a clear role:

- concept reference
- data reference
- rule reference
- methodology
- example

Priority areas:

- `02-data-overview/`
- `03-entry-data-model/`
- `04-entry-input/`
- `05-annotation-policy/`

### Glossary Integration

Integrate glossary references into core pages.
Terms should be defined centrally and reused consistently.

### Section Index Revision

Convert section index pages into navigational guides.
Each index should state:

- purpose
- audience
- prerequisites
- child-page relationships
- links to related sections

### Bilingual Alignment

Clarify the relationship between Japanese and English pages.
Possible future states may include parallel pages, Japanese-primary pages with English summaries, or bilingual supporting pages.
The Roadmap does not choose the final policy, but later standards should.

### Dense Page Decomposition

Some pages combine rules, examples, counts, and commentary.
Long-term refactoring should make these internal roles visible.
Any decomposition should preserve examples, evidence, and scholarly claims.

### Supporting Material Reclassification

Classify progress records, case studies, and workflow notes so they support the reference system without becoming the source of core definitions.

---

## 7. Risks

### Risk: Scholarly Content Drift

Documentation refactoring may accidentally change interpretation, evidence, examples, or database rules.

Mitigation:

- keep scholarly content preservation explicit
- separate structural edits from scholarly edits
- require review for any change affecting interpretation, examples, identifiers, encoding rules, or specifications

### Risk: Architecture Without Adoption

The Blueprint may remain abstract if not translated into editing standards and page conventions.

Mitigation:

- create project standards before broad refactoring
- classify pages by document type
- make section index pages reflect the architecture

### Risk: Terminology Fragmentation

Local definitions may continue to diverge if glossary work is delayed.

Mitigation:

- establish a glossary baseline early
- document accepted variants
- link terminology-bearing pages to the glossary

### Risk: Bilingual Inconsistency

Japanese and English pages may drift further apart if edited independently.

Mitigation:

- define language-version policy
- record whether pages are parallel, summary, bilingual, or Japanese-primary
- avoid assuming one-to-one translation where none exists

### Risk: Link Repair Without Conceptual Review

Fixing links mechanically may preserve weak conceptual relationships.

Mitigation:

- repair broken paths
- also classify the intended relationship of each cross reference

### Risk: Over-Refactoring

Excessive restructuring may make the Documentation harder to maintain or review.

Mitigation:

- keep edits scoped
- prioritize navigability and clarity
- preserve existing file evidence and examples
- refactor dense pages only after terminology and standards are stable

---

## 8. Success Criteria

The Roadmap is successful if it leads to a Documentation system in which:

- the Charter governs all major documentation decisions
- every major page has an identifiable document type
- core reference layers are distinguishable from examples, records, and workflow notes
- internal navigation is reliable
- cross references express meaningful conceptual relationships
- a central glossary supports terminology consistency
- Japanese and English content follow an explicit language policy
- data reference pages are easy to find and interpret
- editorial and encoding rules are separate from research applications
- annotation methodology is visible as methodology, not scattered only through examples
- future contributors and AI assistants can work without rediscovering the architecture
- scholarly content is preserved unless explicitly reviewed and revised

---

## 9. Priority Task Matrix

### High Priority

Task: Create project-wide editing standards.

Affected areas:

- `AGENTS.md`
- `CLAUDE.md`
- future style and editorial conventions

Expected work:

- define document types
- define permissible AI/editor actions
- define link, terminology, and language conventions

Rationale:

- later refactoring needs stable rules.

Task: Audit and normalize internal navigation.

Affected areas:

- `content/docs/krm/_index.*.md`
- `content/docs/krm/*/_index*.md`
- pages linking to `/docs/notes/...`

Expected work:

- identify stale paths
- verify current targets
- align section navigation with the active structure

Rationale:

- navigation reliability is a prerequisite for user trust and later review.

Task: Establish glossary baseline.

Affected areas:

- terminology-bearing pages in `03-entry-data-model/`, `04-entry-input/`, and `05-annotation-policy/`

Expected work:

- collect core terms
- record Japanese/English correspondences
- document accepted variants

Rationale:

- terminology stability supports all later editing.

### Medium Priority

Task: Classify existing pages by document type.

Affected areas:

- all files under `content/docs/krm/`

Expected work:

- assign each page a role such as overview, concept reference, data reference, rule reference, methodology, example, workflow, or record

Rationale:

- classification should precede structural refactoring.

Task: Define Japanese/English documentation policy.

Affected areas:

- `.ja.md`, `.en.md`, and unsuffixed `.md` files

Expected work:

- define expected relation between language versions
- identify pages needing language-status labels or editorial treatment

Rationale:

- bilingual consistency cannot be solved page by page without policy.

Task: Refine section index pages.

Affected areas:

- `content/docs/krm/*/_index*.md`

Expected work:

- make index pages describe scope, audience, prerequisites, child-page relationships, and related sections

Rationale:

- section indexes are the main navigation surface for the target architecture.

### Low Priority

Task: Classify supporting material.

Affected areas:

- `content/docs/krm/06-typesetting/`
- `content/docs/krm/07-progress/`
- `content/docs/krm/08-case-studies/`

Expected work:

- distinguish workflow notes, records, and applications from core reference content

Rationale:

- important for long-term architecture, but less urgent than core navigation and terminology.

Task: Review external tool and broken-link notes.

Affected areas:

- `content/docs/krm/06-typesetting/`
- online tool lists

Expected work:

- classify time-sensitive external-link information
- decide how link status should be represented

Rationale:

- useful for maintenance, but not central to the reference model.

Task: Prepare long-term maintenance conventions.

Affected areas:

- future maintenance documentation
- publication/update notes

Expected work:

- define review cadence
- define terminology review process
- define rules for adding new pages

Rationale:

- necessary for Phase 6, but depends on earlier standards.

---

## 10. Implementation Sequence

The recommended sequence is:

1. Accept `ROADMAP.md` as the practical planning document under `PROJECT_CHARTER.md`.
2. Create project standards for AI and human contributors.
3. Audit links, section indexes, and current navigation.
4. Establish a glossary baseline.
5. Define Japanese/English documentation policy.
6. Classify existing pages by document type.
7. Refactor core reference sections.
8. Classify and integrate supporting materials.
9. Establish long-term maintenance procedures.

This sequence is intended to reduce risk.
It moves from governance and standards to navigation and terminology, then to deeper chapter-level refactoring.

---

## 11. Non-Goals

This Roadmap does not authorize:

- rewriting scholarly interpretations
- changing examples
- changing bibliography
- changing datasets
- changing encoding rules
- changing identifiers
- changing database specifications
- merging or deleting Documentation without review
- treating English pages as automatically authoritative over Japanese pages, or vice versa

Any work touching those areas requires explicit instruction and appropriate scholarly review.

---

## 12. Roadmap Review

This Roadmap should be reviewed whenever:

- `PROJECT_CHARTER.md` changes
- the Documentation Blueprint changes
- project standards are created or revised
- major chapter-level refactoring begins
- KRM publication or maintenance workflow changes

The Roadmap should remain practical.
If it becomes inconsistent with the Charter or the Blueprint, the higher-level document should govern.
