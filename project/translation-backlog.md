# Translation Backlog

`content/docs/krm/` 全体のレビュー（Review Trial 001〜014、および継続的なEN/JA対応監査）を通じて
確認された、日英間で未整備のページの一覧。カテゴリの意味は次のとおり。

- **Core Documentation** — Core Documentation（用字注・音注・義注・和訓注釈のポリシー等）のうち、
  英語版が存在するが実質未翻訳（本文が日本語のまま）のページ。優先度が最も高い。
- **Summary Only** — 英語版が全訳ではなく、意図的な短い要約にとどめられているページ。誤りではないが、
  将来的に全訳するかどうかはプロジェクトオーナーの判断による。
- **Pending Japanese Translation** — 英語版が先行して作成・改訂され、対応する日本語版がまだ
  追いついていないページ。英語版の構成・表記が確定した後に対応する方針（進行中）。
- **Japanese Only** — `I18N_POLICY.md` の方針により、そもそも英語版が必須とされていないページ
  （Records/progress pages、Case studies）。翻訳の要否自体がオープンな判断事項。

2026年8月1日時点。チェックは翻訳（または翻訳要否の判断）が完了した時点で入れる。

---

## Pending Translation

### Core Documentation

現時点で該当なし。`05-annotation-policy/` 全ページ（05-01〜05-07）は日英とも翻訳済み。

- [x] 05-03 (`05-03-jitaichu-formats`) — 字体注の種類と記載形式（セッション開始前に翻訳完了、コミット`fbfdbf6e`）
- [x] 05-04 (`05-04-onchu-problems`) — 音注の種類と解読上の問題点（セッション開始前に翻訳完了、コミット`61a48fce`）
- [x] 05-05 (`05-05-gichu-quantity`) — 義注の種類と数量（セッション開始前に翻訳完了、コミット`c734a627`。以前記載していた「見出し二重残存」の不具合は現在確認されず解消済み）
- [x] 05-06 (`05-06-wakun-materials`) — 和訓注釈のための基礎資料（Translation Review Trial 004 で全訳完了）
- [x] 05-07 (`05-07-annotation-examples`) — 注釈記述の具体例（Translation Review Trial 005 で全訳完了）

### Summary Only

- [x] 06-04 (`06-04-vscode-texlive`) — 古辞書・訓点資料のためのLuaTeX組版備忘録（2026年8月1日、全訳完了。コード例・bibエントリ等は原文のまま保持）

### Pending Japanese Translation

英語版が先行して改訂され、日本語版への反映が保留中。英語版の構成・表記確定後に対応する。

- [ ] `content/docs/krm/_index.en.md` の冒頭再構成（About This Documentation／Resource Documented／
  Relationship to the HDIC Project／About the Ruiju Myōgishō／How This Documentation Is Organized 等）
  → `_index.ja.md` へ反映
- [ ] `09-development-history/_index.en.md`（新設章） → `09-development-history/_index.ja.md` の作成

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
`05-annotation-policy` 全ページ／`06-01`〜`06-05`）は、Review TrialおよびEN/JA対応監査で
日英とも完全な翻訳・構造一致であることを確認済みであり、このバックログには含まれない。

なお、2026年8月1日のEN/JA対応監査（ページ対応・見出し対応・図表対応の確認）で発見された
構造上の不整合（見出しレベルのずれ、部分的な未翻訳箇所）は、発見と同時に修正済み。
