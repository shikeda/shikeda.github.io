## Review Trial 012

Target: `06-typesetting/` (`_index.{ja,en}.md`, `06-01-hanazono-mincho.{ja,en}.md`, `06-02-glyphwiki.{ja,en}.md`, `06-03-sfkanbun-sty.{ja,en}.md`, `06-04-vscode-texlive.{ja,en}.md`, `06-05-online-tools.{ja,en}.md` — 6 file pairs, 12 files). First full review of this section.

Purpose: Twelfth pilot of the KRM Documentation review workflow. This section is Workflow and Tool Notes (`I18N_POLICY.md` §5: "language-specific or bilingual recommended... depends on audience and stability"), a lighter-weight documentation type than Core Documentation. Findings were mechanical (heading structure, a stray character, a broken list marker) plus one language-coverage item the project owner had already flagged before this review began.

---

### Scope

12 files reviewed. Document layer: Workflow and Tool Notes. Document type: procedural/how-to reference (LuaTeX/LaTeX typesetting setup). Protected content: minimal — mostly TeX/LaTeX example code and external tool links, not scholarly transcription or dataset content. Review level: AI-assisted review, Full Documentation Review Checklist. Reviewer: Claude (this session). Review date: 2026-07-27.

---

### Findings and Fixes

#### Required Revisions (Allowed, fixed and verified)

**RR1 — Trailing space in a section heading**
`06-04-vscode-texlive.ja.md:461`: `### sfkanbunパッケージ (漢文) sfkanbun.sty ` had a trailing space. Removed.

**RR2 — En dash used as a Markdown list marker, breaking the list**
`06-04-vscode-texlive.ja.md:172`: one bullet in a reference list used `–` (en dash, U+2013) instead of `-`, unlike every other item in the same list. Since `–` is not a valid Markdown bullet marker, this line rendered as a plain paragraph, breaking out of the surrounding `<ul>` (confirmed by build: the fixed list now renders 23 `<li>` items instead of splitting at this line). Changed `–` to `-`.

**RR3 — Missing/mismatched H1 in `06-05-online-tools.{ja,en}.md`**
Both files jumped from front matter directly to a lower-level heading instead of an H1 matching the page title, unlike every other page in this section (which all have H1 == title, confirmed by directory-wide check). `06-05-online-tools.ja.md` had no H1 at all, starting straight at `## よく使うオンラインツールのリンク`. `06-05-online-tools.en.md` had only `# Links to frequently used online tools` as its sole heading — used as an H1 but not matching the front matter title `"Online Tools"`. Added `# オンラインツール` / `# Online Tools` as the H1 in each file, demoting the existing heading to H2 beneath it (matching the established `H1 = title, H2 = content sections` pattern used throughout this directory). `EDITORIAL_CONVENTIONS.md` Authority Matrix explicitly lists "Align title and H1 when meaning is unchanged" and "fix hierarchy" under `Headings`/`Page title and H1` as `Allowed`.

All three: `Allowed under existing standards; no additional approval required` — stray whitespace, a markup-breaking typo with a confirmed rendering defect, and a heading-hierarchy fix with no wording change (matches the Editorial Authority Matrix's explicit "Allowed" entries for headings).

#### Unresolved but Recorded (Requires Confirmation, not fixed)

**UR1 — `06-04-vscode-texlive.en.md` is a deliberate English summary, not a full translation**
The Japanese original (`06-04-vscode-texlive.ja.md`, 580 lines) is a detailed, code-heavy LuaTeX/LaTeX setup memorandum. Its English counterpart (`06-04-vscode-texlive.en.md`, 14 lines) is a short prose summary of the same content, closing with "Please refer to the Japanese version for details." This is a different situation from Trial 011's UR1 (accidental untranslated body wearing an "Under preparation." marker): here the English page is genuinely written in English, accurately scoped as a summary, and honestly directs readers to the Japanese original — it matches `I18N_POLICY.md` §7's `English summary available` supplementary-availability category for a page whose full form is language-specific. The project owner had already flagged this page's incomplete translation before this review began. Recorded per instruction rather than fixed, since deciding whether/when to expand this into a full translation (as opposed to leaving it as a summary, which the policy explicitly permits) is a scope decision for the project owner, consistent with the translation-backlog UR left open in Trial 011.

---

### Change and Validation

Files changed: `06-04-vscode-texlive.ja.md` (2 edits: heading trailing space, en dash → hyphen), `06-05-online-tools.ja.md` (1 edit: added H1), `06-05-online-tools.en.md` (1 edit: added H1, demoted prior heading to H2).

Verified: `git status --short` showed only these three files modified before and after editing; `hugo --minify` build — 157 JA / 51 EN pages, 0 errors. Rebuilt pages confirm: the `sfkanbunパッケージ...` heading anchor renders with no trailing artifact; the `fn2end` list item now renders inside the `<ul>` (23 `<li>` items total, no longer split into a stray paragraph); `06-05-online-tools`'s Japanese page renders `<h1 id=オンラインツール>オンラインツール` and the English page renders `<h1 id=online-tools>Online Tools`, each with the prior heading text now appearing as the first H2 / TOC entry. Scratch build directory removed after verification.

---

### Final Review Result

Overall judgment: **Pass**. Required revisions: none remaining (RR1–RR3 resolved and verified). Confirmation-blocking issues: none. Non-blocking improvement candidates: none. Unresolved but recorded: UR1 (`06-04-vscode-texlive.en.md` is a deliberate, policy-consistent English summary rather than a full translation — a project-owner scope decision, not a defect). Files changed: `06-typesetting/06-04-vscode-texlive.ja.md`, `06-05-online-tools.ja.md`, `06-05-online-tools.en.md`. Reviewer: Claude (this session). Review date: 2026-07-27.
