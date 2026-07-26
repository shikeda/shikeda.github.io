# Review Trial Template

Reusable template for KRM Documentation Review Trial records, per `REVIEW_CHECKLIST.md` §7.1.

This file is kept outside `content/` deliberately, so that a blank or partially filled copy is never built or published as a Hugo page. It is not itself a Review Record.

**To use it**: copy this file, fill in every applicable bracketed field, and delete this instructional header. Following the convention already established by `content/docs/krm/governance/review-trials/REVIEW_TRIAL_001.md` and `REVIEW_TRIAL_002.md`, completed records currently live under `content/docs/krm/governance/review-trials/` as the next `REVIEW_TRIAL_NNN.md` — and are therefore published. Whether that should change is a separate decision, not implied by this template.

Delete any section that does not apply (for example, §9 when no external audit was performed) rather than leaving it as an empty placeholder.

This template supports the judgment already made during a review; it does not replace `REVIEW_CHECKLIST.md`, and a Review Record built from it does not need to reproduce every checklist row (see `REVIEW_CHECKLIST.md` §7.1).

---

## 1. Summary

[2–4 sentences: what was reviewed, what was found, what was fixed, what remains open, and the final judgment.]

---

## 2. Scope of Review

- **Primary files**: [file paths]
- **Related files**: [summary of inbound/outbound links, section indexes, ja/en counterparts, or other related files inspected — a summary, not a full re-listing]
- **Files changed**: [file paths actually changed in this trial, or `none — review only`. Keep this distinct from "files reviewed" above; a review does not imply an edit]
- **Document layer**: [per `DOCUMENTATION_BLUEPRINT.md`]
- **Document type**: [per `DOCUMENTATION_STYLE_GUIDE.md` §4]
- **Language status**: [per `I18N_POLICY.md` §6, or `not recorded`]
- **Review level**: [Mechanical check / AI-assisted review / Human editorial review / Human scholarly review — per `REVIEW_CHECKLIST.md` §3]
- **AI involvement**: [describe; confirm it is traceable per `AGENTS.md`]
- **Reviewer**: [name or AI reviewer identity]
- **Review date**: [ISO date]
- **Protected content**: [present / not present; if present, state whether it was touched — per `EDITORIAL_CONVENTIONS.md`]
- **Excluded concerns**: [what was deliberately out of scope, and why]

For an audit-only review with no edit, `Files changed` may simply read `none — review only`.

---

## 3. Review Progression

- **Minimal Review result**: [pass / needs revision / etc., and what it found]
- **Escalated to Full Review**: [yes / no]
- **Reason for escalation** (if yes): [cite the `REVIEW_CHECKLIST.md` §5 trigger condition that applied]
- **Conditional Reviews applied**: [list from `REVIEW_CHECKLIST.md` §6, each with a one-line reason. In a strict audit record, mark unused ones N/A with a short reason; in a lightweight record, items with no plausible relevance may simply be omitted]

---

## 4. Findings

Classify every finding into exactly one of the three groups below. Do not blend "required" and "candidate" items in one list.

For each finding, record what is possible from the following fields. Distinguish confirmed evidence from assumption.

- **Issue**: [one-line description]
- **File and location**: [path:line]
- **Evidence**: [what was actually observed/verified]
- **Classification**: [mechanical / editorial / technical / linguistic / scholarly]
- **Severity / Impact**: [brief]
- **Proposed action**: [what would resolve it]
- **Authority status**: one of `Allowed under existing standards; no additional approval required` / `Allowed with Care` / `Requires Confirmation`. These map directly onto the `Allowed`, `Allowed with Care`, and `Requires Confirmation` levels in `EDITORIAL_CONVENTIONS.md`'s Authority Matrix — this template does not define new authority levels. If a finding falls under `Prohibited Unless Explicitly Instructed`, state that explicitly and do not act without instruction.
- **Human confirmation required**: [yes / no]
- **Resolution / Disposition**: [`fixed and verified` / `deferred` / `Approval obtained` (approver, date) / `not actioned this round`, etc. — this records the outcome, it is not itself a fourth authority level]

### Required Revisions

[Findings that must be resolved, or explicitly deferred with reason, before Overall judgment can be `Pass`.]

### Non-blocking Improvement Candidates

[Findings recorded for the backlog. Explicitly not required before acceptance. State why each is non-blocking.]

### Unresolved but Recorded

[Findings that are neither a required fix nor a backlog candidate — e.g. items a governing standard explicitly does not yet require (cite the standard), or acceptable differences already classified as such (e.g. an `I18N_POLICY.md` §10 difference category).]

---

## 5. Maintenance Flow

Use the full chain when a strict audit trail is needed:

```text
detect → record → classify → assign → review → determine authority →
update when permitted → verify → record outcome → preserve state →
close or carry forward
```

For a routine, single mechanical fix, a lightweight one-line record is sufficient — do not build a full table for it:

```text
detected → recorded → classified as mechanical →
assigned under user instruction → reviewed →
Allowed under existing standards; no additional approval required →
updated → verified → outcome recorded → remaining items carried forward → closed
```

[Record the flow actually followed, in either form, adapting the middle steps to what happened.]

---

## 6. Change and Validation

- **Files changed**: [paths, or `none`]
- **Verification method**: [e.g. `git status --short`, `git diff`, a Hugo build, rendered-output inspection — whatever was actually used]
- **Build result** (only if a Hugo build was run): [page counts, error count]
- **Protected-content check**: [confirm no protected content — terminology, examples, data specifications, image or citation attributes — was altered]

---

## 7. Final Review Result

- **Overall judgment**: [`Pass` / `Needs revision` / `Needs confirmation` / `Unresolved but recorded`]
- **Required revisions remaining**: [list, or `none`]
- **Confirmation-blocking issues**: [list, or `none`]
- **Non-blocking improvement candidates**: [list, or `none`]
- **Unresolved but recorded**: [list, or `none`]
- **Files changed**: [paths, or `none`]
- **Validation performed**: [summary]
- **Reviewer**: [name]
- **Review date**: [ISO date]

---

## 8. Governance Observations

[Freeform: what this trial revealed about the review process, the standards stack, or the checklist itself — not about the reviewed page's content. Distinguish confirmed fact from inference. Proposals to change a governing standard belong here as proposals, not as edits made in the same trial.]

---

## 9. Audit Outcome (only if an external audit was performed)

[Delete this entire section if no external audit occurred. If one did: name the auditor/process, and record its findings, distinguishing the audit's judgment from this trial's own self-assessment in §7–8.]
