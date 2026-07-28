---
title: "Translation Backlog"
weight: 62
# bookFlatSection: false
# bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Translation Backlog

`content/docs/krm/` 全体のレビュー（Review Trial 001〜014）を通じて確認された、英語版が未整備の
ページの一覧。カテゴリの意味は次のとおり。

- **Core Documentation** — Core Documentation（用字注・音注・義注・和訓注釈のポリシー等）のうち、
  英語版が存在するが実質未翻訳（本文が日本語のまま）のページ。優先度が最も高い。
- **Summary Only** — 英語版が全訳ではなく、意図的な短い要約にとどめられているページ。誤りではないが、
  将来的に全訳するかどうかはプロジェクトオーナーの判断による。
- **Japanese Only** — `I18N_POLICY.md` の方針により、そもそも英語版が必須とされていないページ
  （Records/progress pages、Case studies）。翻訳の要否自体がオープンな判断事項。

2026年7月28日時点。チェックは翻訳（または翻訳要否の判断）が完了した時点で入れる。

---

## Pending Translation

### Core Documentation

`05-annotation-policy/` — 本文が日本語のまま英語版に残っている（"Under preparation." の表示は正しい）。
出典: Review Trial 011, UR1。

- [ ] 05-03 (`05-03-jitaichu-formats`) — 字体注の種類と記載形式
- [ ] 05-04 (`05-04-onchu-problems`) — 音注の種類と解読上の問題点
- [ ] 05-05 (`05-05-gichu-quantity`) — 義注の種類と数量（英語版に未翻訳の日本語見出しが二重に残る付随的な不具合あり）
- [ ] 05-06 (`05-06-wakun-materials`) — 和訓注釈のための基礎資料（同上）
- [ ] 05-07 (`05-07-annotation-examples`) — 注釈記述の具体例

### Summary Only

英語版は誤りではなく意図的な要約。全訳するかどうかを検討。
出典: Review Trial 012, UR1。

- [ ] 06-04 (`06-04-vscode-texlive`) — 古辞書・訓点資料のためのLuaTeX組版備忘録

### Japanese Only

`I18N_POLICY.md` §5 により、英語版は方針上必須ではない。将来的に英語版（全訳または要約）を追加するかどうかを検討。

**07-progress**（Records and progress pages）
出典: Review Trial 007。

- [ ] 07-progress (`_index`, `1`〜`7`)

**08-case-studies**（Case studies）
出典: Review Trial 013。

- [ ] 08-01 (`08-01-ugoku`) — 和訓「ウゴク」の調査
- [ ] 08-02 (`08-02-miru`) — 和訓「ミル」の調査
- [ ] 08-03 (`08-03-wakun-uf`) — 和訓の使用頻度
- [ ] 08-04 (`08-04-kana-split`) — 同仮名異語の区別
- [ ] 08-05 (`08-05-dhsjr`) — DHSJRとの連携
- [ ] 08-06 (`08-06-getting_started_ai_humanities`) — 人文系研究者のための「AI対話型」文献分析入門

---

## 完全に翻訳済みの参考（Not backlog）

上記以外の章（`01-introduction`／`02-data-overview`／`03-entry-data-model`／`04-entry-input`／
`05-01-basic-policy`／`05-02-headword-count`／`06-01`〜`06-03`／`06-05`／トップレベルの `_index`）は、
各 Review Trial で日英とも完全な翻訳であることを確認済みであり、このバックログには含まれない。
