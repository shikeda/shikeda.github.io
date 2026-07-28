# Translation Review Trial 002

## 1. Summary

Translated `05-04-onchu-problems.ja.md` into `05-04-onchu-problems.en.md`, replacing the
untranslated-body state flagged in Review Trial 011, following
`project/workflows/translation-workflow.md` for the first time as a formal SOP (Translation
Review Trial 001 was a retroactive record of work done before the SOP existed). One issue
requiring a source-file change was found and resolved before translation began: the tone-mark
notation issue logged as `project/issues.md` item 6 was confirmed present in this file and fixed,
per explicit project-owner confirmation, in both language versions. Status: complete.

**Follow-up update (2026-07-28, same day)**: the two informational items noted in §5/§8 (the
missing い typo, and the underspecified 同音字注/仮名音注/声点 sections) were both resolved the
same day. The project owner fixed the typo directly in `05-04-onchu-problems.ja.md`. For the
underspecified sections, the project owner asked for a summary of the relevant explanations
already present in `content/docs/krm/08-case-studies/08-05-dhsjr.md` (§§"声点", "仮名注", "類音",
"類音注の整理"); a condensed Japanese summary with 2–3 examples each was produced, reviewed, and
then written into `05-04-onchu-problems.ja.md`'s "同音字注", "仮名音注", and "声点" sections
(replacing the single-line stubs), and translated into `05-04-onchu-problems.en.md`'s
corresponding sections to match. `project/issues.md` item 7 (which tracked these two items) has
been removed as resolved. See §9 for terminology/content details of this follow-up.

---

## 2. Scope

