# Maintenance Conventions

Long-Term Maintenance Operations for KRM Documentation

This document defines how KRM Documentation should be kept healthy over time.
It applies to both human contributors and AI assistants.

This document does not create new editorial, scholarly, terminology, or language rules.
It defines how existing Project Standards are continuously applied through maintenance work.

---

## 1. Purpose and Scope

Maintenance keeps the Documentation usable, consistent, and aligned with project standards over time.

This document covers:

- maintenance scope
- routine maintenance
- event-driven maintenance
- staleness and priority principles
- roles and authority
- workflow status
- content state
- maintenance records
- relationship to `REVIEW_CHECKLIST.md`

It applies primarily to:

- `content/docs/krm/`
- `content/posts/`
- Project Standards
- maintenance records or issue records related to KRM Documentation

---

## 2. Relationship to Project Standards

Maintenance work must follow existing standards:

- `PROJECT_CHARTER.md`
- `AGENTS.md`
- `DOCUMENTATION_STYLE_GUIDE.md`
- `EDITORIAL_CONVENTIONS.md`
- `GLOSSARY_CONVENTIONS.md`
- `I18N_POLICY.md`
- `REVIEW_CHECKLIST.md`

`PROJECT_CHARTER.md` governs preservation.
Maintenance must not silently change scholarly interpretations, bibliography, examples, datasets, encoding rules, identifiers, or database specifications.

`REVIEW_CHECKLIST.md` is used to review specific changes produced by maintenance work.
It does not define maintenance schedules.

---

## 3. Core Principles

Maintenance is not automatic correction.

Use this controlled workflow:

```text
Detect
-> Record
-> Classify
-> Assign
-> Review
-> Update when authorized
-> Record outcome
-> Preserve state
```

Do not immediately fix every detected issue.

Record uncertainty before resolving it.
Classify the issue before assigning work.
Update only when the relevant authority exists.

Historical information, deprecated information, archived information, unresolved issues, and language differences should be preserved with appropriate status rather than deleted.

---

## 4. Maintenance Scope

Maintenance may include the following areas.
These areas do not require the same frequency or priority.

| Area | Examples |
| --- | --- |
| Core Documentation | Orientation, Concept Reference, Data Reference, Rule Reference, Annotation Methodology. |
| Supporting materials | Workflow notes, tool notes, supplementary explanations. |
| Case Studies | Japanese-only by policy pages, optional English summaries, links to Core Documentation. |
| Records | Progress pages, status notes, historical records. |
| Blog Posts | Posts that may contain stable information candidates for Core Documentation. |
| Links | Internal links, external links, obsolete paths, development-only links. |
| Metadata | Front matter, titles, H1, weight, ordering, language suffixes. |
| Information architecture | Document layer, document type, section indexes, navigation. |
| Terminology | Glossary status, provisional terms, deprecated terms, unresolved terminology. |
| I18N | Page language status, supplementary language availability, bilingual-required gaps, language differences. |
| Protected content risk | Examples, citations, transcriptions, bibliography, identifiers, data specifications, encoding rules. |
| Unresolved issues | Recorded questions, conflicts, or pending confirmations. |
| Project Standards | Standards consistency, outdated references, conflicts after standards changes. |

---

## 5. Routine Maintenance

Routine maintenance is periodic or recurring documentation health work.
Frequency should be adjusted to project needs.
The examples below are not mandatory schedules.

Examples:

- internal link checks
- external link status checks
- obsolete or development-only path detection
- metadata consistency review
- section index and navigation consistency review
- page language status inventory
- bilingual-required gap review
- glossary and terminology status review
- unresolved issue inventory
- Project Standards consistency review

Example timing, if useful:

- light checks before a documentation release
- broader health checks before major refactoring
- terminology and I18N checks before Core Documentation restructuring
- standards consistency checks after standards or governance changes

---

## 6. Event-Driven Maintenance

Event-driven maintenance is triggered by a specific change or discovery.
When an event occurs, first assess the impact scope before deciding what to update.

Examples of triggering events:

- new data release
- database or schema specification change
- directory or URL restructuring
- major documentation refactoring
- Project Standard revision
- Charter, Blueprint, or Roadmap change
- preferred term or official translation approval
- I18N policy or language-status change
- new English version of Core Documentation
- external site or URL change
- new contributor or AI workflow introduction

Changes to higher-level standards may require review of:

- related standards
- `REVIEW_CHECKLIST.md`
- AI instructions
- Core Documentation
- glossary conventions or entries
- I18N status records

Do not assume that an event requires immediate content edits.
Record and classify the impact first.

---

## 7. Staleness and Priority

Staleness is not determined by update date alone.

Consider:

- consistency with current Project Standards
- consistency with current data or specifications
- link validity
- metadata consistency
- terminology status
- I18N status and alignment
- navigation and section structure
- current workflow
- known unresolved issues
- superseding pages or specifications

An old page is not automatically obsolete or deprecated.
A recently edited page may still be stale if it conflicts with current standards or specifications.

Priority should be based on impact and risk, not fixed page order.

Consider:

- impact
- urgency
- reader risk
- relation to Core Documentation
- data or specification risk
- protected content risk
- navigation impact
- number of affected pages
- dependency on other work
- authorization readiness

