# Translation Review Trial Template

Reusable template for KRM Documentation Translation Review Trial records, per
`project/workflows/translation-workflow.md` §6.2.

This is a sibling artifact to `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`, adapted for
translation tasks specifically (Japanese → English, per the current translation direction). A
content Review Trial asks whether a page is internally correct against the governing standards; a
Translation Review Trial asks whether an English rendering is accurate, terminologically
consistent with previously translated pages, and free of untranslated fragments or unauthorized
scholarly additions — it does not re-litigate the Japanese source's own correctness (that is the
job of the ordinary Review Trial process).

This file is kept outside `content/` deliberately, so that a blank or partially filled copy is
never built or published as a Hugo page. It is not itself a Translation Review Record.

**To use it**: copy this file, fill in every applicable bracketed field, and delete this
instructional header. Completed records live alongside this template, under
`governance/translation-review-trials/`, as the next `TRANSLATION_REVIEW_TRIAL_NNN.md`.

Delete any section that does not apply rather than leaving it as an empty placeholder.

---

## 1. Summary

[2–4 sentences: which file was translated, what terminology/context questions came up, what was
confirmed with the project owner, and the final status (complete / partial / blocked).]

---

## 2. Scope

- **Source file**: [path to the `.ja.md` file translated]
- **Target file**: [path to the `.en.md` file created or updated]
- **Related files consulted for terminology precedent**: [paths — e.g. sibling already-translated
  pages, `GLOSSARY_CONVENTIONS.md`]
- **Files changed**: [paths actually changed — the target `.en.md`, and any other file touched,
  e.g. the `.ja.md` source if a data gap was corrected under separate instruction]
- **Translator**: [name or AI identity]
- **Translation date**: [ISO date]

Per `project/workflows/translation-workflow.md` §5: **the Japanese source file must not be
modified** as part of ordinary translation work. If a `.ja.md` change was made in the same
session, it must have been under separate, explicit instruction (e.g. correcting a data error
found while translating) — state that explicitly here, distinct from the translation itself.

---

## 3. Terminology Decisions

[List each significant term/phrase where an English rendering had to be chosen or confirmed.
For each: the Japanese term, the English rendering adopted, and the precedent or reasoning
(existing glossary entry, an already-translated sibling page, a project-owner confirmation, or a
new decision made in this trial). Distinguish terms that reuse established precedent from terms
decided for the first time in this trial — the latter become precedent for future trials.]

| Japanese term | English rendering | Basis |
| --- | --- | --- |
| [term] | [rendering] | [existing precedent (cite file) / new decision, confirmed by project owner on DATE / new decision, low-risk, not escalated] |

---

## 4. Questions Raised and Owner Confirmations

[Every point where translation could not proceed on precedent alone — ambiguous terminology,
uncertain context, a passage bordering on scholarly interpretation, or a data issue noticed while
translating (e.g. a source-table gap). For each: what was asked, and the project owner's answer
(or "not yet resolved" if still open). This section is the translation-specific equivalent of a
content Review Trial's Unresolved/Confirmation items — do not silently resolve anything in this
category without confirmation, per `project/workflows/translation-workflow.md` §4.]

---

## 5. Translation-Specific Issues

[Anything that doesn't fit cleanly into §3/§4: untranslated fragments found and fixed, formatting
or structural mismatches between the `.ja.md` and `.en.md` versions, quoted primary-source
material and how it was handled (kept in original script vs. translated — per §3's "Primary
Sources" guideline), or any place structural parity with the Japanese source was not maintained
(and why, since `translation-workflow.md` §3 requires project-owner approval for that).]

---

## 6. Change and Validation

- **Files changed**: [paths]
- **Verification method**: [e.g. `git status --short`, `git diff`, a Hugo build, rendered-output
  inspection]
- **Build result** (if a Hugo build was run): [page counts, error count]
- **Protected-content check**: [confirm quoted transcriptions, citations, and data values were
  reproduced faithfully rather than paraphrased]

---

## 7. Final Review Result

- **Overall status**: [`Complete` / `Complete, pending owner confirmation on open items` /
  `Partial — stopped for confirmation` ]
- **Open items remaining**: [list, or `none`]
- **Files changed**: [paths]
- **Translator**: [name or AI identity]
- **Translation date**: [ISO date]

---

## 8. Remaining Follow-up Actions

[e.g. "glossary update required for term X," "the next file in the translation queue is Y," "an
issue was found in the Japanese source and logged in `project/issues.md`," "a site-wide sweep for
pattern Z is still pending." This section feeds directly into what `project/workflows/
translation-workflow.md` §2 should be updated to for the next execution, and into `project/
translation-backlog.md` once the whole section is complete.]
