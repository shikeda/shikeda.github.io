---
title: "古辞書・訓点資料のためのLuaTeX組版備忘録"
weight: 34
---

# 古辞書・訓点資料のためのLuaTeX組版備忘録

この文書は、LuaTeX (TeX Live, VS Code推奨) 環境で、花園明朝、GlyphWiki、および `sfkanbun.sty` (またはLuaTeX対応化した `kunten2e.sty`) を用いて古辞書や訓点資料の翻刻・注釈を組版するための設定方法を解説する備忘録です。


まず、VS Code での **LuaLaTeX 環境設定の要点**（latexmk, LaTeX Workshop）と、日本語組版に関する多数のオンライン参考資料を紹介する。


次に、**`jlreq` ドキュメントクラスを利用した組版設定**について詳述する。『訓点語と訓点資料』のスタイルを参考に、基本版面設定（A4縦書き2段組、マージン、フォントサイズ等）、論文題目・著者名のカスタムレイアウト、後注の表示方法、`natbib.sty` を用いた日本語参考文献リスト（五十音順ソート対応）の作成手順を説明する。

最後に、**翻刻本文の具体的な作成方法**として、`luatexja-fontspec` による花園明朝・IPAexMinchoのフォント設定、`bxglyphwiki.sty` によるGlyphWikiの利用設定を提示する。さらに、藤田眞作氏の `sfkanbun.sty` をLuaLaTeXに対応させた `sfkanbun-lua.sty` の利用法や、`kunten2e.sty` のマクロ (`\sougyou`, `\hukusougyou`) との互換性を保つためのコマンド再定義、`\kundoku` コマンドの使用例と組版結果を示す。また、過去の資産である `kunten2e.sty` をLuaLaTeXで利用するための修正点にも触れる。

## LuaLaTeX 環境設定の要点

VS Code (Visual Studio Code) は Microsoft が提供する無料の高機能なコードエディタで、様々な言語や拡張機能に対応している。Windows、MacOS、Linuxのいずれでも利用できる。


ポイントは次の2点である。

1. `latexmk`を利用するため`.latexmkrc`を設定。
2. VS Codeのプラグイン（LaTeX Workshop）と`settings.json`の設定。


以前は、toyjack'blogoに「vscodeでlualatex」という記事があったが現在はリンク切れなので、
私の設定を次に貼り付けておく。

まず、`.latexmkrc`の中身は次のとおりである。

```text
#!/usr/bin/env perl

@default_files    = ('main.tex');
$aux_dir          = "build/";
$out_dir          = "build/";


# $lualatex = 'lualatex -shell-escape -synctex=1 -interaction=nonstopmode %O %S';
$lualatex = 'lualatex -shell-escape -synctex=1 -interaction=nonstopmode';
$pdflualatex  = $lualatex;
$biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex = 'upbibtex %O %B';
$pdf_mode = 4;

$max_repeat   = 1;

# uplatex settings
# $latex = 'uplatex %O -shell-escape -kanji=utf8 -no-guess-input-enc -synctex=1 -interaction=nonstopmode %S';
# $pdflatex = 'pdflatex %O -synctex=1 -interaction=nonstopmode %S';
# $lualatex = 'lualatex %O -synctex=1 -interaction=nonstopmode %S';
# $xelatex = 'xelatex %O -synctex=1 -interaction=nonstopmode %S';
# $biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
# $bibtex = 'upbibtex %O %B';
# $makeindex = 'upmendex %O -o %D %S';
# $dvipdf = 'dvipdfmx %O -o %D %S';
# $dvips = 'dvips %O -z -f %S | convbkmk -u > %D';
# $ps2pdf = 'ps2pdf.exe %O %S %D';
# $pdf_mode = 3;
```

`$max_repeat` は、最大何回コンパイルするかを指定するもの。ここは1回にしている。
その他のオプションの説明は省略。

`settings.json` の中身は次のようである。

