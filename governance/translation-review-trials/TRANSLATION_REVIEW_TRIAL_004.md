# Translation Review Trial 004

## 1. Summary

Translated `05-06-wakun-materials.ja.md` into `05-06-wakun-materials.en.md`, following
`project/workflows/translation-workflow.md`. The prior `.en.md` was not a translation at all — it
was a stub reading "Under preparation." followed by a raw, untranslated copy of an *older revision*
of the Japanese source (predating several edits to the `.ja.md`, including citation additions in
the Kobayashi Kyōji list and a different set of examples in the "和訓の同定" section). This trial
produced a full translation from the current `.ja.md`, which is overwhelmingly a bibliography page
(~90 citations across three abbreviation tiers) plus two short worked philological examples.
Status: **complete**, with several citation-level items flagged in §4/§5 for project-owner
awareness rather than resolved unilaterally, consistent with the preservation policy on
bibliography content. **Update (same day, 2026-07-29):** the project owner reviewed the flagged
items and confirmed three corrections, applied in a follow-up pass — see §9.

---

## 2. Scope

- **Source file**: `content/docs/krm/05-annotation-policy/05-06-wakun-materials.ja.md`
- **Target file**: `content/docs/krm/05-annotation-policy/05-06-wakun-materials.en.md`
- **Related files consulted for terminology precedent**:
  `content/docs/krm/05-annotation-policy/05-01-basic-policy.en.md` (five abbreviated-work
  citations reused verbatim: Masamune's Index, Mochizuki's Wakun Collection, Kusakawa's Wakun
  Collection, Nakamura's Monzen, Kunten Goi Shūsei; also Nikkoku/Daikanwa/Kokun Isan dictionary
  citations),
  `content/docs/krm/05-annotation-policy/05-04-onchu-problems.en.md` and
  `05-05-gichu-quantity.en.md` (established the light-touch citation format — romanized title with
  English gloss in parentheses, journal name romanized/italicized without a separate English
  gloss — used throughout this page's bibliography, as distinct from `01-01-introduction.en.md`'s
  heavier Chicago-style apparatus, which glosses journal names too),
  `content/docs/krm/01-introduction/01-01-introduction.en.md` (source of ~20 reused
  author/title/journal romanizations for papers that also appear in that page's master
  References list — e.g. Inukai Morimasa, Takase Shōichi, Kazama Rikizō, Yamamoto Hideto/Shingo,
  Kōno Toshihiro, Ishii Yukio, Takahashi Hiroyuki, Katō Kōji, Hagihara Yoshio),
  `AGENTS.md` §7–8 and `GLOSSARY_CONVENTIONS.md` (preservation of bibliography/identifiers;
  terminology handling).
- **Files changed**:
  - `content/docs/krm/05-annotation-policy/05-06-wakun-materials.en.md` (full translation, net new
    — the previous content was a stub, not a translation, so nothing prior was overwritten in a
    substantive sense)
  - `project/translation-backlog.md` (checked off the `05-06` line, which was already tracking this
    page as untranslated — routine backlog housekeeping, not scholarly content)
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-29

No change was made to `05-06-wakun-materials.ja.md`. Unlike Trial 003, no new scholarly content was
added to the Japanese source in this session.

---

## 3. Terminology Decisions

