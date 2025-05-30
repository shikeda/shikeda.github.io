---
title: "Setting up sfkanbun.sty"
weight: 33
---

# Setting up `sfkanbun.sty`


The style file for *kunten* materials, `kunten2e.sty`, can be used with upLaTeX but is not compatible with LuaLaTeX. Some existing document files were created using this `kunten2e.sty` style file.

The sfkanbun package (`sfkanbun.sty` for Kanbun texts) originates from the work on [Typesetting Kanbun with *Kundoku* Marks (漢文の訓点文の組版), featured in "Introduction to Vertical and Horizontal Document Composition" (入門・縦横文書術) by Fujita Shinsaku](http://xymtex.com/fujitas/kanbun/kanbunex.html). A modified version of this style file, adapted for LuaLaTeX compatibility and renamed `sfkanbun-lua.sty`, has been made available at [https://github.com/shikeda/rose](https://github.com/shikeda/rose).

Therefore, to minimize changes to existing TeX source files, frequently used macros in `kunten2e.sty` have been mapped to macros in `sfkanbun.sty` that provide equivalent functionality, or compatibility has been otherwise ensured.



## Sōgyō (双行 - Double-Line Annotations)

*Sōgyō* (双行) refers to a type of **`Interlinear Note`** (割注, *warichū*), specifically one that is typically presented in two lines.

In `kunten2e.sty`, this is input as follows:

~~~tex
\sougyou{right-hand line}{left-hand line}
~~~
*(In vertical text, the "right-hand line" is typically the first line of the two-line note, and the "left-hand line" is the second.)*

In `sfkanbun.sty`, the `\tagyobox` command (for multi-line interlinear notes) is used:

~~~tex
\tagyobox{item 1 \\ item 2 \\ ...}
~~~

Since an **`Interlinear Note`** (*warichū*) often consists of just two lines (corresponding to "item 1" and "item 2" above), the following custom LaTeX command can be defined to simplify input for such cases:

~~~tex
\newcommand{\sougyou}[2]{\tagyobox{#1 \\ #2}}
~~~


## Nested Double-Line Annotations (副双行, *Fukusōgyō*)

A *fukusōgyō* (副双行) refers to creating an additional double-line annotation (*sōgyō*) within an existing *sōgyō* (double-line interlinear note).
In `kunten2e.sty`, this is input as follows:

~~~tex
\hukusougyou{right-hand line}{left-hand line}
~~~

This functionality can be achieved in `sfkanbun.sty` using its feature for nested multi-line interlinear notes (`\fukutagyobox`).

~~~tex
\fukutagyobox{item 1 \\ item 2 \\ ...}
~~~

Since a nested double-line annotation typically requires only two items (lines), the following custom LaTeX command can be defined to simplify input for such cases:

~~~tex
\newcommand{\hukusougyou}[2]{\fukutagyobox{#1 \\ #2}}
~~~

## Okurigana and Kaeriten Marks (送り仮名、返り点)

The `\kundoku` command from `sfkanbun.sty` is useful for typesetting *okurigana* (送り仮名, inflectional kana endings) and *kaeriten* (返り点, guiding marks for Japanese reading order of Kanbun). Its syntax is:

~~~tex
\kundoku[control_options]{base_character}{ruby_text}{okurigana}{kaeriten_mark}[shoulder_kaeriten_mark](punctuation_mark)
~~~

The `(punctuation_mark)` argument is optional.

## Ruby (ルビ)

Several macros are available for using ruby (ルビ, small phonetic glosses alongside characters). After experimentation, we decided to use `luatexja-ruby.sty`.

The basic syntax is:
~~~tex
\ltjruby[⟨option⟩]{親|文|字}{おや|も|じ}
~~~

In this example, the command specifies that the ruby text 'おや' (*oya*) is to be applied to the base character '親'; 'も' (*mo*) to '文'; and 'じ' (*ji*) to '字'.

An alias `\ruby` is also defined for this command.

Although the exact circumstances are no longer recalled, ruby was previously applied using a custom command named `\ukun`. To avoid rewriting original files that used this command, `\ukun` has been (re)defined as follows:

~~~tex
\newcommand{\ukun}[2]{\ltjruby{#1}{#2}}
~~~

Alternatively, all instances of `\ukun` could be globally replaced with `\ruby`.
