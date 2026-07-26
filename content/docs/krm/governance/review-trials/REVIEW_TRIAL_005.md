## Review Trial 005

Purpose: Fifth pilot of the KRM Documentation review workflow, run in the combined review-and-fix mode established in Trials 003–004. Target is the KRM Annotation Methodology layer (`05-annotation-policy/`) — the section every governing document treats as the most scholarship-sensitive area of the Documentation — specifically its section index and the first policy article.

---

### 1. Summary

A combined review-and-fix pass was run on the `05-annotation-policy/` section index and its basic-policy article, in both languages. One mechanical defect was found and fixed directly under `Allowed` authority: a front-matter `title` on the Japanese section index that did not match its own H1, the English counterpart's title, or the established usage already present in the KRM top-level navigation — a discrepancy already named as technical debt in `CURRENT_STATE_REPORT.md`. One further item was found in the English basic-policy article — a diagram note referencing "the glossary," which does not yet exist as a Core Documentation layer anywhere on the site — and was left unmodified and recorded as `Requires Confirmation`. All work was verified with a Hugo build comparing rendered output before and after. No scholarly content — annotation principles, the worked '覲' example, citations, or bibliographic entries — was touched.

---

### 2. Scope of Review

- **Primary files**: `content/docs/krm/05-annotation-policy/_index.ja.md`, `content/docs/krm/05-annotation-policy/_index.en.md`, `content/docs/krm/05-annotation-policy/05-01-basic-policy.ja.md`, `content/docs/krm/05-annotation-policy/05-01-basic-policy.en.md`
- **Related files**: `content/docs/krm/_index.ja.md` / `.en.md` (inbound links into this section, and the source of the established correct section title used to verify RR1), `CURRENT_STATE_REPORT.md` (source of the pre-existing known-issue claim for RR1), `content/posts/glossary_for_KRM_db.md` (checked to confirm no formal Core Documentation glossary currently exists, relevant to UR1)
- **Files changed**: `content/docs/krm/05-annotation-policy/_index.ja.md` (1 line)
- **Document layer**: Annotation Methodology (`DOCUMENTATION_BLUEPRINT.md` Layer 5)
- **Document type**: `_index.*.md` — Overview (well-formed: distinct per-child-page summaries, not a duplicate of article content, unlike the pattern flagged as NB1 in Trial 003 for `01-introduction/_index.*.md`); `05-01-basic-policy.*.md` — Methodology with embedded Example content, consistent with `DOCUMENTATION_BLUEPRINT.md` §10's mapping of `05-annotation-policy/` to "Annotation Methodology, with some Example and Glossary material"
- **Language status**: bilingual-required by policy (ja/en pairs present for both files)
- **Review level**: AI-assisted review — Minimal Acceptance Checklist, escalated to Full Documentation Review Checklist (Annotation Methodology is Core Documentation, and this is the section every governing document singles out for the highest scholarly-preservation care)
- **AI involvement**: Full — review, fix, and verification all performed by Claude Code in this session; traceable in this record
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27
- **Protected content**: Present and extensive — annotation-category definitions, the worked '覲' example (phonetic glosses, tone marks, *Guangyun* collation, *wakun* etymology), an extensive bibliography of primary and reference sources, and quantitative counts (approx. 32,600 entries / 86,800 gloss elements) presented in a mermaid diagram. None of it was touched by RR1; UR1 concerns a diagram annotation *about* this content, not the content itself.
- **Excluded concerns**: The scholarly accuracy of the '覲' phonological analysis and citations was not independently verified; the ~90 external bibliographic/reference-tool links (GlyphWiki, HNG, SAT, ctext.org, suzukish.sakura.ne.jp, etc.) were not checked for liveness; the mermaid diagram's numeric values were cross-checked between language versions for consistency only, not re-derived from source data.

---

### 3. Review Progression

