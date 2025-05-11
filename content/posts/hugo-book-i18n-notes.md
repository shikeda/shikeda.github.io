---
title: "Hugo Book I18n Notes"
date: 2025-05-10T18:27:43+09:00
# bookComments: false
# bookSearchExclude: false
---

# Hugo Book テーマにおける多言語対応と言語切替リンク設置まとめ

## 1. 言語設定（`config.toml`）

```toml
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = true

[languages]
  [languages.ja]
    languageName = "Japanese"
    weight = 1

  [languages.en]
    languageName = "English"
    weight = 2
```

- `defaultContentLanguageInSubdir = true` にすることで、デフォルト言語（日本語）も `/ja/` サブディレクトリに配置され、明示的な切替が可能になります。

---

## 2. コンテンツ構成

- `content/` フォルダ内に `_index.ja.md` と `_index.en.md` を用意。
- 各言語ごとに対応する `.md` ファイルを準備すると `.Translations` が有効に機能します。

例：
```
content/
  _index.ja.md
  _index.en.md
  docs/
    krm/
      _index.ja.md
      _index.en.md
```

---

## 3. 言語切替リンクの作成

### `layouts/partials/docs/language-switcher.html`

```gohtml
{{ $currentLang := .Site.Language.Lang }}
{{ range .Translations }}
  {{ if eq .Lang "ja" }}
    <a href="{{ .RelPermalink }}">日本語</a>
  {{ else if eq .Lang "en" }}
    <a href="{{ .RelPermalink }}">English</a>
  {{ end }}
{{ end }}
```

> `.Translations` は現在のページと同じファイルパスの他言語ページを配列で保持します。

---

## 4. `baseof.html` に挿入するコード（ヘッダ部分）

### `layouts/_default/baseof.html` の修正

```gohtml
<div class="book-page">

  <div style="text-align: right; padding: 1rem;">
    {{ partial "docs/language-switcher.html" . }}
  </div>

  <header class="book-header">
```

> サイドバーの上や本文の前に挿入して、切り替えリンクを表示します。

---

## 5. 注意点

- `.Translations` が動作するためには、対応する言語のページが存在している必要があります。
- ページが一方の言語にしか存在しない場合、そのページ上ではリンクは表示されません。

---

## 6. 不要なテンプレートの整理

- `layouts/partials/docs/header.html` が残っていると、`baseof.html` の `{{ template "header" . }}` によって古い内容が干渉することがあります。
- 不要であれば削除または中身を整理してください。

---

## 7. よくあるエラーと対処

- **エラー内容**：
  ```
  can't evaluate field GetByLang in type page.Pages
  ```

  → 原因：`.Translations` に対して `GetByLang` メソッドは存在しないため、`range` で処理する必要があります。

---

## 参考

- Hugo 多言語サイト公式ガイド: https://gohugo.io/content-management/multilingual/
- Hugo Book テーマ: https://github.com/alex-shpak/hugo-book
