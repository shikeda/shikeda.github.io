# Review Checklist

Acceptance Review Tool for KRM Documentation

This checklist is for reviewing KRM Documentation changes.
It applies to both human contributors and AI assistants.

This document does not create new editing, scholarly, terminology, or language rules.
It converts existing project standards into reviewable checklist items.

Use the checklist sections that match the change.
Do not apply every conditional checklist to every page.

---

## 1. Source Standards and Planning References

Use this checklist with the following governing and planning documents:

- `PROJECT_CHARTER.md`
- `DOCUMENTATION_BLUEPRINT.md`
- `ROADMAP.md`

Use this checklist with the following project standards:

- `AGENTS.md`
- `DOCUMENTATION_STYLE_GUIDE.md`
- `EDITORIAL_CONVENTIONS.md`
- `GLOSSARY_CONVENTIONS.md`
- `I18N_POLICY.md`

`PROJECT_CHARTER.md` is the highest-level governing document.
It is the source for preservation rules and project authority.

`DOCUMENTATION_BLUEPRINT.md` is a planning reference for document layers, document types, information architecture, and target conceptual structure.
It should be used when reviewing whether a page's architectural role is clear.

`ROADMAP.md` is a planning reference for implementation priorities, dependencies, milestones, and non-goals.
It should be used when reviewing whether a change fits the current implementation strategy.

The Project Standards are the day-to-day operational standards for AI behavior, page style, editorial authority, glossary management, and language policy.

In checklist tables, the `Source standard` column may cite `DOCUMENTATION_BLUEPRINT.md` or `ROADMAP.md` when the check depends on architectural or implementation-planning context.
Those citations do not make the Blueprint or Roadmap ordinary editing standards.

If standalone `INFORMATION_ARCHITECTURE_STANDARDS.md` or `LINKING_AND_NAVIGATION_CONVENTIONS.md` files are created later, use them as source standards for the relevant checks.
Until then, information architecture and linking checks are governed through `DOCUMENTATION_STYLE_GUIDE.md`.

---

## 2. Judgment Values

Use these judgment values.

| Judgment | Meaning |
| --- | --- |
| `Pass` | The item satisfies the relevant standard. |
| `Needs revision` | The item can be corrected through ordinary documentation editing. |
| `Needs confirmation` | The item requires confirmation from the project owner, an authorized scholarly editor, or an authorized technical maintainer where applicable. |
| `N/A` | The item does not apply to this change. |
| `Unresolved but recorded` | The issue is unresolved, explicitly recorded, and does not block accepting the current change. |

Unresolved status is not automatically a failure.
Do not force a conclusion when the standards require confirmation or further review.

---

## 3. Review Types

Use the lightest review type that fits the change.

| Review type | Use for |
| --- | --- |
| Mechanical check | File presence, Markdown structure, heading levels, link syntax, obvious path issues. |
| AI-assisted review | Standards-based structural review, risk detection, document type checks, I18N and glossary flags. |
| Human editorial review | Clarity, structure, scope, navigation, unresolved issue acceptability. |
| Human scholarly review / authorized approval | Scholarly interpretation, examples, citations, transcriptions, bibliography, identifiers, data specifications, encoding rules, official terms, official translations. |

AI involvement is not a reason for failure.
AI-assisted work must be traceable.

---

## 4. Minimal Acceptance Checklist

Use this checklist for routine documentation changes.

### Scope of Review

| Field | Value |
| --- | --- |
| Files reviewed |  |
| Change summary |  |
| Document layer |  |
| Document type |  |
| Language status |  |
| Review level |  |
| AI involvement |  |
| Reviewer |  |
| Review date |  |

Use `unresolved` for unknown or undecided fields.

### Minimal Checks

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Review scope is clear. |  |  | `AGENTS.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Changed files are identified. |  |  | `AGENTS.md` |  |
| Document role, layer, and type are clear or recorded as unresolved. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `DOCUMENTATION_BLUEPRINT.md` |  |
| Change does not conflict with higher-level standards. |  |  | `PROJECT_CHARTER.md`; `ROADMAP.md` |  |
| Protected content was not changed without confirmation. |  |  | `PROJECT_CHARTER.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Headings, titles, links, and navigation are appropriate for the change. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Terminology status was not invented or silently changed. |  |  | `GLOSSARY_CONVENTIONS.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Language policy is respected. |  |  | `I18N_POLICY.md` |  |
| Confirmation-required matters are identified. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Unresolved issues are recorded rather than forced into a conclusion. |  |  | `EDITORIAL_CONVENTIONS.md`; `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |
| AI involvement, if any, is traceable. |  |  | `AGENTS.md` |  |
| No unrelated files or content were changed. |  |  | `AGENTS.md`; `EDITORIAL_CONVENTIONS.md` |  |

Routine changes do not require a full review unless the change touches protected content, Core Documentation structure, terminology authority, or language-version alignment.

---

## 5. Full Documentation Review Checklist