Higher-impact examples:

- broken Core Documentation navigation
- data or specification inconsistency
- terminology conflict affecting multiple pages
- bilingual-required gap in core reference
- protected content risk

Lower-impact examples:

- old formatting in a non-core blog post
- external link note in supporting material
- case study without English summary where Japanese-only status is policy-compliant

These examples are guidance, not fixed priority rules.

---

## 8. Roles and Authority

Maintenance involves distinct roles.

| Role | May be performed by | Responsibility |
| --- | --- | --- |
| Detection | Tools, AI assistants, human editors, readers | Find possible issues. |
| Recording | AI assistants, human editors, maintainers | Record issue, file, evidence, and date. |
| Classification | AI assistants, human editors, maintainers | Propose issue type and risk level. |
| Proposal | AI assistants, human editors, maintainers | Suggest possible handling or next step. |
| Assignment | Maintainer, project owner | Assign review or action responsibility. |
| Review | Human editor, maintainer, AI-assisted review | Check against standards and scope. |
| Approval | Project owner, scholarly editor, authorized technical maintainer | Approve protected, scholarly, terminology, translation, or specification-sensitive changes. |
| Update | Human editor, AI assistant under instruction, maintainer | Apply authorized change. |
| Outcome recording | Human editor, AI assistant, maintainer | Record result and remaining state. |

AI and tools may assist with detection, recording, classification candidates, and proposed fixes.

The following require appropriate confirmation or approval:

- scholarly interpretation
- protected content
- data and schema specifications
- identifiers and encoding rules
- preferred terminology
- official translations
- language-version substantive differences

Technical maintainer authority is limited to technical scope, such as data-field naming, schema-related terminology, and technical metadata.

---

## 9. Maintenance Workflow and Status

Keep workflow status separate from content state.

### Workflow Status

Use these statuses when helpful:

| Status | Meaning |
| --- | --- |
| `detected` | Issue has been found. |
| `recorded` | Issue has been documented with file/path and evidence. |
| `classified` | Issue type or risk category has been identified. |
| `assigned` | Responsibility has been assigned. |
| `in review` | Issue is under review. |
| `needs confirmation` | Authorized confirmation is required. |
| `approved` | Required approval has been obtained. |
| `updated` | Authorized update has been applied. |
| `deferred` | Work is intentionally postponed. |
| `closed` | Maintenance item has been resolved or accepted in current state. |

These statuses are optional operational labels.
They do not require a specific issue tracker.

### Content or Resolution State

Use these states for the content itself when helpful:

| State | Meaning |
| --- | --- |
| `current` | Content is considered current for its role. |
| `unresolved` | Issue remains undecided but recorded. |
| `deprecated` | Content or term is no longer recommended for new use, but preserved. |
| `historical` | Content is retained as historical information. |
| `archived` | Content is preserved as an archive or record. |
| `superseded` | A newer page, specification, or rule supersedes the content. |

Do not require all statuses for all issues.
Use the lightest record that preserves the needed information.

---

## 10. Preservation and Lifecycle States

Do not delete the following merely because they appear old or inconsistent:

- historical terminology
- deprecated terms
- old paths
- superseded specifications
- archived pages
- progress and record pages
- unresolved scholarly or technical issues
- language-version differences

Appropriate handling may include:

- redirect
- superseded notice
- archive status
- historical note
- deprecated status
- unresolved issue record
- link to current reference page

This document does not decide the treatment of individual pages.
Specific actions should follow existing standards and required approvals.

---

## 11. Maintenance Records

Maintenance records should be lightweight.
They should not become more burdensome than the maintenance work itself.

Use this template when useful:

```markdown
## Maintenance Item

Issue or item:

File or path:

Detected by:

Detection date:

Classification:

Evidence:

Priority rationale:

Assigned role:

Required review or confirmation:

Workflow status:

Content or resolution state:

Outcome:

Unresolved notes:
```

Short records are acceptable when the issue is simple.
For protected content, terminology, I18N, or specification-sensitive issues, record enough evidence to support review.

---

## 12. Relationship to REVIEW_CHECKLIST.md and Boundaries

`MAINTENANCE_CONVENTIONS.md` detects, records, classifies, assigns, and manages issues over time.

`REVIEW_CHECKLIST.md` decides whether a specific new page, edit, revision, or standards change can be accepted.

When maintenance leads to an edit, that edit should be reviewed with `REVIEW_CHECKLIST.md`.

`REVIEW_CHECKLIST.md` does not set maintenance schedules.
This document does not duplicate the acceptance checklist.

This document does not decide:

- new editorial rules
- scholarly conclusions
- preferred glossary terms
- official translations
- fixed maintenance calendar
- mandatory issue tracker
- project management tool implementation
- individual page deletion or archival decisions

If a conflict or unresolved issue appears among standards, record it, classify it, and route it for confirmation.
Do not resolve it silently.

---

## 13. Summary Rules

Detect before editing.

Record before resolving.

Classify before assigning.

Review before updating.

Update only when authorized.

Preserve historical, deprecated, archived, unresolved, and language-difference states when they remain meaningful.
