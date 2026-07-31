---
title: "Setting up GlyphWiki"
weight: 32
---


# Setting up GlyphWiki

## The BXglyphwiki Package Bundle

To use Hanazono fonts with LuaLaTeX, refer to the [BXglyphwiki package bundle](https://github.com/zr-tex8r/BXglyphwiki).

A [template file](https://github.com/toyjack/template_lualatex_wikiglyphwiki) by toyjack is also available.

## Sample File for Using bxglyphwiki with LuaLaTeX

The following is a sample file that demonstrates the use of user-created characters (作字, *sakuji*) from GlyphWiki in addition to Hanazono fonts.



~~~tex
\documentclass{jlreq}
\usepackage{luatexja-fontspec}
% A setting where: HanaMinA is used for BMP (Basic Multilingual Plane) characters and HanaMinB is used for SIP (Supplementary Ideographic Plane) characters; however, these are to be replaced by IPAexMincho if possible.
\setmainjfont[AltFont={
  {Range="20000-"2FFFF, Font=HanaMinB},
  {Range="0080-"FFFF, Font=IPAexMincho},
}]{HanaMinA}
% Hanazono Mincho AFDKO version 2017-06-20

% Below are the GlyphWiki settings.
\usepackage[luatex]{graphicx}

% Use Chinese character forms registered on GlyphWiki in Lualatex.
% \GWI{zihai-021005}
% Place bxglyphwiki.lua in the same folder as the tex source file.
\usepackage[luatex]{bxglyphwiki}

\begin{document}

Here's an example of "壽 (u58fd)" from GlyphWiki.


(u58fd-g) (=zihai-024114) is displayed as \GWI{u58fd-g},
(u58fd-itaiji-009) is displayed as \GWI{u58fd-itaiji-009},
(u58fd-itaiji-010) is displayed as \GWI{u58fd-itaiji-010}.

\end{document}
~~~


If it works fine, then edit this sample file as needed.

## Notes

`gb4e.sty` is commonly used to present numbered linguistic examples. It is used together with `cgloss4e.sty`, which is distributed alongside it. However, it is incompatible with `bxglyphwiki.sty`.

Instead of using `gb4e.sty`, numbered examples are presented using the `enumerate` environment. An example is given below.

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

With this approach, the numbering can correspond as (6), (6a), (6b).
