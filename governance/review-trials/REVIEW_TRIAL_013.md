## Review Trial 013

Target: `08-case-studies/` (`_index.md`, `08-01-ugoku.md`, `08-02-miru.md`, `08-03-wakun-uf.md`, `08-04-kana-split.md`, `08-05-dhsjr.md`, `08-06-getting_started_ai_humanities.md` — 7 files, unsuffixed/language-neutral per `I18N_POLICY.md` §5 "Case studies: Japanese-only by policy"). First full review of this section.

Purpose: Thirteenth pilot of the KRM Documentation review workflow. This section is Case Studies — worked scholarly analyses with extensive character lists, frequency tables, and annotation-classification enumerations. Mechanical (Hugo/wording) findings were minor, but a deep read surfaced several internal-consistency problems in the scholarly content itself (counts that don't sum, a duplicated list entry, a mislabeled enumeration, and a likely copy-paste leftover in a worked example) — these are recorded as Unresolved per instruction, since correcting them requires the project owner's judgment about which value is authoritative, not a mechanical edit.

**Confirmation update (2026-07-28, next day)**: the project owner reviewed UR1 and UR2 and directed resolutions for both. UR1: during the exchange, the project owner initially misidentified the duplicated character as "擺"; I flagged that the two lists at `08-01-ugoku.md:64-71` actually share "躁" (擺 does not appear there at all — it is UR2's duplicate, at line 246), and the project owner confirmed the correction should target 躁. Resolution: 躁 belongs in the "included" (27字) list; removed from the "excluded" list, which becomes 7字 (27+7=34, now matching the document's own stated base count of 34 characters — corroborating that this was the correct fix). UR2: confirmed as originally found; removed the duplicate 擺 from the 30-character list, updating the count to 29字. Both applied and verified — see the updated entries and §Change and Validation below.

**Confirmation update (2026-07-28, same day)**: the project owner reviewed UR3 and UR4 and directed resolutions for both, confirming the counts found during review were the correct replacements. UR3: "単字訓として104例、熟字訓として1例、都合105例" corrected to "単字訓として103例、熟字訓として1例、都合104例"; the later reference to "日国表記欄の105例" corrected to "104例". UR4: "6字あった" corrected to "7字あった" (matching the 7 correction pairs actually listed). Both applied and verified — see the updated entries and §Change and Validation below.

**Confirmation update (2026-07-28, same day)**: the project owner reviewed UR5, UR6, and UR7 and directed resolutions for all three. UR5: confirmed a specific 16-item list to replace the mislabeled/duplicated 17-line enumeration — the confirmed list matches the systematic reconstruction proposed during review. UR6: confirmed the table total should be corrected to 25,196 (matching the sum of its own components) rather than left as the author's approximate figure. UR7: the project owner identified this as their own data-entry mistake and confirmed "僧" should read "測". All three applied and verified — see the updated entries and §Change and Validation below.

---

### Scope

7 files reviewed. Document layer: Case Studies (`DOCUMENTATION_BLUEPRINT.md` Layer, Japanese-only by policy). Protected content: extensive — character-list enumerations, worked manuscript examples, frequency-count tables, and annotation-classification schemes drawn from the KRM dataset. Review level: AI-assisted review (mechanical checks by direct grep/script, plus a full-text deep read via a read-only research pass) — this trial deliberately did not evaluate the linguistic/scholarly correctness of any analysis, only internal consistency (do stated counts match the lists actually given, are list items duplicated, etc.). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Double space after heading marker (3 instances)**
`08-02-miru.md:182`, `08-06-getting_started_ai_humanities.md:260,285`. Each heading had `##  ` or `###  ` (two spaces instead of one) before the heading text. Normalized to a single space.

**RR2 — Stray trailing whitespace (5 instances)**
`08-06-getting_started_ai_humanities.md:179` (inside a bash code fence), `08-04-kana-split.md:478,561` (also one mid-sentence double space at `:478`), `08-05-dhsjr.md:617,962` (identical list items, fixed with one `replace_all` edit). Ordinary trailing/extra whitespace with no content effect; removed.

**RR3 — Project-acronym typos, "HDIR" and "HDSJR"**
`08-05-dhsjr.md:434`: "これは、**HDIR**のKRMでも同様である。" — every other occurrence in this file (6 total) correctly reads "HDIC". `08-05-dhsjr.md:872`: "次に、**HDSJR**の関連部分を..." — every other occurrence in this file (52 total) correctly reads "DHSJR". Both are unambiguous letter-transposition typos in a project acronym, not a scholarly claim. Fixed to match the overwhelmingly established usage in the same file.

**RR4 — Duplicate list number**
`08-05-dhsjr.md:622-624`: a 7-item enumeration of 類音注 patterns had two items both labeled "7.":
```
6. 類音注 + 声点
7. 類音注 + 仮名注
7. 類音注 + 声点 + 仮名注
```
Renumbered the last item to "8." — the item text itself was already correct and distinct; only the number was wrong.

All four: `Allowed under existing standards; no additional approval required` — ordinary whitespace, unambiguous acronym typos corrected against dozens of correct occurrences in the same file, and a simple sequential-numbering slip with no ambiguity about the intended value.

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — Character appears in both the "included" and "excluded" lists for 日国表記欄 (08-01-ugoku.md:64-71)**
Text states 34 characters have 和訓「ウゴク」; of these, 27 are listed as recorded in 日国表記欄 (line 66) and 8 as not recorded (line 71) — 27+8=35, one more than the stated base of 34. The character **躁** appears in both the 27-character and the 8-character list. Resolving this needs the project owner to determine which list 躁 actually belongs in (or whether the base count of 34 is itself off).
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: 躁 belongs in the "included" (27字) list; its appearance in the "excluded" list was the error. Removed from `08-01-ugoku.md:71`; the "次の8字である" lead-in at line 69 updated to "次の7字である". Verified with a further Hugo build: the rebuilt "excluded" list now reads 債・搯・頷・振・掉・忧・戁 (7 characters), and 27 (included) + 7 (excluded) = 34, matching the document's own stated base count — corroborating the fix. Fixed and verified; closed.

**UR2 — Duplicated character in a 30-character enumeration (08-01-ugoku.md:246)**
The list of "次の30字" with 和訓「ウゴカス」 contains **擺** twice, giving only 29 unique characters against the stated count of 30.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: remove the duplicate 擺, update the count to 29字. Applied to `08-01-ugoku.md:244,246`. Verified with a further Hugo build: the rebuilt list now contains 29 unique characters and the lead-in reads "次の29字に和訓「ウゴカス」の収録が確認できる。". Fixed and verified; closed.

**UR3 — Count mismatch in 単字訓/熟字訓 total (08-02-miru.md:107)**
"和訓「ミル」は単字訓として104例、熟字訓として1例、都合105例が記載されている。" A count of every bracketed group in the preceding classification list (lines 88-105) gives 103 single-character entries + 1 compound entry (目覩) = 104 total, not the stated 104+1=105.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: the counted values (103 single-character + 1 compound = 104 total) are correct; the stated figures were the error. Applied to `08-02-miru.md:107`: "単字訓として104例、熟字訓として1例、都合105例" → "単字訓として103例、熟字訓として1例、都合104例". The downstream reference at `08-02-miru.md:133` ("日国表記欄の105例") also updated to "104例" for consistency. Verified with a further Hugo build: both corrected figures render as expected. Fixed and verified; closed.

**UR4 — "6字" stated but 7 correction pairs listed (08-02-miru.md:133-141)**
"日国表記欄の入力ミスと判断されるものが6字あった。" is followed by 7 correction pairs (呪→眖, 嘸→瞴, 𥊰→𥊲, 腸→䁑, 𥆑→䀽, 眐→⿱正目, 明→眀).
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: "6字" was the error; corrected to "7字" to match the 7 listed pairs. Applied to `08-02-miru.md:133`. Verified with a further Hugo build: "日国表記欄の入力ミスと判断されるものが7字あった。" renders correctly. Fixed and verified; closed.

**UR5 — Mislabeled/duplicated item in a combinatorial enumeration (08-05-dhsjr.md:643-661)**
Text states "反切上字の4種類と反切4種類を組み合わせたパターンは16種類となる。" but 17 items are listed. Item 16's text ("反切上字 + 声点 + 仮名注 + 反切下字 + 声点") is a verbatim duplicate of item 14, and the final item is mislabeled "15" (a repeated number) rather than "17". Comparing against the systematic pattern used by the surrounding items (5-8, 9-12), the item currently mislabeled "15" appears to hold the content that a correctly-numbered item 16 should have had, and the actual "16" line looks like the erroneous one — but confirming and correcting an enumerated technical scheme like this is a project-owner decision, not a mechanical edit.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: replace the 17-line enumeration with a confirmed, correctly-numbered 16-item list (items 1-15 unchanged; erroneous duplicate "16." removed; final item renumbered 16, content "反切上字 + 声点 + 仮名注 + 反切下字 + 声点 + 仮名注" unchanged) — matching the systematic reconstruction identified during review. Applied to `08-05-dhsjr.md:659-661`. Verified with a further Hugo build: the rebuilt list contains exactly 16 items, ending "16. 反切上字 + 声点 + 仮名注 + 反切下字 + 声点 + 仮名注" with no duplicate text or mislabeled numbers. Fixed and verified; closed.

**UR6 — Table total does not match its own component sum (08-05-dhsjr.md:690-696)**
音注種類 counts (仮名注 2,299 / 反切 10,016 / 類音 12,398 / その他 483) sum to 25,196, not the stated 合計 of 25,159 (off by 37). Note: the surrounding text already acknowledges the tally is approximate ("分類は不十分であり、正確な数値ではないが、大まかな傾向をみるために示してみる"), so this may be within the author's own accepted margin of imprecision rather than a data-entry error — recorded for the project owner to judge either way.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: correct 合計 to match the component sum. Applied to `08-05-dhsjr.md:695`: "25,159" → "25,196". Verified with a further Hugo build: the rebuilt table shows 合計 25,196, matching 2,299+10,016+12,398+483. Fixed and verified; closed.

**UR7 — Likely copy-paste leftover in a worked example table (08-05-dhsjr.md:1758-1759)**
The worked example is explicitly introduced as being about the character 測 ("「測」に「音測（S）「シキ（L_）」」の音注が見える"), but row 2 of the resulting example table gives 単字_見出し as **僧** rather than 測:
```
|1 |F17762_01 |F17762_01 |測 | 入 | 入 |          |        |      |音測 |
|2 |F17762_01b|F17762_01 |僧 | 入 | 入 |シキ（平＊）|      |       |     |
```
"僧" looks like a leftover from an unrelated 僧/曽 worked example earlier in the same file (around lines 1505-1523). This is a directly quoted example data value — protected content per `EDITORIAL_CONVENTIONS.md` §11 — left unchanged pending confirmation.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-28)**: the project owner identified this as their own data-entry mistake; "僧" should read "測". Applied to `08-05-dhsjr.md:1759`. Verified with a further Hugo build: row 2 of the rebuilt table now reads `<td>測</td>` in the 単字_見出し column. Fixed and verified; closed.

