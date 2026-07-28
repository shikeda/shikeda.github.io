## Review Trial 014

Target: `content/docs/krm/_index.ja.md`, `content/docs/krm/_index.en.md` — the top-level KRM Documentation landing page pair.

Purpose: Fourteenth pilot of the KRM Documentation review workflow. This is the site's top-level index/navigation page for the whole KRM Documentation tree. Findings were link/wording/Hugo-level, so this record is short.

**Confirmation update (2026-07-28, same day)**: the project owner confirmed UR1 — `bookFlatSection: true`/`bookToc: true` being active only on `_index.en.md` was leftover from a past experiment, not an intentional design choice. Resolution: commented both out in `_index.en.md`, matching `_index.ja.md`'s existing (already-correct) state. Applied and verified — see the updated entry and §Change and Validation below.

---

### Scope

2 files reviewed (the section-root `_index` pair, one level above the chapter directories already reviewed in Trials 001–013). Protected content: minimal — mostly navigation links, an acknowledgements section, and a short methodology summary; no data specifications or scholarly transcriptions. Reviewer: Claude (this session). Review date: 2026-07-28.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Stale chapter-number links in the "内容" navigation list (`_index.ja.md`)**
Links to "進捗状況" and "事例研究" pointed to `/docs/krm/06-progress/` and `/docs/krm/07-case-studies/`, but the actual directories (confirmed by listing `content/docs/krm/`) are `07-progress/` and `08-case-studies/` — matching what the English version already links to correctly. Off-by-one stale links, same class as prior trials' stale-path fixes. Corrected to `07-progress/` and `08-case-studies/`.

**RR2 — Leftover trailing space in a navigation link's text (`_index.ja.md`)**
The link text "音注の種類と解読上の問題点 " (with a trailing space) is a leftover copy of the page title before it was fixed in Trial 012's RR1 — the target page itself no longer has this trailing space. Removed here too, for consistency.

**RR3 — Ordinary trailing whitespace (both files)**
`_index.ja.md:18` (end of a sentence) and `_index.en.md:93` (end of a sentence). Removed.

**RR4 — Romanization typo, "Myeigi" vs "Meigi" (`_index.en.md`)**
Line 18 reads "Kūkai's *Tenrei Banshō Myeigi*"; every other occurrence of this title in the same file (4 instances) correctly reads "Meigi". Corrected the one outlier.

**RR5 — Double space in the H1 (`_index.en.md`)**
`#  *Ruiju Myōgishō*...` had two spaces after the `#`. Normalized to one.

**RR6 — Inconsistent link depth for the first Contents item (`_index.en.md`)**
Every other item in the "Contents" list (items 2–8, and item 1 in the Japanese version) links to its chapter's root index (e.g. `./02-data-overview/`), but item 1 uniquely linked to a sub-page, `./01-introduction/01-01-introduction/`, instead of the chapter root `./01-introduction/` (which exists and has real content — confirmed by reading `01-introduction/_index.en.md`). Corrected to match the established pattern.

**RR7 — `weight` mismatch between the language pair**
`_index.ja.md` has `weight: 1`; `_index.en.md` had `weight: 2`. Every other `_index.{ja,en}.md` chapter pair in the site has matching weights (confirmed by checking all of them). This mismatch currently has no visible ordering effect (there is only one section under `content/docs/`), but it is inconsistent with the sitewide convention and is pure Hugo metadata, not content — corrected `_index.en.md`'s weight to `1` to match.

All seven: `Allowed under existing standards; no additional approval required` — stale/leftover links corrected against an unambiguous, already-correct reference (the sibling language version or the fixed target page itself), ordinary typos and whitespace, and Hugo metadata alignment with zero content change.

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — `bookFlatSection`/`bookToc` front matter differs between the language pair, with real rendering effect**
`_index.en.md` has `bookFlatSection: true` and `bookToc: true` active (uncommented); `_index.ja.md` has both commented out (inactive). Checking every other `_index.*.md` in the site: `bookToc: true` being active is the norm in both languages for sibling chapters (01-introduction, 03-entry-data-model, 04-entry-input all have it active in both `.ja.md` and `.en.md`), so `_index.ja.md`'s commented-out `bookToc` looks like it may be missing something. But `bookFlatSection: true` appears nowhere else in the entire site except this one English file — it is not simply "off" in Japanese and "on" in English by an established pattern; it is unique to this file. Unlike the other findings in this trial, this changes actual navigation/sidebar rendering behavior for the English KRM section, not just wording or a dead link, so it is recorded rather than silently aligned — the project owner should confirm whether `bookFlatSection: true` on the English top page is an intentional design choice or a leftover from an earlier experiment, and whether `bookToc` should be enabled on the Japanese top page to match its siblings.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: both settings were leftover from a past experiment, not intentional. Commented out `bookFlatSection: true` and `bookToc: true` in `_index.en.md:5-6`, matching `_index.ja.md`'s existing state (no change needed there). Verified with a further Hugo build: the English page builds cleanly (0 errors, 51 EN pages) and renders its H1 and all 12 navigation links as before. Fixed and verified; closed.

---

### Change and Validation

**Initial pass (RR1–RR7)**: Files changed: `_index.ja.md` (4 edits: 2 stale links, 1 leftover trailing space in link text, 1 sentence-end trailing space), `_index.en.md` (5 edits: Myeigi→Meigi, H1 double space, sentence-end trailing space, 01-introduction link depth, weight 2→1).

Verified: `git status --short` showed only these two files modified before and after editing; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt pages confirm: the Japanese page's 進捗状況/事例研究 links resolve to `/docs/krm/07-progress/` and `/docs/krm/08-case-studies/`; zero remaining occurrences of "Myeigi" and "Meigi" appears correctly; the English H1 anchor renders cleanly (`id=ruiju-myōgishō-krm-full-text-database-of-the-kanchi-in-manuscript`, no leading-space artifact); the English "Overview" link now points to `./01-introduction/` rather than the sub-page.

**Confirmation pass (UR1)**: Files changed: `_index.en.md` (1 edit: commented out `bookFlatSection: true` and `bookToc: true`).

Verified: `git diff` confirmed the new change was limited to the designated lines; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms the English page still renders its H1 and all 12 navigation links correctly. Scratch build directories removed after each verification.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR7 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: UR1 confirmed and resolved — none remain open. Files changed: `docs/krm/_index.ja.md`, `docs/krm/_index.en.md`. Reviewer: Claude (this session). Review date: 2026-07-28.
