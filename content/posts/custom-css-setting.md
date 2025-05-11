---
title: "コードブロックの配色調整"
date: 2025-05-10T05:56:42+09:00
# bookComments: false
# bookSearchExclude: false
---

# Hugo Book でのカスタム CSS 設定手順

## 目的

コードブロックの背景色と文字色を、図や全体の配色と調和するように変更する。

---

## 1. `custom.css` の作成と設置

**パス**：
static/css/custom.css


**内容（例）：**
```css
/* コードブロックの色調整（青紫系に） */
pre code {
  background-color: #f3f0ff !important;  /* やや白に近い淡い青紫 */
  color: #000 !important;
}

pre {
  background-color: #f3f0ff !important;
}

```

## 2. head に読み込ませる設定

パス：

~~~swift
themes/hugo-book/layouts/partials/docs/html-head.html
~~~

追加箇所（</head> の直前など）：


~~~html
<link rel="stylesheet" href="/css/custom.css">
~~~

## 3. サイトの確認


ローカルサーバで Hugo サイトを起動し、ブラウザで表示を確認します。

```bash
hugo server
```

## 4. 不要ファイルの削除

~~~bash
rm static/css/old-custom.css
rm themes/hugo-book/layouts/partials/docs/html-head-old.html
~~~

## 補足

`custom.css` は `static/css/` に配置すれば、`/css/custom.css` として公開される。

Hugo Book テーマでは `<head>` のカスタマイズは `html-head.html` を通じて可能。


Hugo Book テーマでは `config.toml` の `[params] customCSS` はサポートされていないため、CSS を適用するには `html-head.html` に `<link>` を直接書き加える必要がある。

config.toml の最後に追加してあった次を削除。


~~~
[params]
    customCSS = ["/css/custom.css"]
~~~



