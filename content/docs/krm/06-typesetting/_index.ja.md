---
bookCollapseSection: true
title: 翻刻・注釈の組版の設定
weight: 30
---
# 翻刻・注釈の組版の設定

## はじめに

LuaTeX + 花園明朝 + GlyphWiki + sfkanbun.sty
の環境で古辞書の翻刻と注釈の組版を行う方法をまとめる。

LuaTeXはTeX Live、エディターはVS Codeを
使うことを推奨する。TeX LiveとVS Codeのインストールから
使い方までは、Webに多数出ているので、省略する。


## 翻刻・注釈の組版

作成した翻刻と注釈は、Webで表示したり、
検索したりすことができる。

それとは別にWebの内容を著作の形で見やすく組版する
方法を検討する。

Webのコンテンツは、マークダウンで書いてあるので、
これを適切なフォーマットに変換することで対応する。

ここではLuaLaTeXを使った方法について、備忘録として
記載しておく。

## 組版ソフトの条件

古辞書や訓点資料は、難しい漢字が多く、
割注、傍訓など本文が複雑である。

難字の表示・印刷は、次の二つを
簡単に使えるのが条件となる

1. 花園明朝
2. GlypWiki


この二つを簡単に利用するには、
LuaLaTeXがよさそうである。
upLaTeXでも使えそうだが、
使えるように設定するのに苦労しそうである。

割注、傍訓など複雑な組版んついては、
マクロファイルで対応する。
いくつかのものが公表されている。

1. 訓点資料用スタイル・ファイル  kunten2e.sty
2. sfkanbunパッケージ (漢文) sfkanbun.sty

どちらもupLaTeXで利用できる。
しかし、LuaLaTeXではそのまま使えない。
いろいろ調べてみると、sfkanbun.styを
LuaLaTeXで利用できるようにファイルを書き換えれば
よいことが分かった。書き換えはほんの僅かである。

LaTeXで文書ファイルを作成していたのは、
20年以上前である。
その時には、次の組み合わせを利用していた。

1. 訓点資料用スタイル・ファイル kunten2e.sty
2. 今昔文字鏡 mojikyo.sty

この二つで書いたLaTeXの文書ファイルを
若干の手直しをすることで使えるようにすると
便利である。
つまり、古いLaTeXの文書ファイルの再利用が簡単な
方がいい。

kunten2e.styからsfkanbun.styへの移行は
割に簡単そうである。

mojikyo.styは、Unicodeの漢字が自由に使えない
時は便利であったが、現在は、Unicodeの漢字を
そのまま入力・処理できるので、使う必要はない。

花園明朝を使えるようにして、
GlypWikiをLuaLaTeXに対応した
bxglypwiki.styを使えばよいだろう。

- [花園明朝の設定](/docs/krm/06-typesetting/06-01-hanazono-mincho/)
- [GlyphWikiの設定](/docs/krm/06-typesetting/06-02-glyphwiki/)
- [sfkanbun.styの設定](/docs/krm/06-typesetting/06-03-sfkanbun-sty/)
- [古辞書・訓点資料のためのLuaTeX組版備忘録](/docs/krm/06-typesetting/06-04-vscode-texlive/)
- [オンラインツール](/docs/krm/06-typesetting/06-05-online-tools/)
