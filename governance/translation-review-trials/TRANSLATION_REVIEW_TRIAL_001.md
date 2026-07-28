# Translation Review Trial 001

## 1. Summary

Translated `05-03-jitaichu-formats.ja.md` into `05-03-jitaichu-formats.en.md`, replacing the
untranslated-body state flagged in Review Trial 011. This trial predates the formal adoption of
`project/workflows/translation-workflow.md` (added after this work was already complete); it is
recorded retroactively, in the new template, to establish a complete trail before the workflow is
used going forward. Two follow-up rounds occurred after the initial translation: a term-romanization
correction (字級 → *zìjí*, not *jikyū*) and a tone-mark notation modernization (old convention
`@`/`"` → current convention `_`/`V`), the latter also applied to the Japanese source under
separate, explicit instruction. Status: complete, with all raised questions resolved by the
project owner.

---

## 2. Scope

- **Source file**: `content/docs/krm/05-annotation-policy/05-03-jitaichu-formats.ja.md`
- **Target file**: `content/docs/krm/05-annotation-policy/05-03-jitaichu-formats.en.md`
- **Related files consulted for terminology precedent**:
  `content/docs/krm/03-entry-data-model/03-02-types-of-entries.en.md`,
  `03-03-concepts-char.en.md`, `04-entry-input/04-01-id.en.md`, `04-03-handling.en.md`,
  `05-annotation-policy/05-01-basic-policy.en.md`, `05-02-headword-count.en.md`,
  `01-introduction/01-01-introduction.en.md`, `content/docs/krm/_index.en.md`,
  `GLOSSARY_CONVENTIONS.md` (checked; no entries yet for the terms in question)
- **Files changed**:
  `05-03-jitaichu-formats.en.md` (full translation, then two follow-up corrections);
  `05-03-jitaichu-formats.ja.md` (two follow-up corrections — see §2 note below)
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-28

**Note on the `.ja.md` changes**: two edits were made to the Japanese source after the initial
translation, both under separate, explicit project-owner instruction rather than as part of
ordinary translation work (per `translation-workflow.md` §5's "do not modify the Japanese source"
rule for the translation task itself):
1. The notation-format table's blank "合計" (Total) cell was filled in as `264`, after the project
   owner confirmed this value against the table's own subtotals (see §4).
2. The tone-mark notation in the quoted manuscript annotations was modernized from the old
   convention (`@` = no tone mark, `"` = voiced tone mark) to the current convention (`_`, `V`),
   per explicit project-owner instruction, applied identically to both language versions.

---

## 3. Terminology Decisions

