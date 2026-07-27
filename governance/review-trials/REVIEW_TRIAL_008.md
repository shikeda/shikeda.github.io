## Review Trial 008

Target: `02-data-overview/` (`_index.{ja,en}.md`, `02-01-main` through `02-07-ndl`, `.ja.md`/`.en.md` — 8 file pairs, 16 files).

**Premise correction**: the request described this section as Japanese-only. That is not the case — every file in `02-data-overview/` has a complete `.ja.md`/`.en.md` pair (confirmed by directory listing before starting the review). The review proceeded on that basis, covering both language versions.

Purpose: Eighth pilot of the KRM Documentation review workflow. This section is Core Documentation (Data Reference layer), so the review was run at Full-Checklist depth, but the findings turned out to be link/wording-level, so this record is kept proportionate rather than exhaustively long, per instruction.

**Confirmation update (2026-07-27, same day)**: the project owner confirmed UR1's correction (align the Japanese explanation with the already-correct English column) and directed it be applied. Applied and verified — see the updated UR1 entry and §Change and Validation below.

---

### Scope

16 primary files + 1 related file (`04-entry-input/04-03-handling.en.md`, touched only because the inbound-link check into `02-data-overview/` surfaced a defect there). Document layer: Data Reference (`DOCUMENTATION_BLUEPRINT.md` Layer 3). Document type: Data Reference. Protected content: present (column specifications, ID-format definitions, version-comparison tables); not altered except where noted in the Unresolved item below (not fixed). Review level: AI-assisted review, Full Documentation Review Checklist (Core Documentation). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Broken case-study cross-reference (real 404, not previously documented)**
- Files: `02-06-pronunciations.ja.md:89`, `02-06-pronunciations.en.md:68`
- Evidence: both linked to `/docs/krm/08-case-studies/5-dhsjr/`. The actual file is `content/docs/krm/08-case-studies/08-05-dhsjr.md` (title "DHSJRとの連携", matching the link text exactly) — the correct path is `/docs/krm/08-case-studies/08-05-dhsjr/`. This was a genuinely broken link, not caught by any prior trial or `CURRENT_STATE_REPORT.md`.
- Fix: corrected the path in both files.
- Authority: `Allowed under existing standards; no additional approval required` (target unambiguous — file exists, title matches link text).

**RR2 — Missing trailing slash on two internal links**
- Files: `_index.ja.md:63` (`./02-02-notes` → `./02-02-notes/`), `02-02-notes.en.md:60` (`./02-01-main` → `./02-01-main/`)
- Evidence: every other internal link across these 16 files (and the site generally) uses a trailing slash; these two were the only exceptions.
- Authority: `Allowed under existing standards; no additional approval required` (formatting consistency, target unchanged).

**RR3 — Missing `/en/` language prefix, related file (`04-entry-input/04-03-handling.en.md`)**
- Lines 49 and 61: both linked to `/docs/krm/02-data-overview/` (no `/en/` prefix) from within English prose, sending English readers to the Japanese version instead.
- Found via this trial's inbound-link check into `02-data-overview/`, not part of the original file list, but directly relevant and unambiguous to fix.
- Fix: both corrected to `/en/docs/krm/02-data-overview/`.
- Authority: `Allowed under existing standards; no additional approval required`.

