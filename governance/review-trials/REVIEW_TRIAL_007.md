## Review Trial 007

Target: `07-progress/` (`_index.md`, `1.md`–`7.md`) — Japanese-only by policy (`I18N_POLICY.md` §5: "Records and progress pages | Language-specific allowed"), no English counterpart exists or is expected.

Purpose: Seventh pilot of the KRM Documentation review workflow. This section is a Record (progress/status data), not Core Documentation, and the known issue was pre-identified by the user as link breakage — this record is kept proportionate to what was found: mostly link fixes and one non-trivial data question.

**Confirmation update (2026-07-27, same day)**: the project owner, who has direct domain knowledge of the radical data, resolved both UR1 and UR2. UR1: confirmed target is `05-annotation-policy/05-02-headword-count/`. UR2: confirmed `1.md`'s distinction between radical 14 (口) and radical 70 (囗) is correct, and that `01-01-introduction.{ja,en}.md`'s "70口" was the error (should be "70囗"); also directed unifying 049/116 to the traditional forms 齒/龜 across `01-01-introduction.{ja,en}.md`. Both applied and verified — see updated entries and §Change and Validation below.

---

### Scope

8 files reviewed. Document layer: Publication/Records (Supporting Materials, per `DOCUMENTATION_BLUEPRINT.md` §10). Document type: Record — status/progress counts, per `EDITORIAL_CONVENTIONS.md` §6 "Progress records" row ("Update status or counts" = `Requires Confirmation`). Protected content: present — quantitative annotation-progress counts and a radical-character reference table in `1.md`; not altered. Review level: AI-assisted review, Minimal Acceptance Checklist (Full Checklist not warranted — Supporting Materials, not Core Documentation). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Stale `/docs/notes/krm-main/progress/N/` links (known issue, confirmed)**
- Files/locations: `_index.md:15-21` (7 links), `2.md:35,47,57,69,74,87` (6 links, one pair duplicated).
- Evidence: each link's target is unambiguous — the link text matches the title of the corresponding sibling file (`1.md` title "掲出字" ↔ link text "掲出字", etc.), and this is the same known stale-path pattern already fixed in Trials 002 and 004 (`/docs/notes/krm-.../...` → `/docs/krm/.../...`).
- Fix: `/docs/notes/krm-main/progress/N/` → `/docs/krm/07-progress/N/` for N=1–7.
- Authority: `Allowed under existing standards; no additional approval required`.

**RR2 — Stray non-standard front-matter comment**
- Files: `_index.md`, `2.md`, `3.md`, `4.md`, `5.md`, `7.md` (all had `# 注釈作成の進捗状況` after `title:`; `1.md` and `6.md` did not have it).
- Same pattern already established as zero-impact and `Allowed` in Trial 005 (NB1) — removed directly here rather than re-proposing.
- Fix: comment line removed from all 6 files.

No other Allowed-tier issues found (no data-file-name typos, no other malformed links).

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — Ambiguous legacy link target, `1.md:17-18`**
```text
[注釈データ入力の詳細](http://localhost:1313/docs/notes/krm-main/notes-input/) >
[掲出字](/docs/notes/krm-main/notes-input/2/) > 掲出項目数 > 部首毎の掲出項目数と掲出字数のまとめ
```
Unlike RR1, this is not a simple sibling-file reference — it's a breadcrumb-style path (`notes-input/2/`) from the old site structure with no obvious 1:1 current equivalent, plus a dev-only `http://localhost:1313` prefix (both individually named as known technical debt in `CURRENT_STATE_REPORT.md`). Notably, the link text "注釈データ入力の詳細" was the *pre-Trial-005* front-matter title of `05-annotation-policy/_index.ja.md` (fixed in Trial 005 to "注釈作成の基本方針"), which suggests but does not confirm that section as the intended target. Per `DOCUMENTATION_STYLE_GUIDE.md` §8, "when the intended target is unclear, flag the issue rather than guessing." Authority: `Requires Confirmation`.

**Resolution (project owner, 2026-07-27)**: confirmed target is `05-annotation-policy/05-02-headword-count/` ("掲出字数の算出" — Calculation of Headword Character Count), which matches `1.md`'s actual content (a per-radical headword-count table). Applied: both lines replaced with a single link, `[掲出字数の算出](/docs/krm/05-annotation-policy/05-02-headword-count/)` followed by `> 掲出項目数 > 部首毎の掲出項目数と掲出字数のまとめ` (the absolute-path form was used in place of the relative path given in the request, matching this file's established path convention; the intended target is unaffected). Verified with a further Hugo build: the link resolves to `/docs/krm/05-annotation-policy/05-02-headword-count/`, and zero occurrences of `localhost` or `notes-input` remain on the rebuilt page. Fixed and verified; closed.

