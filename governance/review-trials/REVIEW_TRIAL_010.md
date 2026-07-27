## Review Trial 010

Target: `04-entry-input/` (`_index.{ja,en}.md`, `04-01-id`, `04-02-char`, `04-03-handling`, `.ja.md`/`.en.md` — 4 file pairs, 8 files). `_index.{ja,en}.md` and `04-01-id.{ja,en}.md` were previously reviewed and fixed in Trial 004; re-checked here as part of the full-directory scope and found clean (no new issues, no regressions). `04-03-handling.{ja,en}.md` had only been touched incidentally (a link fix) in Trial 008; this is its first full review.

Purpose: Tenth pilot of the KRM Documentation review workflow. This section is Core Documentation (Editorial and Encoding Rules layer). `04-03-handling.*.md` is a large, dense page (477/487 lines) and produced a substantial number of findings, so this record is longer than recent trials — proportionate to what was actually found, not padded.

**Confirmation update (2026-07-27, same day)**: the project owner reviewed all five Unresolved items and directed resolutions for four of them, confirming the fifth (UR3) as correct as-is. UR1: delete. UR2: fix (English only — the Japanese was already correct). UR3: leave unchanged, explicitly noting the "を" is a deliberate representation of the passage's own subject (a suspected *wokototen* mark), not an error. UR4: delete the first (duplicate) paragraph. UR5: add the proposer's name, "豊島正之" (Toyoshima Masayuki), to the Japanese version. All applied and verified — see the updated entries and §Change and Validation below.

---

### Scope

8 files reviewed. Document layer: Editorial and Encoding Rules (`DOCUMENTATION_BLUEPRINT.md` Layer 4). Document type: Rule Reference (`04-02-char`, `04-03-handling`) and Concept/Rule Reference (`04-01-id`, already clean from Trial 004). Protected content: extensive — transcription/encoding rules, dozens of worked manuscript examples, `Compiler's Remarks` citations, and one directly-quoted `definition` data value. Review level: AI-assisted review, Full Documentation Review Checklist (Core Documentation). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Stale `/docs/notes/...` link (documented known issue, confirmed)**
`04-03-handling.ja.md:47`: `/docs/notes/krm_main/contens/` → `/docs/krm/02-data-overview/`. This exact file is named in `CURRENT_STATE_REPORT.md`'s list of pages retaining stale `/docs/notes/...` paths. Target confirmed by the English counterpart's equivalent sentence, which already links to `/en/docs/krm/02-data-overview/`.

**RR2 — Stray unpaired closing quotation mark**
`04-03-handling.en.md:37`: sentence ended `...nasal sound symbols."` with no matching opening quote anywhere in the paragraph. Removed the stray `"`.

**RR3 — Stray standalone full-width period**
`04-03-handling.en.md:399`: a lone `。` sat on its own line between two English sentences, with no Japanese text around it (an apparent leftover from translation). Removed.

**RR4 — Dangling footnote references with no definitions**
`04-03-handling.en.md:117-119`: `[^1]`, `[^2]`, `[^3]` were referenced after **`Transposition Marks`**, **`Deletion Marks`**, and **`Interpolation Marks`**, but none of the three were ever defined anywhere in the file (confirmed by search; the file's one legitimate footnote, `[^note1]`, is unrelated and unaffected). Verified via Hugo build that undefined footnote references render as nothing (silently dropped, not shown as broken links or raw text) — removing them changes no visible output, only cleans up dead source markup. Removed all three markers; left the surrounding prose (which already fully explains each term inline) unchanged.

**RR5/RR6 — Broken shortcode-escaping example, `04-02-char.{ja,en}.md`**
Both files contained an "example code" line meant to show the literal `{{< figure ... >}}` syntax, escaped as `{{&lt; figure ... &gt;}}`. This is not Hugo's shortcode-escaping syntax, and Goldmark's autolinker partially processed the embedded URL and smart-quoted the attribute quotes, producing garbled output: a broken `<a href=...%22>` fragment with mismatched quote characters (confirmed via Hugo build before fixing). Fixed by wrapping the example in a fenced code block using Hugo's actual shortcode-escaping syntax, `{{</* figure ... */>}}`, matching the code-fence convention already used for the `![正β](...)` examples earlier in the same file. Re-verified via build: the code block now displays the literal, correctly-escaped shortcode text, followed by the actual working `<figure>` element — the intended "show the code, then the result" pattern. (Note: an initial attempt using only a plain ` ```markdown ` fence without Hugo's `/* */` escape did **not** work — Hugo expands shortcodes before Goldmark processes code fences, so the fence briefly contained the *rendered* `<figure>` output instead of literal text. This was caught and corrected before finalizing.)

