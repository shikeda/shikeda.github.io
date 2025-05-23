---
title: "花園明朝の設定"
weight: 31
---
Under preparation.
## 前提

[TeX Live](https://texwiki.texjp.org/?TeX%20Live)が使えるように設定しておく。


## 花園明朝の設定

### 花園フォント

[花園明朝のフォント](http://fonts.jp/hanazono/)をパソコンにインストールしておく。

### ブラウザでの確認

たとえば、
Chromeで
[ctext.orgのDictionaryの一部のページ](https://ctext.org/dictionary.pl?if=en&rad=1)
を見てください。

漢字の一覧が表示されているかを確認。

### 花園フォントをTexLiveにインストール

TeX Live での font の追加は、texmf-localディレクトリの下のfontsにいれる。
fontsの中にopyetypeディレクトリがあるので、その中に入れれば大丈夫。
システムによってはfontsの場所が違うことがある。

私は、Windows 11 にWSLでUbuntuを入れて、TeX Liveをインストールした環境にしたが、
これだと

  /usr/local/texlive/texmf-local/fonts/opentype/hanazono

に HanaMinA.ttfと HanaMinB.ttfを入れた。


### LuaLaTeXのサンプルファイル

次をsample1.texなどと名前を付けて保存し、
LuaLaTeXでpdfファイルを生成する。

```
$ lualatex sample1.tex
```

短いテキストだが、ちょっと時間がかかる。
といっても1分かそこらだが、瞬時に生成されるわけではない。


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
\begin{document}

これはctext.orgのデータです。

《康熙字典·一部》の「三」の項目です。

「𡘋與三同」の最初の文字が表示されるかどうかを確認してください。

Kangxi:	《康熙字典·一部·二》三：〔古文〕弎《唐韻》《集韻》《韻會》蘇甘切《正韻》蘇監切，𡘋颯平聲。《說文》三，天地人之道也。謂以陽之一合隂之二，次第重之，其數三也。《老子·道德經》一生二，二生三，三生萬物。《史記·律書》數始於一，終於十，成於三。又《周禮·冬官考工記》凡兵無過三其身。又《左傳·昭七年》士文伯曰：政不可不愼，務三而已。一擇人，二因民，三從時。又《晉語》民生於三，事之如一。又《周語》人三爲衆，女三爲粲，獸三爲羣。又姓。明三成志。又漢複姓。屈原之後有三閭氏，三飯尞之後有三飯氏，三州孝子之後有三州氏。又去聲。《韻會》蘇暫切。《論語》三思而後行。又本作參。《博雅》參，三也。《周禮·冬官考工記》參分其股圍。《前漢·𠛬法志》秦造參夷之誅。𡘋與三同。又《韻補》叶疏簪切，音森。《詩·召南》摽有梅，其實三兮。下叶今。叁。\\

次は「一部」の部首画数順のリストです。

0 strokes:	一\\
1 strokes:	丁 丂 七 丄 丅 丆 𠀀 𠀁 𠀂 𫠠 𬺰\\
2 strokes:	万 丈 三 上 下 丌 亐 卄 𠀃 𠀄 𠀅 𠀆 𪜀 𪜁 𫝀 𬺱 𬺲 𬺳 𬺴\\
3 strokes:	不 与 丏 丐 丑 丒 专 丗 𠀇 𠀈 𠀉 𠀊 𠀋 𠀌 𪜂 𫠡 𬺵 𬺶 𬺷 𬺸 𬺹\\
4 strokes:	㐀 且 丕 世 丘 丙 业 丛 东 丝 𠀍 𠀎 𠀏 𠀐 𠀑 𠀒 𠀓 𠀔 𠀕 𠀖 𠀗 𫠢 𫠣 𬺺 𬺻 𬺼 𬺽 𬺾\\
5 strokes:	㐁 㐂 丞 丟 丠 両 丢 𠀘 𠀙 𠀚 𠀜 𠀞 𠀟 𠀠 𫝁 𫠤 𫠥 𬺿 𬻀 𬻁 𬻂 𬻃 𬻄 𬻅 𬻆 𬻇 𬻈 𬻉\\
6 strokes:	丣 两 严 丽 鿖 𠀡 𠀢 𠀣 𠀤 𠀦 𠀧 𠀨 𠀪 𠀫 𫝂 𫠦 𫠧 𫠨 𫠩 𬻊 𬻋 𬻌 𬻍 𬻎 𬻏 𬻐 𬻑 𬻒 丽\\
7 strokes:	並 丧 並 𠀬 𠀭 𠀮 𠀰 𠀱 𠀲 𠀳 𠀴 𪜃 𫠪 𫠫 𫠬 𫠭 𬻓 𬻔 𬻕 𬻖 𬻗 𬻘\\
8 strokes:	鿗 𠀵 𠀶 𠀸 𠀺 𠀻 𪜄 𫠮 𬻙 𬻚 𬻛 𬻜 𬻝\\
9 strokes:	𠀽 𠀾 𠀿 𠁀 𠤢 𪜅 𫠯 𫠰 𫠱 𫠲 𬻞 𬻟 𬻠\\
10 strokes:	𠁁 𠁂 𠁃 𠁄 𠁅 𪜆 𫠳 𫠴 𫠵 𬻡 𬻢 𬻣 𬻤 𬻥\\
11 strokes:	𠁆 𠁇 𠁈 𠁊 𠁋 𫠶 𬻦 𬻧 𬻨\\
12 strokes:	𠁌 𠁍 𫠷 𫠸 𫠹 𫠺 𫠻 𬻩 𬻪 𬻫 𬻬 𬻭 𬻮\\
13 strokes:	𠁎 𠁏 𠁐 𠁑 𠁒 𫝃 𫠼 𫠽 𬻯\\
14 strokes:	𠁓 𠁔 𫠾 𫠿 𬻰\\
15 strokes:	𠁕 𠁗 𠁘 𠁙 𠁚 𠁛 𠁝 𤳏 𪜇 𫡀\\
16 strokes:	𠁖\\
17 strokes:	𠁟 𫡁 𫡂\\
19 strokes:	𠁠\\
21 strokes:	𬻱\\
\end{document}
~~~

うまくできているようなら、このサンプルファイルを
適宜、修正・加工する。