Use this checklist for Core Documentation creation, major revisions, structural changes, dense page refactoring, or language-version alignment review.

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval when protected content is involved

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Page purpose is explicit. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Documentation layer is identified. |  |  | `DOCUMENTATION_BLUEPRINT.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Document type is identified. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Opening summary explains the page role. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Section structure supports the page purpose. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Information architecture distinguishes core reference from supporting material. |  |  | `DOCUMENTATION_BLUEPRINT.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Links and navigation express meaningful relationships. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Terminology use is preserved, linked, or flagged for glossary review. |  |  | `GLOSSARY_CONVENTIONS.md` |  |
| Examples and evidence are preserved unless confirmation exists. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Bibliography, citations, transcriptions, identifiers, data values, and specifications are protected. |  |  | `PROJECT_CHARTER.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Language coverage and language-version relationship are recorded where relevant. |  |  | `I18N_POLICY.md` |  |
| Required confirmations or approvals are identified. |  |  | `EDITORIAL_CONVENTIONS.md`; `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |
| Unresolved issues are recorded. |  |  | `EDITORIAL_CONVENTIONS.md`; `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |
| Overall acceptance judgment is recorded. |  |  | `REVIEW_CHECKLIST.md` |  |

---

## 6. Conditional Checklists

Use only the conditional checklists that apply.

### 6.1 New Page Review

Primary review types:

- Mechanical check
- AI-assisted review
- Human editorial review

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Page role is defined. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Documentation layer is appropriate or recorded as unresolved. |  |  | `DOCUMENTATION_BLUEPRINT.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Document type is appropriate. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Language status is defined or recorded as unresolved. |  |  | `I18N_POLICY.md` |  |
| File naming follows current policy or unresolved status is recorded. |  |  | `I18N_POLICY.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Title, H1, and front matter align. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Related pages and navigation are provided where useful. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Stable information is placed in the appropriate core layer. |  |  | `DOCUMENTATION_BLUEPRINT.md`; `DOCUMENTATION_STYLE_GUIDE.md`; `I18N_POLICY.md` |  |

### 6.2 Revision Review

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval when protected content is involved

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Original scholarly meaning is preserved. |  |  | `PROJECT_CHARTER.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Removed or relocated content is accounted for. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Examples, citations, transcriptions, identifiers, and specifications are preserved unless confirmed. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Conceptual links were not silently changed. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Language-version differences are recorded rather than automatically resolved. |  |  | `I18N_POLICY.md` |  |
| Change remains within the approved scope. |  |  | `AGENTS.md`; `EDITORIAL_CONVENTIONS.md` |  |

### 6.3 AI-Assisted Work Review

Primary review types:

- AI-assisted review
- Human editorial review

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Governing standards were identified. |  |  | `AGENTS.md` |  |
| Changed files were reported. |  |  | `AGENTS.md` |  |
| Protected content was not silently altered. |  |  | `AGENTS.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Confirmation-needed matters were flagged. |  |  | `AGENTS.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Preferred terms or official translations were not invented. |  |  | `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |
| One language version was not assumed to be automatically authoritative. |  |  | `I18N_POLICY.md` |  |
| Unresolved matters were not forced into a conclusion. |  |  | `EDITORIAL_CONVENTIONS.md`; `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |

AI involvement itself should not be judged as failure.

### 6.4 Document-Type-Specific Review

Use only the row matching the relevant document type.

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval when protected content is involved