**UR2 — Possible radical-character discrepancies between `1.md`'s table and the reference list in `01-introduction/01-01-introduction.ja.md`**
Three rows in `1.md`'s per-radical count table use different characters than the corresponding entries in `01-01-introduction.ja.md`'s canonical 120-radical list: row 049 uses 齒 (vs. 歯), row 070 uses 囗 (vs. 口), row 116 uses 龜 (vs. 亀). The 齒/歯 and 龜/亀 pairs are plausibly an intentional kyūjitai/shinjitai (traditional/simplified) convention difference consistent across both rows; 囗/口 is not such a pair — 囗 ("enclosure") and 口 ("mouth") are visually similar but distinct radicals, so this one is more likely a genuine transcription difference. This is quantitative/radical-identification data — squarely protected content per `EDITORIAL_CONVENTIONS.md` §15 ("Data and Specifications") — and was not touched. Authority: `Requires Confirmation`.

**Resolution (project owner, 2026-07-27)**: confirmed `1.md`'s distinction is correct — radical 14 (口, "mouth") and radical 70 (囗, "enclosure") are genuinely different radicals, so `01-01-introduction.ja.md`/`.en.md`'s "70口" was a transcription error and should read "70囗". Also directed: unify 049 and 116 to the traditional (kyūjitai) forms 齒 and 龜 across both language versions, matching `1.md`. Applied: `01-01-introduction.ja.md` and `01-01-introduction.en.md` — row 49 (歯→齒), row 70 (口→囗), row 116 (亀→龜) — in both files. The edit was scoped precisely to these three radical-list entries; `01-01-introduction.en.md`'s row 14 (口, "mouth") was confirmed unaffected, since it is a different, correctly-口 radical. Verified with a further Hugo build: both language versions render 49齒/70囗/116龜 (ja) and "49 齒"/"70 囗"/"116 龜" (en) with zero remaining occurrences of the old forms in this list, while row 14's 口 is unchanged. Fixed and verified; closed.

#### Non-blocking Improvement Candidate

**NB1 — Duplicate "その他" reference link in `2.md`** (lines, now, 74 and 87): the same "詳細は...を参照。" sentence appears both before and after the その他 table, unlike the other four subsections (字体注/音注/義注/和訓), which each have it only once, after their table. Both now point to a valid target after RR1, so this is cosmetic inconsistency, not a defect. Not actioned.

---

### Change and Validation

**Initial pass (RR1, RR2)**: Files changed: `content/docs/krm/07-progress/_index.md`, `2.md`, `3.md`, `4.md`, `5.md`, `7.md` (6 files). `1.md` and `6.md` not modified at this stage.

Verified: `git status --short` clean before editing; `git diff` confirmed changes limited to the designated lines across the 6 files; `hugo --minify` build — 163 JA pages / 51 EN pages, 0 errors. Rebuilt `_index.md` and `2.md` pages resolve all 13 links to `/docs/krm/07-progress/N/` with zero remaining `docs/notes/krm-main` occurrences. The stray front-matter comment does not appear in any rebuilt page's `<head>`/metadata; the identical wording that does appear in `_index.md`'s rendered body text is unrelated ordinary prose (from the page's own introductory sentence), not a leftover of the removed comment.

**Confirmation pass (UR1, UR2)**: Files changed: `content/docs/krm/07-progress/1.md` (link replacement), `content/docs/krm/01-introduction/01-01-introduction.ja.md` and `01-01-introduction.en.md` (three radical-character corrections each, out of this trial's original primary scope but a direct result of investigating UR2).

Verified: `git status --short` before this pass showed only the 6 files from the initial pass, confirming a clean starting point for the new edits; `git diff` confirmed the new changes were limited to the designated lines in the 3 files; `hugo --minify` build — 164 JA pages / 51 EN pages, 0 errors (the JA increase from 163 reflects `REVIEW_TRIAL_007.md` itself becoming a built page, the same effect noted in prior trials). Rebuilt `1.md` resolves to `/docs/krm/05-annotation-policy/05-02-headword-count/` with zero remaining `localhost`/`notes-input` occurrences. Rebuilt `01-01-introduction.{ja,en}.md` render 齒/囗/龜 at rows 49/70/116 with zero remaining occurrences of the old forms, while row 14's 口 (a genuinely different, correctly unchanged radical) was confirmed intact in both language versions.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1, RR2 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: NB1 (still open — not addressed). Unresolved but recorded: none remaining — UR1 and UR2 both confirmed and resolved by the project owner; see Findings above. Files changed: `07-progress/_index.md`, `1.md`, `2.md`, `3.md`, `4.md`, `5.md`, `7.md`, `01-introduction/01-01-introduction.ja.md`, `01-introduction/01-01-introduction.en.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
