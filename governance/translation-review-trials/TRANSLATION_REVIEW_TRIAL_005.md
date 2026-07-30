# Translation Review Trial 005

## 1. Summary

Translated `05-07-annotation-examples.ja.md` into `05-07-annotation-examples.en.md`, following
`project/workflows/translation-workflow.md`. The prior `.en.md` was a stub: only the frontmatter
title and H1 had been translated, followed by a placeholder "Under preparation." line and then a
raw, untranslated copy of the entire Japanese source. This trial produced a full translation from
the current `.ja.md` — the densest page in `05-annotation-policy/` so far, consisting of a
foreword, a worked bibliographic/access note for five manuscript witnesses, a conventions section,
and 24 headword entries (K-number / GlyphWiki-keyed) carrying roughly 90 individually numbered
philological notes (fanqie readings, tone marks, manuscript collation, dictionary citations).
Status: **complete**. No passage required scholarly interpretation beyond ordinary terminology
choices already covered by precedent from Trials 001–004 and the untranslated `05-01`–`05-06`
sibling pages; several low-risk, first-time terminology decisions were made and are listed in §3
for future-trial precedent, and a small number of observations are flagged in §4/§5 for
project-owner awareness rather than resolved unilaterally.

---

## 2. Scope

- **Source file**: `content/docs/krm/05-annotation-policy/05-07-annotation-examples.ja.md`
- **Target file**: `content/docs/krm/05-annotation-policy/05-07-annotation-examples.en.md`
- **Related files consulted for terminology precedent**:
  `content/docs/krm/05-annotation-policy/05-01-basic-policy.en.md` (tone/rhyme/initial
  romanization pattern — "Departing tone, *Zhen* rhyme (震韻)" — and the *Guangyun*/*Tenrei Banshō
  Meigi*/*Yupian*/*Longkan Shoujian* bibliography-abbreviation conventions),
  `05-04-onchu-problems.en.md` and `05-05-gichu-quantity.en.md` (same romanization pattern applied
  at higher density; short in-line English glosses for quoted one- to four-character definitions;
  short-form "*Banshō Meigi*" vs. full "*Tenrei Banshō Meigi*"),
  `05-06-wakun-materials.en.md` and its Trial 004 record (manuscript-name romanizations —
  Kanchi-in, Kōzan-ji, Renjō-in, Sainenji — reference-work short names — Masamune's Index,
  Kusakawa's Wakun Collection, Nakamura's Monzen, *Kunten Goi Shūsei*, *Nikkoku* — the full
  Kobayashi Kyōji "Kanchi-in-bon/Sainenji-bon ni (Nai) Kanji/Katakana Chūki" citation series, the
  Nishihata *Gosha Shorei* citation, and "Ikeda's note:" for 池田按),
  `01-01-introduction.en.md` (manuscript facsimile-edition citations — *Shin Tenri Toshokan Zenpon
  Sōsho*, Yagi Shoten, Kichō Tosho Fukuseikai, the Renjō-in manuscript's *Sanpō Ruiju Myōgishō*
  facsimile and its 1986 Benseisha reprint, "Archives and Mausolea Department of the Imperial
  Household Agency" for 宮内庁書陵部, "National Institute of Japanese Literature" for
  国文学研究資料館, "Okada, Mareo" as the established romanization of 岡田希雄, the *Ganlù Zìshū*
  romanization used for 干禄字書 in a Tamura Natsuki paper title),
  `04-entry-input/04-03-handling.en.md` (`fanqie`/`Kana gloss`/`Go-on`/`Wa-on` field-notation
  conventions, "Kōzan-ji ms." precedent, "存疑" as "(uncertain, 存疑)"),
  `05-02-headword-count.en.md` (Dōen-bon manuscript of the *Wamyō Ruijushō*, further "Ikeda's
  note:" precedent),
  `05-03-jitaichu-formats.en.md` (**`Form Classification Tag`** terminology, e.g. "二正"/"二俗"
  kept untranslated as literal tags), `AGENTS.md` and `GLOSSARY_CONVENTIONS.md` (preservation of
  primary-source quotations, identifiers, and bibliographic data; terminology-decision authority
  levels).
- **Files changed**:
  - `content/docs/krm/05-annotation-policy/05-07-annotation-examples.en.md` (full translation, net
    new in substance — the previous content was an untranslated raw copy, not a translation)
  - `project/translation-backlog.md` (checked off the `05-07` line)
  - `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_005.md` (this file)
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-30

No change was made to `05-07-annotation-examples.ja.md`.

---

## 3. Terminology Decisions

| Japanese term | English rendering | Basis |
| --- | --- | --- |
| 観智院本／高山寺本／蓮成院本／西念寺本 | Kanchi-in manuscript / Kōzan-ji manuscript / Renjō-in manuscript / Sainenji manuscript | Existing precedent (`02-data-overview`, `05-01`, `05-03`, `01-01-introduction`) |
| 万象名義 | *Tenrei Banshō Meigi* | Existing precedent (`05-01`, `05-04`); used the fuller form throughout rather than `05-05`'s shorter "*Banshō Meigi*", since `05-07` is denser and the fuller form is unambiguous on first and repeated mention alike |
| 広韻／宋本玉篇／龍龕手鏡／説文（解字） | *Guangyun* / Song edition of the *Yupian* / *Longkan Shoujian/Shoujing* / *Shuowen Jiezi* | Existing precedent (`05-01`, `05-04`, `05-05`) |
| 声点・平声／上声／去声／入声 | **`Tone Mark`**; Level / Rising / Departing / Entering tone | Existing precedent (`05-01`, `05-04`) |
| 韻 (rhyme names, e.g. 願韻／術韻／線韻／仙韻／支韻／紙韻／陽韻／漾韻／養韻／怗韻／送韻／感韻／尾韻／緩韻／阮韻) | Pinyin romanization + kanji in parentheses, e.g. "Yuan rhyme (願韻)" | Existing pattern (`05-01`: "*Zhen* rhyme (震韻)"), extended here to roughly 15 distinct rhyme names occurring at much higher density than in any prior trial; kanji retained alongside every romanization specifically so a phonologically-ambiguous romanization (e.g. 陽/漾/養 all romanize to "Yang") remains disambiguated by the untouched primary kanji — flagged for owner spot-check in §4 |
| 見母／喩四母／從母／邪母／疑母／日母 (initial-consonant class names) | "Jian initial", "*Yu* IV initial", "Cong initial", "Xie initial", "Yi initial", "Ri initial" | Existing pattern (`05-05`: "*Chan* III initial", "*Yu* IV initial"), extended to the additional initials appearing in `05-07` |
| 池田按 | "Ikeda's note:" | Existing precedent (`04-03-handling.en.md`, `05-02-headword-count.en.md`) |
| 岡田希雄『類聚名義抄の研究』 | Okada Mareo, *Ruiju Myōgishō no Kenkyū* | Existing precedent (`01-01-introduction.en.md` bibliography, `05-06.en.md` "Okada's Study") |
| 草川昇「類聚名義抄和訓小考」 | Kusakawa, Noboru, "Ruiju Myōgishō Wakun Shōkō" | Existing precedent (`04-03-handling.en.md`) |
| 小林恭治「観智院本にない漢字注記(N)」／「観智院本にないカタカナ注記(N)」 | Kobayashi Kyōji, "Kanchi-in-bon ni Nai Kanji/Katakana Chūki (N)" | Existing precedent (`05-06.en.md` bibliography, Trial 004) — exact numbered-series titles matched |
| 西端誤写諸例 | Nishihata, *Gosha Shorei* (Examples of Scribal Errors) | Existing precedent (`04-03-handling.en.md`) |
| 道円本和名抄 | the Dōen-bon manuscript of the *Wamyō Ruijushō* | Existing precedent (`05-02-headword-count.en.md`) |
| 宮内庁書陵部 | Archives and Mausolea Department of the Imperial Household Agency | Existing precedent (`01-01-introduction.en.md`) |
| 国文学研究資料館 | National Institute of Japanese Literature | Existing precedent (`01-01-introduction.en.md`) |
| 天理図書館 | Tenri Central Library | Existing precedent (`02-data-overview/_index.en.md`) |
| 八木書店 | Yagi Shoten | Existing precedent (`01-01-introduction.en.md`, `05-06.en.md`); used consistently over the alternate `02-data-overview` gloss "Yagi Bookstore," since `01-01`/`05-06` are the closer terminological neighbors for this citation style |
| 貴重図書複製会 | Kichō Tosho Fukuseikai | Existing precedent (`01-01-introduction.en.md`) |
| 鎮国守国神社蔵本三宝類聚名義抄 | *Sanpō Ruiju Myōgishō*, Held by Chinkoku Shukoku Shrine (Benseisha, 1986) | Existing precedent (`01-01-introduction.en.md` §"Renjō-in Manuscript") — matched title and publisher exactly |
| 三宝類字集　高山寺本（新天理図書館善本叢書第8巻） | *Sanbō Ruiji-shū Kōzan-ji-bon* (*Shin Tenri Toshokan Zenpon Sōsho*, vol. 8) | Existing precedent (`05-06.en.md` bibliography, Yamamoto Hideto citation) — matched exactly |
| 干禄字書 | *Ganlu Zishu* | New decision, low-risk — pinyin form attested only inside a Japanese paper title in `01-01-introduction.en.md` ("*Kanroku Jisho* to..."); here the primary text itself is cited directly, so pinyin (matching the *Guangyun*/*Shuowen Jiezi*/*Yupian* undiacritic-pinyin convention) was used rather than the Japanese-reading form |
| 白川字通 | Shirakawa's *Jitsū* | New decision, low-risk — no prior precedent found project-wide; follows the established "Author's ShortTitle" pattern (Masamune's Index, Nakamura's Monzen) |
| クラウン日中辞典 | *Crown Japanese-Chinese Dictionary* | New decision, low-risk — no prior precedent; literal translation of the dictionary's own name |
| 庵点（〽） | *iori-ten* mark (〽) | New decision, low-risk — no prior precedent; romanized rather than translated since no single-word English equivalent exists, matching how other manuscript-notation marks (声点, *shōten*) are handled |
| 缺筆／諱 (Zhao Kuangyin naming taboo) | "an omitted stroke, in observance of the naming taboo (避諱)... (缺筆)" | New decision, low-risk — no prior precedent for 避諱/缺筆 project-wide |
| 折葉の丁付け (folio references, e.g. 9オ／21オ／25オ／17ウ／天理版34ウ) | "fol. 9r" / "fol. 21r" / "fol. 25r" / "fol. 17v" / "folio 34 verso" | New decision, low-risk — extends the one existing precedent (`05-02-headword-count.en.md`: "p. 48 verso") to the recto/verso convention throughout `05-07` |
| 中村文選 citation work-abbreviations (西京／東都／蜀／魯／閑／甘／羽／上／序／表) | Left untranslated (kept as bare parenthetical tags, e.g. "(西京)") | New decision — these are terse single/double-character pointers to which *fu* or piece within the *Wen Xuan* a quotation is drawn from (e.g. 西京 = *Xijing fu*, 東都 = *Dongdu fu*); expanding them correctly would require independently re-identifying each cited Wen Xuan piece, which risks a bibliographic misattribution the project owner has not authorized — flagged in §4 for the owner's option to supply full expansions as project-standard precedent |

---

## 4. Questions Raised and Owner Confirmations

No passage required scholarly interpretation or was ambiguous enough to block translation
outright. The following items are flagged for optional project-owner review rather than resolved
unilaterally, per the instruction not to alter citations/identifiers/interpretation without
explicit direction:

- **Rhyme-name pinyin romanization density**: `05-07` cites roughly 15 distinct *Guangyun*/*Jiyun*
  rhyme names at far higher density than any previously translated page (`05-01`/`05-04` each
  romanized only a handful, each individually checked in depth). This trial romanized all of them
  following the same convention, always pairing the romanization with the untouched original
  kanji specifically so any small romanization imprecision remains recoverable and does not affect
  the underlying (unaltered) primary data. A specialist spot-check of these ~15 rhyme-name
  romanizations would be worthwhile before treating them as settled precedent for the still-pending
  `05-03`/`05-04`/`05-05` full translations (05-04/05-05 already have their own committed English
  text, so this affects future work only, not those pages).
- **Nakamura's Monzen work-abbreviations left untranslated**: see the last row of §3's table. The
  Japanese source's terse parenthetical tags after each Nakamura's Monzen page citation (西京, 東都,
  蜀, 魯, 閑, 甘, 羽, 上, 序, 表) were not expanded into full *Wen Xuan* piece titles, to avoid an
  unauthorized bibliographic identification. If the project owner can confirm the intended
  expansions, they can be added in a follow-up pass and adopted as precedent for `05-06.en.md`,
  which does not currently cite Nakamura's Monzen with this level of internal detail.
- **Citation-title variant**: `05-07` cites "小林恭治「西念寺本に見えない漢字注記」" (with 見えない,
  "not visible") twice (K0106251 note 3, K0106254 note 1), which differs slightly from the exact
  title "西念寺本にない漢字注記" ("Sainenji-bon ni Nai Kanji Chūki") recorded in `05-06.en.md`'s
  formal bibliography (established in Trial 004). Since `05-07` gives no full bibliographic
  citation for this paper (only the short in-line form), the phrase was translated literally as
  written — "Sainenji-bon ni Mienai Kanji Chūki" — rather than silently normalized to match
  `05-06`'s bibliography entry. This may be the same paper cited with a slightly different
  in-line shorthand, or a distinct paper; not resolved here.
- **Empty quotation in source**: `05-07-annotation-examples.ja.md` line 344 (K0106253, note 2)
  reads "蓮成院本「」を掲出字と同じ大きさに書写。" — the quotation marks are empty in the source
  itself (likely an unrendered or dropped character in the original). This was preserved exactly
  as empty quotation marks in the translation rather than guessed at.
- **Data-parity anomaly, not corrected**: K0106231's note ("観智院本・高山寺本同、西念寺本
  「⿺辶屲」") cites the Sainenji-manuscript variant as the identical string to the entry's own
  **`Headword`** ("⿺辶屲"), which reads oddly (comparison against itself). This was translated
  literally, preserving the source's own wording rather than silently correcting or omitting it.

---

## 5. Translation-Specific Issues

- **Density of primary-source data vs. prose**: `05-07` is structured as ~90 short numbered notes,
  each pairing a literal quoted fragment (a reading, a fanqie spelling, a dictionary citation, a
  manuscript variant) with a short explanatory sentence. Per §3's "Primary Sources" and
  "Non-Translate Targets" guidelines, every quoted Japanese/Chinese primary-source fragment,
  phonetic/tonal notation (e.g. "居彦(RV)反", "(LH)", "(__LV)"), K-number identifier, `Ta`-prefixed
  identifier, GlyphWiki image reference, and **`Form Classification Tag`** (e.g. "二同", "俗", "正",
  "或") was left completely untranslated; only the connecting Japanese analytical prose around
  these fragments was translated into English.
- **Short semantic glosses added**: where a note quotes a short (one- to four-character) dictionary
  definition (e.g. 説文「受物之器」), a brief English gloss was added in parentheses immediately
  after, following the established pattern from `05-05-gichu-quantity.en.md` (e.g. "'進也' (to
  advance)"). This is an "Audience Adjustment" under the workflow's guidelines, not a change to the
  underlying quotation.
- **Manuscript-name abbreviations expanded**: the source repeatedly uses single-character
  shorthand for manuscript names in dense comparison sentences — 西本／西 for 西念寺本, 高本 for
  高山寺本, 観本 for 観智院本 (e.g. K0106283 note 6: "西本には高本や観本に見えない..."). These were
  expanded to the full established English manuscript names ("the Sainenji manuscript," "the
  Kōzan-ji manuscript," "the Kanchi-in manuscript") throughout, for clarity, without adding or
  omitting any comparison the source did not make.
- **Structural parity**: full one-to-one structural parity with the `.ja.md` was maintained — same
  heading structure (Foreword → A Trial Draft of the Annotations → Texts Used → Conventions →
  *Butsujō* → per-radical subsections → per-**`Entry`** subsections with (Main Text)/(Notes)
  blocks), same 24 **`Entries`**, same ~90 numbered notes in the same order, same set of GlyphWiki
  image references (verified identical between `.ja.md` and `.en.md` via automated diff — see §6).
  Radical-grouping subheadings "### 3辵" and "### 4匚" were left untranslated, treated as
  structural/identifier labels from the manuscript's own radical organization rather than
  ordinary prose, since their precise scholarly meaning (stroke count within radical? sequence
  index?) was not obvious enough to translate with confidence without guessing.
- **Frontmatter title left unchanged**: `05-07-annotation-examples.en.md`'s existing frontmatter
  `title` ("Concrete Examples of Annotation Description") was already set (presumably at the time
  the stub was created) and was left as-is, even though `05-annotation-policy/_index.en.md`'s
  table-of-contents link text uses slightly different phrasing ("Specific Examples of Annotation
  Practice") for the same page. Not reconciled here, since changing an established page title falls
  outside ordinary translation work; flagged for the project owner's awareness only.

---

## 6. Change and Validation

- **Files changed**:
  - `content/docs/krm/05-annotation-policy/05-07-annotation-examples.en.md`
  - `project/translation-backlog.md` (checkbox only)
  - `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_005.md` (this file)
- **Verification method**: `git status`/`git diff` review before and after; full `hugo --quiet`
  production build with zero errors; automated diff confirming the `.en.md` and `.ja.md` contain an
  identical set of GlyphWiki image URLs (24 for 24) and an identical count of `#### K`-prefixed
  **`Entry`** headings (24 for 24); rendered-HTML spot check of the multi-line tab-indented note
  paragraphs (K0106221, K0106243) to confirm they render as ordinary paragraphs with line breaks,
  matching how the untranslated `.ja.md` itself already renders (not as a stray code block).
- **Build result**: `hugo --quiet` exit code 0, no warnings.
- **Protected-content check**: all quoted primary-source fragments, fanqie spellings, tone-mark
  notations, K-number/`Ta`-number identifiers, GlyphWiki references, and **`Form Classification
  Tags`** were reproduced character-for-character from the `.ja.md` source; none were altered,
  paraphrased, or omitted. No scholarly interpretation, argument, or conclusion was added, removed,
  or softened beyond the short in-parentheses English glosses described in §5.

---

## 7. Final Review Result

- **Overall status**: Complete.
- **Open items remaining**: see §4 (rhyme-romanization spot-check, Nakamura's Monzen
  work-abbreviation expansions, the two citation/data-parity observations) — none block the
  translation from standing as complete; all are optional refinements pending project-owner input.
- **Files changed**: see §6
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-30

---

## 8. Remaining Follow-up Actions

- Per `project/translation-backlog.md`, the remaining pending Core Documentation translation
  targets are `05-03-jitaichu-formats`, `05-04-onchu-problems`, and `05-05-gichu-quantity` (05-01,
  05-02, 05-06, and now 05-07 are complete).
- `project/workflows/translation-workflow.md` §2 ("Current Translation Target") should be updated
  to point at whichever of `05-03`, `05-04`, or `05-05` the project owner wants translated next.
- If the project owner confirms the Nakamura's Monzen work-abbreviation expansions (§4), consider
  applying them both here and, if applicable, enriching `05-06.en.md`'s Nakamura's Monzen citation.
- If a specialist review of the ~15 rhyme-name pinyin romanizations (§4) surfaces corrections,
  apply them here and treat the corrected forms as settled precedent for `05-03`/`05-04`/`05-05`.
