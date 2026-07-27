## Review Trial 011

Target: `05-annotation-policy/` (`_index.{ja,en}.md`, `05-01-basic-policy.{ja,en}.md`, `05-02-headword-count.{ja,en}.md`, `05-03-jitaichu-formats.{ja,en}.md`, `05-04-onchu-problems.{ja,en}.md`, `05-05-gichu-quantity.{ja,en}.md`, `05-06-wakun-materials.{ja,en}.md`, `05-07-annotation-examples.{ja,en}.md` — 8 file pairs, 16 files). `_index.{ja,en}.md` and `05-01-basic-policy.{ja,en}.md` were previously reviewed and fixed in Trial 005; re-checked here as part of the full-directory scope and found clean (no new issues, no regressions). The remaining six pairs are their first full review.

Purpose: Eleventh pilot of the KRM Documentation review workflow. This section is Core Documentation (Annotation Policy layer). The dominant finding this trial is not a mechanical defect but a translation-completeness gap spanning five of the six newly reviewed file pairs, so the Unresolved section is longer than a typical trial — proportionate to what was found, not padded.

**Confirmation update (2026-07-27, same day)**: the project owner reviewed all three Unresolved items. UR3: confirmed correct and fixed. UR1 and UR2: acknowledged as accurate; translation work will begin after the overall documentation review is complete — left unchanged for now. See UR3's updated entry and §Change and Validation below.

---

### Scope

16 files reviewed. Document layer: Editorial and Encoding Rules / Annotation Policy (`DOCUMENTATION_BLUEPRINT.md` Layer 4). Document type: Rule Reference (`05-02` through `05-07`), already-clean Concept/Rule Reference (`_index`, `05-01`, from Trial 005). Protected content: extensive — worked annotation examples with `kazama_location`/`hanzi_entry`/`definition`/`remarks` citations, bibliographic reference lists (~80+ entries), manuscript comparison tables, GlyphWiki image references. Review level: AI-assisted review, Full Documentation Review Checklist (Core Documentation). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Trailing space in title/H1**
`05-04-onchu-problems.ja.md:2` (front matter `title:`) and `:11` (H1): both read `"音注の種類と解読上の問題点 "` with a trailing full-width-adjacent space before the closing quote/line end. Removed the trailing space from both.

**RR2 — Missing sentence-final "。"**
`05-04-onchu-problems.ja.md:22`: "...約24,000あり、照合には時間を要する" ran directly into the next sentence ("まずは、...") with no closing punctuation. Added "。" after "要する".

Both: `Allowed under existing standards; no additional approval required` — ordinary typographical corrections (stray whitespace, missing terminal punctuation) with no effect on meaning or protected content.

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — Five `.en.md` files are untranslated Japanese text wearing an English title, not actual translations**
`05-03-jitaichu-formats.en.md`, `05-04-onchu-problems.en.md`, `05-05-gichu-quantity.en.md`, `05-06-wakun-materials.en.md`, `05-07-annotation-examples.en.md`. Each carries an English `title`, an accurate "Under preparation." marker, and (in four of the five) an English H1 — but the entire body beneath is the Japanese source text, essentially unchanged from the corresponding `.ja.md` file (confirmed by direct comparison; content length and wording match the Japanese originals, not English prose). This differs from the "Under preparation." pattern resolved in Trials 004 and 010 (`04-01-id.en.md`, `04-03-handling.en.md`), where the marker was a stray leftover on an otherwise-complete English translation and was deleted after confirmation. Here the marker is accurate and must **not** be deleted — the underlying gap is a real, substantial translation backlog, matching `I18N_POLICY.md`'s `translation-pending` status category. Resolving this is a scope/scheduling decision for the project owner (whether and when to commission full translations for these five pages), not a mechanical or single-line content fix, and is well outside anything an `Allowed` or ordinary `Requires Confirmation` edit could address. For contrast: `05-02-headword-count.en.md` (1060 lines) was checked and confirmed to be a genuine, complete English translation — the gap is specific to these five pages, not the section as a whole.

**UR2 — Duplicate H1 (leftover untranslated heading) in two of the five affected files**
`05-05-gichu-quantity.en.md:12,16` and `05-06-wakun-materials.en.md:11,15`: each has a correct English H1 matching its title, immediately followed by a second, untranslated Japanese H1 duplicating the same heading (e.g. `# Types and Quantity of Meaning Notes` then `# 義注の種類と数量`). This is a sub-detail of UR1 — evidence of the same incomplete translation-wrapper process — and is not sensibly fixable in isolation while the page body beneath remains wholesale untranslated.

**UR3 — Likely dropped character in a repeated bibliographic journal title**
`05-06-wakun-materials.ja.md:78`: cites `『鶴見大学仏教文化研究所紀』15、37–60頁、2010年`. The same journal is cited correctly as `『鶴見大学仏教文化研究所紀要』` (with `要`) in nine other entries in the same list (lines 58, 60, 62, 64, 66, 68, 70, 72, 74, 76). Classified as `Requires Confirmation` rather than `Allowed` despite the strong internal evidence, since this is a directly quoted bibliographic/source title (`EDITORIAL_CONVENTIONS.md` §11-class protected content, same category as Trial 010's UR2).
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: confirmed correct, fix. Applied to `05-06-wakun-materials.ja.md:78`: `『鶴見大学仏教文化研究所紀』15` → `『鶴見大学仏教文化研究所紀要』15`. Verified with a further Hugo build: the rebuilt page shows `鶴見大学仏教文化研究所紀要』15` with zero remaining occurrences of the truncated form. Fixed and verified; closed.

---

### Change and Validation

**Initial pass (RR1–RR2)**: Files changed: `05-04-onchu-problems.ja.md` (3 edits: title trailing space, H1 trailing space, missing "。").

Verified: `git status --short` showed only this one file modified before and after editing; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms: `<title>音注の種類と解読上の問題点 | HDIC project</title>` (no trailing space), and the sentence "...照合には時間を要する。" renders with the closing period.

**Confirmation pass (UR3 — UR1, UR2 left unchanged)**: Files changed: `05-06-wakun-materials.ja.md` (1 edit: `紀` → `紀要`).

Verified: `git status --short` confirmed only the two designated files modified; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms `鶴見大学仏教文化研究所紀要』15` renders correctly with zero remaining truncated occurrences. Scratch build directories removed after each verification.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR2 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: UR3 confirmed and resolved; UR1 and UR2 acknowledged as accurate and left unchanged — translation work for the affected pages will begin after the overall documentation review concludes. Files changed: `05-annotation-policy/05-04-onchu-problems.ja.md`, `05-06-wakun-materials.ja.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