All six: `Allowed under existing standards; no additional approval required` — stale link (matches established pattern), stray punctuation (ordinary typos), dead markup with zero rendering effect (confirmed by build), and a rendering-syntax fix with no content change (matches Trial 002's F2 precedent).

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — Stray "Under preparation." marker in a fully developed article**
`04-03-handling.en.md:12`. Same pattern as Trial 004's UR1 (`04-01-id.en.md`, ultimately deleted after confirmation). No Japanese counterpart.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: delete. Removed from `04-03-handling.en.md:12`. Verified with a further Hugo build: zero remaining occurrences of "Under preparation" on the rebuilt page. Fixed and verified; closed.

**UR2 — Self-contradictory letter/codepoint mismatch in an encoding rule**
`04-03-handling.en.md:329`: "The nasal sound symbol...is represented by the English letter **'V'** (U+004E)." U+004E is the codepoint for **N**, not V — and the Japanese original (`04-03-handling.ja.md`, 鼻音符号 section) says "英字 N（U+004E）", confirming 'N' is correct. This appears to be a copy-paste error from the immediately preceding 濁音 (voiced sound) paragraph, which correctly uses 'V' (U+0056). Classified as `Requires Confirmation` rather than `Allowed` despite the strong internal evidence, since it is Encoding Rule content (`EDITORIAL_CONVENTIONS.md` §6 "Encoding rules" row).
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: fix the English letter from 'V' to 'N'; the Japanese version was confirmed already correct and needed no change. Applied to `04-03-handling.en.md:326`: "...represented by the English letter 'V' (U+004E)..." → "...represented by the English letter 'N' (U+004E)...". Verified with a further Hugo build: the rebuilt page reads "represented by the English letter 'N' (U+004E)". Fixed and verified; closed.

**UR3 — Possible transcription discrepancy in a quoted `definition` data value**
`04-03-handling.en.md:402` (a worked example under `Morphosyntactic Glosses`/ヲコト点) reads `definition: ...琢「ミカク」玉を工也`, while the Japanese original (`04-03-handling.ja.md:396`) and a second, later citation of the same phrase within the English file itself (`04-03-handling.en.md:478`, `琢「ミカク」玉工也`) both lack the character `を`. This is a directly quoted manuscript transcription value — squarely protected content (`EDITORIAL_CONVENTIONS.md` §11, "Editors must not silently change...a transcription").
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: leave unchanged. The project owner noted this location is specifically discussing a suspected *wokototen* mark, and the "を" is a deliberate representation of that reading within the transcription — not a transcription error. No change made; closed with no action.

**UR4 — Likely-duplicate paragraph in the Japanese introduction**
`04-03-handling.ja.md:21-24` and `:25-29` are two consecutive paragraphs that open with the identical sentence ("次に、名義抄では、漢字の形・音・義に関わる多様な情報を...") but diverge at the end: the first (older-looking) paragraph says "省略符号、合符を扱う" and stops; the second says "代用符号を扱う" and continues with additional detail. The file's own later section heading is "### 代用符号" (matching the second paragraph's terminology, not the first's "省略符号"). The English version (`04-03-handling.en.md:21`) has only one clean paragraph, matching the second/updated Japanese wording — no duplicate. This mirrors Trial 003's UR1 pattern (a likely leftover draft paragraph), now with stronger corroborating evidence from the English version's absence of the duplicate.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: delete the first (older, "省略符号") paragraph, lines 21-23. Removed from `04-03-handling.ja.md`. Verified with a further Hugo build: zero remaining occurrences of "省略符号" on the rebuilt page, and "代用符号" (the correct, retained term) still appears throughout as expected. Fixed and verified; closed.

**UR5 — English-only attribution not present in the Japanese original**
`04-02-char.en.md:48`: "This Beta Method was proposed by Toyoshima Masayuki." has no counterpart in `04-02-char.ja.md`'s β方式 section. Same category as Trial 009's UR1 (an English-only added claim).
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: accurate; reverse-import into Japanese (same resolution pattern as Trial 009's UR1). Added to `04-02-char.ja.md`'s β方式 definition: "近い字形とβ、γ等とを組み合せて記述する方式である。" → "...組み合せて記述する方式である。この方式は豊島正之氏の提唱による。" Verified with a further Hugo build: "豊島正之氏の提唱による" renders correctly on the rebuilt Japanese page. Fixed and verified; closed.

---

### Change and Validation

**Initial pass (RR1–RR6)**: Files changed: `04-03-handling.ja.md` (1 line), `04-03-handling.en.md` (4 edits: stray quote, stray period, 3 footnote markers), `04-02-char.ja.md` (1 block), `04-02-char.en.md` (1 block).

Verified: `git status --short` clean before editing; `git diff` confirmed changes limited to the designated locations across the 4 files; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors, run three times (initial fix pass, a correction after the first shortcode-escaping attempt proved wrong, and final re-verification). Rebuilt pages confirm: the `02-data-overview` link resolves correctly with zero remaining `docs/notes` occurrences; zero remaining stray `"` or standalone `。`; the three footnote markers produce no visible change (confirmed absent before and after, as expected); the `04-02-char` example block now renders literal shortcode syntax followed by the working image, with no broken autolink/quote artifacts.

**Confirmation pass (UR1, UR2, UR4, UR5 — UR3 left unchanged)**: Files changed: `04-03-handling.en.md` (2 more edits: delete "Under preparation.", V→N), `04-03-handling.ja.md` (1 more edit: delete duplicate paragraph), `04-02-char.ja.md` (1 more edit: add attribution).

Verified: `git diff` confirmed the new changes were limited to the designated locations; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt pages confirm: zero remaining "Under preparation" occurrences; the nasal-sound-symbol sentence now reads "the English letter 'N' (U+004E)"; zero remaining "省略符号" occurrences while "代用符号" still appears 10 times as expected; "豊島正之氏の提唱による" renders correctly in the Japanese β方式 section.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR6 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: none remaining — UR1, UR2, UR4, and UR5 confirmed and resolved; UR3 confirmed correct as-is (no change). See Findings above for each disposition. Files changed: `04-entry-input/04-02-char.ja.md`, `04-02-char.en.md`, `04-03-handling.ja.md`, `04-03-handling.en.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
