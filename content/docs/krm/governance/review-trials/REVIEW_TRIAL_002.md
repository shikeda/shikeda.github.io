## Review Trial 002

Purpose: Second pilot of the KRM Documentation review workflow, run against a Concept Reference page rather than a Data Reference page (Trial 001), to test whether the same governance stack and checklist procedure generalize across document types. This record does not redo the review; it documents what was already performed.

---

### 1. Summary

A pilot acceptance review was run on a core terminology-defining Concept Reference page using the full governance document stack. The initial request specified a target path with an extra, non-existent directory level; this was resolved against the actual repository structure before proceeding. The review confirmed one pre-documented broken-link issue (required revision) and discovered one previously undocumented rendering defect (required revision), plus one structural gap (non-blocking improvement candidate) and two low-impact items (unresolved but recorded). Only the two required revisions were fixed, verified with a Hugo build comparing generated output across language versions, and re-checked with the Minimal Acceptance Checklist. No protected content — terminology definitions, transcribed examples, or image attributes — was altered.

---

### 2. Scope of Review

- **Primary files**: `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md`, `content/docs/krm/03-entry-data-model/03-01-data-structure.en.md`
- **Path resolution note**: the review request specified `.../03-01-data-structure/03-01-data-structure.{ja,en}.md`, an extra directory level that does not exist in the repository. The actual files, at `content/docs/krm/03-entry-data-model/03-01-data-structure.{ja,en}.md`, were confirmed to exist and used as the primary target; the discrepancy was disclosed rather than silently assumed away.
- **Related files (summary)**: KRM and section landing pages (`content/docs/krm/_index.{ja,en}.md`, `03-entry-data-model/_index.{ja,en}.md`), a page that links into this one (`03-entry-data-model/03-04-data-example.{ja,en}.md`), the link-target section (`04-entry-input/`) to confirm real vs. stale paths, and `CURRENT_STATE_REPORT.md` for the pre-existing known-issue claim
- **Document layer**: Conceptual Reference (`DOCUMENTATION_BLUEPRINT.md` Layer 2)
- **Document type**: Concept Reference, with embedded Example/Case content (a dense page per `DOCUMENTATION_STYLE_GUIDE.md` §11)
- **Language status**: bilingual-required by policy (ja/en pair present); no explicit `Page language status` front-matter field recorded
- **Review level**: AI-assisted review — Minimal Acceptance Checklist, escalated to Full Documentation Review Checklist, plus applicable Conditional Checklists (I18N Review, Document-Type-Specific: Concept Reference, Glossary and Terminology Review, AI-Assisted Work Review)
- **AI involvement**: Full — review, fix, and re-verification all performed by Claude Code in this session; traceable in this record
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-26
- **Protected content**: Present — this page defines core terminology (`Entry`, `Headword`, `Original Glosses`, etc.) named by `ROADMAP.md` Priority 3 as a core terminology source, and contains transcribed manuscript examples with a facsimile image. Not touched: no definition, transcription, or image attribute (`src`/`alt`/`width`) was changed; edits were confined to link-path text and shortcode delimiter syntax.

---

### 3. Review Progression

Minimal → Full escalation reason: the target is a core terminology source page (`ROADMAP.md` Priority 3) implicated in language-version alignment, both explicit Full-checklist trigger conditions under `REVIEW_CHECKLIST.md` §5. Minimal Review alone detected F1 via its "links and navigation" item. F2 was not detectable from the Minimal checklist and only surfaced while working through the Full checklist's "links and navigation express meaningful relationships" item — and even then, source inspection alone (noticing stray backslashes) was not sufficient to confirm it as a real defect rather than a harmless stylistic quirk. Confirming F2 required comparing rendered Hugo build output between the Japanese and English versions of the page.

---

### 4. Findings

**Required Revision**

- **F1** (known issue, confirmed) — `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md`, lines 110–111. Old links: `/docs/notes/krm/04-entry-input/` and `/docs/notes/krm/04-entry-input/04-03-handling/`. Corrected to `/docs/krm/04-entry-input/` and `/docs/krm/04-entry-input/04-03-handling/`. This matches an issue already named in `CURRENT_STATE_REPORT.md`'s list of pages retaining stale `/docs/notes/...` paths; the correct target was confirmed unambiguous because the English version already used the corrected path at the equivalent location. Classification: mechanical, Allowed under `EDITORIAL_CONVENTIONS.md`. No confirmation required.
- **F2** (newly detected, not previously documented) — `content/docs/krm/03-entry-data-model/03-01-data-structure.en.md`, line 50. Old: `{{\< figure src="/images/krm-item-sample1.png" alt="entry structure" width="500px" \>}}` (backslash-escaped, not a valid Hugo shortcode). Corrected to `{{< figure src="/images/krm-item-sample1.png" alt="entry structure" width="500px" >}}`. Not listed in `CURRENT_STATE_REPORT.md` or `ROADMAP.md`. Confirmed only by building the site and comparing output: before the fix, the Japanese page rendered `<figure><img ...></figure>`, while the English page rendered the literal escaped shortcode text with no image at all. Classification: mechanical/technical (Hugo shortcode syntax), Allowed. No confirmation required; image path, alt text, and width were not altered.

