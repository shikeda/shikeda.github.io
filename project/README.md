# Project Management Documents

このディレクトリ（リポジトリ直下、`content/` の外＝非公開）には、`content/docs/krm/` の運用・整備状況を
管理するためのドキュメントを置く。`governance/review-trials/` と同様、Hugo のビルド対象外であり、
サイトとして公開されることはない。

## このディレクトリのファイル

- **[issues.md](./issues.md)** — Review Trial（`governance/review-trials/`）で見つかったが未解決のまま
  残っている項目の一覧。翻訳状況に関する2項目（Translation Pending / Intentional Summary）と、
  その他の軽微なバックログ項目をまとめている。
- **[translation-backlog.md](./translation-backlog.md)** — 英語版が未整備のページを
  「Core Documentation（未翻訳）」「Summary Only（意図的な要約）」「Japanese Only（方針上、翻訳不要）」
  の3区分に整理したチェックリスト。
- **[workflows/](./workflows/)** — 翻訳作業など、継続的なタスクの手順（SOP）を定義する再利用可能な
  プロンプト集。詳細は [workflows/README.md](./workflows/README.md) を参照。翻訳タスクの実施記録は、
  `governance/review-trials/` と対をなす非公開ディレクトリ `governance/translation-review-trials/`
  に `TRANSLATION_REVIEW_TRIAL_NNN.md` として残す。

## 背景：Review Trial による統治文書ベースのレビュー

2026年7月、`PROJECT_CHARTER.md` を頂点とする統治文書群（`AGENTS.md`、
`DOCUMENTATION_STYLE_GUIDE.md`、`EDITORIAL_CONVENTIONS.md`、`GLOSSARY_CONVENTIONS.md`、
`I18N_POLICY.md`、`MAINTENANCE_CONVENTIONS.md`、`REVIEW_CHECKLIST.md`）に基づき、
`content/docs/krm/` 以下の全ページを対象に、Review Trial 001〜014（AI支援によるレビュー、
`governance/review-trials/` に記録）を実施した。

各 Review Trial では、

- **Allowed** 区分の機械的な問題（リンク切れ、誤字、見出し構造など）はその場で修正・Hugo build で検証し、
- **Requires Confirmation** 以上の問題はプロジェクトオーナーの確認を経てから対応する

という方針で進めた。この一連のレビューにより見つかった問題の大半は確認・解決済みだが、
翻訳未整備のページなど、まとまった作業量を要する項目は backlog として本ディレクトリに記録している。

## 今後の見通し

`content/docs/krm/` のレビュー完了後の想定作業は次のとおり（2026年7月28日時点）。

1. `content/docs/krm/` レビュー完了（Review Trial 001〜014）
2. 本ディレクトリの Open Issues／Translation Backlog 作成
3. 日本語のみのページへの英文要旨の付与（英語版作成） ← 今ここ（`05-annotation-policy/` から着手、
   `workflows/translation-workflow.md` の SOP に従って順次翻訳中）
4. Documentation 公開
5. `content/posts/` は日本語中心で継続（必要な記事だけ後から英訳）
