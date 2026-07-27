## Review Trial 001

Purpose: Validate the KRM Documentation review workflow (`REVIEW_CHECKLIST.md` plus the governing standards stack) against a real Core Documentation page, and leave an auditable lightweight record of the review, the mechanical fix applied, and its verification. This record does not redo the review; it documents what was already performed.

---

### 1. Summary

A pilot acceptance review was run on a Data Reference page using the full governance document stack. The review surfaced one confirmed broken internal link (required revision) and one structural gap (non-blocking improvement candidate), plus three low-impact items recorded as unresolved but not requiring action. Only the required revision was fixed, verified with a Hugo build, and re-checked with the Minimal Acceptance Checklist. A subsequent Codex governance audit judged the review's procedural design as `Pass` and its record completeness as `Needs revision`; this document is the completion of that record.

---

### 2. Scope of Review

- **Primary files**: `content/docs/krm/02-data-overview/02-03-headword-chars.ja.md`, `content/docs/krm/02-data-overview/02-03-headword-chars.en.md`
- **Related files (summary)**: KRM landing pages (`content/docs/krm/_index.ja.md`, `.en.md`), the `02-data-overview` section index (`.ja.md`, `.en.md`), and pages that reference `krm_headword_chars` in prose or links (`04-entry-input/04-01-id.*.md`, `03-entry-data-model/03-02-types-of-entries.*.md`, `04-entry-input/04-02-char.*.md`), plus `CURRENT_STATE_REPORT.md` for the pre-existing known-issue claim
- **Document layer**: Data Reference (`DOCUMENTATION_BLUEPRINT.md` Layer 3)
- **Document type**: Data Reference (`DOCUMENTATION_STYLE_GUIDE.md` §4)
- **Language status**: bilingual-required by policy (ja/en pair present); no explicit `Page language status` front-matter field recorded (see F3)
- **Review level**: AI-assisted review — Minimal Acceptance Checklist, escalated to Full Documentation Review Checklist, plus applicable Conditional Checklists (I18N Review, Document-Type-Specific: Data Reference, Glossary and Terminology Review, AI-Assisted Work Review)
- **AI involvement**: Full — review, fix, and re-verification all performed by Claude Code in this session; traceable in this record
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-26
- **Protected content**: Not touched. Column/field definitions and data specifications in the primary files were read and evaluated but never edited.

---

### 3. Review Progression

Minimal → Full escalation reason: the target is Core Documentation (Data Reference), which `REVIEW_CHECKLIST.md` §5 identifies as warranting the Full checklist. In practice, the Minimal checklist alone detected F1 (broken link) via its "links and navigation" item, but did not surface F2 — the missing cross-references to `krm_main`/`krm_notes`/`krm_wakun` and related rule pages only emerged from the Full checklist's "links and navigation express meaningful relationships" item together with the Data Reference structure expected by `DOCUMENTATION_STYLE_GUIDE.md` §4. This confirmed the escalation criterion added real value rather than being redundant.

---

### 4. Findings

**Required Revision**

- **F1** — `content/docs/krm/_index.en.md`, line 34. Old link: `./02-data-overview/02-03-headword_chars/`. Corrected link: `./02-data-overview/02-03-headword-chars/`. Classification: mechanical, Allowed under `EDITORIAL_CONVENTIONS.md`'s authority matrix ("fix stale links when the intended target is clear"). No confirmation required.

**Non-blocking Improvement Candidate**

- **F2** — `krm_main`/`krm_notes`/`krm_wakun` and related-rule mentions in the primary files are plain backticked text, not hyperlinks. This is classified as non-blocking, not a required revision, because it does not break navigation (no invalid target, unlike F1) and only falls short of `DOCUMENTATION_STYLE_GUIDE.md` §4's recommended Data Reference structure ("relationship to other files," "related rules"). Deferred as backlog; Allowed-level change, no confirmation required.

**Unresolved but Recorded**

- **F3** — No `Page language status` front-matter field on either primary file. Not required now: `I18N_POLICY.md` §17 does not yet mandate this metadata.
- **F4** — English version uses bold+backtick emphasis (e.g. `**\`Headwords\`**`) not mirrored in the Japanese version. Classified as `reader-adaptation difference` / `expression difference` under `I18N_POLICY.md` §10; acceptable audience adaptation, not a data or concept inconsistency.
- **F5** — Commented-out front-matter fields (`# bookFlatSection: false`, etc.) are a site-wide pattern, not specific to this page; out of this trial's page-level scope.

---

### 5. Maintenance Flow

```text
detected → recorded → classified as mechanical → assigned under user instruction → reviewed → authorized under existing standards → updated → verified → closed
```

---

### 6. Change and Validation

- **Changed file**: `content/docs/krm/_index.en.md` (one line, F1 only). No other file was modified.
- **Verification method**: `hugo --minify --destination <scratch dir>` build, followed by inspection of the generated output.
- **Build result**: 157 JA pages / 51 EN pages, 0 build errors. The corrected target page (`en/docs/krm/02-data-overview/02-03-headword-chars/index.html`) exists in the output; the old underscore path does not exist; the rendered link on the KRM English landing page resolves to `.../02-03-headword-chars/`.
- **Re-check**: Minimal Acceptance Checklist was re-run against the single-line diff after the fix; all items returned `Pass`.

---

### 7. Final Review Result

- **Overall judgment**: Pass (post-fix, Minimal Acceptance Checklist)
- **Revisions required**: none remaining (F1 resolved and verified)
- **Confirmations required**: none
- **Unresolved but recorded**: F2 (non-blocking improvement candidate), F3, F4, F5 — all carried forward, none blocking

---

### 8. Governance Observations

- Evidence recorded at file:line level made it possible to confirm the pre-existing known-issue claim (`ROADMAP.md`, `CURRENT_STATE_REPORT.md`) as verified fact rather than assumption, and to distinguish it from a newly surfaced item (F2).
- `REVIEW_CHECKLIST.md` does not explicitly distinguish an audit of existing, unchanged content from a review of an active edit; several Minimal Checklist fields ("changed files," "change summary") required reinterpretation for this trial.
- `REVIEW_CHECKLIST.md` has no standalone conditional checklist for link/navigation review; it is currently covered indirectly through the Minimal/Full generic items and `DOCUMENTATION_STYLE_GUIDE.md` §8.
- The initial review output existed only as an in-session report; without a persisted record such as this file, the review would not have been independently auditable — consistent with the Codex audit finding below.

---

### 9. Codex Audit Outcome

An independent Codex governance audit of this trial found:

- **Procedure design**: `Pass` — the review correctly applied the governing document hierarchy, used the Minimal→Full escalation path appropriately, and distinguished required revisions from non-blocking candidates.
- **Record completeness**: `Needs revision` — the review and fix had been reported only in-session, with no persisted, third-party-auditable record under `content/docs/krm/governance/`. This document was created to close that gap.
