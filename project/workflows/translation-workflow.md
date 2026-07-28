# Standard Translation Task Prompt

The goal is not merely to translate the text, but to preserve the scholarly intent, editorial consistency, and long-term maintainability of the KRM Documentation.

---

## 1. Context
We are sequentially translating the Japanese KRM Documentation into English.
The current translation target is specified below.

## 2. Current Translation Target
Translate the following file:
- `05-05-gichu-quantity.ja.md`
↓
- `05-05-gichu-quantity.en.md`

*(Note: Update the target files above for each execution.)*

## 3. Translation Guidelines
The objective is to produce an English page that is accurate, consistent, maintainable, and suitable for long-term documentation.

- **Style & Formatting:** Translate in a style consistent with the existing English KRM Documentation. Maintain the exact formatting and capitalization used in previously translated pages.
- **Terminology:** Ensure terminology is consistent with `GLOSSARY_CONVENTIONS.md` and previously translated pages. Reuse previously established terminology whenever possible. Do not introduce new English equivalents for established technical terms unless necessary.
- **Primary Sources:** Keep cited Chinese and Japanese primary texts in their original language unless an English translation is strictly necessary for basic comprehension.
- **Audience Adjustments:** Add brief explanatory wording only when required for an international reader. Do not expand the scholarly argument, alter the scholarly discussion, or introduce new interpretations.
- **Non-Translate Targets:** Do NOT translate the following elements:
  - filenames
  - directory names
  - URLs
  - Markdown syntax
  - Hugo shortcodes
  - code blocks
  - identifiers
- **Structural Preservation:** Preserve the structure of the original page. The English page should correspond one-to-one with the Japanese page unless the project owner explicitly approves otherwise.

## 4. Escalation Rules
- If the issue can be resolved by applying the existing Governance documents, do so. Otherwise, stop and ask for confirmation.
- If you are unsure about specific terms, context, or translation choices that cannot be resolved by Governance documents, stop and ask for confirmation before proceeding.
- If a passage requires scholarly interpretation rather than standard translation, stop and ask the project owner for direction.

## 5. Translation Workflow
- Follow the existing Governance documents. Apply the Documentation Review methodology where applicable, and adapt it for translation-specific review.
- **Do not modify the Japanese source file.** Only create or update the corresponding English page.

## 6. Deliverables
Produce and report the following deliverables upon task completion:

### 6.1 English Page
Create or update the target `.en.md` file according to the guidelines above.

### 6.2 Translation Review Trial Record
Output a Translation Review Trial record to `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_001.md`. 
*(Note: Increment the trial number for each execution.)*

Use or create `TRANSLATION_REVIEW_TEMPLATE.md`, focusing on terminology, consistency, untranslated fragments, and explanatory additions.

The Translation Review Trial record MUST explicitly include:
- terminology decisions (e.g., which English terms were adopted)
- questions raised
- owner confirmations
- translation-specific issues
- files modified
- remaining follow-up actions (e.g., glossary update required, translation pending, owner confirmation required)

# 翻訳タスク

## 1. コンテキスト
`content/docs/krm/05-annotation-policy/` 配下にある日本語ファイルを、順次英語に翻訳しています。

## 2. 現在の翻訳対象
以下のファイルを翻訳してください。
- `05-05-gichu-quantity.ja.md`
↓
- `05-05-gichu-quantity.en.md`

*(注：新しい翻訳タスクのたびに上記の対象ファイルを更新してください。)*

## 3. 翻訳のガイドライン
- **スタイルとフォーマット:** 既存の英語版KRMドキュメンテーションと一貫性のあるスタイルで翻訳してください。これまでに翻訳されたページで使用されているフォーマットと大文字・小文字の使い分け（キャピタライゼーション）を正確に維持してください。
- **用語:** `GLOSSARY_CONVENTIONS.md` およびこれまでに翻訳されたページと用語の一貫性を保ってください。絶対に必要な場合を除き、定着している専門用語に対して新しい英語の対応語を導入しないでください。
- **一次資料:** 引用されている漢文および日本語の一次資料は、基本的な内容理解のために英語訳が厳密に必要となる場合を除き、元の言語のままにしてください。
- **読者に向けた調整:** 国際的な読者にとって必要な場合にのみ、簡潔な説明の文言を追加してください。学術的な議論を広げたり、学術的な考察を改変したり、新たな解釈を導入したりしないでください。
- **翻訳対象外:** 以下の要素は翻訳**しないでください**。
  - ファイル名
  - ディレクトリ名
  - URL
  - Markdown構文
  - Hugoショートコード
  - コードブロック
  - 識別子
- **構造の保持:** 元のページの構造を維持してください。プロジェクトオーナーが明示的に承認しない限り、英語ページは日本語ページと1対1で対応するようにしてください。

## 4. エスカレーションと確認のルール
- 既存のガバナンス・ドキュメントを適用することで解決できる場合は、そのとおりに解決してください。それ以外の場合は、作業を一旦停止し、確認を求めてください。
- 特定の用語、文脈、または翻訳の選択について、ガバナンス・ドキュメントだけでは解決できず迷う箇所があれば、作業を進める前に一旦停止し、確認を求めてください。
- 単なる翻訳ではなく学術的な解釈が必要な箇所がある場合は、作業を一旦停止し、プロジェクトオーナーに指示を仰いでください。

## 5. 翻訳ワークフロー
既存のガバナンス・ドキュメントに従ってください。適用可能な場合はドキュメンテーション・レビューの手法を適用し、それを翻訳専用のレビューに適合させてください。

## 6. 成果物
タスク完了時に、以下の成果物を作成し報告してください。

### 6.1 英語版ページ
上記のガイドラインに従い、対象の `.en.md` ファイルを作成または更新してください。

### 6.2 翻訳レビュートライアル記録
翻訳レビュートライアルの記録を `governance/translation-review-trials/TRANSLATION_REVIEW_TRIAL_001.md` に出力してください。
*(注：実行のたびにトライアル番号を増やしてください。)*

用語、一貫性、未翻訳の断片、追加された説明などに焦点を当てた `TRANSLATION_REVIEW_TEMPLATE.md` を作成するか、それを使用してください。

翻訳レビュートライアルの記録には、以下を**必ず**含めてください。
- 用語の決定事項（例：どの英単語を採用したか）
- 生じた疑問点
- オーナーへの確認事項
- 翻訳特有の課題
- 変更されたファイル
- 残作業（例：用語集の更新が必要、翻訳未了、オーナー確認が必要 など）

