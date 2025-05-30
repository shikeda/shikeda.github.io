---
title: "A Memorandum on LuaTeX Typesetting for Old Dictionaries and Kunten Materials"
weight: 34
---
# A Memorandum on LuaTeX Typesetting for Old Dictionaries and Kunten Materials

This document is a memorandum detailing the setup methods for typesetting transcriptions and annotations of old dictionaries and *kunten* materials. It focuses on using a LuaTeX environment (with TeX Live and VS Code recommended), along with Hanazono Mincho fonts, GlyphWiki, and either `sfkanbun.sty` or a LuaLaTeX-compatible version of `kunten2e.sty`.

First, it introduces the **key aspects of setting up the LuaLaTeX environment in VS Code** (utilizing `latexmk` and the LaTeX Workshop extension) and provides numerous online references for Japanese typesetting.

Next, it elaborates on **typesetting configuration using the `jlreq` document class**. Referencing the style of the journal *Kunten-go to Kunten-shiryō* (訓点語と訓点資料), this part explains basic page layout settings (such as A4 vertical two-column format, margins, and font sizes), custom layouts for article titles and author names, methods for displaying endnotes, and procedures for creating a Japanese bibliography (sortable by *gojūon* order) using `natbib.sty`.

Finally, under **specific methods for creating the transcribed main text**, it presents font settings for Hanazono Mincho and IPAexMincho using `luatexja-fontspec`, and instructions for configuring the use of GlyphWiki with `bxglyphwiki.sty`. Furthermore, it demonstrates the usage of `sfkanbun-lua.sty` (a version of Fujita Shinsaku's `sfkanbun.sty` adapted for LuaLaTeX), command redefinitions to maintain compatibility with `kunten2e.sty` macros (such as `\sougyou` and `\hukusougyou`), and provides examples and typesetting results for the `\kundoku` command. It also addresses modifications needed to use legacy `kunten2e.sty` files with LuaLaTeX.

**Please refer to the Japanese version for details.**