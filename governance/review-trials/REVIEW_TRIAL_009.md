## Review Trial 009

Target: `03-entry-data-model/` (`_index.{ja,en}.md`, `03-01-data-structure` through `03-04-data-example`, `.ja.md`/`.en.md` — 5 file pairs, 10 files). `03-01-data-structure.*.md` was previously reviewed in Trials 002/004; re-checked here as part of the full-directory scope and found clean (no new issues).

Purpose: Ninth pilot of the KRM Documentation review workflow. This section is Core Documentation (Conceptual Reference layer). Findings were link/wording/title-alignment level, so this record is kept proportionate rather than exhaustively long, per instruction.

**Confirmation update (2026-07-27, same day)**: the project owner confirmed the "predecessor" claim in UR1 as accurate and directed the opposite resolution from the usual default — rather than removing the English-only addition, reverse-import it into the Japanese version so both language versions carry the same level of detail. The project owner also supplied the correct Japanese proper noun ("石塚漢字字体資料") after a clarifying question, since the reviewer's own back-translation was only a provisional guess. Applied and verified — see the updated UR1 entry and §Change and Validation below.

---

### Scope

10 files reviewed. Document layer: Conceptual Reference (`DOCUMENTATION_BLUEPRINT.md` Layer 2). Document type: mostly Concept Reference, with `03-04-data-example.*.md` functioning as a worked Data Reference/Workflow example. Protected content: present (terminology definitions, the '功'/'加復'/'助' worked transcription examples, the Ishizuka *shotai/jitai/jikei* citation, publication-date list); not altered except the item recorded as Unresolved below (not fixed). Review level: AI-assisted review, Full Documentation Review Checklist (Core Documentation). Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Romanization typo, `03-03-concepts-char.en.md:44`**
- `**Character Standards` (*iitai*)** → `(*jitai*)`. The correct romanization *jitai* is used consistently everywhere else in the same file (front matter, headings, and 3+ other prose occurrences); "*iitai*" appeared exactly once. Ordinary typo in prose, not a scholarly-term variant.

**RR2 — Duplicated article, `03-04-data-example.en.md:147`**
- "...clearly preserves **the an** audit trail of changes" → "...clearly preserves **an** audit trail of changes". Ordinary grammatical typo.

**RR3 — Front-matter title not matching the page's own H1, `03-04-data-example.en.md`**
- title was `"Examples of Entry Data Files"`; H1 reads `# Publication and Updates of Entry Data Files`, matching the Japanese counterpart's title/H1 (`項目データファイルの公開・更新`) and the KRM top-level English navigation (`content/docs/krm/_index.en.md`, already using "Publication and Updates of Entry Data Files"). Same pattern as Trial 005's RR1. Fixed the title to match.

**RR4 — Section-index link label not matching the target page's current title, `_index.ja.md:24`**
- `[項目データファイルの例]` → `[項目データファイルの公開・更新]`, matching `03-04-data-example.ja.md`'s own title/H1 and the equivalent English section index (`_index.en.md:24`, already reading "Publication and Updates of Entry Data Files"). The link target itself was already correct; only the label text was stale.

All four: `Allowed under existing standards; no additional approval required` — ordinary typos and title/label alignment where the correct form is already established elsewhere in the same document set.

No data-file-name hyphen/underscore inconsistencies, stale `/docs/notes/...` paths, `localhost` references, or broken internal links were found in this section.

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — English-only added claim about an unnamed "predecessor" database, `03-03-concepts-char.en.md:45`**
- Evidence: "...The **Hanzi Normative Glyphs Database (HNG)** was intended to empirically demonstrate this model. Related data, **including materials from its predecessor (the Ishizuka Register of Chinese Character Standards of Writing)**, can be accessed via the **Hanzi Normative Glyphs Dataset**..." The bolded clause has no counterpart in the Japanese original (`03-03-concepts-char.ja.md:48-49`: "**漢字字体規範データベース（HNG）**はそのモデルの実証を意図するものである。HNGは[漢字字体規範史データセット](https://www.hng-data.org)で利用できる。" — no mention of a "predecessor" or any "Ishizuka Register").
- Classification: I18N substantive addition — `EDITORIAL_CONVENTIONS.md` §5 treats introducing a new named source/claim as evidence-and-example handling requiring confirmation, and `I18N_POLICY.md` §10 requires classifying English-only additions before resolving them (this reads as more than ordinary "supplementary difference," since it names a specific prior database not otherwise documented on this site).
- Proposed action: confirm whether "the Ishizuka Register of Chinese Character Standards of Writing" is an accurate, citable predecessor to HNG, and if so, whether it should also appear in the Japanese version; if not accurate, it should be removed.
- Authority status: `Requires Confirmation`.
- Human confirmation required: Yes.
- Resolution / Disposition: **Confirmation obtained (project owner, 2026-07-27)**: the claim is accurate. Directed resolution: reverse-import the English-only addition into the Japanese version (rather than removing it from English) so both language versions describe the predecessor data at the same level of detail. A draft Japanese sentence was proposed; the reviewer's placeholder term for the predecessor's name was explicitly flagged as an uncertain back-translation, and the project owner supplied the correct term, "石塚漢字字体資料." Applied to `03-03-concepts-char.ja.md`: "HNGは[漢字字体規範史データセット]...で利用できる。" → "HNGには、その前身にあたる石塚漢字字体資料のデータも含まれており、[漢字字体規範史データセット]...で利用できる。" Verified with a further Hugo build: "石塚漢字字体資料" renders correctly, and the existing `https://www.hng-data.org` link target is unchanged. Fixed and verified; closed.

---

### Change and Validation

**Initial pass (RR1–RR4)**: Files changed: `03-03-concepts-char.en.md` (1 line), `03-04-data-example.en.md` (2 lines: title + prose), `_index.ja.md` (1 line). `03-03-concepts-char.en.md`'s UR1 location was read and evaluated but not edited at this stage.

Verified: `git status --short` clean before editing; `git diff` confirmed changes limited to the designated lines across the 3 files; `hugo --minify` build — 157 JA pages / 51 EN pages, 0 errors. Rebuilt pages confirm: zero remaining occurrences of "iitai" or "the an audit"; the `03-04-data-example` English page's `<title>` now reads "Publication and Updates of Entry Data Files | HDIC project"; the Japanese section index's link to `03-04-data-example/` now displays "項目データファイルの公開・更新".

**Confirmation pass (UR1)**: Files changed: `03-03-concepts-char.ja.md` (1 line — the English counterpart was not modified further, since the resolution was to add the missing detail to Japanese rather than remove it from English).

Verified: `git diff` confirmed the change was limited to the designated sentence; `hugo --minify` build — 157 JA pages / 51 EN pages, 0 errors. Rebuilt Japanese page confirms "石塚漢字字体資料" renders correctly and the `https://www.hng-data.org` link target is unchanged.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR4 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: none remaining — UR1 confirmed accurate and resolved by reverse-importing the detail into the Japanese version; see Findings above. Files changed: `03-entry-data-model/03-03-concepts-char.en.md`, `03-03-concepts-char.ja.md`, `03-04-data-example.en.md`, `_index.ja.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
