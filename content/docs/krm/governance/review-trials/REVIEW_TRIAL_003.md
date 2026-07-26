## Review Trial 003

Purpose: Third pilot of the KRM Documentation review workflow, and the first run in the combined review-and-fix mode (Allowed-tier items fixed directly; Requires-Confirmation-tier items left untouched and recorded) rather than the separate review-only / fix-only two-stage process used in Trials 001–002. Target is the KRM Orientation layer (`01-introduction/`) rather than Data Reference (Trial 001) or Concept Reference (Trial 002).

---

### 1. Summary

A combined review-and-fix pass was run on the KRM Orientation section's overview page and its section index, in both languages. Three mechanical defects were found and fixed directly under `Allowed` authority: a malformed internal link, a missing closing quotation mark, and a stray space before a comma — all in the English version. Three further items were found that involve dates, a scholarly-accuracy footnote, and a judgment call about duplicated prose; these were left unmodified and recorded as `Requires Confirmation`, per instruction. All fixes were verified with a Hugo build comparing rendered output before and after.

---

### 2. Scope of Review

- **Primary files**: `content/docs/krm/01-introduction/01-01-introduction.ja.md`, `content/docs/krm/01-introduction/01-01-introduction.en.md`, `content/docs/krm/01-introduction/_index.ja.md`, `content/docs/krm/01-introduction/_index.en.md`
- **Related files**: `content/docs/krm/_index.ja.md` / `.en.md` (inbound links into this section), `content/menu/index.md` (inbound link via `relref`), `content/posts/2026-05-24-hugo-github-actions-setup.md` (an unrelated mention of this section's URL, inspected but out of scope)
- **Files changed**: `content/docs/krm/01-introduction/_index.en.md` (1 line), `content/docs/krm/01-introduction/01-01-introduction.en.md` (2 lines)
- **Document layer**: Orientation (`DOCUMENTATION_BLUEPRINT.md` Layer 1)
- **Document type**: Overview (`01-01-introduction.*.md` is a dense page combining Overview framing with Concept Reference/bibliographic content; `_index.*.md` are section index pages per `DOCUMENTATION_STYLE_GUIDE.md` §6)
- **Language status**: bilingual-required by policy (ja/en pairs present for both the article and the index)
- **Review level**: AI-assisted review — Minimal Acceptance Checklist, escalated to Full Documentation Review Checklist (Orientation is Core Documentation and this trial specifically probes language-version alignment)
- **AI involvement**: Full — review, fix, and verification all performed by Claude Code in this session; traceable in this record
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27
- **Protected content**: Present — bibliographic entries (86 references), manuscript/edition descriptions, dates, and a data-revision footnote. Not touched by the three fixes made; the items that touch this territory (UR1–UR3 below) were deliberately left unmodified rather than resolved.
- **Excluded concerns**: The 86-entry bibliography's citation accuracy was not individually verified; the reference-list formatting conventions were not audited; the radical/volume data table values were not re-checked against source material.

---

### 3. Review Progression

- **Minimal Review result**: needs revision — detected the malformed link in `_index.en.md` via the "links and navigation" item.
- **Escalated to Full Review**: yes.
- **Reason for escalation**: `01-01-introduction.*.md` is Core Documentation in the Orientation layer with a bilingual pair, meeting both the "Core Documentation" and "language-version alignment" trigger conditions in `REVIEW_CHECKLIST.md` §5. Escalation surfaced two further mechanical issues (the missing quotation mark and stray space) that the Minimal checklist's link-focused item would not have caught, plus the three Requires-Confirmation items in §4.
- **Conditional Reviews applied**: I18N Review (bilingual page; found UR2 and UR3 as language-version differences), Document-Type-Specific: Overview (child-page/reader-guidance role checked), AI-Assisted Work Review (this trial's own traceability). Glossary and Terminology Review: N/A — no glossary-candidate terminology issues were found in this pass.

---

### 4. Findings

Authority status values used below follow `EDITORIAL_CONVENTIONS.md`'s Authority Matrix directly (see `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`).

#### Required Revisions

**RR1 — Malformed relative link**
- File and location: `content/docs/krm/01-introduction/_index.en.md:22`
- Evidence: `[Date of Compilation](./01-introduction/01-01-introduction#date-of-compilation)`, carrying a stray extra `01-introduction/` segment not present in any of the 11 sibling TOC links in the same list (all of which use `./01-01-introduction#...`). From this page's own location, the malformed relative path resolves to a non-existent nested path.
- Classification: mechanical
- Severity / Impact: Low–Medium — one TOC entry in the section landing page's table of contents was unreachable.
- Proposed action: remove the stray `01-introduction/` segment.
- Authority status: `Allowed under existing standards; no additional approval required`
- Human confirmation required: No
- Resolution / Disposition: fixed and verified — Hugo build confirms the link now resolves to `./01-01-introduction#date-of-compilation` with zero remaining occurrences of the doubled path.

**RR2 — Missing closing quotation mark**
- File and location: `content/docs/krm/01-introduction/01-01-introduction.en.md:74`
- Evidence: `...such as "Upper," "Middle," and "Lower.` (no closing `"` after "Lower"), in ordinary explanatory prose, not a scholarly term, transcription, or citation.
- Classification: mechanical
- Severity / Impact: Low — cosmetic.
- Proposed action: add the closing quotation mark.
- Authority status: `Allowed under existing standards; no additional approval required`
- Human confirmation required: No
- Resolution / Disposition: fixed and verified — rendered output shows the paired curly quotes (`&ldquo;...&rdquo;`).

**RR3 — Stray space before punctuation**
- File and location: `content/docs/krm/01-introduction/01-01-introduction.en.md:183`
- Evidence: `Kōfuku-ji's Renjō-in , this fragmentary manuscript` (space before the comma), in ordinary explanatory prose.
- Classification: mechanical
- Severity / Impact: Very low — cosmetic.
- Proposed action: remove the stray space.
- Authority status: `Allowed under existing standards; no additional approval required`
- Human confirmation required: No
- Resolution / Disposition: fixed and verified.

#### Non-blocking Improvement Candidates

**NB1 — Section index duplicates the full article header rather than summarizing it**
- File and location: `content/docs/krm/01-introduction/_index.ja.md`, `_index.en.md`
- Evidence: both index pages reproduce the article's full author line, publication dates, and opening paragraph verbatim, then stop after the table of contents — they do not add independent reader guidance, scope framing, or a child-page description distinct from the article itself, as `DOCUMENTATION_STYLE_GUIDE.md` §4 recommends for the Overview document type.
- Classification: editorial/structural
- Why non-blocking: navigation is not broken (both pages work as landing pages), so this falls short of the style guideline without being a defect.
- Authority status: `Allowed with Care` if pursued (rewriting the index's framing without changing the article's content)
- Human confirmation required: No, if scoped to the index-only framing
- Resolution / Disposition: not actioned this round; recorded as backlog.

**NB2 — `weight` inconsistency between language versions**
- File and location: `01-01-introduction.ja.md:3` (`weight: 2`) vs `01-01-introduction.en.md:3` (`weight: 3`)
- Evidence: confirmed via front matter; has no visible ordering effect today since each language version has only one child page under its `_index`, but the values differ without an apparent reason.
- Classification: mechanical/metadata
- Why non-blocking: no observable navigation defect currently.
- Authority status: `Allowed with Care`
- Human confirmation required: No
- Resolution / Disposition: not actioned this round; recorded as backlog.

#### Unresolved but Recorded

**UR1 — Apparently redundant duplicate paragraph in "Significance"**
- File and location: `content/docs/krm/01-introduction/01-01-introduction.en.md:57-69`
- Evidence: a bulleted, term-glossed breakdown (lines 57–64) plus a synthesis sentence (line 66) is immediately followed by a separate prose paragraph (lines 68–69) that restates substantially the same content in less detail and without the bold/backtick term-glossing used elsewhere on the site. The Japanese counterpart (`01-01-introduction.ja.md`, "価値" section, lines 69–74) has only one paragraph, with no equivalent duplication.
- Classification: editorial
- Severity / Impact: Low-Medium — likely an editing artifact (leftover draft text), but removing a full paragraph in a Significance/scholarly-value section carries a real risk of losing an intended nuance if the duplication was not accidental.
- Proposed action: confirm with the project owner whether the second paragraph is an accidental leftover before removing it; `EDITORIAL_CONVENTIONS.md`'s Paragraphing row allows removing "accidental repetition" as `Allowed`, but also flags "condense prose where nuance may be lost" as `Requires Confirmation` — this finding sits on that boundary, so it was treated conservatively.
- Authority status: `Requires Confirmation`
- Human confirmation required: Yes
- Resolution / Disposition: not actioned this round; recorded.

**UR2 — Publication-date field mismatch between language versions**
- File and location: `01-01-introduction.ja.md:16-17` vs `01-01-introduction.en.md:16`
- Evidence: the Japanese version records both `初版公開日：2022年11月15日`(original publication date) and `最終更新日：2025年4月20日` (last-updated date). The English version records only `Date published: April 20, 2025` — the last-updated date from the Japanese version, presented as if it were the sole publication date, with no separate original-publication date given.
- Classification: linguistic/factual
- Severity / Impact: Medium — a reader of the English page cannot tell the article was first published in 2022, and may be misled about how long the content has existed.
- Proposed action: confirm the correct original-publication date and update-history convention for the English version.
- Authority status: `Requires Confirmation` — `EDITORIAL_CONVENTIONS.md` §12 explicitly excludes dates from "ordinary typos."
- Human confirmation required: Yes
- Resolution / Disposition: not actioned this round; recorded.

**UR3 — Missing data-revision footnote in the English "Number of Entries" section**
- File and location: `01-01-introduction.ja.md:106-108` (footnote `[^1]`) vs `01-01-introduction.en.md:107-126` (no equivalent footnote)
- Evidence: the Japanese version's entry-count table carries a footnote stating that the figures differ from the previously published 2020 paper's values due to a subsequent correction ("その後の点検により数値を修正した...大勢に影響はない"). No equivalent caveat appears anywhere in the English version's "Number of Entries" section.
- Classification: scholarly/linguistic — a `supplementary difference` under `I18N_POLICY.md` §10, bordering on `substantive inconsistency` since the caveat affects how the cited figures should be trusted against prior publications.
- Severity / Impact: Medium — English readers comparing these figures to the cited 2020 paper have no indication that a correction was made.
- Proposed action: confirm whether an equivalent footnote/caveat should be added to the English version.
- Authority status: `Requires Confirmation` — adding scholarly caveat content is translation/language-adjustment work affecting protected content per `I18N_POLICY.md` §12.
- Human confirmation required: Yes
- Resolution / Disposition: not actioned this round; recorded.

---

### 5. Maintenance Flow

```text
detected → recorded → classified as mechanical (RR1–RR3) or Requires Confirmation (UR1–UR3) →
assigned under user instruction → reviewed →
Allowed under existing standards; no additional approval required (RR1–RR3) →
updated → verified → outcome recorded →
UR1–UR3 carried forward pending confirmation → closed for this round
```

---

### 6. Change and Validation

- **Files changed**: `content/docs/krm/01-introduction/_index.en.md` (1 line), `content/docs/krm/01-introduction/01-01-introduction.en.md` (2 lines). No other file was modified; the Japanese-language files in scope were read and evaluated but not edited.
- **Verification method**: `git status --short`/`git status` before editing (clean baseline); `git diff` after editing, confirming both diffs were limited to the three designated lines; `hugo --minify` build to a scratch destination.
- **Build result**: 159 JA pages / 51 EN pages, 0 build errors.
- **Rendered-output checks**: the English section-index page's generated link resolves to `./01-01-introduction#date-of-compilation` with zero remaining occurrences of the doubled `01-introduction/01-introduction` path; the English article page's rendered HTML shows the quotation mark correctly paired (`&ldquo;...Lower.&rdquo;`) and the stray space before the comma removed.
- **Protected-content check**: none of the three fixes touched dates, citations, transcriptions, bibliographic entries, or data values. The three items that do touch that territory (UR1–UR3) were identified and left unmodified rather than resolved.

---

### 7. Final Review Result

- **Overall judgment**: Pass
- **Required revisions remaining**: none (RR1, RR2, RR3 resolved and verified)
- **Confirmation-blocking issues**: none — UR1–UR3 are recorded as `Requires Confirmation` but do not block acceptance of the fixes made in this round, consistent with the `Unresolved but recorded` judgment value in `REVIEW_CHECKLIST.md` §2
- **Non-blocking improvement candidates**: NB1 (section-index framing), NB2 (`weight` inconsistency)
- **Unresolved but recorded**: UR1 (possible duplicate paragraph), UR2 (publication-date mismatch), UR3 (missing data-revision footnote in English)
- **Files changed**: `01-introduction/_index.en.md`, `01-introduction/01-01-introduction.en.md`
- **Validation performed**: `git status`, `git diff`, `hugo --minify` build (159 JA / 51 EN, 0 errors), rendered-output inspection of the affected pages
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27

---

### 8. Governance Observations

- This trial was run in combined review-and-fix mode rather than the two-stage review-only/fix-only process of Trials 001–002. The Allowed/Requires-Confirmation boundary from `EDITORIAL_CONVENTIONS.md` proved sufficient on its own to gate which items could be actioned immediately within a single pass, without needing a separate approval round for the mechanical items.
- UR1 illustrates a genuine boundary case in `EDITORIAL_CONVENTIONS.md`'s Paragraphing row, which lists "remove accidental repetition" as `Allowed` but "condense prose where nuance may be lost" as `Requires Confirmation`. The same finding could plausibly be argued into either category; this trial resolved the ambiguity by choosing the more conservative classification rather than resolving it unilaterally. This suggests the Paragraphing row's boundary between those two cells could be sharpened, but no change to `EDITORIAL_CONVENTIONS.md` is proposed here.
- UR2 and UR3 were both found via routine bilingual comparison (reading the ja/en pair side by side), not via any specific checklist item naming "compare dates" or "compare footnotes." The I18N Review conditional checklist's existing items ("language differences are classified before being resolved") were broad enough to catch them once the comparison was made, but did not prompt the comparison itself.