- **Source file**: `content/docs/krm/05-annotation-policy/05-04-onchu-problems.ja.md`
- **Target file**: `content/docs/krm/05-annotation-policy/05-04-onchu-problems.en.md`
- **Related files consulted for terminology precedent**:
  `content/docs/krm/02-data-overview/02-06-pronunciations.en.md`,
  `04-entry-input/04-03-handling.en.md`, `03-entry-data-model/03-01-data-structure.en.md`,
  `05-annotation-policy/05-01-basic-policy.en.md`, `05-annotation-policy/05-03-jitaichu-formats.en.md`
  (this session's own prior work), `01-introduction/01-01-introduction.en.md`,
  `content/docs/krm/_index.en.md`
- **Files changed**: `05-04-onchu-problems.en.md` (full translation);
  `05-04-onchu-problems.ja.md` (one tone-mark notation correction, applied under separate
  explicit instruction — see §2 note below)
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-28

**Note on the `.ja.md` change**: per `translation-workflow.md` §5, the Japanese source must not be
modified as part of ordinary translation work. Before translating, the source was checked against
the known tone-mark notation issue logged in `project/issues.md` item 6 (old convention `@`/`"` →
current convention `_`/`V`, found and fixed in `05-03-jitaichu-formats.{ja,en}.md`). One instance
was found, at line 99: `尼(L")尒反`. This was flagged to the project owner *before* proceeding
with translation (per `translation-workflow.md` §4's escalation rule), who confirmed it should be
corrected to `尼(LV)尒反`, matching the 05-03 precedent. Applied identically to both language
versions.

---

## 3. Terminology Decisions

| Japanese term | English rendering | Basis |
| --- | --- | --- |
| 音注 | **`Phonetic Gloss(es)`** | Existing precedent, used site-wide |
| 同音字注 | **`Homophone glosses`** (同音字注, *dōonji-chū*) | Existing precedent (`05-01-basic-policy.en.md:93`) |
| 類音注 | **`Similar sound notes`** (類音注, *ruion-chū*) | Existing precedent, used extensively (`02-06-pronunciations.en.md`, `04-03-handling.en.md`, `03-01-data-structure.en.md`); also matches the Japanese source's own inline English gloss ("Similar sound notes") |
| 仮名音注 | **`Kana glosses`** (仮名音注, *kana-onchū*) | Existing precedent (`05-01-basic-policy.en.md:166`, `04-03-handling.en.md:339`) |
| 声点 | **`Tone Marks`** | Existing precedent |
| 正音 | *Seion* (正音, standard pronunciations) | Existing precedent (`05-01-basic-policy.en.md:95`) |
| 反切 | **`Fanqie spellings`** | Existing precedent |
| 中古音 | Middle Chinese (phonological system) | Existing precedent (`05-01-basic-policy.en.md`) |
| 玄応の一切経音義 | Xuanying's *Yiqiejing yinyi* | Existing precedent (`01-01-introduction.en.md:136`) |
| 高麗本 | the Korean edition | Existing precedent (established in Translation Review Trial 001, for `龍龕手鏡` context) |
| 龍龕手鏡 | *Longkan Shoujian/Shoujing* | Existing precedent, extended in Translation Review Trial 001 |
| 正宗索引 | Masamune's Index | Existing precedent |
| 大正蔵 | the Taishō Tripiṭaka | Existing precedent (`05-01-basic-policy.en.md:107`) |
| 東宮切韻 | *Tōgū Qieyun* | New decision — no prior precedent found; a literal, low-risk romanization of a proper title (東宮 + established *Qieyun* romanization), not escalated |
| 金剛寺本／西方寺本／七寺本 | the Kongō-ji / Saihō-ji / Nanatsu-dera manuscripts | New decision — no prior precedent found; standard Hepburn romanization of well-known temple/manuscript names, matching the site's existing manuscript-naming pattern (e.g. "Kanchi-in manuscript"); not escalated |
| 大灌頂經 | the *Great Consecration Sūtra* | New decision — standard descriptive English rendering; not escalated |
| 七佛神呪經 | the *Sūtra of the Spells of the Seven Buddhas* | New decision — standard descriptive English rendering; not escalated |
| 佛説灌頂七萬二千神王護比丘呪經 (Taishō No. 1331) | the *Sūtra of the Seven Myriad Two Thousand Spirit-King Protector Bhikṣus Spoken by the Buddha at the Consecration* | New decision — full descriptive translation of a specific cited sutra title, kept alongside the Taishō number for verifiability; **lower confidence, flagged to project owner in the completion report** |
| 七佛八菩薩所説大陀羅尼神呪經 (Taishō No. 1332) | the *Great Dhāraṇī Spirit-Spell Sūtra Spoken by the Seven Buddhas and Eight Bodhisattvas* | Same as above — lower confidence, flagged |
| 梵語音訳 | Sanskrit phonetic transliteration | New decision — standard technical term; not escalated |
| 草川（草川昇）／草川和訓集成 | Kusakawa / Kusakawa's *Wakun Shūsei* | New decision — no genuine prior translated precedent existed (the term appears in `05-05-gichu-quantity.en.md` and `05-06-wakun-materials.en.md`, but both are still in their untranslated, Japanese-body state per the Translation Backlog, so those are not real precedent). Romanized following the established "surname-only, running-prose citation" pattern used for 正宗 → "Masamune"; not escalated |
| 参考文献 (bibliography, 20 entries) | Standard `Surname, Given name. "Romanized Title" (English gloss). *Journal*, vol/no. (year): pages.` format | Matched exactly to the established citation format in `01-01-introduction.en.md` (e.g. its entries 246, 249, 252, 255). All 20 entries in this section's References were translated in this format; **not individually spot-checked against each cited source, flagged as an area for optional project-owner review given the volume** |

---

## 4. Questions Raised and Owner Confirmations

**Q1 — Tone-mark notation at `.ja.md:99`.**
See §2 note above. **Resolution (project owner, 2026-07-28)**: correct `"` to `V` (i.e. `尼(L")尒反`
→ `尼(LV)尒反`), matching the 05-03 precedent. Applied to both language versions before the
translation's remaining content was finalized.

No other blocking questions were raised — all remaining terminology decisions (§3) were resolved
via existing site precedent or, where no precedent existed, via low-risk, non-scholarly
romanization/translation choices (proper nouns, standard technical vocabulary, citation
formatting) that did not require escalation under `translation-workflow.md` §4.

---

## 5. Translation-Specific Issues

- **Quoted manuscript/citation data kept in original script.** All `kazama_location`/`hanzi_entry`/
  `definition` data blocks, the two indented sutra-citation code blocks ("郁佡　丘豉反..." etc.),
  and the *Longkan Shoujian/Shoujing* citation were left untranslated, matching the established
  handling of primary-source quotations (see Translation Review Trial 001, §5). The explanatory
  `remarks` prose attached to each data entry *was* translated, consistent with how
  `05-02-headword-count.en.md` handles `remarks` (**`Compiler's Remark`**) fields.
- **Two structural gaps, initially preserved as-is, resolved same-day.** The source's "## 声点"
  (Tone Marks) section heading originally had no body content beneath it, and "## 片仮名と誤認され
  やす反切" appeared to be missing a character (誤認されやす**い** — "easily mistaken," missing the
  final い). At initial translation time, both were reproduced faithfully rather than corrected
  (the empty section was left empty; the heading's *meaning* was translated correctly despite the
  apparent typo, since it was unambiguous) — neither was part of this translation task's original
  scope. Both were resolved later the same day: the project owner fixed the typo directly, and
  asked for the "同音字注"/"仮名音注"/"声点" sections (also underspecified — one-line stubs) to be
  expanded using a summary of `08-05-dhsjr.md`. See §9 for details of that follow-up.
- **Structural parity maintained.** One-to-one heading structure preserved (H1, 2 intro
  paragraphs, then 6 H2 sections: Types of Phonetic Glosses, Fanqie Spellings, Homophone-Character
  Glosses, Kana Glosses, Tone Marks, Fanqie Spellings Easily Mistaken for Katakana, References).

---

## 6. Change and Validation

**Initial pass**: Files changed: `05-04-onchu-problems.en.md`, `05-04-onchu-problems.ja.md`
(tone-mark fix only).

Verified: `git status --short` before/after; `hugo --minify` build to a scratch destination after
the translation and tone-mark fix were both in place; rendered-output inspection. Build result:
157 JA / 51 EN pages, 0 errors. Protected-content check: quoted data entries, sutra citations, and
the *Longkan Shoujian/Shoujing* citation were reproduced verbatim; the tone-mark correction was an
explicit, owner-directed fix applied identically to both language versions, not a translation
choice.

**Follow-up pass (same day)**: Files changed: `05-04-onchu-problems.ja.md` (typo fixed directly by
the project owner; three sections — 同音字注, 仮名音注, 声点 — expanded from single-line stubs),
`05-04-onchu-problems.en.md` (the same three sections translated to match).

Verified: `git status --short` confirmed only these two files changed; `hugo --minify` build —
157 JA / 51 EN pages, 0 errors. Rendered-output inspection confirmed: the 声点 symbol table renders
correctly in both languages (including 声点無/"No tone mark" and 鼻音符号/"Nasal symbol" rows); the
quoted examples (焦(L)「セウ」遼(L)「レウ」二音, 俗云堕ウ, etc.) render identically, verbatim, in
both `.ja.md` and `.en.md`, consistent with this trial's established policy of keeping quoted
manuscript annotations untranslated (see §5).

---

## 7. Final Review Result

- **Overall status**: `Complete`
- **Open items remaining**: none blocking. The two informational items originally noted in §5
  (empty "Tone Marks" section; typo in a heading) were both resolved same-day — see the
  Follow-up update in §1 and §9.
- **Files changed**: `05-annotation-policy/05-04-onchu-problems.en.md`,
  `05-annotation-policy/05-04-onchu-problems.ja.md`
- **Translator**: Claude (this session)
- **Translation date**: 2026-07-28 (initial pass and same-day follow-up)

---

## 8. Remaining Follow-up Actions

- Two lower-confidence terminology decisions (the two specific Taishō-numbered sutra titles, §3)
  are flagged for optional project-owner spot-check; not blocking.
- The 20-entry References section was translated in bulk following established citation format
  but not individually verified against each source; flagged as optional for spot-check given the
  volume.
- `project/translation-backlog.md` remains intentionally not updated (per standing instruction,
  to be updated only once all of `05-annotation-policy/`'s pending translations are complete).
- Next file in the translation queue: `05-05-gichu-quantity.ja.md` → `.en.md` (already reflected in
  `project/workflows/translation-workflow.md` §2).

---

## 9. Follow-up: Content Added to 同音字注/仮名音注/声点 (2026-07-28, same day)

**Source of the added content**: `content/docs/krm/08-case-studies/08-05-dhsjr.md` (a Japanese-only
case-study page, not itself part of the translation queue), specifically its "### 声点" (405–441),
"### 仮名注" (443–459), "### 類音" (477–491), and "### 類音注の整理" (701–753) sections. The
project owner asked for a condensed Japanese summary (~10 lines of explanation, 2–3 examples per
term) of the 類音注/同音字注, 仮名注/仮名音注, and 声点 material in that file; the summary was
produced, reviewed, and then adapted into `05-04-onchu-problems.ja.md`'s corresponding sections
(replacing the pre-existing single-line stubs), and translated into English for `.en.md`.

**Terminology additions** (all consistent with §3's established terms; no new English glossary
terms were introduced by this follow-up):

| Japanese term/concept | English rendering |
| --- | --- |
| 音◯／◯音 (homophone-gloss notation pattern) | '音◯' / '◯音' — kept as literal notation, not translated |
| 二音 (two-reading marker for compounds) | '二音' ("two readings") — literal form kept, gloss added |
| 拗音 | palatalized (*yōon*) sound |
| 濁音 | voiced (*dakuon*) sound |
| 四声／六声 | the four tones / six tones |
| 平・平軽・上・去・入・入軽 (six-tone symbol table) | Level / Light Level / Rising / Departing / Entering / Light Entering — matching the established four-tone names (Level, Rising, Departing, Entering) already used elsewhere in this file and site-wide, extended with "Light" for the two additional light-register tones specific to this six-tone system |
| 声点無 | "No tone mark" |
| 鼻音符号 | "Nasal symbol" |

**Examples reproduced** (kept in original script in both language versions, per this trial's
established primary-source-quotation policy):
- 留「音流」; 鷦鷯「焦(L)「セウ」遼(L)「レウ」二音」; 音鴛之上声 (homophone-gloss/類音注 examples)
- 正「和者ウ」; 堂「俗云堕ウ」(kana-gloss/仮名音注 examples of palatalized/voiced sounds written with Chinese characters)
- The 9-row 声点 symbol table (平/平軽/上/去/入/入軽/濁/声点無/鼻音符号 → L/F/H/R/T/S/V/_/N)

**Scope note**: this follow-up only summarizes and adapts pre-existing explanatory material from
`08-05-dhsjr.md`; it does not alter `08-05-dhsjr.md` itself, and it does not introduce any new
scholarly claims beyond what that page already states.
