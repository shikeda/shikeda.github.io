---
title: "GlyphWikiの設定"
weight: 32
---

## GlyphWikiの設定

### BXglyphwiki パッケージバンドル

花園フォントをLuaLaTeXで使うには、
[BXglyphwiki パッケージバンドル](https://github.com/zr-tex8r/BXglyphwiki)を参考にする。

toyjackによる[テンプレートファイル](https://github.com/toyjack/template_lualatex_wikiglyphwiki
)が出ている。

### LuaLaTeXでbxglyphwikiを使うサンプルファイル

次は、花園フォントに加えて、
GlyphWikiの作字を使うサンプルファイル。

~~~tex
\documentclass{jlreq}
\usepackage{luatexja-fontspec}
% BMPはHanaMinA, SIPはHanaMinB, ただし可能ならIPAexMincho
% で置き換える, という設定
\setmainjfont[AltFont={
  {Range="20000-"2FFFF, Font=HanaMinB},
  {Range="0080-"FFFF, Font=IPAexMincho},
}]{HanaMinA}
% 花園明朝AFDKO版 2017-06-20

%%%%%%%%%%%%%%%% ここからがグリフウィキの設定
% グリフウィキを使うのにも必要
\usepackage[luatex]{graphicx}

% グリフウィキで登録された漢字字形を利用，lualatexで使用
% \GWI{zihai-021005}
% texソース・ファイルと同じフォルダにbxglyphwiki.luaをおいておくこと
\usepackage[luatex]{bxglyphwiki}

\begin{document}

これはGlyphWikiの「壽 (u58fd)」の例。

(u58fd-g) (=zihai-024114)は\GWI{u58fd-g}、
(u58fd-itaiji-009)は\GWI{u58fd-itaiji-009}、
(u58fd-itaiji-010)は\GWI{u58fd-itaiji-010}
と表示される。


\end{document}
~~~

うまくできているようなら、このサンプルファイルを
適宜加工して行く。

### 注意点

言語学の番号付き例文を示すのに、gb4e.styがよく
使われている。これは、
同時に配布されているcgloss4e.styとともに使用する。
しかし、bxglyphwiki.styとの相性が悪い。

gb4e.styの使用を取りやめて、番号付き例文は、
enumerate環境を使う。次はその例。

~~~tex
\begin{enumerate}
	\setcounter{enumi}{5}
	\item　\label{ex:02-6}
	\begin{enumerate}
	\item 滂沲　（省略）　沱　類云正（図書寮本、水部、8頁、『類音決』を引用）\label{ex:02-6a}
	\item 潜潛　干云上谷下正（図書寮本、水部、13頁、「干」は『干禄字書』の略称、「谷」は「俗」の略字）\label{ex:02-6b}
	\end{enumerate}
\end{enumerate}
~~~

この例だと、(6)(6a)(6b)のように番号を対応させることができる。