| Japanese term | English rendering | Basis |
| --- | --- | --- |
| 和訓 | `Japanese Native Reading` (*wakun*) | Existing precedent (05-04, 05-05) |
| 義注／漢文義注 | `Semantic Gloss in Chinese` | Existing precedent (05-05) |
| 仮名音注 | `Kana gloss` | Existing precedent (05-04) |
| 同音字注 | `Homophone gloss` | Existing precedent (05-04) |
| 掲出字 | `Headword` | Existing precedent (project-wide) |
| 注文 | `Original Gloss` | Existing precedent (05-01) |
| 正宗索引 / 望月和訓集成 / 草川和訓集成 / 中村文選 / 訓点語彙集成 | Masamune's Index / Mochizuki's Wakun Collection / Kusakawa's Wakun Collection / Nakamura's Monzen / Kunten Goi Shūsei | Existing precedent, reused verbatim from 05-01 |
| 日国 / 大漢和 / 故訓匯纂 | Nikkoku / Daikanwa / Kokun Isan | Existing precedent, reused verbatim from 05-01 |
| 岡田研究 / 小松論考 / 望月研究 / 築島著作集三 / 吉田国語 | Okada's Study / Komatsu's Study / Mochizuki's Study / Tsukishima's Collected Works, Vol. 3 / Yoshida's Kokugo | New decision, low-risk, not escalated — labels constructed in the same "Author's X" pattern established by 05-01's five reused entries; underlying citations for two of these (Tsukishima 2016, Yoshida 2013) are reused verbatim from `01-01-introduction.en.md` |
| Bibliography citation format (journal articles) | `Author, Given. "Romanized Title" (English gloss). *Romanized Journal* vol, no. (year): pages.` — journal name romanized/italicized but not separately glossed | New decision, low-risk, not escalated — matches the lighter format already established in 05-04/05-05, chosen over 01-01's heavier format (which also glosses journal names) because this page sits in the same 05-annotation-policy chapter as 05-04/05-05 |
| 箋注本和名抄 | *Senchūbon Wamyōshō* (an annotated recension of the *Wamyō Ruijushō*) | New decision, low-risk — minimal explanatory gloss added per the workflow's "Audience Adjustments" allowance, since the work is not otherwise named/glossed anywhere else in translated KRM pages |

---

## 4. Questions Raised and Owner Confirmations

No passage required scholarly interpretation or was ambiguous enough to block translation outright.
However, the following citation-level discrepancies were noticed while cross-checking this page's
bibliography against the overlapping master list in `01-01-introduction.en.md`, and were **not**
resolved unilaterally — the `.ja.md` source's own numbers were kept as authoritative for this page,
per the instruction not to alter citations/identifiers without explicit direction:

- **Kazama Rikizō, "*Ruiju Myōgishō* no *Monzen* Yomi"**: this page's source gives the year as
  1980 (vol. 36, no pages stated); `01-01-introduction.en.md` reference #18 gives the year as 1979
  with pages 8–35. Not reconciled here.
- **Yamamoto Shingo, "Keiō Gijuku Toshokan-zō *Shōryōshū Ryakuchū* Shuttenkō"**: this page's source
  gives pages 47–49; `01-01-introduction.en.md` reference #79 gives pages 32–55. Not reconciled
  here.
- **Kobayashi Kyōji's "Kanchi-in-bon ni Nai Kanji Chūki (3)"** entry: the `.ja.md` source itself
  labels the quoted sub-title "(二)" (i.e., "(2)") even though it is the third item in this
  sequence and follows an item already labeled "(二)" — this looks like a pre-existing typo in the
  Japanese source, not something introduced by translation. Flagged in the English text itself
  (see the file, item "Kanchi-in-bon ni Nai Kanji Chūki (3)") rather than silently corrected.
