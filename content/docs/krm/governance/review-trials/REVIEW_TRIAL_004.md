## Review Trial 004

Purpose: Fourth pilot of the KRM Documentation review workflow, run in the combined review-and-fix mode established in Trial 003. Target is the KRM Editorial/Encoding Rules layer (`04-entry-input/`) — specifically the ID system page (a dense Rule Reference / Concept Reference page) and its section index.

---

### 1. Summary

A combined review-and-fix pass was run on the `04-entry-input/` section index and its ID-system article, in both languages. Four mechanical defects were found and fixed directly under `Allowed` authority: two data-file-name formatting inconsistencies (hyphen instead of the established underscore convention) and two broken internal links (one stale `/docs/notes/...` path, one malformed relative path with a duplicated segment) — all in the Japanese and English section-index pages. Two further items were found in the English ID-system article that involve page-status framing and an apparently self-contradictory editorial note about example data; these were left unmodified and recorded as `Requires Confirmation`. All fixes were verified with a Hugo build comparing rendered output before and after.

**Confirmation update (2026-07-27, same day)**: the project owner reviewed UR1 and UR2 and approved deletion of both. Both were removed from `04-01-id.en.md` and verified with a further Hugo build. See §4 and §6 for details.

---

### 2. Scope of Review

- **Primary files**: `content/docs/krm/04-entry-input/04-01-id.ja.md`, `content/docs/krm/04-entry-input/04-01-id.en.md`, `content/docs/krm/04-entry-input/_index.ja.md`, `content/docs/krm/04-entry-input/_index.en.md`
- **Related files**: `content/docs/krm/_index.ja.md` / `.en.md` (inbound links into this section), `content/docs/krm/03-entry-data-model/03-01-data-structure.ja.md` / `.en.md` (inbound links into this section, both already corrected in Trial 002), `content/docs/krm/02-data-overview/02-03-headword-chars.*.md` (outbound link target from `04-01-id.*.md`), `content/docs/krm/07-progress/_index.md` / `1.md` / `2.md` (checked to confirm that `krm-main`/`krm-notes` hyphenated forms found there are unrelated legacy URL path segments, not evidence of an alternate real file-naming convention)
- **Files changed**: `content/docs/krm/04-entry-input/_index.ja.md` (2 lines), `content/docs/krm/04-entry-input/_index.en.md` (1 line)
- **Document layer**: `_index.*.md` is Editorial and Encoding Rules Orientation (section index); `04-01-id.*.md` is a dense page combining Concept Reference (Headword/Entry definitions) and Rule Reference (ID-format rules) content, per `DOCUMENTATION_BLUEPRINT.md` Layer 4
- **Document type**: `_index.*.md` — Overview; `04-01-id.*.md` — Rule Reference with embedded Concept Reference material (`DOCUMENTATION_STYLE_GUIDE.md` §4)
- **Language status**: bilingual-required by policy (ja/en pairs present for both files)
- **Review level**: AI-assisted review — Minimal Acceptance Checklist, escalated to Full Documentation Review Checklist (Editorial and Encoding Rules is Core Documentation, and `04-01-id.*.md` is explicitly named as a core terminology source area in `ROADMAP.md` Priority 3)
- **AI involvement**: Full — review, fix, and verification all performed by Claude Code in this session; traceable in this record
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27
- **Protected content**: Present — ID-format specifications (F/S/K/T formats), worked examples of ID assignment rules, and citations to the Kazama and Tenri facsimile editions. Not touched by the four fixes made; the two items that touch page-status framing and example interpretation (UR1–UR2 below) were deliberately left unmodified rather than resolved.
- **Excluded concerns**: The correctness of the ID-format rules themselves (e.g., the Character Order assignment logic) was not independently verified against the underlying database; the worked K-format/T-format examples' numeric values were not re-derived from source data.

---

### 3. Review Progression