**Non-blocking Improvement Candidate**

- **F3** — No outbound cross-references to sibling concept pages (`03-02-types-of-entries`, `03-03-concepts-char`) in the page body. Deliberately kept separate from F1/F2 and left unaddressed in this trial: navigation is not broken (both pages remain reachable via the section index), so this falls short of `DOCUMENTATION_STYLE_GUIDE.md` §4's "related concepts" guidance without being a required fix. Recorded as backlog only.

**Unresolved but Recorded**

- **F4** — English version uses bold+backtick emphasis not mirrored in the Japanese version; classified as `reader-adaptation difference` under `I18N_POLICY.md` §10, acceptable audience adaptation.
- **F5** — Commented-out front-matter fields, a site-wide pattern also observed in Trial 001, not specific to this page.

---

### 5. Maintenance Flow

```text
detected → recorded → classified as mechanical (F1: known-issue confirmation; F2: newly detected via rendered-output check) → assigned under user instruction → reviewed → authorized under existing standards → updated → verified via Hugo build → closed
```

---

### 6. Change and Validation

- **Changed files**: `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md` (two link paths, F1), `content/docs/krm/03-entry-data-model/03-01-data-structure.en.md` (one shortcode delimiter fix, F2). No other file was modified.
- **Verification method**: `git status --short` before and after editing (clean → only the two target files); `git diff` confirming both diffs were limited to the designated lines; `hugo --minify` build to a scratch destination.
- **Build result**: 158 JA pages / 51 EN pages, 0 build errors.
- **Rendered-output checks**: the Japanese page's generated HTML resolves to `/docs/krm/04-entry-input/` and `/docs/krm/04-entry-input/04-03-handling/` with zero remaining occurrences of `docs/notes`; the English page's generated HTML contains `<figure><img src=/images/krm-item-sample1.png alt="entry structure" width=500px></figure>` with zero remaining occurrences of escaped shortcode text.
- **Protected-content check**: image `src`/`alt`/`width` values, terminology definitions, and transcribed examples were confirmed unchanged — the diff touches only link-path text and shortcode delimiter syntax, nothing else.
- **Re-check**: Minimal Acceptance Checklist was re-run against the two-file diff after the fix; all items returned `Pass`.

---

### 7. Final Review Result

- **Overall judgment**: Pass
- **Required revisions remaining**: none (F1, F2 resolved and verified)
- **Confirmation-blocking issues**: none
- **Non-blocking improvement candidate**: F3 (sibling concept-page cross-references), explicitly not addressed this round
- **Unresolved but recorded**: F4, F5 — carried forward, none blocking
- **Files changed**: `03-01-data-structure.ja.md`, `03-01-data-structure.en.md`
- **Validation performed**: `git status --short`, `git diff`, `hugo --minify` build (158 JA / 51 EN, 0 errors), rendered-output inspection of both language versions
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-26

---

### 8. Governance Observations

- The review request's target path did not match the repository (an extra directory level). Resolving this against the actual file structure, and disclosing the discrepancy, was a precondition for a valid Scope of Review — an unverified path would have invalidated the rest of the trial.
- F1 and F2 illustrate two different roles a review can play: confirming a pre-documented item of known technical debt as fact (F1), versus discovering an undocumented defect that no prior standard or report had recorded (F2).
- F2 specifically shows that source inspection alone is not always sufficient: the escaped shortcode was visible in the raw file, but only a rendered-output comparison (Hugo build, JA vs. EN) established that it was a material defect — complete loss of the illustrative image for English readers — rather than a stylistic non-issue.
- The Required Revision / Non-blocking Improvement Candidate distinction was preserved through to execution: F1 and F2 were fixed under `Allowed` authority with no confirmation needed, while F3 was deliberately left unaddressed and recorded as backlog rather than folded into this round's scope.
- No protected content was touched. Terminology definitions, transcribed manuscript examples, and the image's `src`/`alt`/`width` attributes remained byte-identical before and after the fix; only link-path text and shortcode delimiter syntax changed.