```
{
    //    "editor.fontSize": 18,
    //    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
    //    "latex-workshop.view.pdf.viewer": "external",
    //    "latex-workshop.latex.outDir": "out",//出力フォルダです
        "latex-workshop.intellisense.package.enabled": true, //自動補完です
    
        //    不要なファイルの削除
        "latex-workshop.latex.autoClean.run": "onBuilt",
        //    保存時コンパイルを無効
        "latex-workshop.latex.autoBuild.run": "never",
    
    //自動削除するキャシューファイルの種類です
        "latex-workshop.latex.clean.fileTypes": [
            "*.aux",
            "*.bbl",
            "*.blg",
            "*.idx",
            "*.ind",
            "*.lof",
            "*.lot",
            "*.out",
            "*.toc",
            "*.acn",
            "*.acr",
            "*.alg",
            "*.glg",
            "*.glo",
            "*.gls",
            "*.ist",
            "*.fls",
            "*.log",
            "*.fdb_latexmk",
            "*.snm",
            "*.nav",
            "*.dvi",
            "*.synctex.gz",
        ],
    //ここからコンパイル関係です。絶対このままにしてください。
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk",
            "tools": [
                "latexmk"
            ]
        },
    ],
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-e",
                "$latex=q/uplatex %O -synctex=1 -interaction=nonstopmode -file-line-error %S/",
                "-e",
                "$bibtex=q/upbibtex %O %B/",
                "-e",
                "$biber=q/biber %O --bblencoding=utf8 -u -U --output_safechars %B/",
                "-e",
                "$makeindex=q/upmendex %O -o %D %S/",
                "-e",
                "$dvipdf=q/dvipdfmx %O -o %D %S/",
                "-norc",
                "-gg",
                "-pdfdvi",
             "%DOC%"
                ],
        },
        ],
        
    //ここまではコンパイル関係です。次はできたPDFをどこにプレビューするオプションです。
    "latex-workshop.view.pdf.viewer": "tab",
    "workbench.preferredHighContrastColorTheme": "Default Dark+",
    "workbench.preferredHighContrastLightColorTheme": "Default Dark+",
    "workbench.preferredLightColorTheme": "Default Dark+",
    "window.autoDetectColorScheme": true,
    "editor.accessibilitySupport": "off",
    "editor.unicodeHighlight.ambiguousCharacters": false,
    "editor.unicodeHighlight.invisibleCharacters": false,
    "editor.largeFileOptimizations": false,
    "window.zoomLevel": 1,
    "vsicons.dontShowNewVersionMessage": true,
    "settingsSync.ignoredExtensions": [],
    "remote.autoForwardPortsSource": "hybrid",
    "hediet.vscode-drawio.resizeImages": null,
    "hediet.vscode-drawio.offline": false,
    "editor.unicodeHighlight.nonBasicASCII": false,
    
}
```

**LaTeX、LuaLaTeXの日本語組版の参考記事**

次に参考にした記事やテンプレートがあるサイトを紹介しておく。
残念ながら訓点資料用の各種スタイルファイルを公開していた
「金水敏 TeX のページ」は現在リンク切れとなっている。

