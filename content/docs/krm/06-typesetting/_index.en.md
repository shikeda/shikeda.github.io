---
bookCollapseSection: true
title: "Typesetting Configuration for Transcriptions and Annotations"
weight: 30
---

# Typesetting Configuration for Transcriptions and Annotations

## Introduction

This document outlines methods for typesetting transcriptions and annotations of old dictionaries using an environment comprising LuaTeX, Hanazono Mincho fonts, GlyphWiki, and the `sfkanbun.sty` package.

It is recommended to use LuaTeX via TeX Live and VS Code as the editor. Instructions for installing and using TeX Live and VS Code are widely available on the web and will be omitted here.


## Typesetting Transcriptions and Annotations

The transcriptions and annotations that have been created can be displayed and searched on the web.

Separately from this, we will consider methods for typesetting the web content into a more readable, book-like format.

Since the web content is written in Markdown, this can be addressed by converting it to an appropriate format.

This section serves as a memorandum on a method using LuaLaTeX.

## Requirements for Typesetting Software

Old dictionaries and *kunten* materials (訓点資料, documents annotated with guiding marks for reading Chinese texts in Japanese) often contain many complex **`Hanzi (Chinese characters)`**, and their texts, including features like **`Interlinear Notes`** (割注, *warichū*) and side-line *kun* readings (傍訓, *bōkun*), can be intricate.

For displaying and printing rare or complex characters, it is essential to be able to easily use the following two resources:

1.  Hanazono Mincho (花園明朝) fonts
2.  GlyphWiki

To utilize both of these resources, LuaLaTeX appears to be a suitable choice. While upLaTeX might also be usable, configuring it to work with these resources seems likely to be a challenging endeavor.

For complex typesetting features such as **`Interlinear Notes`** and side-line *kun* readings, macro files can be used. Several such files have been publicly released:

1.  `kunten2e.sty`: A style file for *kunten* materials.
2.  `sfkanbun.sty`: The sfkanbun package (for Kanbun texts).

Both of these can be used with upLaTeX. However, they cannot be used directly with LuaLaTeX as is. After some investigation, it was found that `sfkanbun.sty` can be made compatible with LuaLaTeX by modifying its files slightly. The necessary modifications are minimal.

It has been over 20 years since I last created document files using LaTeX. At that time, I utilized the following combination:

1.  `kunten2e.sty`: The style file for *kunten* materials.
2.  `mojikyo.sty`: For using Mojikyo fonts.

It would be convenient if LaTeX document files written with these two could be made usable with only minor revisions. In other words, easy reuse of older LaTeX document files is preferable.

Migrating from `kunten2e.sty` to `sfkanbun.sty` appears to be relatively straightforward.

While `mojikyo.sty` was useful when Unicode **`Hanzi (Chinese characters)`** could not be freely used, it is no longer necessary now that Unicode **`Hanzi (Chinese characters)`** can be input and processed directly.

The approach would be to enable the use of Hanazono Mincho fonts and then utilize `bxglyphwiki.sty`, which is compatible with LuaLaTeX, for GlyphWiki integration.

- [Setting up Hanazono Mincho](./06-typesetting/06-01-hanazono-mincho/)
- [Setting up GlyphWiki](./06-typesetting/06-02-glyphwiki/)
- [Setting up sfkanbun.sty](./06-typesetting/06-03-sfkanbun-sty/)
- [A Memorandum on LuaTeX Typesetting for Old Dictionaries and Kunten Materials](./06-typesetting/06-04-vscode-texlive/)
- [Online Tools](./06-typesetting/06-05-online-tools/)