| Japanese term | English rendering | Basis |
| --- | --- | --- |
| 字体注 | **`Notes on Character Form`** | Existing precedent, used site-wide (e.g. `03-01-data-structure.en.md`, `04-03-handling.en.md`) |
| 字級 (as a defined term/concept) | **`Form Classification Tag`** (字級, *zìjí*) | Existing precedent for the English term (`03-02-types-of-entries.en.md:39`). Romanization corrected mid-trial — see §4 |
| 正／俗／通／今／或 (tag values) | standard / popular-vulgar / common / current-present form / alternative | Existing precedent (`03-02-types-of-entries.en.md`, `03-03-concepts-char.en.md`) |
| 古／俗通 (tag values) | archaic / popular-vulgar & common | New decision this trial — no prior precedent found; not escalated (low-risk, plain dictionary-style gloss, not a scholarly claim) |
| 図書寮本 | Zushoryō manuscript | Existing precedent (`01-01-introduction.en.md`, `05-01-basic-policy.en.md`) |
| 蓮成院本 | Renjō-in manuscript | Existing precedent (`01-01-introduction.en.md`, `05-02-headword-count.en.md`) |
| 龍龕手鏡／龍龕手鑑 | *Longkan Shoujian/Shoujing* | Existing combined-form precedent (`05-02-headword-count.en.md:590`), extended consistently to every occurrence of either kanji form in this page |
| 正宗索引 | Masamune's Index | Existing precedent (`05-02-headword-count.en.md`) |
| 万象名義 | *Tenrei Banshō Meigi* | Existing precedent (`05-01-basic-policy.en.md`, `_index.en.md`) |
| 新撰字鏡 | *Shinsen Jikyō* | Existing precedent (`_index.en.md`) |
| HNG | HNG (Hanzi Normative Glyphs Database) | Existing precedent (`03-03-concepts-char.en.md`, `05-01-basic-policy.en.md`) |
| しんにょう（辶） | '辶' (*shinnyō*, motion radical) | Existing precedent (`05-02-headword-count.en.md:48`) |
| 虫損 | wormhole damage | Existing precedent (`04-02-char.en.md`) |
| 入声／平声（tone names） | Entering tone / Level tone | Existing precedent (`05-01-basic-policy.en.md`, `05-02-headword-count.en.md`, `04-03-handling.en.md`) |
| 隋書 | *Book of Sui* | New decision this trial — standard scholarly English name for this classical Chinese official history; not escalated (unambiguous) |
| 反切 citation format (e.g. 「的：都歴切」) | *xiaoyun* '的': *dūlì qiè* (都歴切) | Matched the established *Guangyun*-citation pattern in `05-02-headword-count.en.md:558` (tone, rhyme, *xiaoyun*, *fanqie*) |
| 李景遠 | Lee Kyeong Won | Existing precedent (`03-02-types-of-entries.en.md`, `03-03-concepts-char.en.md`) |
| 張馨方 | Zhang Xinfang | Existing precedent (`content/docs/krm/_index.en.md`) |
| Footnote 1 (李景遠's dissertation) | Full citation reused verbatim from `03-03-concepts-char.en.md:49` | Same source cited there in identical form |

---

## 4. Questions Raised and Owner Confirmations

**Q1 — 字級's romanization: Japanese *jikyū* or Chinese *zìjí*?**
The initial translation used "字級, *jikyū*" (Japanese on-yomi). The project owner pointed out
that Lee Kyeong Won's scholarship is written in Chinese, from a Chinese-linguistics standpoint,
and that the Chinese pinyin reading should be given for consistency. A site-wide grep confirmed
`03-02-types-of-entries.en.md` and `03-03-concepts-char.en.md` both already established
**"字級, *zìjí*"** as the precedent for this specific term (as distinct from the Japanese on-yomi
readings correctly used elsewhere for actual tag-value citations from the manuscript, e.g. "正今"
(*sei kin*) in `04-01-id.en.md`, which are a different thing — a Japanese-manuscript annotation
reading, not the metalinguistic term itself).
**Resolution (project owner, 2026-07-28)**: use *zìjí*, matching `03-02`/`03-03`. Applied to
`05-03-jitaichu-formats.en.md:17`.

**Q2 — Notation-format table's blank "合計" (Total) cell.**
The source table's final row had no value. Flagged to the project owner rather than silently
computing and inserting a number.
**Resolution (project owner, 2026-07-28)**: confirmed as a recording omission; the correct total
is the sum of the six subtotals. Independently recomputed (55+12+1+1+194+1 = 264) and cross-checked
against the sum of all 20 individual instance counts (also 264) before applying — the project
owner's initial recollection was 265, and this discrepancy was raised and resolved via
`AskUserQuestion` before editing. Applied to both `05-03-jitaichu-formats.ja.md:83` and
`05-03-jitaichu-formats.en.md:74` as `264`.

**Q3 — Old vs. current tone-mark notation convention in quoted manuscript annotations.**
Not originally raised by the translator — the translation reproduced the quoted annotations
verbatim, as-is, per the "keep primary sources in original form" guideline. The project owner
subsequently identified that the quoted tone-pattern notation (e.g. `シタヽル(LL@@)`,
`シタヽル(LLL"L)`) used an old transcription convention: `@` (no tone mark) should be `_`, and `"`
(voiced tone mark) should be `V`.
**Resolution (project owner, 2026-07-28)**: apply the corrected notation, scoped to
`05-03-jitaichu-formats.{ja,en}.md` only — a site-wide sweep was explicitly deferred (also affects
at least `05-04-onchu-problems.{ja,en}.md`, `08-case-studies/08-02-miru.md`, and
`08-case-studies/08-04-kana-split.md`; logged to `project/issues.md` item 6). Applied to all 4
occurrences (2 in the Kanchi-in manuscript subsection, 2 in the Renjō-in manuscript subsection) in
both `05-03-jitaichu-formats.ja.md` and `05-03-jitaichu-formats.en.md`.

**Minor, not escalated**: the folio citation "中一12裏" was rendered as "Middle volume, fascicle 1,
folio 12 verso" — no exact precedent for this specific citation shape was found elsewhere on the
site, though the "verso"/"folio" vocabulary itself is established (`05-02-headword-count.en.md`).
Flagged transparently to the project owner in the initial report as an area of lower confidence;
no correction was requested.

---

## 5. Translation-Specific Issues

- **Quoted manuscript annotations kept in original script.** All bolded **`Form Classification
  Tag`** annotations (二正, 或, 二俗, 俗滳字, etc.) and the numbered citation lists of the
  **`Original Glosses`** (including *fanqie* spellings, **`Japanese Native Readings`**, and
  tone-pattern notation) were left untranslated, matching how `05-01-basic-policy.en.md` and
  `05-02-headword-count.en.md` handle directly quoted primary-source content — translating them
  would have meant paraphrasing a manuscript transcription, which is protected content under
  `EDITORIAL_CONVENTIONS.md` §11.
- **Structural parity maintained.** The English page mirrors the Japanese page's heading structure
  and section order one-to-one (H1, 2 H2 sections, 3 H3 subsections), per `translation-workflow.md`
  §3.
- **No untranslated fragments remained** after the initial pass; confirmed via a rebuilt-page
  search for "Under preparation" (zero occurrences) and manual read-through.

---

## 6. Change and Validation

- **Files changed**: `05-03-jitaichu-formats.en.md`, `05-03-jitaichu-formats.ja.md` (the latter for
  the two owner-directed corrections only — see §2 note).
- **Verification method**: `git status --short` before/after each round of edits; `hugo --minify`
  build to a scratch destination, run after the initial translation and after each follow-up
  correction (3 builds total); rendered-output inspection for each change.
- **Build result**: 157 JA / 51 EN pages, 0 errors, across all 3 builds.
- **Protected-content check**: quoted manuscript annotations, *fanqie* spellings, and tone-pattern
  notation were reproduced verbatim (not paraphrased) in the initial translation; the two
  follow-up edits (合計 value, tone-mark notation) were explicit, owner-directed corrections to
  the primary content itself, not translation choices, and were applied identically to both
  language versions to keep them in sync.

---

## 7. Final Review Result

- **Overall status**: `Complete`
- **Open items remaining**: none for this file. Site-wide follow-ups deferred and logged
  separately (see §8).
- **Files changed**: `05-annotation-policy/05-03-jitaichu-formats.en.md`,
  `05-annotation-policy/05-03-jitaichu-formats.ja.md`
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-28

---

## 8. Remaining Follow-up Actions

- The tone-mark notation issue (Q3) is confirmed present in at least `05-04-onchu-problems.{ja,en}.md`
  (the next translation target) and two `08-case-studies/` files; logged as item 6 in
  `project/issues.md`. A full site-wide sweep was explicitly deferred by the project owner.
- `project/translation-backlog.md` is intentionally **not** updated yet for `05-03` — per project
  owner instruction, the backlog checklist will be updated only once all of
  `05-annotation-policy/`'s pending translations (05-03 through 05-07) are complete.
- Next file in the translation queue: `05-04-onchu-problems.ja.md` → `.en.md` (already reflected in
  `project/workflows/translation-workflow.md` §2).
- No `GLOSSARY_CONVENTIONS.md` update was made for the terms decided in §3 of this trial (古/俗通
  glosses, *Book of Sui*) — these were low-risk, non-escalated decisions; whether they warrant
  formal glossary entries is left to the project owner's judgment as more pages are translated and
  these terms recur.
