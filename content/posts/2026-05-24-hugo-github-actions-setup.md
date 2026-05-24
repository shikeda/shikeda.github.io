---
title: "HugoサイトをGitHub Actionsで自動デプロイする設定メモ"
date: "2026-05-24"
draft: false
description: "手動ビルド＆docsディレクトリ運用からGitHub Actions自動デプロイへ移行した際のトラブルシューティングまとめ"
tags:
  - "Hugo"
  - "GitHub Actions"
  - "GitHub Pages"
  - "多言語"
categories:
  - "ツール"
---

## はじめに

HugoサイトをGitHub Pagesで公開する際、従来は以下の手順で手動運用していた。

1. Markdownを編集
2. `hugo` コマンドを実行して `docs/` を生成
3. `docs/` を git commit
4. git push

この運用をGitHub Actionsによる自動ビルド・自動デプロイに移行したので、その手順とトラブルシューティングをまとめる。

## 環境

- Hugo: v0.152.0+extended (darwin/amd64)
- テーマ: hugo-book（git submodule管理）
- 多言語構成: 日本語（デフォルト）／英語
- リポジトリ: GitHub（masterブランチ）

## GitHub Actionsワークフローの設定

`.github/workflows/hugo.yml` を以下の内容で作成する。

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches:
      - master
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.152.0
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb \
            https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb

      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Build with Hugo
        env:
          HUGO_ENVIRONMENT: production
        run: |
          hugo \
            --minify \
            --baseURL "${{ steps.pages.outputs.base_url }}/"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

ポイントは以下のとおり。

- `HUGO_VERSION` は自分の環境に合わせる（`hugo version` で確認）
- テーマをgit submoduleで管理している場合は `submodules: recursive` が必要
- hugo-bookのようなextended版が必要なテーマには `hugo_extended_` を使う

## GitHub Pagesの設定変更

リポジトリの **Settings → Pages → Build and deployment → Source** を  
**"Deploy from a branch"** から **"GitHub Actions"** に変更する。

## config.tomlの修正

`publishDir = "docs"` をコメントアウトし、`.gitignore` に `public/` を追加する。

```toml
# publishDir = "docs"
```

```gitignore
public/
```

## トラブルシューティング

移行作業中にいくつかのエラーが発生した。

### 1. フロントマターの重複定義

**エラー：**
```
mapping key "bookCollapseSection" already defined
```

`_index.md` のフロントマターに同じキーが2回定義されていた。片方を削除して解決。

### 2. TOMLとYAMLの混在

**エラー：**
```
string was used where mapping is expected
```

`---` で囲まれたYAMLフロントマターの中に、TOML形式（`=` を使う記法）が混在していた。以下のようにYAML形式に統一して解決。

```yaml
---
title: "記事タイトル"
date: "2022-01-06"
tags:
  - "タグ1"
categories:
  - "カテゴリ1"
---
```

同様のファイルを一括検索するには：

```bash
grep -rl "^title = " content/
```

### 3. docs/以下がビルドされない（404エラー）

**症状：** `https://example.github.io/docs/krm/01-introduction/` が404になる。

**原因その1：** `content/docs/_index.ja.md` と `content/docs/_index.en.md` が存在しなかった。多言語構成では各セクションに言語別の `_index.md` が必要。

```bash
printf -- '---\ntitle: "Docs"\ndraft: false\n---\n' > content/docs/_index.ja.md
printf -- '---\ntitle: "Docs"\ndraft: false\n---\n' > content/docs/_index.en.md
```

**原因その2：** `config.toml` の `defaultContentLanguage` の記述位置が間違っていた。

TOMLでは `[section]` 以降の設定はすべてそのセクションに属する。`[languages]` セクションの**後ろ**に書いた `defaultContentLanguage = "ja"` は無視され、デフォルトの `en` が使われていた。

**誤った書き方：**
```toml
[languages]
  [languages.ja]
    languageName = "Japanese"

defaultContentLanguage = "ja"  # [languages]セクション内として解釈される
```

**正しい書き方：**
```toml
defaultContentLanguage = "ja"  # [languages]より前に書く
defaultContentLanguageInSubdir = false

[languages]
  [languages.ja]
    languageName = "Japanese"
    weight = 1
  [languages.en]
    languageName = "English"
    weight = 2
```

設定が正しく反映されているかは以下で確認できる：

```bash
hugo config | grep -i "defaultcontent"
```

## 改善後の運用フロー

```
Markdownを編集 → git push → GitHub Actionsが自動ビルド＆公開
```

`docs/` ディレクトリをgit管理から外せるため、リポジトリが軽くなる。ビルド履歴もCIログで確認できる。

## まとめ

今回のつまずきポイントは主に2つだった。

1. **TOMLのセクション仕様**：`[section]` 以降の設定はすべてそのセクションに属するため、グローバル設定は必ずセクションより前に書く必要がある
2. **多言語構成でのセクションindex**：各コンテンツディレクトリに言語別の `_index.md` が必要

どちらもエラーメッセージだけでは原因が見えにくく、設定ファイルの構造を丁寧に確認することで解決できた。