- **Minimal Review result**: needs revision — detected the title/H1 mismatch on `_index.ja.md` via the "document role, layer, and type are clear" and "headings, titles, links, and navigation" items.
- **Escalated to Full Review**: yes.
- **Reason for escalation**: `05-annotation-policy/` is Core Documentation in the highest-sensitivity Annotation Methodology layer, meeting the "Core Documentation" trigger condition in `REVIEW_CHECKLIST.md` §5, and every governing document (`PROJECT_CHARTER.md`, `AGENTS.md`, `EDITORIAL_CONVENTIONS.md`) singles this section out for extra preservation care. Escalation prompted a closer read of prose (not just links and file names), surfacing UR1, which the Minimal checklist would not have caught.
- **Conditional Reviews applied**: Editorial Authority review (used throughout to classify RR1 as `Allowed` and UR1 as `Requires Confirmation`, given the section's sensitivity), Document-Type-Specific: Methodology (checked that principles and evidence categories were presented without altering scholarly judgment — confirmed unaltered), Protected Content review (explicit check that no citation, transcription, or example was touched), I18N Review (ja/en compared; no substantive divergence found beyond UR1, which exists only in the English version). Glossary and Terminology Review: applied to UR1 specifically (see Findings).

---

### 4. Findings

Authority status values used below follow `EDITORIAL_CONVENTIONS.md`'s Authority Matrix directly (see `governance/review-trials/REVIEW_TRIAL_TEMPLATE.md`).

**Confirmation update (2026-07-27, same day)**: the project owner requested a concrete proposal for NB1. A single-removal proposal was drafted, reviewed, approved, applied to both language versions, and verified with a further Hugo build. The project owner then requested a proposal for UR1. Three options were drafted (delete the note; remove only the false glossary claim while keeping the term-mapping clarification; leave as a forward-looking placeholder); the middle option was approved, applied, and verified. See the updated NB1 and UR1 entries and §6 for details.

#### Required Revisions

**RR1 — Front-matter title does not match the page's own H1 or established usage (documented known issue, confirmed)**
- File and location: `content/docs/krm/05-annotation-policy/_index.ja.md:2`
- Evidence: front matter `title: "注釈データ入力の詳細"` ("Details of Annotation Data Input"), while the page's own H1 (line 13) reads `# 注釈作成の基本方針` ("Basic Policy for Annotation Creation"). The English counterpart's title (`_index.en.md:2`) is `"Basic Policy for Annotation Creation"`, matching the H1's meaning. The KRM top-level navigation (`content/docs/krm/_index.ja.md:52`) already links to this section as `[注釈作成の基本方針](/docs/krm/05-annotation-policy/)`. **Verified**: `CURRENT_STATE_REPORT.md:448` already names this exact mismatch as technical debt ("Legacy or transitional page titles, such as `注釈データ入力の詳細` in the front matter of `05-annotation-policy/_index.ja.md`, while the page heading is `注釈作成の基本方針`"), confirming this was a pre-existing, documented issue rather than a newly invented judgment.
- Classification: mechanical/navigational
- Severity / Impact: Low-Medium — the browser tab title, search-index entry, and any auto-generated title reference for this Core Documentation section landing page did not match its own content or its established name elsewhere on the site.
- Proposed action: change the front-matter title to `注釈作成の基本方針`, matching the H1, the English counterpart, and existing site-wide usage.
- Authority status: `Allowed under existing standards; no additional approval required` — `EDITORIAL_CONVENTIONS.md` §6 "Page title and H1" row: "Align title and H1 when meaning is unchanged" is `Allowed`. This is not a scope or classification change: the corrected title is already the section's established name everywhere else on the site.
- Human confirmation required: No
- Resolution / Disposition: fixed and verified — Hugo build confirms the rendered `<title>` tag now reads "注釈作成の基本方針 | HDIC project" with zero remaining occurrences of the old title string on the page.

#### Non-blocking Improvement Candidates

**NB1 — Stray non-standard comment in front matter (both language versions)**
- File and location: `content/docs/krm/05-annotation-policy/_index.ja.md:3`, `_index.en.md:3`
- Evidence: both files carry a commented-out line `# 掲出字と注文の分類` ("Classification of Headwords and Original Glosses") immediately after `title:` — unlike the standard commented-out `bookFlatSection`/`bookToc`/etc. fields seen throughout the site, this is free-text Japanese, possibly a leftover alternative-title draft. It does not render and has zero functional effect.
- Classification: metadata/editorial
- Why non-blocking: no rendering or navigation impact; matches the general "commented-out front matter" pattern already recorded as low-priority/site-wide in Trials 001 and 003, rather than being specific to this page.
- Authority status: `Allowed under existing standards; no additional approval required` — on further review, this carries zero rendering or scope impact (the comment was never rendered), so it does not warrant the `Allowed with Care` caveat originally recorded; reclassified accordingly when the removal proposal was drafted.
- Human confirmation required: No, though the project owner requested to see the specific proposal before it was applied
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: a single-removal proposal was presented and approved. The line `# 掲出字と注文の分類` removed from both `_index.ja.md:3` and `_index.en.md:3`. Verified with a further Hugo build: the comment string does not appear anywhere in either page's rendered HTML (confirming it was never rendered, before or after), and both pages' `<title>` tags are unaffected. Fixed and verified; closed.

#### Unresolved but Recorded

**UR1 — Diagram note references "the glossary," which does not currently exist as a Core Documentation layer**
- File and location: `content/docs/krm/05-annotation-policy/05-01-basic-policy.en.md:40`
- Evidence: `"Note: In the diagram, "Japanese Native Readings" refers to `Japanese Native Readings` (*wakun*) as defined in the glossary."` No equivalent note exists in the Japanese version's diagram (`05-01-basic-policy.ja.md:30`, which has no comparable annotation). A repository check confirms no formal Core Documentation Glossary currently exists under `content/docs/krm/`; the only related file, `content/posts/glossary_for_KRM_db.md`, is a Blog Post per `I18N_POLICY.md` §15, not the Glossary layer described in `DOCUMENTATION_BLUEPRINT.md` §6 and tracked as not-yet-established in Trials 001–004.
- Classification: editorial/terminology — the note makes a factual claim about the site's own structure (that a glossary defining this term exists) that does not currently hold.
- Severity / Impact: Low-Medium — unlikely to mislead about scholarly content itself, but points readers toward a glossary entry that does not exist, which could read as a broken promise or a dead cross-reference once a reader looks for it.
- Proposed action: confirm with the project owner whether this note should be removed (no glossary exists yet), rephrased to describe the term without the glossary claim, or left as a forward-looking placeholder pending `ROADMAP.md` Milestone 4 (Glossary and Terminology Baseline).
- Authority status: `Requires Confirmation` — this is a structural/terminology claim about the Documentation itself, not an ordinary prose typo, and `GLOSSARY_CONVENTIONS.md` §10 reserves terminology-authority decisions (including how and where a term is formally defined) for confirmed decisions rather than ordinary editing.
- Human confirmation required: Yes
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: a three-option proposal was presented (delete the note entirely; remove only the false "as defined in the glossary" claim while keeping the diagram-label-to-documented-term mapping; leave as a forward-looking placeholder). The middle option was approved and applied: the sentence now reads "Note: In the diagram, "Japanese Native Readings" refers to the term `Japanese Native Readings` (*wakun*) used throughout this documentation." in `05-01-basic-policy.en.md:40`. Verified with a further Hugo build: the phrase "as defined in the glossary" no longer appears anywhere on the rendered page, and the replacement sentence renders correctly. Fixed and verified; closed.

---

### 5. Maintenance Flow

```text
detected → recorded → classified as mechanical (RR1), non-blocking (NB1), or Requires Confirmation (UR1) →
assigned under user instruction → reviewed →
Allowed under existing standards; no additional approval required (RR1) →
updated → verified → outcome recorded →
NB1 proposal drafted on request → approved same day → NB1 updated → NB1 verified →
UR1 proposal (3 options) drafted on request → one option approved same day →
UR1 updated → UR1 verified → outcome recorded → closed
```

---

### 6. Change and Validation

- **Files changed**: `content/docs/krm/05-annotation-policy/_index.ja.md` (2 lines: RR1 title fix, NB1 comment removal), `content/docs/krm/05-annotation-policy/_index.en.md` (1 line: NB1 comment removal), `content/docs/krm/05-annotation-policy/05-01-basic-policy.en.md` (1 line: UR1 rephrase, after confirmation). `05-01-basic-policy.ja.md` was read and evaluated but not edited — it had no identified issues.
- **Verification method**: `git status --short` before editing (clean baseline); `git diff` after each round of editing; `hugo --minify` build to a scratch destination, run three times — after RR1, after the NB1 removals, and after the UR1 rephrase.
- **Build result**: 161 JA pages / 51 EN pages, 0 build errors after RR1; 162 JA pages / 51 EN pages, 0 build errors after the NB1 removals; 162 JA pages / 51 EN pages, 0 build errors after the UR1 rephrase (the JA count increase between the first and second checks reflects `REVIEW_TRIAL_005.md` itself becoming a built page, the same effect noted in Trials 001–004).
- **Rendered-output checks**: the rebuilt Japanese section-index page's `<title>` tag reads "注釈作成の基本方針 | HDIC project," matching the H1 and the already-correct KRM top-level navigation link text. Zero remaining occurrences of the old title string. After the NB1 removals, both language versions' rendered HTML contain zero occurrences of the removed comment string, and both `<title>` tags are unchanged. After the UR1 rephrase, the rendered English article contains zero occurrences of "as defined in the glossary," and the replacement sentence renders correctly as prose with the intended code span and italics.
- **Protected-content check**: none of the four changes (RR1, NB1 ×2, UR1) touched any annotation-category definition, worked example, citation, bibliographic entry, or quantitative count. UR1's edit was confined to a diagram-annotation sentence describing terminology usage, not the terminology's meaning or scope.

---

### 7. Final Review Result

- **Overall judgment**: Pass
- **Required revisions remaining**: none (RR1 resolved and verified)
- **Confirmation-blocking issues**: none
- **Non-blocking improvement candidates**: none remaining — NB1 resolved (proposal approved, applied, verified); see §4
- **Unresolved but recorded**: none remaining — UR1 confirmed and resolved (one of three proposed options approved, applied, verified); see §4
- **Files changed**: `05-annotation-policy/_index.ja.md`, `05-annotation-policy/_index.en.md`, `05-annotation-policy/05-01-basic-policy.en.md`
- **Validation performed**: `git status`, `git diff`, three `hugo --minify` builds (161 JA / 51 EN after RR1; 162 JA / 51 EN after the NB1 removals; 162 JA / 51 EN after the UR1 rephrase), rendered-output inspection of all affected pages and cross-check against the KRM top-level navigation
- **Reviewer**: Claude (this session)
- **Review date**: 2026-07-27

---

### 8. Governance Observations

- This trial is the first to touch the Annotation Methodology layer, which every governing document treats as the section requiring the most caution. In practice, the Allowed/Requires-Confirmation boundary from `EDITORIAL_CONVENTIONS.md` scaled down cleanly to this heightened-sensitivity context: the one Allowed item (RR1) was a pure navigation-label fix with zero scholarly surface area, and the one Requires-Confirmation item (UR1) was correctly withheld precisely because it touched a claim about the Documentation's own structure. No finding required treating "this section is sensitive" as a reason to second-guess an otherwise-clear `Allowed` classification, nor did it loosen the bar for what counted as `Requires Confirmation`.
- RR1 is the second finding across five trials (after Trial 002's F1) that was independently corroborated by `CURRENT_STATE_REPORT.md` before being classified as fact rather than assumption. Both cases followed the same verification pattern: cross-check the suspected error against the documented known-issues list, then independently confirm it against current file content rather than trusting either source alone.
- UR1 is a new category of finding not seen in Trials 001–004: a page making a claim about the Documentation's *own infrastructure* (the existence of a glossary) rather than about scholarly content, a link target, or a data specification. `GLOSSARY_CONVENTIONS.md` and `DOCUMENTATION_BLUEPRINT.md` already anticipate this gap (the Glossary layer is explicitly not yet built, per `ROADMAP.md` Milestone 4), but neither document currently instructs reviewers on how to handle *existing prose that assumes the gap is already closed*. This may be worth a short note in a future standards revision, but no change is proposed in this trial.
- NB1's initial classification (`Allowed with Care`) was revised to plain `Allowed` once a concrete removal proposal was drafted and its zero rendering impact was confirmed — the more cautious initial label reflected uncertainty about the comment's purpose, not an actual risk in removing it. The project owner still asked to see the specific proposal before approving, independent of the authority level; this confirms `Requires Confirmation` and "wants to review a specific proposal first" are separate concerns — `EDITORIAL_CONVENTIONS.md`'s authority levels govern what may be done without asking, not whether a low-risk change is nonetheless worth showing before it is made.
- UR1's resolution illustrates that a `Requires Confirmation` finding is not necessarily a binary keep-or-delete choice: the approved fix preserved the note's legitimate function (mapping a diagram label to the full documented term) while removing only the specific claim that made it inaccurate (the nonexistent glossary). Presenting multiple options rather than a single yes/no proposal — as was also done for Trial 003's UR3 — again let the project owner select a middle path that neither the "leave as-is" nor "delete outright" framing alone would have surfaced.