- **Minimal Review result**: needs revision — detected the stale `/docs/notes/...` path and the malformed relative link in the two `_index.*.md` files via the "links and navigation" item.
- **Escalated to Full Review**: yes.
- **Reason for escalation**: `04-01-id.*.md` is Core Documentation and is explicitly named in `ROADMAP.md` Priority 3 as a core terminology source page, meeting the "Core Documentation" trigger condition in `REVIEW_CHECKLIST.md` §5. Escalation, combined with a data-file-name consistency check under `EDITORIAL_CONVENTIONS.md` §6, surfaced the two `krm-main.tsv`/`krm-notes` hyphenation inconsistencies that the Minimal checklist's link-focused item would not have caught, plus the two Requires-Confirmation items in §4.
- **Conditional Reviews applied**: Link and Navigation review (found RR3, RR4), Document-Type-Specific: Rule Reference / Overview, Glossary and Terminology Review (checked `krm_main`/`krm_notes` file-name consistency; found RR1, RR2), AI-Assisted Work Review (this trial's own traceability). I18N Review: applied — found UR1 as a ja/en-only divergence (the "Under preparation." marker has no Japanese counterpart).

---

### 4. Findings

Authority status values used below follow `EDITORIAL_CONVENTIONS.md`'s Authority Matrix directly (see `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`).

#### Required Revisions

**RR1 — Data file name formatted with a hyphen instead of the established underscore convention**
- File and location: `content/docs/krm/04-entry-input/_index.ja.md:14`
- Evidence: `` `krm-main.tsv` `` (hyphen). Every other reference to this file across the site — including the English counterpart of this same page (`_index.en.md:13`, `` `krm_main.tsv` ``) and `04-01-id.ja.md:221` (`krm_main.tsv`) — uses the underscore form. A repository-wide check confirmed the only other hyphenated `krm-main`/`krm-notes` occurrences are unrelated legacy URL path segments under `07-progress/` (e.g. `/docs/notes/krm-main/progress/1/`), not an alternate real file name.
- Classification: mechanical
- Severity / Impact: Low — cosmetic, but could mislead a reader searching for the actual published file (which is `krm_main.tsv`).
- Proposed action: change `krm-main.tsv` to `krm_main.tsv`.
- Authority status: `Allowed under existing standards; no additional approval required` — `EDITORIAL_CONVENTIONS.md` §6 "Data file names" row: "Format names such as `krm_main` consistently" is `Allowed`.
- Human confirmation required: No
- Resolution / Disposition: fixed and verified.

**RR2 — Same issue for `krm_notes`**
- File and location: `content/docs/krm/04-entry-input/_index.ja.md:16`
- Evidence: `` `krm-notes` `` (hyphen), versus the underscore form used in the English counterpart (`_index.en.md:15`, `` `krm_notes` ``) and elsewhere.
- Classification: mechanical
- Severity / Impact: Low — cosmetic.
- Proposed action: change `krm-notes` to `krm_notes`.
- Authority status: `Allowed under existing standards; no additional approval required`
- Human confirmation required: No
- Resolution / Disposition: fixed and verified.

**RR3 — Stale `/docs/notes/...` internal link**
- File and location: `content/docs/krm/04-entry-input/_index.ja.md:16`
- Evidence: `[公開データの概要](/docs/notes/krm/02-data-overview/)`. The current directory is `content/docs/krm/02-data-overview/`; the correct current path is `/docs/krm/02-data-overview/`, as already used consistently elsewhere on the site and as fixed under the same pattern in Trial 002's F1.
- Classification: mechanical
- Severity / Impact: Medium — a Core Documentation cross-reference to the Data Reference section was unreachable.
- Proposed action: remove the `/notes` segment.
- Authority status: `Allowed under existing standards; no additional approval required` — `EDITORIAL_CONVENTIONS.md` §7 "fixing stale links when the intended target is clear."
- Human confirmation required: No
- Resolution / Disposition: fixed and verified — Hugo build confirms the link resolves to `/docs/krm/02-data-overview/` with zero remaining `docs/notes` occurrences on the page.

**RR4 — Malformed relative link with a duplicated path segment**
- File and location: `content/docs/krm/04-entry-input/_index.en.md:15`
- Evidence: `[Overview of Public Data](../krm/02-data-overview/)`. From this page's location (`content/docs/krm/04-entry-input/_index.en.md`), the relative path `../krm/02-data-overview/` resolves to a non-existent `content/docs/krm/krm/02-data-overview/` path (one level up reaches `content/docs/krm/`, and the link then re-appends `krm/`).
- Classification: mechanical
- Severity / Impact: Medium — same cross-reference as RR3, broken in the English version.
- Proposed action: change to `../02-data-overview/`.
- Authority status: `Allowed under existing standards; no additional approval required`
- Human confirmation required: No
- Resolution / Disposition: fixed and verified — Hugo build confirms the link resolves to `../02-data-overview/`, matching the correct target, with zero remaining `krm/krm/` occurrences on the page.

#### Non-blocking Improvement Candidates

None identified in this trial beyond the items already recorded as Unresolved but Recorded below.

#### Unresolved but Recorded

**UR1 — Stray "Under preparation." status marker in a fully developed English article**
- File and location: `content/docs/krm/04-entry-input/04-01-id.en.md:11`
- Evidence: the line `Under preparation.` appears immediately after the front matter and before the H1 heading. The rest of the page (236 lines of detailed ID-system rules, worked examples, and citations) is fully developed and closely parallels the complete Japanese version, which has no equivalent status marker anywhere. `DOCUMENTATION_STYLE_GUIDE.md` §5 lists "temporary editorial notes" among things to avoid opening a page with.
- Classification: editorial/status
- Severity / Impact: Low-Medium — likely a leftover draft marker rather than an accurate status, but removing a status claim is more than a formatting fix: it asserts the page is complete, which is a judgment about the page's own state.
- Proposed action: confirm with the project owner whether this line should be removed (page is not actually under preparation) or whether it reflects a genuine, currently-accurate caveat.
- Authority status: `Requires Confirmation` — closest to `EDITORIAL_CONVENTIONS.md` §6 "Progress records" row: "Update status or counts" is `Requires Confirmation`.
- Human confirmation required: Yes
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: deletion approved. `Under preparation.` removed from `04-01-id.en.md:11`. Verified with a further Hugo build: the line no longer appears in the rendered output, and the page opens directly with the H1 heading, consistent with the Japanese version. Fixed and verified; closed.

**UR2 — Apparently self-contradictory editorial note about example data**
- File and location: `content/docs/krm/04-entry-input/04-01-id.en.md:165`
- Evidence: `"...would be as follows (using hypothetical Tenri IDs for illustration, actual examples below):"`, immediately followed by the "Examples of `tenri_location` IDs" list itself — i.e., the note claims the IDs shown are "hypothetical" while also saying "actual examples" follow "below," but the list that follows *is* the same set of IDs being introduced, not a separate "actual" list. The Japanese counterpart (`04-01-id.ja.md:182-183`) has no equivalent caveat and presents its parallel example list as ordinary illustrative examples, matching how the Kazama-edition examples are presented earlier in both language versions without any "hypothetical" qualifier.
- Classification: editorial/example-handling
- Severity / Impact: Low-Medium — likely another drafting artifact, but the note asserts something about the interpretive status of example data (real vs. hypothetical IDs), which `EDITORIAL_CONVENTIONS.md` §5 "Evidence and Example Handling" treats conservatively ("Requires Confirmation for changing... how [examples] are interpreted").
- Proposed action: confirm with the project owner whether the parenthetical should be removed (the Tenri IDs are presented as ordinary illustrative examples, consistent with the rest of the page) or whether it reflects an intentional distinction not otherwise documented.
- Authority status: `Requires Confirmation`
- Human confirmation required: Yes
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: deletion approved. The parenthetical `(using hypothetical Tenri IDs for illustration, actual examples below)` removed from `04-01-id.en.md:165`, leaving "...would be as follows:" flowing directly into the examples list. Verified with a further Hugo build: the phrase no longer appears in the rendered output, and the sentence reads correctly. Fixed and verified; closed.

---

### 5. Maintenance Flow

```text
detected → recorded → classified as mechanical (RR1–RR4) or Requires Confirmation (UR1–UR2) →
assigned under user instruction → reviewed →
Allowed under existing standards; no additional approval required (RR1–RR4) →
updated → verified → outcome recorded →
UR1–UR2 carried forward pending confirmation →
Approval obtained same day (UR1 deletion, UR2 deletion) →
UR1–UR2 updated → UR1–UR2 verified → outcome recorded → closed
```

---

### 6. Change and Validation

- **Files changed**: `content/docs/krm/04-entry-input/_index.ja.md` (2 lines: RR1, RR2+RR3 on the same line), `content/docs/krm/04-entry-input/_index.en.md` (1 line: RR4), `content/docs/krm/04-entry-input/04-01-id.en.md` (2 deletions for UR1 and UR2, after confirmation). `04-01-id.ja.md` was read and evaluated but not edited — it had no identified issues.
- **Verification method**: `git status --short` before editing (clean baseline); `git diff` after each round of editing; `hugo --minify` build to a scratch destination, run twice — once after RR1–RR4, once after the UR1/UR2 deletions.
- **Build result**: 160 JA pages / 51 EN pages, 0 build errors after RR1–RR4; 161 JA pages / 51 EN pages, 0 build errors after the UR1/UR2 deletions (the JA count increase reflects `REVIEW_TRIAL_004.md` itself becoming a built page between the two checks, the same effect noted in Trials 001–003).
- **Rendered-output checks**: the Japanese section-index page's generated HTML shows `krm_main.tsv` and `krm_notes` (underscore form) with zero remaining hyphenated occurrences, and its "Overview of Public Data" link resolves to `/docs/krm/02-data-overview/` with zero remaining `docs/notes` occurrences. The English section-index page's generated HTML shows the same link resolving to `../02-data-overview/` with zero remaining `krm/krm/` occurrences. After the UR1/UR2 deletions, the English ID-system article's rendered HTML contains zero occurrences of "Under preparation" and zero occurrences of "hypothetical," and the Tenri-location introductory sentence reads "...would be as follows:" flowing directly into the examples list.
- **Protected-content check**: none of the six changes (RR1–RR4, UR1, UR2) touched ID-format specifications, worked examples' data values, citations, or scholarly content. UR1 and UR2 removed editorial/status framing text only; the substantive rule and example content around them is unchanged.

---

### 7. Final Review Result

- **Overall judgment**: Pass
- **Required revisions remaining**: none (RR1–RR4 resolved and verified)
- **Confirmation-blocking issues**: none
- **Non-blocking improvement candidates**: none identified this trial
- **Unresolved but recorded**: none remaining — UR1 and UR2 confirmed and resolved (both deletions approved, applied, and verified); see §4
- **Files changed**: `04-entry-input/_index.ja.md`, `04-entry-input/_index.en.md`, `04-entry-input/04-01-id.en.md`
- **Validation performed**: `git status`, `git diff`, two `hugo --minify` builds (160 JA / 51 EN after RR1–RR4; 161 JA / 51 EN after the UR1/UR2 deletions), rendered-output inspection of all three affected pages
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27

---

### 8. Governance Observations

- RR1 and RR2 (file-name hyphenation) were found only because the English counterpart of the same page used the correct underscore form — a direct product of the routine ja/en side-by-side comparison established as a habit in earlier trials, not of any checklist item specifically naming "compare data file name spelling across languages." `GLOSSARY_CONVENTIONS.md`/`EDITORIAL_CONVENTIONS.md`'s "format consistently" authority made these easy to classify as `Allowed` once found, but finding them depended on the comparison itself.
- UR1 and UR2 are both cases where a page contains a stray editorial/meta note about its own status or its own examples, rather than an error in scholarly content, data, or links. Neither the Minimal nor Full checklist has an item specifically aimed at "leftover drafting notes not caught by the opening-page-style guidance in `DOCUMENTATION_STYLE_GUIDE.md` §5" — both were found through close reading rather than a targeted checklist item. This mirrors the same gap noted for UR2/UR3 in Trial 003 (I18N differences found by direct comparison rather than a prompting checklist item), suggesting a recurring pattern worth watching across further trials rather than a one-off.
- Repository-wide verification (checking `07-progress/` before classifying RR1/RR2 as typos) again proved necessary before treating a suspected error as fact, consistent with the "distinguish confirmed fact from inference" instruction repeated across all trials so far.
- The same-day confirmation round for UR1 and UR2 was faster than Trial 003's: both were approved for deletion outright, with no draft-options step, since neither involved protected scholarly content (unlike Trial 003's UR3, which needed a citation-form choice). This suggests the `Requires Confirmation` category spans a real range of turnaround cost — from a one-line yes/no to a drafted-and-approved addition — and `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`'s single `Requires Confirmation` value does not need to distinguish these further; the difference showed up naturally in each finding's own evidence and proposed action.
