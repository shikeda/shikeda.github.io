---
title: "sfkanbun.styの設定"
weight: 33
---

# sfkanbun.styの設定

訓点資料用スタイル・ファイル（kunten2e.sty）は、
upLaTeXであれば使えるが、
LuaLaTeXで使えない。このスタイル・ファイルで
作成した文書ファイルもある。

sfkanbunパッケージ（漢文sfkanbun.sty）は、
[漢文の訓点文の組版（藤田眞作著「入門・縦横文書術」所載）](http://xymtex.com/fujitas/kanbun/kanbunex.html)のものだが、
LuaLaTeX対応させたスタイル・ファイル（sfkanbun-lua.styにリネーム）を
[https://github.com/shikeda/rose](https://github.com/shikeda/rose)においてある。


そこで、kunten2e.styでよく利用するマクロと同機能
sfkanbun.styのマクロを対応させて、TeXのソースファイルの
変更を最小限とすることにした。

## 双行

双行とは割注のことである。

kunten2e.styでは、次のように入力する。

~~~tex
\sougyou{右行}{左行}
~~~

sfkanbun.styでは、多行割を用いる。

~~~tex
\tagyobox{項目１ \\ 項目２ \\ ...}
~~~

割注は、項目１と項目２とで十分なので、次のような
コマンドを定義しておく。

~~~tex
\newcommand{\sougyou}[2]{\tagyobox{#1 \\ #2}}
~~~

## 副双行

副双行とは、双行中にさらに双行を作るものである。
kunten2e.styでは次のように入力する。

~~~tex
\hukusougyou{右行}{左行}
~~~

これは、sfkanbun.styの複多行割で対応できる。

~~~tex
\fukutagyobox{項目１ \\ 項目２ \\ ...}
~~~

副双行は、項目１と項目２とで十分なので、次のような
コマンドを定義しておく。

~~~tex
\newcommand{\hukusougyou}[2]{\fukutagyobox{#1 \\ #2}}
~~~

## 送り仮名、返り点

sfkanbun.styの\kundokuが便利である。

~~~tex
\kundoku[制御]{親文字}{ルビ}{送りがな}{返り点}[肩返り点](句読点)
~~~

(句読点)はオプション。

## ルビ

ルビを使うマクロはいくつかものがある。
いろいろ試したが、luatexja-ruby.styを
使うことにした。

~~~tex
\ltjruby[⟨option⟩]{親|文|字}{おや|も|じ}
~~~

\rubyという別名も定義されている。

経緯はわすれたが、\ukunというコマンドを
定義してルビを付けていたので、次のように
して元のファイルの書き換えをしないようにした。

~~~tex
\newcommand{\ukun}[2]{\ltjruby{#1}{#2}}
~~~

\ukunを\rubyに一括変換してもよい。