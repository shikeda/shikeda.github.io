# Maintenance Log

Lightweight running record of maintenance changes to `content/docs/krm/`,
per `MAINTENANCE_CONVENTIONS.md` §11. Newest entries first. Scholarly content,
bibliography, examples, identifiers, and specifications are out of scope for
these entries (see `PROJECT_CHARTER.md` preservation policy).

> **On every 07-progress statistics refresh, also update the figures in
> `07-progress/_index.en.md`** (the English summary). It is the only English page
> in this section and is kept in sync by hand.

---

## 2026-09-02 — 07-progress: add English summary page

Issue or item: `content/docs/krm/07-progress/` was Japanese-only; English readers
hit a dead end at this section.

File or path: `content/docs/krm/07-progress/_index.en.md` (new);
`content/docs/krm/_index.en.md` and `_index.ja.md` (chapter-list wording).

Classification: Records section — English summary added under I18N_POLICY §5
("Records and progress pages: language-specific allowed"); the detailed
per-fascicle tables remain Japanese-only.

Changes:
- New `_index.en.md`: prose summary of the current entry/gloss counts and the
  *wakun* → *Nihon Kokugo Daijiten* linkage progress, citing data versions, with
  a link to the Japanese detail pages. No per-fascicle tables.
- Main chapter list: item 7 now points to `/en/docs/krm/07-progress/` and states
  the English/Japanese coverage split; JA wording adjusted to match.

Verification: `hugo --minify` build clean; `/en/docs/krm/07-progress/` now builds.

Workflow status: applied to working tree, pending user review / commit.

Unresolved notes: the summary figures must be refreshed whenever the JA tables
are (note added at the top of this file).

---

## 2026-09-02 — 07-progress/02-04-wakun.md: statistics refresh (wakun)

Issue or item: The four tables on the 和訓 progress page still showed the
2024-12-11 snapshot.

File or path: `content/docs/krm/07-progress/02-04-wakun.md`

Detected by: user request

Classification: Records page (progress) — derived-statistics refresh, not
scholarly revision.

Data sources / method:
- 日国IDの付与状況 / 日国未収録確認済み / 和訓の異形と異体字 — recomputed from
  `krm_wakun.tsv` v1.2.20 (last update 2026-08-19). Volume from
  `kazama_location` (`K`+2 digits). ID付与済 = `japan_knowledge_id` is a real id;
  日国未収録 = `japan_knowledge_id` == `null`; 和訓異形 = `wakun_variant_in_hanzi`
  non-empty; 漢字異体 = `variant_hanzi_for_wakun` non-empty.
- 注釈の作成状況 — `krm_wakun.tsv` has no `remarks` column; recomputed by joining
  `definition_seq_id` to `krm_notes.tsv` v1.2.40 (2026-08-25) `remarks` column
  (non-empty), variant b/c/d rows inheriting the base row's status.

Changes:
- All four tables updated to current figures. 和訓総数 36,351 → 36,352
  (法中 4,446 → 4,447; `definition_seq_id` renumbering, krm commits 2026-08).
- Corrected a transcription error in the previous 注釈の作成状況 table: the
  仏下末 row read 1,360 / 87.24% (a copy of that volume's 日国処理済み figure);
  recomputed value is 791 / 50.74%. Confirmed with the user before applying.
- Per-table date/version lines added:
  「（krm_wakun.tsv v1.2.20、2026年8月19日現在）」for the wakun-only tables,
  「（krm_wakun.tsv v1.2.20 ／ krm_notes.tsv v1.2.40、2026年8月25日現在）」for
  注釈の作成状況.
- One-sentence progress note added after each table (2024-12-11 → 2026-08).

Progress over the period: 日国ID付与 30,356 → 30,467 (+111); 日国未収録確認
1,154 → 1,158 (+4); 照合完了 (ID+null) 86.68% → 87.00%, ~4,700 unchecked;
注釈記述 ~+1,200 → 19,505 (53.66%); 和訓異形 2,014 → 2,007; 漢字異体
3,060 → 3,152 (+92).

Required review or confirmation: user review of the diff before commit.

Verification: `hugo --minify` build clean; both table structure and column
headers unchanged.

Workflow status: applied to working tree, pending user review / commit.

Unresolved notes: none.

---

## 2026-08-28 — 07-progress/1.md–7.md: statistics refresh + file rename (commit f731c723)

Issue or item: 注文 frequency tables showed the 2024-12-12 snapshot; section
files were bare-numeric (`1.md`–`7.md`).

File or path: `content/docs/krm/07-progress/` (all pages + `_index.md`)

Classification: Records pages (progress) — derived-statistics refresh +
navigation/discoverability rename.

Changes:
- Tables in 掲出字 / 注文 / 字体注 / 音注 / 義注 / その他 recomputed from
  `krm_notes.tsv` v1.2.40 (2026-08-25), `definition_type_code` /
  `definition_type_name`. 注文小計 86,779 → 86,796.
- Date lines changed to cite the data version (v1.2.40).
- Renamed to descriptive filenames on the repo's NN / NN-MM scheme:
  `01-headwords`, `02-definitions` (parent), `02-01-jitaichu`, `02-02-onchu`,
  `02-03-gichu`, `02-04-wakun`, `02-05-others`. Internal links in `_index.md`
  and `02-definitions.md` updated. No aliases.
- 和訓 page left unchanged in that commit (different data source — see the
  2026-09-02 entry).

Verification: `hugo --minify` build clean; no stale `07-progress/[1-7]/` links.

Workflow status: committed (f731c723) and pushed by the user.