No data-file-name hyphen/underscore inconsistencies, stale `/docs/notes/...` paths, or `localhost` references were found in this section (unlike Trials 002/004/007).

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — Leftover editorial review note plus a likely-incorrect data-specification claim, `02-06-pronunciations.{ja,en}.md`**
- File and location: `02-06-pronunciations.ja.md:56`, `02-06-pronunciations.en.md:40` (same table row, present identically in both files since the row's rightmost column is Japanese-language text even in the English file).
- Evidence: the `pronunciation_id` row's Japanese explanation reads "...変異形を追加したものには末尾にxを付した。 *(User indicates 'x' is incorrect, and 'b,c,d' is correct for variants)*" — a literal, unresolved editorial review comment embedded directly in the published table, plus an apparently uncorrected error it describes. Same row, English explanation column, already reads "Suffixes 'b', 'c', 'd' are appended for variant forms" — i.e., the English column was already fixed at some point, but the Japanese column and the leftover comment about it were not. This is corroborated by `02-04-wakun.ja.md:67`'s `wakun_id` row, which independently uses the same "b, c, d" suffix pattern for the analogous case.
- Classification: this bundles two things — (a) a stray editorial note (arguably `Allowed` to remove on its own, per precedent in Trials 004/005), and (b) a change to the actual column-specification text ("xを付した" → "b, c, dを付した"), which is Data/Specification content per `EDITORIAL_CONVENTIONS.md` §6 ("Column explanation: Requires Confirmation") and §12 (data values are not ordinary typos). Removing only (a) while leaving (b) uncorrected would strand a known-wrong spec description with no flag at all, so the two were kept together and left entirely untouched.
- Proposed action: confirm that the Japanese explanation should read "...末尾にb, c, dを付した" (matching the English column and `02-04-wakun`'s pattern), then remove the bracketed review comment.
- Authority status: `Requires Confirmation`.
- Human confirmation required: Yes.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: correction confirmed and directed — align the Japanese explanation with the English column. Applied in both `02-06-pronunciations.ja.md:56` and `02-06-pronunciations.en.md:40` (the row's Japanese-language explanation column is present in both files): "...変異形を追加したものには末尾にxを付した。 *(User indicates 'x' is incorrect, and 'b,c,d' is correct for variants)*" → "...変異形を追加したものには末尾にb, c, dを付した。" Verified with a further Hugo build: zero remaining occurrences of "xを付した" or "User indicates" on either rebuilt page; "b, c, dを付した" renders correctly in both. Fixed and verified; closed.

No non-blocking improvement candidates were identified.

---

### Change and Validation

**Initial pass (RR1–RR3)**: Files changed: `02-data-overview/_index.ja.md`, `02-02-notes.en.md`, `02-06-pronunciations.ja.md`, `02-06-pronunciations.en.md` (4 files, primary scope), plus `04-entry-input/04-03-handling.en.md` (1 file, related-scope). `02-06-pronunciations.{ja,en}.md`'s UR1 location was read and evaluated but not edited at this stage.

Verified: `git status --short` clean before editing; `git diff` confirmed changes limited to the designated lines across the 5 files; `hugo --minify` build — 157 JA pages / 51 EN pages, 0 errors. Rebuilt pages confirm: the DHSJR link resolves to `/docs/krm/08-case-studies/08-05-dhsjr/` (ja) and `/docs/krm/08-case-studies/08-05-dhsjr/` (en) with zero remaining occurrences of the old unprefixed `08-case-studies/5-dhsjr` path; the two trailing-slash fixes render as `./02-02-notes/` and `./02-01-main/`; both `04-03-handling.en.md` links now resolve to `/en/docs/krm/02-data-overview/`.

**Confirmation pass (UR1)**: Files changed: `02-06-pronunciations.ja.md`, `02-06-pronunciations.en.md` (the same 2 files already touched in the initial pass, now further edited at a different location).

Verified: `git diff` confirmed the new change was limited to the designated table cell in both files; `hugo --minify` build — 157 JA pages / 51 EN pages, 0 errors. Rebuilt pages confirm zero remaining occurrences of "xを付した" or "User indicates" on either page, and "b, c, dを付した" renders correctly in both.

**Incidental observation (not a documentation finding)**: partway through editing, an active Vim swap file (`content/docs/krm/._index.en.md.swp`) was observed, indicating the project owner has `content/docs/krm/_index.en.md` open in a concurrent editing session. That file was not touched by this trial (it was never in scope), and the swap file was left untouched.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR3 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: none remaining — UR1 confirmed and resolved by the project owner; see Findings above. Files changed: `02-data-overview/_index.ja.md`, `02-02-notes.en.md`, `02-06-pronunciations.ja.md`, `02-06-pronunciations.en.md`, `04-entry-input/04-03-handling.en.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
