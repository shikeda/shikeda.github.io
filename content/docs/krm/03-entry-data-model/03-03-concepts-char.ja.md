---
title: "文字表記に関する概念"
weight: 6
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 文字表記に関する概念


## 書体・字体・字形

「書体」「字体」「字形」の用語は
石塚晴通『図書寮本 日本書紀 研究篇』（汲古書院、1984）に見える次の定義に従う。

- **書体** --- 漢字の形に於て存在する社会共通の様式。多くは其の漢字資料の目的により決まる。楷書・草書等
- **字体** --- 書体内に於て存在する一々の漢字の社会共通の基準
- **字形** --- 字体内に於て認識する一々の漢字の書写された形そのもの

「書体」「字体」「字形」を階層的に捉える点がこの定義の特徴である。


石塚による英文の定義は次のようになっている[^注1]。

[^注1]:Harumichi Ishizuka, Shoju Ikeda, Jun Shirai, and Tomokazu Takada, "The data-base focusing on the standard of writing Chinese characters in Dunhuang manuscripts," in *Proceedings of the Nara Symposium for Digital Silk Roads*: December 10-12, 2003, Nara-ken New Public Hall, Nara, Japan, ed. Kinji Ono (Tokyo: National Institute of Informatics, 2004), 133.


書體 (*Shotai*): Socially common form of the type of a Chinese character. In many instances, the usage of a particular type is determined by the purpose of writing, 楷書, 草書, etc.
字體 (*Jitai*): Socially common standard of writing Chinese character existing within the 書體.
字形 (*Jikei*): Shape itself of a Chinese character as recognized within the standard of the 字體.

この英文の説明を踏まえて、この文書では、
「書體（書体）」は **`Script Styles` (*Shotai*)**、
「字體（字体）」は **`Standard of Writing Chinese Characters` (*jitai*)**、
「字形」は **`Shapes of Chinese Characters` (*jikei*) (字形)**という用語を用いることとする。


## 異体字

**異体字**（Variant Characters）は「字体」レベルにおいて、「正字」に対応する概念である。
石塚晴通「漢字字体の日本的標準」（『国語と国文学』76（5）、1999）
などに示される漢字字体史研究のモデルでは、漢字字体の標準は
時代・地域により変遷するという考えをとっており、
**漢字字体規範データベース（HNG）**はそのモデルの実証を意図するものである。
HNGは[漢字字体規範史データセット](https://www.hng-data.org)で利用できる。

異体字は「正字」でない字体を指すのが一般の理解であるが、石塚のモデルでは、時代・地域により、漢字字体の標準、すなわち「正字」が相違するのであるから、あらかじめ「正字」と「異体字」とを区別することができない。ここでは、異体字を漢字字体のバリエーションとして捉え、「正」「俗」「通」「或」等の字体注記（字級）が施されていれば異体字を示していると判断する。

「正」「俗」等の字体注記を**字級**（Form Classification Tag）と呼ぶのは、
李景遠『隋唐字様學研究』（國立臺灣師範大學國文研究所博士論文、1997）による。

## 形近字

**形近字**（Graphically Similar Characters）とは、字形が近似しているが別字であるものである。**類形別字**あるいは**類形異字**と呼ばれる。観智院本『類聚名義抄』の研究では、
酒井憲二「類聚名義抄の字順と部首排列」（『本邦辞書史論叢』三省堂、1967）
が部首内の字順について「類似字形排列」を見出しているが、
これは、異体字および形近字が連続して掲出されると言い換えることができる。