- **Author-name romanizations without prior precedent in this project**, constructed by the
  translator from standard readings and not yet confirmed by the project owner: こまつひでお
  (rendered "Komatsu, Hideo" — written in hiragana in the source, apparently to distinguish this
  author from the kanji-written 小松英雄 cited two lines above), 呉美寧 (rendered "Go, Bimei" —
  lowest-confidence romanization in this trial; could plausibly be a Korean name romanized
  differently), 蔵中進 ("Kuranaka, Susumu"), 添田建治郎 ("Soeda, Kenjirō"), 門前正彦 ("Monzen,
  Masahiko"), 近藤泰弘 ("Kondō, Yasuhiro"), 平子達也 ("Hirako, Tatsuya"), 佐藤栄作 ("Satō, Eisaku"),
  松本光隆 ("Matsumoto, Mitsutaka"). None of these affect scholarly content — they are Latin-script
  reference conveniences for readers — but a project-owner or specialist pass to confirm these
  readings (especially 呉美寧) would be worthwhile before treating them as settled precedent for
  future trials.

---

## 5. Translation-Specific Issues

- **Primary-source quotations**: the *Guangyun*/*Tenrei Banshō Meigi*/Song-*Yupian*/周礼/*Kangxi
  Zidian* excerpts quoted in the "和訓の同定" section were kept in their original Chinese/kanbun,
  per §3's "Primary Sources" guideline; only short technical terms (e.g. individual glosses) were
  given brief English glosses in parentheses where already established by precedent (e.g. 05-05).
  The three bulleted 腊-entry citations (万象名義, 宋本玉篇, 広韻) were left completely untranslated
  as block quotations, matching how comparable passages were handled in 05-04/05-05.
- **Stale draft discrepancy**: the previous `.en.md` stub was based on an older `.ja.md` revision
  containing different examples than the current source (an extra concluding paragraph citing
  Xuanying's *Yiqiejing yinyi* and a full 周礼 excerpt, which no longer exist in the current
  `.ja.md`). The new translation follows the *current* `.ja.md` only; none of that removed content
  was reintroduced.
- **Ellipsis-based citation shorthand caught in self-review**: an early draft of the ~30-entry
  Kobayashi Kyōji citation list used a "..." ditto convention to avoid repeating the base title
  each time. This was corrected before finalizing — every citation now spells out its full
  romanized title and English gloss in full, matching how the `.ja.md` source itself repeats the
  full quoted title in every bullet.
- **Structural parity**: full one-to-one structural parity with the `.ja.md` was maintained —
  same heading structure (`## References` / `### References Cited by Abbreviation` / `###
  References Cited Without Abbreviation` / `## Identifying Wakun` with its two sub-examples), same
  number of bibliography entries (15 abbreviated non-Kobayashi + 30 Kobayashi + 45 non-abbreviated
  = 90 total), same two worked examples in the same order.
- **`kazama_location`/`hanzi_entry`/`definition` field blocks**: left as unlabeled/untranslated
  field names, matching the convention already established in 05-04 and 05-05 for these structured
  data excerpts.

---

## 6. Change and Validation

- **Files changed**:
  - `content/docs/krm/05-annotation-policy/05-06-wakun-materials.en.md`
  - `project/translation-backlog.md` (checkbox only)
  - `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_004.md` (this file)
- **Verification method**: `git status`/`git diff` review before and after; full `hugo --quiet`
  production build run twice (once after the initial draft, once after the ellipsis cleanup pass)
  with zero errors both times; manual full read-through of the rendered `.en.md` source for
  leftover placeholder text, stray ellipses, or malformed Markdown.
- **Build result**: `hugo --quiet` exit code 0, no warnings surfaced in output, both times.
- **Protected-content check**: all bibliographic identifiers (volume numbers, page ranges, years)
  were copied from the `.ja.md` source without alteration, including in the two cases (§4) where
  they conflict with a different page's citation of the same paper — the discrepancy was preserved
  and flagged, not silently harmonized. The two worked philological examples in "和訓の同定" were
  translated for exposition but their factual claims, character-form arguments, and citation
  content were not altered, added to, or removed.

---

## 7. Final Review Result

- **Overall status**: Complete. Owner confirmation on the flagged open items received and applied
  the same day (see §9).
- **Open items remaining**: see §9 for what was resolved; the reconciliation question in the
  now-superseded list below (Kazama Rikizō / Yamamoto Shingo citation-detail discrepancies against
  `01-01-introduction.en.md`) remains open — the owner's confirmation did not address these two.
- **Files changed**: see §6 and §9
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-29

---

## 8. Remaining Follow-up Actions

- Per `project/translation-backlog.md`, the next pending Core Documentation translation targets
  are `05-03-jitaichu-formats` and `05-07-annotation-examples` (05-01, 05-02, 05-04, 05-05, and now
  05-06 are complete).
- `project/workflows/translation-workflow.md` §2 ("Current Translation Target") should be updated
  to point at whichever of `05-03` or `05-07` the project owner wants translated next.
- The Kazama Rikizō / Yamamoto Shingo citation-detail discrepancies against
  `01-01-introduction.en.md` (§4) remain unresolved and are not addressed by §9's corrections;
  revisit if either page is touched again.

---

## 9. Follow-up: Owner Confirmation and Corrections Applied (2026-07-29, same day)

The project owner reviewed the open items in §4 and gave the following direction:

1. **`.ja.md` typo confirmed and fixed**: the project owner confirmed the "(2)"/"(3)" labeling
   mismatch identified in §4 was indeed a copy-paste typo in the Japanese source, not a
   deliberate numbering. Per explicit instruction, `05-06-wakun-materials.ja.md` line 64 was
   corrected: the quoted sub-title's trailing "(二)" was changed to "(三)", so the citation now
   reads "…観智院本にない漢字注記について―(三)」", matching its bold label
   "**観智院本にない漢字注記(3)**" and its already-distinct volume/page/year (vol. 8, 27–55頁,
   2003年). No other part of the line (author, journal, volume, pages, year) was touched. This is
   the one case in this trial where the `.ja.md` source itself was edited, and it was done only
   after explicit owner instruction, per `project/workflows/translation-workflow.md` §5.
   `05-06-wakun-materials.en.md`'s corresponding entry ("Kanchi-in-bon ni Nai Kanji Chūki (3)") was
   updated in lockstep, and the now-resolved "apparent labeling inconsistency" caveat was removed
   from the English entry.
2. **門前正彦 romanization corrected**: "Monzen, Masahiko" → **"Kadosaki, Masahiko"**, per owner
   instruction. Both occurrences in `05-06-wakun-materials.en.md` (the 1960 "并" reading paper and
   the 1963 "欲" reading paper) were updated.
3. **呉美寧 romanization corrected**: "Go, Bimei" → **"Oh, Miyoung"**, per owner instruction
   (confirms this is a Korean name, romanized in Revised Romanization/McCune–Reischauer-adjacent
   style rather than as a Sino-Japanese reading). The one occurrence in
   `05-06-wakun-materials.en.md` was updated.
4. **All other provisional romanizations in §4 confirmed correct as-is** by the project owner:
   こまつひでお ("Komatsu, Hideo"), 蔵中進 ("Kuranaka, Susumu"), 添田建治郎 ("Soeda, Kenjirō"), 近藤泰弘
   ("Kondō, Yasuhiro"), 平子達也 ("Hirako, Tatsuya"), 佐藤栄作 ("Satō, Eisaku"), 松本光隆 ("Matsumoto,
   Mitsutaka"). These are now settled precedent for future trials touching the same authors.

**Files changed in this follow-up**:
- `content/docs/krm/05-annotation-policy/05-06-wakun-materials.ja.md` (one-character fix, line 64,
  under explicit owner instruction)
- `content/docs/krm/05-annotation-policy/05-06-wakun-materials.en.md` (matching fix to the
  Kobayashi Kyōji (3) entry; both Kadosaki, Masahiko occurrences; the Oh, Miyoung occurrence)
- `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_004.md` (this section)

**Verification**: `hugo --quiet` rebuilt cleanly (exit 0) after all four edits; `grep` confirmed no
remaining occurrences of "Monzen, Masahiko" or "Go, Bimei", and no remaining "(二)" mislabel on
`.ja.md` line 64.

**Still open**: the Kazama Rikizō (year/pages) and Yamamoto Shingo (page range) discrepancies
against `01-01-introduction.en.md`, noted in §4, were not part of this confirmation round and
remain unresolved. **Resolved in §10, below.**

---

## 10. Follow-up: Kazama Rikizō / Yamamoto Shingo Citation Corrections (2026-07-29, same day)

Investigating the §4/§9 open item, the project owner confirmed the correct facts directly (as the
author of several of the surveyed works and the person best positioned to verify them):

- **Kazama Rikizō, "*Ruiju Myōgishō* no *Monzen* Yomi"**: the correct publication year is **1979**,
  not 1980. Both `05-06-wakun-materials.ja.md` (line 110) and `01-01-introduction.ja.md` (line 267)
  had independently carried the same wrong year, "1980年" — i.e., this was a pre-existing error in
  the `.ja.md` source, not something introduced by translation.
  `01-01-introduction.en.md`'s existing "(1979)" turns out to have been correct all along; the
  apparent "mismatch" flagged in §4 was actually the `.ja.md` source being wrong, not the `.en.md`.
- **Yamamoto Shingo, "Keiō Gijuku Toshokan-zō *Shōryōshū Ryakuchū* Shuttenkō"**: the correct page
  range is **32–55**, not 47–49. `05-06-wakun-materials.ja.md` (line 115) had the wrong range;
  `01-01-introduction.ja.md` (line 282) carries no page range at all for this entry, so it wasn't
  wrong, just incomplete. `01-01-introduction.en.md`'s existing "32–55" was correct.

**Correction applied, per explicit owner instruction**:
- `05-06-wakun-materials.ja.md` line 110: "1980年" → "1979年"
- `05-06-wakun-materials.ja.md` line 115: "47-49頁" → "32-55頁"
- `05-06-wakun-materials.en.md`: the Kazama Rikizō entry's year updated to "(1979)"; the Yamamoto
  Shingo entry's page range updated to "32–55"

**Not changed in this pass**: `01-01-introduction.ja.md` line 267 still carries the same "1980年"
error as `05-06` originally did (not yet corrected, since it is a different page outside this
trial's stated scope — flagged here for a possible separate, explicit fix). The Kazama Rikizō
page range (8–35, per `01-01-introduction.en.md`) was not added to `05-06`, since the owner
confirmed only the year and `05-06-wakun-materials.ja.md` itself still states no page range for
this entry; adding unconfirmed page numbers would have repeated the exact fabrication risk noted
in Trial 003.

**Verification**: `hugo --quiet` rebuilt cleanly (exit 0) after both edits; `grep` confirmed both
`.ja.md` and `.en.md` now agree (1979; 32–55) and no stale "1980"/"47" values remain for these two
entries.

**Revised open item**: whether to also correct `01-01-introduction.ja.md` line 267 (same "1980年"
error, propagated independently into that page's source) is still open and requires separate,
explicit instruction before editing, since it falls outside `05-06`'s scope. **Resolved in §11.**

---

## 11. Follow-up: `01-01-introduction.ja.md` Correction and Full Cross-Check (2026-07-29, same day)

Per explicit owner instruction, `01-01-introduction.ja.md` line 267 was corrected to match
`05-06`: "1980年" → "**1979年**". `01-01-introduction.en.md` already read "(1979)" and required no
change — its year was correct all along; the `.ja.md` was the file in error.

Having found two independent citation errors that both trace back to the `.ja.md` layer, a
systematic cross-check was then run: every author appearing in both `05-06-wakun-materials.ja.md`
and `01-01-introduction.ja.md`'s bibliographies was diffed line-by-line (犬飼守薫 ×3, 高瀬正一, 山本秀人
×10, 河野敏宏, 石井行雄, 高橋宏幸 ×4, 加藤浩司, 萩原義雄, 小林恭治, 山本真吾, 風間力三). Result: aside from
the two already-corrected entries, every shared year and volume/issue number matched between the
two `.ja.md` files. The many entries where `01-01.ja.md` lacks page numbers that `05-06.ja.md`
states are **not** errors — `01-01-introduction.ja.md` line 238 carries an explicit editorial note,
"なお、最初と最後の頁の記載は省略した" (page numbers of the first and last pages have been omitted), meaning
that bibliography intentionally omits page ranges project-wide.

One further discrepancy surfaced during this sweep and was put to the project owner, who confirmed
it as a correction (not left open):

- **Takase Shōichi, "Wakun yori Mita 'Shinsen Jikyō' to 'Kanchi-in bon Ruiju Myōgishō' ni Tsuite"**:
  both `.ja.md` sources cited the journal issue as "44" only; `01-01-introduction.en.md` alone
  read "*Gobun Kenkyū*, nos. 44/45 (1978): 103–114." The project owner confirmed the paper was
  published in the **combined issue 44/45** of *Gobun Kenkyū*, i.e. `01-01-introduction.en.md` was
  correct and both `.ja.md` sources were incomplete.

**Correction applied, per explicit owner instruction**:
- `05-06-wakun-materials.ja.md` line 109: "『語文研究』44、" → "『語文研究』44・45、"
- `01-01-introduction.ja.md` line 266: "『語文研究』44、" → "『語文研究』44・45、"
- `05-06-wakun-materials.en.md`: Takase entry updated from "*Gobun Kenkyū* 44 (1978)" to
  "*Gobun Kenkyū*, nos. 44/45 (1978)", now matching `01-01-introduction.en.md`'s existing text
  exactly.

**Files changed in this follow-up**: the same four files as §10, plus this section.

**Verification**: `hugo --quiet` rebuilt cleanly (exit 0) after each edit; final `grep` across all
four files confirms full agreement on all three corrected facts (Kazama: 1979; Yamamoto Shingo:
32–55; Takase: 44/45).

**Net result of §9–§11**: three genuine data errors were found and corrected across the `.ja.md`
sources of two different KRM Documentation pages (05-06 and 01-01) — none were introduced by
translation; all were pre-existing errors in Japanese source material that this translation pass
happened to surface by cross-referencing overlapping bibliography entries between pages. No other
discrepancies remain among the citations shared between these two pages.