- [私家版日本語 LaTeX テンプレート（2017年5月版）](https://id.fnshr.info/2017/05/20/my-latex-templates-201705/)  jlreq ドキュメントクラス
- [LuaLaTeXで日本語文書を作成する際のヒントや気になったこと](https://lualatexlab.blog.fc2.com/blog-entry-62.html)  【基本】LuaLaTeXで縦書きする
- [LaTeX（LuaLaTeX） で A5・縦書き・2段組の小説本・エッセイ本を作る](https://adbird.hatenablog.com/entry/2018/12/27/161700)
- [日本語 LaTeX の新常識 2021](https://qiita.com/wtsnjp/items/76557b1598445a1fc9da)
– [[LaTeX] fn2end --- footnote を endnote に変換する](https://konoyonohana.blog.fc2.com/blog-entry-424.html)
- [jlreq](https://www.tug.org/texlive//Contents/live/texmf-dist/doc/latex/jlreq/jlreq-ja.html)
- [jlreq sample](https://github.com/zr-tex8r/latex-jlreq-sample)
- [adbird（広告鳥） 備忘録](https://adbird.hatenablog.com/archive/category/LaTeX)
- [金水敏 TeX のページ](http://www.let.osaka-u.ac.jp/~kinsui/tex/top.htm) **リンク切れ（2025年5月29日確認）**
- [TeX Part3 文字・記号・数式、その他](http://xyoshiki.web.fc2.com/texindex3.html)


## `jlreq` ドキュメントクラスを利用した組版設定

訓点語学会の機関誌『訓点語と訓点資料』のスタイル・ファイルは「金水敏 TeX のページ」で公開していた
『訓点語と訓点資料』用スタイル・ファイル（kunj2e11.sty）が参考になる。
その仕様は次にようになっている。

1. ページのレイアウト（基本版面）
2. 論文題目・著者名の設定（\title、\author、\maketitle）
3. 注番号表示（\chuu）
4. 論文末注釈一覧形式（chuulist 環境）
5. 凡例一覧形式（hanrei 環境）
6. 参考文献一覧形式（shomeilist 環境）
7. 丸括弧による注記（ポイントを落として表示する。\skakko）

しかしそのままでは、LuaLaTeXで使うことができない。
そこで、同様のことができるようにしてみたい。


『訓点語と訓点資料』は、B5判2段組縦書きである。
論文執筆者は、A4判で印刷したものを所定の台紙に貼り付けて、
提出すると、B5判に縮小して印刷するという方式である。
以下は、LuaLaTeXでjlreqを使うための設定の備忘録である。

[jlreq](https://www.tug.org/texlive//Contents/live/texmf-dist/doc/latex/jlreq/jlreq-ja.html)の説明がわかりやすい。


### ページのレイアウト（基本版面）

まず、documentclassで基本版面を設定する。

これは『訓点語と訓点資料』スタイル・ファイル（kunj2e11.sty）の仕様
と
高山寺典籍文書綜合調査団の『研究報告論集』の仕様をベースにして
みる。

後者の仕様は次のとおりである。

- Ａ４判　マージン上端・下端・左端・右端とも各２４ｍｍ
- 題目・氏名段抜き(一段組) ５行取り　題目１８ポ　著者氏名１４ポ
- 本文原則２段組２５行取り　１行３０字詰(１１ポ)　段間１４㎜

実際の設定。

~~~
\documentclass[
lualatex,                   % lualatexを使う
report,                     % デフォルトは横書きのarticle相当
                            % report、book、ltjtarticleもある。
                            % 縦書き論文はtateを指定するだけでもよい。
tate,                       % 縦書き、デフォルトは横書き
oneside,                    % 奇数/偶数ページを同じレイアウト、articleとreportでのデフォルト
%twoside,                   % 奇数/偶数ページを異なるレイアウト、bookでのデフォルト
notitlepage,                % 標題・概要のページの設定、bookはtilepageがデフォルト、それ以外はnotitlepage
twocolumn,                       % 二段組、onecolumnがデフォルト
paper=a4,                        % 用紙サイズ
fontsize=11pt, jafontsize=11pt,    % フォントサイズ、ptでの設定
%fontsize=13Q, jafontsize=13Q,    % フォントサイズ、Qでの設定
line_length=30zw,                % 一行の文字数（zw=全角一文字の幅）
number_of_lines=25,              % 行数
gutter=24mm,                     % ノド側の余白
column_gap=14mm,                 % 段と段の空白
head_space=24mm,                 % 天の余白（天/地どちらか一方を指定）
%foot_space=24mm,                 % 地の余白
baselineskip=1.7zw,              % 行送り、デフォルトはjafontsizeの1.7倍
headfoot_verticalposition=1.5zw, % ノンブルと本文の間の空白
hanging_punctuation]             % ぶら下げ、組み方
{jlreq}
~~~


### 論文題目・著者名の設定

論文題目・著者は段抜き(一段組)５行取りで、題目は18pt、著者氏名は14ptである。

文字サイズと文字サイズの変更命令は次のようである。

| 変更命令            | 10pt | 11pt | 12pt |
|---------------|------|------|------|
| \tiny          | 5    | 6    | 6    |
| \scriptsize    | 7    | 8    | 8    |
| \foootnotesize | 8    | 9    | 10   |
| \small         | 9    | 10   | 11   |
| \normalsize    | 10   | 11   | 12   |
| \large         | 12   | 12   | 14   |
| \Large         | 14   | 14   | 17   |
| \LARGE         | 17   | 17   | 20   |
| \huge          | 20   | 20   | 25   |
| \Huge          | 25   | 25   | 25   |


\normalsizeがデフォルトである。

高山寺典籍文書綜合調査団の『研究報告論集』の仕様とすると、
本文11pt、
論文題目18ptは、\LARGEの17ptか\hugeの20ptが近い。
著者氏名14ptは \Largeと同じになる。


『訓点語と訓点資料』スタイル・ファイル（kunj2e11.sty）の仕様とすると、
本文11pt、
論文題目は\Hugeで20pt、
著者氏名\LARGEで17ptになる。


とりあえず、kunj2e11.styに近い設定として、次のようにしてみた。

~~~
\makeatletter
\def\@maketitle{
    \vspace{1.5\zw}
    \begin{flushleft}
        {\huge 　\@title \par}  
        \vspace{0.5em}  
    \end{flushleft}
    \begin{flushright}
        {\Large \@author 　　}
    \end{flushright}
    \par      
    \vspace{2\zw}  
}
~~~

### 注番号表示

jlreqには、注の形式が複数用意されている。

- 脚注 \footnote（縦組みでは傍注）
- 傍注 \sidenote（縦組みでは脚注）
- 後注 \endnote（注自身の出力は見出し直前）

後注の\endnoteは、デフォルトでは\sectionの最後
に出力される。

\jlreqsetupにendnote_positionを渡すことで制御できる。

~~~
\jlreqsetup{
endnote_position={_chapter,_section}
}
~~~

注は、(1)の形式で出力される。

endnote_position={_chapter,_section}とすると、
\chapterと\sectionの直前に出力。

本文と参考文献の間に注の一覧を付ける場合は、
\theendnotesで挿入箇所を指定してやればよい
（endnote_positionの指定はいらない）。

### 参考文献一覧形式

『訓点語と訓点資料』スタイル・ファイル（kunj2e11.sty）の仕様では
残りは次の三つである。

- 凡例一覧形式（hanrei 環境）
- 参考文献一覧形式（shomeilist 環境）
- 丸括弧による注記（ポイントを落として表示する。\skakko）

凡例一覧形式は、enumerate環境、またはlist環境を設定することで
対応する。

丸括弧による注記（ポイントを落として表示する）のは、ポイントを
落とさない方式もあるので、後回しにする。

参考文献一覧形式と丸括弧による注記は、bibtexで対応できる。

プリアンブルに次を記載してnatbib.styを読み込む。

~~~
% bibtexで参考文献を作成する場合に必要
\usepackage{natbib}
~~~

論文末尾の参考文献の見出しがBibliographyと表示されることがある。
その時は、次のように明示的に指定すればよい。
文書クラスのreportを仕様しているので、bibnameを指定している。

~~~
% bibtexで参考文献を作成する場合に必要
\usepackage{natbib}
%\renewcommand{\refname}{参考文献} % 論文型クラスの場合
\renewcommand{\bibname}{{\Large 参考文献}} % 書籍/報告書型クラスの場合
~~~

文字サイズが気に入らないときは、適宜変更する。ここでは\Largeにした。

\end{document}の前あたりで、使用する論文のstyleと
論文一覧のbibファイルを指定する。

~~~
\bibliographystyle{tate} % 論文のスタイル・ファイル
\bibliography{tate}      % 使用するbibファイル
~~~

\bibliographystyleは拡張子がbst、
\bibliographyは拡張子がbibになる。

bstファイルは、英語文献用のものはたくさんあるが、日本語用は
多くない。ここでは、jecon.bstを使う。
jecon.bstは、経済学用のBibTeXスタイル・ファイルである。
これをカスタマイズして使う。ファイル名は任意のものでよい。
ここではtate.bstとした。

bibファイルは、次のような形式のファイルである。

~~~
@article{池田証寿1995図書寮本類聚名義抄と類音決,
author = {池田, 証寿},
title = {図書寮本類聚名義抄と類音決},
journal = {訓点語と訓点資料},
publisher = {訓点語学会},
year = {1995},
volume = {96},
number = {},
pages = {26--37},
Yomi = {いけだしょうじゅ},
}
@incollection{池田証寿2020高山寺の古辞書音義,
author = {池田, 証寿},
booktitle = {高山寺経蔵の形成と伝承},
editor = {高山寺典籍文書綜合調査団},
isbn = {9784762936463},
pages = {79--98},
publisher = {東京：汲古書院},
title = {高山寺の古辞書音義},
year = {2020},
Yomi = {いけだしょうじゅ},
}
~~~

jecon.bstではyomiのフィールドがあって、これをキーにして
日本語の五十音順に並べ替えることができる。


### 注と参考文献の順序

人文系の論文では、本文の後に「注」が来て、最後に
「参考文献」のリストを記載することが多い。

本文と参考文献の間に注の一覧を付ける場合は、
\theendnotesで挿入箇所を指定してやればよい
（endnote_positionの指定はいらない）。

（注）や〈注〉などの見出しは、適宜付け加え、
行間も\vspace{}で調整する。

## 翻刻本文の具体的な作成方法

### 花園明朝とグリフウィキ

花園明朝が使えるように設定。

~~~
\usepackage{luatexja-fontspec}
% BMPはHanaMinA, SIPはHanaMinB, ただし可能ならIPAexMincho
% で置き換える, という設定
\setmainjfont[AltFont={
  {Range="20000-"2FFFF, Font=HanaMinB},
  {Range="0080-"FFFF, Font=IPAexMincho},
}]{HanaMinA}
% 花園明朝AFDKO版 2017-06-20
~~~

グリフウィキが使えるように設定。

~~~
% グリフウィキを使うのにも必要
\usepackage[luatex]{graphicx}

% グリフウィキで登録された漢字字形を利用，lualatexで使用
% texソース・ファイルと同じフォルダにbxglyphwiki.luaをおいておくこと
\usepackage[luatex]{bxglyphwiki}
% 書式例　\GWI{zihai-021005}
~~~

bxglyphwiki.styは他のスタイル・ファイルと相性が
悪いことがあるらしい。うまく行かないときは、
他のスタイル・ファイルを外したり、順序を入れ替えたり、
調整してください。

### sfkanbunパッケージ (漢文) sfkanbun.sty 

藤田眞作氏作成のスタイルファイルを利用する。

[TeX/LaTeX Applications by Shinsaku Fujita](http://xymtex.com/fujitas2/texlatex/index.html)の「縦組パッケージファイル」から入手する。

そのままではLuaLaTeXで使えないので、[Re: LuaLaTeXで漢文の訓点を使いたい](https://oku.edu.mie-u.ac.jp/tex/mod/forum/discuss.php?d=2655&parent=15518)（**リンク切れ**）を参考にして手を加えた。
sfkanbun-lua.styにリネームしたものを
[https://github.com/shikeda/rose](https://github.com/shikeda/rose)においてある。

また、\nointerlineskipの前に\parを追加しておいたほうがよさそうである。

ファイル名はsfkanbun.styのままでもよいが、紛らわしくなる可能性があるので、
sfkanbun-lua.styにリネームしておく。

sfkanbun.styの内部処理で必要になるjdkintou.styも
上記した藤田眞作氏のサイトから入手して、
同じフォルダに入れておく。

kunten2e.styでは\sougyou（双行）で指定する。
これに対してsfkanbun.styでは\tagyobox（多行割）で指定する。

kunten2e.styの
\sougyouで作成したTeXファイルが多いので、
\sougyouで\tagyoboxが使えるように設定する。

また、kunten2e.styの
\hukusougyou（複双行）は\fukutagyobox（複多行割）
が使えるように設定する。

~~~
\usepackage{sfkanbun-lua}
% 多行割（kunten2e.styのsougyouに対応させる）
% 文字の大きさ\scriptsize(可変)
% \tagyobox{項目１ \\ 項目２ \\ ...}
\newcommand{\sougyou}[2]{\tagyobox{#1 \\ #2}}
% 複多行割（kunten2e.styのhukusougyouに対応させる）
\newcommand{\hukusougyou}[2]{\fukutagyobox{#1 \\ #2}}
~~~

次は入力例。

~~~
新字鏡云醍𨟾\sougyou{同勅礼反}{平下酒也}醐餬\sougyou{同侯孤}{反䬫餬□}\\
	玉篇云醍\sougyou{他禮切酒紅色}{又音提　} 醐 \sougyou{戸吾切}{醍醐也} 䣫𨟾 \sougyou{上音离下}{音秖乳腐}\\
~~~

[漢文の訓点文の組版](http://xymtex.com/fujitas/kanbun/kanbunex.html)から、
藤田眞作氏のサンプルを少しご覧に入れる。

~~~
顔淵・季路\kundoku{侍}{}{ス}{}(。)
子\kundoku{曰}{}{ハク}{}(、)
\kundoku{盍}{なん}{ゾ}{三}<ルト>
各\ninojiten\kundoku{言}{}{ハ}{二}
\kundoku{爾}{なんぢ}{ノ}{}
\kundoku{志}{}{ヲ}{一}(。)
~~~

書式は次のとおり。

```
\kundoku[制御]{親文字}{ルビ}{送りがな}{返り点}[肩返り点](句読点)
```

これでかなりのことができそうである。

次はその例である。

~~~
{\large 後} \tagyobox{\vspace{0.5\zw}
    \kundoku{后}{＼}{}{}六 \\ \vspace{0.5\zw} 
    \kundoku{ノ}{＼}{}{}チ　
    \kundoku{ウ}{＼}{}{}シロ　
    \kundoku{シ}{＼}{}{}リへ \vspace{0.5\zw} \\ 
    \kundoku{オ}{＼}{}{}ク\kundoku{レ}{ル}{}{} タリ　
    \kundoku{オ}{＼}{}{}クラ\kundoku{ス}{レ}{}{} \vspace{0.5\zw} \\ 
    \kundoku{オ}{＼}{}{}コタル　
    \kundoku{オ}{＼}{}{}ソシ　
    \kundoku{禾}{＼}{}{}コ\kundoku{オ}{レ}{}{} \vspace{0.5\zw} \\ 
    　　　　　\kundoku{𢓵}{＼}{}{}
    }
~~~


そうすると、次のように組み上がる。


![古辞書「後」の翻字](/images/jikyo-sample1.png) 


### 訓点資料用スタイル・ファイル  kunten2e.sty

ここまでやってきて、2005年頃に作成したTeXの
ファイルを見ると、newcommnadで定義し直すのが
面倒になってきた。

2005年頃のファイルは、金水敏氏のkunten2e.styを
使っているので、コマンドはそのまま使えるように
検討してみた。

どうやら、
金水敏氏のkunten2e.styをLuaLaTeXで使うには変更が必要のようである。

次のような変更を加えた。

    \kanjiskip --> \ltjgetparameter{kanjiskip}
    \xkanjiskip --> \ltjgetparameter{xkanjiskip}
    zw --> \zw
    zh --> \zh

他に変更が必要な箇所があるかもしれないが、当面はこれで進める。

ファイル名は、kunten2e-lua.styに変更した。

sfkanbun.styでは次の変更も行った。

    \nointerlineskip --> \par\nointerlineskip

kunten2e.styでは該当箇所がない。
