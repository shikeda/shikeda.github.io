# 未解決事項一覧 (Open Issues)

このファイルは、`governance/review-trials/`（リポジトリ直下、非公開）に記録された各 Review Trial のうち、
**現時点で未解決のまま残っている項目**をまとめたものである。Review Trial で見つかった問題の大半は
その場で修正・検証済みだが、本ファイルに挙げる項目は、プロジェクトオーナーの判断や、まとまった作業量を
要するため、意図的に手を付けずに記録のみされている。

各 Review Trial の詳細な経緯・根拠・検証記録は、`governance/review-trials/REVIEW_TRIAL_NNN.md` を参照。

2026年7月28日時点の状況。

---

## 1. 翻訳状況に関する項目 (Translation Status)

`05-annotation-policy/` と `06-typesetting/` のレビュー（Review Trial 011, 012）で見つかった、
英語版ページの翻訳状況に関する2種類の課題。詳細は [translation-backlog.md](./translation-backlog.md) を参照。

### Translation Pending（未翻訳）

`05-annotation-policy/` の5ページの英語版は、"Under preparation." の表示自体は正しいが、
本文が日本語のまま英語版に残っている（意図的な要約ではなく、翻訳が単に未着手の状態）。

- `05-03-jitaichu-formats.en.md`
- `05-04-onchu-problems.en.md`
- `05-05-gichu-quantity.en.md`
- `05-06-wakun-materials.en.md`
- `05-07-annotation-examples.en.md`

このうち `05-05`, `05-06` は、正しい英語見出し(H1)の直後に未翻訳の日本語見出しがそのまま残る、という
付随的な構造上の不具合も持つ（本文が未翻訳である間は個別修正の対象にならない）。

出典: Review Trial 011, UR1・UR2。

### Intentional Summary（意図的な要約）

`06-04-vscode-texlive.en.md` は、"Under preparation." の表示はなく、正しい英文で書かれた要約になっている
（「詳細は日本語版を参照」という一文で締めくくられる）。これは `I18N_POLICY.md` §7 の
"English summary available" に相当し、上記の Translation Pending とは性質が異なる
（誤りではなく、意図的にスコープを絞った状態）。

出典: Review Trial 012, UR1。

---

## 2. その他の未対応バックログ項目 (Non-blocking, Still Open)

Requires Confirmation ではなく Allowed 相当だが、記事内容そのものへの影響が小さいため
その場では対応せず、backlog として記録されたままになっている項目。

| # | 出典 | 内容 | 対象ファイル |
| --- | --- | --- | --- |
| 1 | Trial 001 F2 | `krm_main`／`krm_notes`／`krm_wakun` 等への言及がプレーンテキストのままで、ハイパーリンク化されていない | `02-data-overview/02-03-headword-chars.*.md` ほか |
| 2 | Trial 002 F3 | 兄弟関係にある概念ページ（`03-02-types-of-entries`、`03-03-concepts-char`）への相互参照リンクがない | `03-entry-data-model/03-01-data-structure.*.md` |
| 3 | Trial 003 NB1 | セクション索引ページが、要約ではなく本文記事のヘッダーをそのまま複製している | `01-introduction/_index.ja.md`, `_index.en.md` |
| 4 | Trial 003 NB2 | `weight` の値が言語版間で不一致（ja: 2 / en: 3）。現状表示への影響はない | `01-introduction/01-01-introduction.ja.md`, `.en.md` |
| 5 | Trial 007 NB1 | 「その他」節への参照リンクの一文が、他の節と異なり表の前後で重複している | `07-progress/2.md` |
| 6 | 05-03 翻訳時 (2026-07-28) | 声点表記が古い翻刻方針のまま（声点無し `@` → `_`、濁声点 `"` → `V` に統一する必要あり）。`05-03-jitaichu-formats.{ja,en}.md` は修正済み。全体的な見直しは後回しにしている | `05-annotation-policy/05-04-onchu-problems.{ja,en}.md`、`08-case-studies/08-02-miru.md`、`08-case-studies/08-04-kana-split.md` ほか、声点付き和訓・音注を含む可能性のある全ページ |

---

## 3. 解決済み項目について

上記以外の Requires Confirmation 項目（Trial 001〜014 の UR1〜UR7 等、多数）は、
すべてプロジェクトオーナーの確認を経て解決済み・クローズ済みである。個別の経緯は
各 `governance/review-trials/REVIEW_TRIAL_NNN.md` を参照。

---

## 更新履歴

- 2026-07-28: `content/docs/krm/project/issues.md` として作成、公開を避けるためリポジトリ直下
  `project/issues.md` に移動。
- 2026-07-28: 項目6（声点表記の古い翻刻方針）を追加。