| Document type | Check | Judgment | Evidence | Source standard | Notes |
| --- | ----- | -------- | -------- | --------------- | ----- |
| Overview | Introduces scope, audience, child pages, and related sections. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Concept Reference | Defines concepts and links to fuller data/rule/example pages as needed. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `GLOSSARY_CONVENTIONS.md` |  |
| Data Reference | Preserves file, field, schema, and data relationship meanings. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Rule Reference | States rules clearly and distinguishes rules from examples. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Methodology | Presents method and evidence categories without changing scholarly judgment. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Example / Case | Preserves example content and links to relevant core reference where needed. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Workflow | Describes workflow without redefining core concepts or data specifications. |  |  | `DOCUMENTATION_STYLE_GUIDE.md` |  |
| Record | Preserves time/status context and does not rewrite record content as current rule. |  |  | `DOCUMENTATION_STYLE_GUIDE.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Glossary Entry | Records status, source pages, definition source, and unresolved issues where applicable. |  |  | `GLOSSARY_CONVENTIONS.md` |  |

### 6.5 I18N Review

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval when language differences affect protected content

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Page language status is identified or recorded as unresolved. |  |  | `I18N_POLICY.md` |  |
| `bilingual-required` pages have corresponding versions or translation-pending status recorded. |  |  | `I18N_POLICY.md` |  |
| `bilingual-recommended` pages are not treated as automatically failing if one version is absent. |  |  | `I18N_POLICY.md` |  |
| `language-specific` pages are accepted as complete when policy allows. |  |  | `I18N_POLICY.md` |  |
| `translation-pending`, `alignment-review-needed`, `legacy`, or `unresolved` status is recorded when applicable. |  |  | `I18N_POLICY.md` |  |
| Case Studies and Blog Posts are not treated as failed solely because they are Japanese-only by policy. |  |  | `I18N_POLICY.md` |  |
| Supplementary language availability is recorded separately from page language status when relevant. |  |  | `I18N_POLICY.md` |  |
| Language differences are classified before being resolved. |  |  | `I18N_POLICY.md` |  |
| Audience adaptation does not change core concepts, data specifications, identifiers, encoding rules, or scholarly judgment. |  |  | `I18N_POLICY.md`; `EDITORIAL_CONVENTIONS.md` |  |

Language difference categories:

- `expression difference`
- `supplementary difference`
- `update-timing difference`
- `substantive inconsistency`
- `scholarly nuance difference`
- `reader-adaptation difference`
- `unresolved difference`

### 6.6 Glossary and Terminology Review

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval for normative terminology decisions

| Check | Judgment | Evidence | Source standard | Notes |
| ----- | -------- | -------- | --------------- | ----- |
| Term status was not silently changed. |  |  | `GLOSSARY_CONVENTIONS.md`; `EDITORIAL_CONVENTIONS.md` |  |
| Preferred, accepted variant, deprecated, or official translation status was not invented. |  |  | `GLOSSARY_CONVENTIONS.md` |  |
| Provisional and unresolved status are used where authority is not established. |  |  | `GLOSSARY_CONVENTIONS.md` |  |
| Source pages are recorded where needed. |  |  | `GLOSSARY_CONVENTIONS.md` |  |
| Definition source is recorded where needed. |  |  | `GLOSSARY_CONVENTIONS.md` |  |
| Reading, romanization, translation, and official English term roles are not confused. |  |  | `GLOSSARY_CONVENTIONS.md`; `I18N_POLICY.md` |  |
| Glossary entry does not replace full Concept/Data/Rule/Methodology explanation. |  |  | `GLOSSARY_CONVENTIONS.md`; `DOCUMENTATION_STYLE_GUIDE.md` |  |

### 6.7 Editorial Authority Review

Primary review types:

- AI-assisted review
- Human editorial review
- Human scholarly review / authorized approval where required

Apply the four authority levels from `EDITORIAL_CONVENTIONS.md`.
This checklist does not create new authority.

| Authority level | Check | Judgment | Evidence | Source standard | Notes |
| --- | ----- | -------- | -------- | --------------- | ----- |
| Allowed | Change is ordinary documentation editing. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Allowed with Care | Meaning is preserved and risk has been considered. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Requires Confirmation | Required confirmation has been obtained or is recorded as pending. |  |  | `EDITORIAL_CONVENTIONS.md` |  |
| Prohibited Unless Explicitly Instructed | Explicit instruction exists, or the change was not made. |  |  | `EDITORIAL_CONVENTIONS.md` |  |

---

## 7. Recording Review Results

Use this template when recording a review result.
Keep it brief.

```markdown
## Review Result

Files reviewed:

Review level:

Overall judgment:

Revisions required:
- 

Confirmations required:
- 

Unresolved but recorded items:
- 

Reviewer:

Review date:
```

Overall judgment should use:

- `Pass`
- `Needs revision`
- `Needs confirmation`
- `Unresolved but recorded`

Use `N/A` only for individual checklist items.

---

### 7.1 Review Records vs. Checklist Execution

This checklist supports the judgment made during a review. It does not require every stored Review Record to reproduce every checklist row.

A summary-style Review Record is acceptable when it remains third-party traceable: scope, judgment, evidence, source standards, required actions, and unresolved items must all be recoverable from the record.

Preserve the full row-by-row checklist output when a strict audit trail is required.

Distinguish `files reviewed` from `files changed`. A review does not imply an edit.

For an audit-only review with no edit, `change summary` may be recorded as `no changes; review only` or equivalent.

A reusable template for summary-style Review Records is maintained outside `content/`, at `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`, so that blank or partially filled copies are never published as Hugo pages. It does not replace this checklist.

---

## 8. Boundary with Maintenance

This checklist is for deciding whether a specific new page, edit, revision, or standards change can be accepted.

It does not define recurring maintenance.

The following belong to future `MAINTENANCE_CONVENTIONS.md`:

- recurring review schedules
- periodic link checking
- stale-page detection
- routine language-alignment monitoring
- maintenance priority
- issue lifecycle
- archiving and deprecation workflow
- recurring ownership and assignment

Do not use this checklist to set maintenance frequency or schedules.

---

## 9. Summary Use

For routine changes, use:

- Scope of Review
- Minimal Acceptance Checklist
- Review Result

For major changes, add:

- Full Documentation Review Checklist
- relevant Conditional Checklists

For protected content, terminology authority, official translation, data specifications, identifiers, encoding rules, examples, citations, or manuscript readings, record `Needs confirmation` unless authorized approval already exists.