`08-03-wakun-uf.md` and `08-04-kana-split.md` (beyond the two whitespace items already fixed) and `_index.md` were reviewed and found clean of this class of issue; the word-frequency tables in `08-03-wakun-uf.md` were treated as dataset content and not individually re-tallied.

---

### Change and Validation

**Initial pass (RR1–RR4)**: Files changed: `08-02-miru.md` (1 edit: heading space), `08-04-kana-split.md` (2 edits: trailing/extra whitespace), `08-05-dhsjr.md` (5 edits: 2× trailing whitespace via one `replace_all`, HDIR→HDIC, HDSJR→DHSJR, duplicate list number), `08-06-getting_started_ai_humanities.md` (3 edits: 2× heading space, 1× trailing whitespace in a code fence).

Verified: `git status --short` showed only these four files modified before and after editing; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt pages confirm: zero remaining occurrences of "HDIR" or "HDSJR" on the `08-05-dhsjr` page; the `NotebookLMの得意なこと`/`NotebookLMの苦手なこと` heading anchors render cleanly with no double-space artifact.

**Confirmation pass (UR1, UR2)**: Files changed: `08-01-ugoku.md` (2 edits: removed 躁 from the excluded list and updated its count to 7字; removed the duplicate 擺 from the ウゴカス list and updated its count to 29字).

