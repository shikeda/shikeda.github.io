---
title: "Hugo BookテーマでのMermaid"
date: 2025-05-13
# bookComments: false
# bookSearchExclude: false
---

# Hugo Book テーマでの Mermaid の扱い


VS Codeで次の Mermaidで作図したER図は表示されますが、Hugo の book では図が描けない。
どうしたら表示できるか。

Claude にきいてみた。

結局のところ、まだうまくいっていません。drawioでしのいでます。


~~~mermaid
erDiagram

    main {
        string entry_id PK
        string hanzi_id
        string kazama_location FK
        string tenri_location
        string volume_name
        string radical_name
        string volume_radical_name
        string hanzi_entry
        string original_entry
        string definition
    }

    headword_chars {
        string hanzi_id PK
        string entry_id FK
        string constituent_char
        int character_order
        string kazama_location_id
        string tenri_location_id
        string img_file_name
    }

    notes {
        string definition_seq_id PK
        string entry_id FK
        string kazama_location
        string tenri_location
        string volume_name
        string radical_name
        string volume_radical_index
        string hanzi_entry
    }

    definition_core {
        string definition_seq_id PK
        string original_entry
        string definition_elements
        int definition_type_code
        string definition_type_name
        text remarks
    }

    wakun {
        string wakun_id PK
        string definition_seq_id FK
        string kazama_location FK
        string hanzi_entry
        string wakun_elements
        string wakun_form
        string wakun_standard_hanzi
        string wakun_variant_in_hanzi
        string variant_hanzi_for_wakun
        string japanknowledge_id
    }

    main ||--o{ headword_chars : has
    main ||--o{ notes : has
    notes ||--|| definition_core : "includes"
    notes ||--o{ wakun : has
~~~


## Claude の回答

Hugoのbookテーマでmermaidダイアグラムを表示するには、いくつかの手順が必要です。問題の解決方法を説明します。

## Hugoでmermaidを表示する方法##

### 1. mermaid.jsを追加する

 まず、Hugoの設定でmermaid.jsを有効にする必要があります。以下の方法のいずれかを試してください：

**方法1: layouts/partials/extend_head.htmlを作成・編集**

プロジェクトのルートにlayouts/partials/extend_head.htmlファイルを作成し、以下の内容を追加します：
```html
html<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function () {
    mermaid.initialize({
      startOnLoad: true,
      theme: 'neutral'
    });
  });
</script>
```

**方法2: config.tomlに設定を追加**

config.tomlファイルを編集し、以下の設定を追加します：

```toml
toml[params]
  BookEnableJS = true

[markup.goldmark.renderer]
  unsafe = true
```
さらに、assets/js/mermaid.jsファイルを作成し、以下の内容を追加します：
```javascriptmermaid.initialize({
  startOnLoad: true,
  theme: 'neutral'
});
```

### 2. コードブロックの書き方を変更する
Hugo Bookテーマでは、mermaidコードブロックを以下のように記述する必要があります：

```
{{</* mermaid */>}}
erDiagram
    main {
        string entry_id PK
        string hanzi_id
        ...
    }
    ...
{{</* /mermaid */>}}
```
または、mermaid初期化に対応できるようにHTMLで直接記述する方法もあります：

```
<div class="mermaid">
erDiagram
    main {
        string entry_id PK
        string hanzi_id
        ...
    }
    ...
</div>
```

### 3. シンタックスハイライトの問題を解決する

Hugo Bookのデフォルトのシンタックスハイライトがmermaidと競合する場合は、以下の設定をconfig.tomlに追加して特定のコードブロックでのハイライトを無効にできます：

```toml
[markup]
  [markup.highlight]
    codeFences = true
    noClasses = false
  [markup.goldmark.renderer]
    unsafe = true
```

**重要な注意点**

- Hugo BookテーマではER図のサブグラフ構文（main { ... }など）がサポートされていない可能性があります。その場合は標準的なER図の構文に変更する必要があります。
- unsafe = trueの設定は、HTMLタグをレンダリングするために必要ですが、セキュリティリスクを考慮してください。

上記の手順を試してみて、それでも問題が解決しない場合は、Hugoのバージョンとbookテーマのバージョンを確認し、最新バージョンへの更新を検討してください。

---

Hugo のバージョン

```bash
$ hugo version
Hugo Static Site Generator v0.68.3/extended linux/amd64 BuildDate: 2020-03-25T06:15:45Z
```

bookテーマのバージョン

テーマファイル内のバージョン情報を確認
themes/book/theme.toml ファイルを開き、version 情報がないか確認します:

```
# theme.toml template for a Hugo theme
# See https://github.com/gohugoio/hugoThemes#themetoml for an example

name = "Book"
license = "MIT"
licenselink = "https://github.com/alex-shpak/hugo-book/blob/master/LICENSE"
description = "Hugo documentation theme as simple as plain book"
homepage = "https://github.com/alex-shpak/hugo-book"
demosite = "https://hugo-book-demo.netlify.app"
tags = ["responsive", "clean", "documentation", "docs", "flexbox", "search", "mobile", "multilingual", "disqus"]
features = []
min_version = "0.68"

[author]
  name = "Alex Shpak"
  homepage = "https://github.com/alex-shpak/"
```

min_version = "0.68" と見える

## 注意点

- Hugo Bookテーマは比較的シンプルなテーマで、公式な「バージョン番号」を明示的に表示していない場合があります。その場合は、Gitのコミットハッシュを参照するのが最も確実です。
- 最新バージョンに更新したい場合は、導入方法に応じて以下のコマンドを使用します:
    - Git Submodule: cd themes/book && git pull
    - Go Module: hugo mod get -u github.com/alex-shpak/hugo-book



これらの方法でバージョン情報を確認した後、公式リポジトリ（https://github.com/alex-shpak/hugo-book）と比較して、最新版かどうかを判断できます。
