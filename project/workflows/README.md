# Workflows

This directory holds reusable task prompts — Standard Operating Procedures for recurring, ongoing
work on `content/docs/krm/` — as distinct from `project/issues.md` and
`project/translation-backlog.md`, which are point-in-time status records.

## Files

- **[translation-workflow.md](./translation-workflow.md)** — the SOP for translating a KRM
  Documentation page from Japanese to English. It is written as a directly reusable AI prompt: §2
  ("Current Translation Target") is a live field, updated to the next file in the queue at the end
  of each translation task, so the document is always ready to hand to the next translation
  session as-is.

## How this relates to the rest of `project/`

- **`project/translation-backlog.md`** lists *which* pages still need translation, grouped by
  category (Core Documentation / Summary Only / Japanese Only). It is updated in batches (per
  project-owner instruction, only once all of a section's pending translations are complete), not
  after every individual file.
- **`translation-workflow.md`** (this directory) defines *how* each individual translation task is
  carried out — terminology precedent, escalation rules for ambiguous terms or scholarly
  interpretation, required deliverables, and structural-parity requirements.
- **`governance/translation-review-trials/`** (repository root, non-published — sibling to
  `governance/review-trials/`) is where the deliverable defined in `translation-workflow.md` §6.2
  actually lands: one `TRANSLATION_REVIEW_TRIAL_NNN.md` per translation task, recording the
  terminology decisions made, questions raised and how the project owner resolved them, and any
  follow-up actions. `TRANSLATION_REVIEW_TEMPLATE.md` in that directory is the reusable template
  for these records, mirroring `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`'s role for
  ordinary content Review Trials.

In short: `translation-backlog.md` tracks the queue, `translation-workflow.md` is the prompt run
for each item in the queue, and `governance/translation-review-trials/` is the resulting audit
trail.

## Maintenance

After each translation task, update `translation-workflow.md` §2 to point at the next file in
`project/translation-backlog.md`'s Core Documentation list, so the prompt is ready to reuse
immediately. If a translation task surfaces a terminology decision, ambiguity, or issue worth
carrying forward (e.g. affecting other not-yet-reviewed pages), log it in `project/issues.md`
rather than leaving it only inside a single trial record.