Verified: `git diff` confirmed the new changes were limited to the designated locations; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms: the excluded-character list reads 債・搯・頷・振・掉・忧・戁 (7 characters, 27+7=34 matching the document's stated base count) and the ウゴカス list contains 29 unique characters matching its updated "次の29字" lead-in.

**Confirmation pass (UR3, UR4)**: Files changed: `08-02-miru.md` (2 edits: corrected 単字訓/熟字訓/合計 counts at line 107 from 104/1/105 to 103/1/104; corrected "6字" to "7字" at line 133, and its "105例" to "104例").

Verified: `git diff` confirmed the new changes were limited to the designated locations; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms: "単字訓として103例、熟字訓として1例、都合104例" and "日国表記欄の104例を観智院本で確認してみると、日国表記欄の入力ミスと判断されるものが7字あった。" both render as corrected.

**Confirmation pass (UR5, UR6, UR7)**: Files changed: `08-05-dhsjr.md` (3 edits: replaced the mislabeled/duplicated 17-line combinatorial enumeration with a confirmed, correctly-numbered 16-item list; corrected the 音注種類 table's 合計 from 25,159 to 25,196; corrected "僧" to "測" in the worked example table's row 2).

Verified: `git diff` confirmed the new changes were limited to the designated locations; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt page confirms: the combinatorial list renders exactly 16 items ending "16. 反切上字 + 声点 + 仮名注 + 反切下字 + 声点 + 仮名注" with no duplicates; the 音注種類 table shows 合計 25,196; the worked example table's row 2 shows 測 in the 単字_見出し column. Scratch build directories removed after each verification.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1-RR4 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: UR1-UR7 all confirmed and resolved — none remain open. Files changed: `08-case-studies/08-01-ugoku.md`, `08-02-miru.md`, `08-04-kana-split.md`, `08-05-dhsjr.md`, `08-06-getting_started_ai_humanities.md`. Reviewer: Claude (this session). Review date: 2026-07-27 (initial pass), 2026-07-28 (confirmation passes).
