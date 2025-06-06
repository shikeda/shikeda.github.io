---
title: "Basic Policy and Subjects of Analysis for Annotation Creation"
weight: 17
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Basic Principles and Analytical Focus for Annotation Creation

This section provides an overview of the structure of **`Entries`** and the approximate number of **`Original Glosses`**. It then outlines the basic principles for creating annotations, using a single **`Entry`** as an example for illustration.

## `Entry` Structure and Number of `Original Glosses`

An **`Entry`** consists of a **`Headword`** and **`Original Glosses`**.

The **`Original Glosses`** are further composed of elements such as **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings` (*wakun*)**, **`Notes on Character Form`**, and **`Other`** information.

The structure of an **`Entry`** is illustrated in the diagram below. For reference, the approximate number of **`Entries`** and the count for each type of **`Original Gloss`** element are also indicated. The total number of **`Original Gloss`** elements is approximately 86,800.

{{< mermaid title="Entry Structure" >}}
graph TB
    A(Entry) --> B(Headword);
    B --- I(("Approx. 32,600 Entries"));
    A --> C(Original Glosses);
    C --> D(Notes on Character Form);
    D --- K(("Approx. 13,400"));
    C --> E(Phonetic Glosses);
    E --- L(("Approx. 24,100"));
    C --> F(Semantic Glosses in Chinese);
    F --- M(("Approx. 12,600"));
    C --> G(Japanese Native Readings);
    G --- N(("Approx. 35,400"));
    C --> H(Other);
    H --- O(("Approx. 1,300"));
{{< /mermaid >}}
Note: In the diagram, "Japanese Native Readings" refers to `Japanese Native Readings` (*wakun*) as defined in the glossary.

## Understanding the Main Text

### Example of an **`Entry`**

Let's examine the content of an **`Entry`** using '覲' as an example.

```text
    Headword: 覲
    Original Glosses: 音僅（R）　ミル（LH）　マミユ（HLH）　和後ン（_L）
        Elements of Original Glosses:
            Phonetic Gloss: 音僅（R）
            Japanese Native Reading (*wakun*): ミル（LH）
            Japanese Native Reading (*wakun*): マミユ（HLH）
            Phonetic Gloss: 和後ン（_L）
```

In this **`Entry`**, for the single **`Headword`** '覲', two **`Phonetic Glosses`** and two **`Japanese Native Readings` (*wakun*)** are provided.

Below, we will provide some explanation for the **`Headword`**, **`Phonetic Glosses`**, and **`Japanese Native Readings` (*wakun*)** in order.

### **`Headword`**

Although the **`Headword`** is transcribed as '覲', its actual glyph form in the original manuscript, when reproduced using GlyphWiki, appears as:
![覲](https://glyphwiki.org/glyph/hdic-tanki01_hkrm-02081630.50px.png).

Information on the character '覲' in GlyphWiki can be found at [https://glyphwiki.org/wiki/u50c5](https://glyphwiki.org/wiki/u50c5). Various glyphs are registered there; if the desired glyph is available, it can be used. If not, one can create and register a new glyph.

Glyphs in HDIC (Integrated Database of Hanzi Dictionaries in Early Japan) typically begin with the prefix `hdic-`. For the Kanchi-in manuscript of the *Ruiju Myōgishō*, an additional `hkrm-` is appended, followed by an 8-digit number indicating its location information to form the GlyphWiki glyph name.

Regarding the glyph ![覲](https://glyphwiki.org/glyph/hdic-tanki01_hkrm-02081630.50px.png),
searching for '覲' in the HNG (Hanzi Normative Glyphs Database) at [https://search.hng-data.org/search](https://search.hng-data.org/search) confirms that an example exists in the Ueno manuscript of the *Hanshu* (Book of Han), specifically in the *Yang Xiong* (楊雄) section.

When creating annotations related to **`Headwords`**, it may be necessary to create and display glyphs using GlyphWiki, or to create and display cropped images from the original manuscript.

However, for text-based annotation creation, such visual representations can reduce readability. Therefore, using the IDS (Ideographic Description Sequence) method is often more practical. The aforementioned glyph ![覲](https://glyphwiki.org/glyph/hdic-tanki01_hkrm-02081630.50px.png) can be represented, for example, as `⿰⿳艹口土見`.



### Examining `Phonetic Glosses`

#### The *Guangyun* (広韻)

The character '覲' is listed in the *Guangyun* under the Departing tone (去声, *qùshēng*) and the *Zhen* rhyme (震韻). Its semantic gloss (義注, *gichū*) is given as "見也" (to see), and it belongs to the *xiaoyun* (小韻, phonetic group) '僅', which is indicated by the *fanqie* spelling "渠遴切" (*qú lìn qiè*).

Taking '覲' as an example, there are two primary ways to present this information in an annotation:

1.  Indicating only the phonetic information: '覲' is given in the *Guangyun* as "渠遴切" (*qú lìn qiè*; Departing tone, *Zhen* rhyme (震韻), under *xiaoyun* '僅').
2.  Indicating both phonetic and semantic information: '覲' is given in the *Guangyun* as "見也" (to see; Departing tone, *Zhen* rhyme (震韻), under *xiaoyun* '僅': "渠遴切" *qú lìn qiè*).

#### Standard Pronunciation (*Seion*)

The first **`Phonetic Gloss`** in the Kanchi-in manuscript entry for '覲' is a homophone gloss (同音字注, *dōonji-chū*) given as "音僅（R）". This corresponds to the *xiaoyun* character '僅' from the *Guangyun*'s Departing tone, *Zhen* rhyme (震韻). The 'R' is the symbol indicating the Departing tone, so the tone also matches.

While *Kan-on* (漢音, Han pronunciations) are also referred to as *Seion* (正音, standard pronunciations), their tones often align with those in the *Guangyun*. The Kanchi-in manuscript's entry for '覲' also matches the *Guangyun* tone.

Therefore, for annotation purposes, it would likely be sufficient to indicate only the phonetic information, such as: "'覲' is given in the *Guangyun* as "渠遴切" (*qú lìn qiè*; Departing tone, *Zhen* rhyme (震韻), under *xiaoyun* '僅')."

It should be noted that the character '音' (sound/pronunciation) in the original manuscript often appears as the abbreviated character '亠', but our policy is to normalize it to the standard form '音' in transcriptions.

#### Japanese-adapted Pronunciation (*Wa-on*)

Another **`Phonetic Gloss`** provided is "和後ン（_L）", indicating that the *Wa-on* (和音, Japanese-adapted pronunciation) is "後ン" with a low, level tone pattern (_L). The '和' (for *Wa-on*) in the original manuscript often appears as the abbreviated character '禾', but this too is normalized to the standard form '和' in transcriptions.

The '後' in "後ン" is understood to represent the voiced sound *go*. The **`Tone Mark` (*shōten*)** is applied only to 'ン' as a level tone (平声, *pingshēng*). In the *Guangyun*, '覲' is a Departing tone character, and the Departing tone is considered to be a rising or high falling tone. Although the tone of '後' in the Kanchi-in manuscript's *Wa-on* reading is unclear, 'ン' is marked with a level tone, making it difficult to interpret as a rising or high falling tone. It was likely a low, level tone. From these points, it is evident that the tonal pronunciations differ between the *Seion* and the *Wa-on*.

The textual sources for *Wa-on* readings are believed to reflect the pronunciations used when reciting sutras such as the Lotus Sutra (法華経, *Hokekyō*) and the Great Perfection of Wisdom Sutra (大般若経, *Dai-Hannya-kyō*). Checking with the SAT Taishō Tripiṭaka Text Database (大正新脩大蔵経データベース), '覲' appears multiple times in both the Lotus Sutra and the Great Perfection of Wisdom Sutra.

Examining the Zushoryōbon manuscript of the original compilation of the *Ruiju Myōgishō*, we find citations from Shingō's *Dai-Hannya-kyō Onkun* (大般若経音訓, Phonetic Readings and Meanings of the Great Perfection of Wisdom Sutra) and Fujiwara no Kintō's *Dai-Hannya-kyō Jishō* (大般若経字抄, Character Excerpts from the Great Perfection of Wisdom Sutra). While the *Dai-Hannya-kyō Onkun* is a lost work (逸書, *issho*), the Ishiyama-dera manuscript of the *Dai-Hannya-kyō Jishō* is extant and can be collated. Upon investigation, '覲' does not appear in the *Dai-Hannya-kyō Jishō*.

For annotation purposes, it is necessary to note any questions regarding the character forms of **`Hanzi (Chinese characters)`** or kana, and the placement of **`Tone Marks` (*shōten*)**. The distinction between red and black ink for these marks, as well as the condition of any manuscript damage (e.g., wormholes), should be recorded as needed. Furthermore, one might note the presence or absence of the character in the Lotus Sutra and the Great Perfection of Wisdom Sutra, record relevant content from the Ishiyama-dera manuscript of the *Dai-Hannya-kyō Jishō* or from extant fragments of the *Dai-Hannya-kyō Onkun*, and add critical analysis (考証, *kōshō*).


### Examining `Japanese Native Readings` (*wakun*)

Two **`Japanese Native Readings` (*wakun*)** are provided for '覲': "ミル" (*miru*; LH) and "マミユ" (*mamiyu*; HLH).

The character '覲' is explained in the *Shuowen Jiezi* (説文解字), under the "見" (see) radical section, as: "諸侯秋朝曰覲，勞王事。从見堇聲" (When feudal lords have an audience with the sovereign in autumn, it is called *jìn* (覲); they are exerting themselves in the king's affairs. The character is composed of the radical 見 and takes its sound from 堇). This corresponds to the *wakun* "ミル" (*miru*) in the sense of "to have an audience with," or "to be granted an audience."

A relevant passage can be found in the *Zhouli* (周禮; Rites of Zhou), in the "Spring Offices - Great Minister of Rites" (春官・大宗伯, *Chūnguān Dàzōngbó*) section: "春見曰朝、夏見曰宗、秋見曰覲、冬見曰遇、時見曰會、殷見曰同。" (An audience in spring is called *cháo*; in summer, *zōng*; in autumn, *jìn* (覲); in winter, *yù*; an audience at any time, *huì*; and an audience with various lords together, *tóng*.)


## Creating Annotations

Ideally, annotations would be created to cover all the types of content discussed above.
However, conducting critical investigations for approximately 32,600 **`Entries`** and about 86,800 **`Original Gloss`** elements—totaling around 119,400 items—would require an immense amount of time and effort.

The areas where research has been most extensively accumulated are, firstly, **`Japanese Native Readings` (*wakun*)**, and secondly, **`Phonetic Glosses`**. Research concerning **`Notes on Character Form`** and **`Semantic Glosses in Chinese`** is less abundant.
Therefore, we will begin by incorporating the research findings of previous scholars concerning **`Japanese Native Readings` (*wakun*)**.

### Annotating **`Japanese Native Readings` (*wakun*)**

There are many scholarly works that discuss **`Japanese Native Readings` (*wakun*)** to which **`Tone Marks` (*shōten*)** have been applied. Furthermore, not a few *wakun* have identifiable sources, such as those found in *Monzen* (文選) readings.

The following publications are essential references for determining the lexical forms of **`Japanese Native Readings` (*wakun*)**. As they are frequently used in creating annotations, they will be referred to by the abbreviations shown below:

* **Masamune's Index (正宗索引, *Masamune Sakuin*)**: Masamune Atsuo, ed. *Ruiju Myōgishō, Dainikan: Kanji Sakuin, Kana Sakuin* (類聚名義抄 第二巻 漢字索引仮名索引, *Ruiju Myōgishō*, Vol. 2: Kanji Index, Kana Index). Tokyo: Kazama Shobō, 1955.
* **Mochizuki's Wakun Collection (望月和訓集成, *Mochizuki Wakun Shūsei*)**: Mochizuki Ikuko, ed. *Ruiju Myōgishō: Yonshu Shōten-tsuki Wakun Shūsei* (類聚名義抄：四種声点付和訓集成, *Ruiju Myōgishō*: A Collection of Wakun with Four Types of Tone Marks; Kasama Sakuin Sōkan 44). Tokyo: Kasama Shoin, 1974.
* **Kusakawa's Wakun Collection (草川和訓集成, *Kusakawa Wakun Shūsei*)**: Kusakawa Noboru, ed. *Gohon Taishō Ruiju Myōgishō Wakun Shūsei* (五本対照類聚名義抄和訓集成, A Collection of Wakun from Five Collated Manuscripts of the *Ruiju Myōgishō*). Tokyo: Kyūko Shoin, 2000.
* **Nakamura's Monzen (中村文選, *Nakamura Monzen*)**: Nakamura Munehiko. *Kujōke-bon Monzen Kokunshū* (九条家本 文選古訓集, Old Japanese Readings of the *Monzen* from the Kujō Family Manuscript). Tokyo: Kazama Shobō, 1983.
* **Kunten Goi Shūsei (訓点語彙集成, *Kunten Goi Shūsei*)**: Tsukishima Hiroshi, ed. *Kunten Goi Shūsei* (訓点語彙集成, A Comprehensive Collection of *Kunten* Vocabulary). 8 vols. and 1 supplementary vol. Tokyo: Kyūko Shoin, 2007–2009.

Many other books and articles also contain relevant descriptions. For example, the following works will be consulted sequentially:

* **Iroha Ryakuchū (色葉略注)**: Satō Kiyoji. *Iroha Jiruishō Ryakuchū* (色葉字類抄略注, Annotated Abridgment of the *Iroha Jiruishō*). 3 vols. (Jō, Chū, Ge). Tokyo: Meiji Shoin, 1995.
* **Kunten-go Jiten (訓点語辞典)**: Yoshida Kanehiko, Tsukishima Hiroshi, Ishizuka Harumichi, and Tsukimoto Masayuki. *Kunten-go Jiten* (訓点語辞典, Dictionary of *Kunten* Japanese). Tokyo: Tōkyōdō Shuppan, 2001.

When there are many **`Hanzi (Chinese characters)`** sharing the same *kun* reading, only the primary ones have been listed.

Among large-scale Japanese and Kanwa (Chinese-Japanese) dictionaries, the following are representative. Only the latest editions are listed:

* *Nihon Kokugo Daijiten Dainihan* Henshū Iinkai and Shōgakukan Kokugo Jiten Henshūbu, eds. *Nihon Kokugo Daijiten* (日本国語大辞典, Comprehensive Japanese Dictionary). 2nd ed. Tokyo: Shōgakukan, 2000–2002.
    * Content made available via JapanKnowledge starting November 2006.
* Morohashi Tetsuji. *Dai Kan-Wa Jiten, Shūtei Daini-han* (大漢和辞典 修訂第二版, The Great Chinese-Japanese Dictionary, Revised 2nd Edition). Edited by Kamata Tadashi and Yoneyama Toratarō. 12 vols., plus Vocabulary Index and Supplement. Tokyo: Taishūkan Shoten, 1990–2000.
    * Included as additional content in JapanKnowledge starting April 2021.

As a lexicographical tool for classical Chinese, the following is useful:

* Zong Fukang (宗福邦), Chen Shiyao (陳世鐃), and Xiao Haibo (蕭海波), chief eds. *Guxun Huizuan* (故訓匯纂, Compilation of Ancient Glosses). Beijing: Shangwu Yinshuguan (商務印書館), 2003.

The copy I have in my possession is the two-volume edition published in 2007. It is a compilation of glosses found in 250 texts from the Pre-Qin period to the late Qing dynasty. Prior to this, Ruan Yuan's (阮元) *Jingji Zuan Gu* (經籍纂詁) was the standard rhyme-arranged lexicographical tool for ancient glosses. The *Guxun Huizuan* is arranged by radical and stroke count, and it includes a significantly larger number of source texts.


### Annotating `Phonetic Glosses`

For **`Phonetic Glosses`**, the primary necessity is to collate them with the *Guangyun* (広韻). Using this as a foundation, analyses will be conducted on **`Tone Marks` (*shōten*)**, **`Kana glosses`** (仮名音注, *kana-onchū*), *Wa-on* notes (和音注, *wa-on chū*), and *Go-on* notes (呉音注, *go-on chū*). Since many **`Headwords`** are not found in the *Guangyun*, it is also necessary to refer to descriptions in texts such as the *Tenrei Banshō Meigi* (篆隷万象名義), extant fragments of the original *Yupian* (原本玉篇残巻, *genpon Gyokuhen zankan*), the Song edition of the *Yupian* (宋本玉篇, *Sōhon Gyokuhen*), the *Longkan Shoujian* (龍龕手鑑, *Ryūgan Shukan*), and the *Yiqiejing Yinyi* (一切経音義).

Various facsimile editions and indexes of these works are available. Additionally, many dictionaries and rhyme books can now be searched online.

The following are a list of resources primarily from my personal collection that I have utilized to date. Online versions are also noted for reference.




**Rhyme Dictionaries: *Qieyun*, *Guangyun*, and *Jiyun***

* Chen Pengnian (陳彭年), ed. *Jiaozheng Songben Guangyun, Fu Suoyin* (校正宋本廣韻　附索引, Collated Song Edition of the *Guangyun*, with Index). Taipei: Yiwen Yinshuguan (藝文印書館), 1967.
    * A photoreproduction of the Zecuntang (澤存堂) edition, with a character index arranged by radical and stroke count.
* Liu Fu (劉復), ed. *Shiyun Huibian* (十韵彙編, Compilation of Ten Rhyme Dictionaries). Taipei: Xuesheng Shuju (学生書局), 1975.
    * Presents fragments of the *Qieyun* in the upper register, corresponding to the *Guangyun* in the lower register.
* Ding Du (丁度) et al., eds. *Jiyun: Fu Suoyin* (集韻：附索引, The *Jiyun*: With Index). Shanghai: Shanghai Guji Chubanshe (上海古籍出版社), 1985.
    * Contains a photoreproduction of the Shugutang (述古堂) manuscript copy of a Song edition, held in the Shanghai Library. Includes a Four-Corner Index.
* Suzuki Shingo (鈴木慎吾). ["Hen'in Dētabēsu (PYDB)" (篇韻データベース, Rhyme Database PYDB)](https://suzukish.sakura.ne.jp/search/).
    * The *Qieyun*, *Guangyun*, and Middle Chinese phonology section includes "Web韻圖～廣韻檢索～" (Web Rhyme Charts - *Guangyun* Search), "『切韻』諸本輯覽" (Collected Editions of the *Qieyun*), and "『切韻』佚文檢索" (Search for Lost Texts of the *Qieyun*).
* Ueda Tadashi (上田正). *Setsuin Itsubun no Kenkyū* (切韻逸文の研究, A Study of Lost Texts of the *Qieyun*). Tokyo: Kyūko Shoin (汲古書院), 1984
* [Chinese Text Project (CTP)](https://ctext.org/dictionary.pl?if=en) (中國哲學書電子化計劃).
    * The [Dictionary](https://ctext.org/dictionary.pl?if=en) search function provides information from texts such as the *Shuowen Jiezi*, the Song edition of the *Guangyun*, and the *Kangxi Zidian*. Searching for "集韻" (*Jiyun*) in the Title Search (書名檢索) allows access to various full-text versions (however, note that some may be "未經校對" - uncollated/uncorrected).



**The *Yupian* (玉篇)**

* Gu Yewang (顧野王), comp. *Yuánběn Yùpiān Cánjuàn* (原本玉篇殘卷, Surviving Fragments of the Original *Yupian*). In *Gǔdài Zìshū Jíkān* (古代字書輯刊, Collection of Ancient Dictionaries). Beijing: Zhonghua Shuju (中華書局), 2004.
* Zang Kehe (臧克和). *Zhōnggǔ Hànzì Liúbiàn* (中古漢字流變, Evolution of Middle Chinese Characters). Shanghai: Huadong Shifan Daxue Chubanshe (華東師範大學出版社), 2008.
    * Collates and annotates the *Shuowen Jiezi*, surviving fragments of the original *Yupian*, the Song edition of the *Yupian*, and the *Tenrei Banshō Meigi*.
* Lü Hao (呂浩). *“Yupian” Wenxian Kaoshu* (《玉篇》文獻考述, A Philological Study of *Yupian* Documents). Shanghai: Shanghai Renmin Chubanshe (上海人民出版社), 2018.
    * In addition to studies on the *Yupian*, the appendices include "Yuánběn Yùpiān Cánjuàn Jiàodiǎnběn" (原本《玉篇》殘卷校點本, A Collated and Punctuated Edition of the Surviving Fragments of the Original *Yupian*) and "Yùpiān Yìwén Jílù" (《玉篇》逸文輯録, A Compilation of Lost Texts of the *Yupian*).
* Gu Yewang (顧野王), comp., and Yao Yongming (姚永銘), coll. and ed. *“Yuánběn Yùpiān Cánjuàn” Jiàozhèng* (《原本玉篇殘卷》校證, A Collated and Annotated Edition of the Surviving Fragments of the Original *Yupian*). Hangzhou: Zhejiang Guji Chubanshe (浙江古籍出版社), 2023.
    * Exhaustively collects surviving texts related to the original *Yupian*, performs comparative collation, and provides detailed annotations.
* Gu Yewang (顧野王), comp. *Daguang Yihui Yupian* (大廣益會玉篇, The Great Expanded and Assembled *Yupian*). In *Gǔdài Zìshū Jíkān* (古代字書輯刊, Collection of Ancient Dictionaries). Beijing: Zhonghua Shuju (中華書局), 1987.
    * A photoreproduction of the Zecuntang (澤存堂) edition, with a Four-Corner Index.
* Gu Yewang (顧野王), comp., and Lü Hao (呂浩), coll. and ed. *Daguang Yihui Yupian* (大廣益會玉篇, The Great Expanded and Assembled *Yupian*). In *Zhōngguó Gǔdài Yǔyánxué Jīběn Diǎnjí Cóngshū* (中國古代語言學基本典籍叢書, Basic Classical Works on Ancient Chinese Linguistics Series). 3 vols. (upper, middle, lower). Beijing: Zhonghua Shuju (中華書局), 2019.
    * Based on the Song dynasty edition held by the Imperial Household Agency Archives (宮内庁書陵部蔵宋本, *Kunaichō Shoryōbu-zō Sōhon*), collated against the Song 11-line edition (宋十一行本, *Sòng shíyī háng běn*), the Qing Rentei edition (清楝亭本, *Qīng liàn tíng běn*; known as the Yangzhou Shiju (揚州詩局) edition, held by the Nanjing Library), among others.
* [Integrated Database of Hanzi Dictionaries in Early Japan (HDIC)](https://github.com/shikeda/HDIC). "*Songben Yupian* (Song Edition *Yupian*)" (SYP).
    * An input version based on the Song dynasty edition held by the Imperial Household Agency Archives. Searchable via Suzuki Shingo's "Hen'in Dētabēsu" (PYDB) under [*Sōhon Gyokuhen Kensaku* (宋本玉篇検索, Song Edition *Yupian* Search)](https://suzukish.sakura.ne.jp/search/yupian/search_top.php).

**The *Tenrei Banshō Meigi* (篆隷万象名義)**

The *Tenrei Banshō Meigi* is an abridged version of the original *Yupian* and can therefore be used as a substitute for it.

* Kōyasan Daigaku and Kōyasan Daigaku Mikkyō Bunka Kenkyūjo (高野山大学・高野山大学密教文化研究所), eds. *Tenrei Banshō Meigi* (篆隷萬象名義). Kōyasan: Mikkyō Bunka Kenkyūjo (密教文化研究所), 1966.
* Kūkai (空海) and Yamada Yoshio (山田孝雄). *Tenrei Banshō Meigi* (篆隷萬象名義). In *Sūbun Sōsho* (崇文叢書, Sūbun Series), Dai 1-shū no 27–43. Tokyo: Sūbun’in (崇文院), 1926.
* Kōzanji Tenseki Monjo Sōgō Chōsadan (高山寺典籍文書綜合調査団), ed. *Kōzanji Kojisho Shiryō Daiichi* (高山寺古辭書資料第一, Kōzan-ji Old Dictionary Materials, Vol. 1). In *Kōzanji Shiryō Sōsho* (高山寺資料叢書, Kōzan-ji Materials Series), vol. 6. Tokyo: Tōkyō Daigaku Shuppankai (東京大學出版會), 1977.
* Lü Hao (吕浩). *Zhuànlì Wànxiàng Míngyì Jiàoshì* (篆隷萬象名義校釋, Collated and Annotated *Tenrei Banshō Meigi*). Shanghai: Xuelin Chubanshe (學林出版社), 2007.
* [Integrated Database of Hanzi Dictionaries in Early Japan (HDIC)](https://github.com/shikeda/HDIC). "*Tenrei Banshō Meigi* (Kōsan-ji manuscript)" (KTB).


**The *Longkan Shoujian/Shoujing* (龍龕手鑑/鏡 - Dragon Niche Hand Mirror/Guide)**

* Shi Xingjun (釋行均), ed. *Longkan Shoujing* (龍龕手鏡, Dragon Niche Hand Mirror). Beijing: Zhonghua Shuju (中華書局), 1985.
    * Contains photoreproductions of Volume 1, Volume 3, and Volume 4 of the Goryeo edition. The entirety of Volume 2 (missing from the Goryeo edition), along with the last page of Volume 1, and the table of contents and the first page of the "見" (jiàn/miru) radical section of Volume 3, are supplemented from a Song edition.
* Fujimoto Yukio (藤本幸夫) and Jeong Gwang (鄭光). *Ryūkan Shukyō (Shukan) Kenkyū* (龍龕手鏡（鑑）研究, Studies on the *Longkan Shoujing/Shoujian*). Kashiwa: Reitaku Daigaku Shuppankai (麗澤大学出版会) / Hiroike Gakuen Jigyōbu (廣池学園事業部), 2015.
    * Comprises three research papers and photoreproductions. The photoreproductions follow the same composition as the Zhonghua Shuju edition.
* Shi Xingjun (釋行均), comp., and Kyōjō Teikoku Daigaku Hōbun Gakubu (京城帝國大學法文學部), ed. *Ryūkan Shūkyō* (龍龕手鏡, Dragon Niche Hand Mirror). 3 vols. (Vol. 1, Vol. 2, and Commentary). Tokyo: Shichijō Kenzō (七条憲三), 1928–1929.
    * The photoreproductions in the two aforementioned books are both based on this edition. Difficult to obtain.



**The *Yiqiejing Yinyi* (一切経音義 - Pronunciation and Meaning in the Entire Buddhist Canon)**

Many old manuscripts and early printed editions of Xuan Ying's (玄応) *Yiqiejing Yinyi* (一切経音義) are extant. Furthermore, some parts of Xuan Ying's *Yiqiejing Yinyi* are also included verbatim in Huilin's (慧琳) *Yiqiejing Yinyi*.

-  Kōkyō Shoin (弘教書院), ed. *Dainihon Kōtei Daizōkyō Ongibu Iroku* (大日本校訂大藏經音義部爲六, The Great Japan Collated Tripitaka, Lexicographical Section, Vol. 6). Tokyo: Kōkyō Shoin (弘教書院), 1885.
    * Contains the Goryeo edition. A typeset edition.
-  Yamada Yoshio (山田孝雄). *Issaikyō Ongi Sakuin* (一切經音義索引, Index to the *Yiqiejing Yinyi*). Tokyo: Seitō Shobō (西東書房), 1925.
    * An index to both Xuan Ying's and Huilin's *Yiqiejing Yinyi*. Includes Yamada Yoshio's "Issaikyō Ongi Kankō no Tenmatsu" (一切経音義刊行の顛末, An Account of the Publication of the *Yiqiejing Yinyi*).
-  Xuan Ying (玄應) and Yamada Yoshio (山田孝雄). *Issaikyō Ongi* (一切經音義). Tokyo: Seitō Shobō (西東書房), 1932.
    * A photoreproduction of the Hōryū-ji Issaikyō manuscript copied in the Daiji era (1126-1131) (abbreviated as the Daiji-bon 大治本). Currently held by the Imperial Household Agency Archives. Contains 19 fascicles in 5 cases (vols. 1-2 and 9-25). Missing parts are supplemented from the Goryeo edition.
-  Xuan Ying (玄應) and Zhou Fagao (周法高). *Xuán Yìng Yīqièjīng Yīnyì* (玄應一切經音義). In *Zhōngyāng Yánjiūyuàn Lìshǐ Yǔyán Yánjiūsuǒ Zhuānkān* (中央研究院歴史語言研究所專刊, Special Publications of the Institute of History and Philology, Academia Sinica) 47: *Xuán Yìng Yīqièjīng Yīnyì Fǎnqiè Kǎo, Fùcè* (玄應一切經音義反切考・附冊, A Study of the Fanqie Spellings in Xuan Ying's Yiqiejing Yinyi, with Supplement). Taipei: Zhongyang Yanjiuyuan Lishi Yuyan Yanjiusuo (中央研究院歴史語言研究所), 1962.
    * Contains the Kōkyō Shoin edition.
-  Yi Seon-geun (이선근, 李瑄根), ed. *Ilchegyeong Eumui: Oe Sibib部* (일체경음의: 외십이부, 一切經音義：外十二部, The *Yiqiejing Yinyi*: With Twelve Other Works). In *Goryeo Daejanggyeong* (고려대장경, 高麗大藏經, The Goryeo Tripitaka), vol. 32. Seoul: Dongguk Daehakgyo Chulpanbu (동국대학교 출판부, Dongguk University Press), 1975.
    * Contains Xuan Ying's *Yiqiejing Yinyi*.
-  Huilin (慧琳) and Yi Seon-geun (이선근, 李瑄根), ed. *Hyerin Gyeong Eumui* (혜림경음의, 慧琳經音義, Huilin's *Yiqiejing Yinyi*). In *Goryeo Daejanggyeong* (고려대장경, 高麗大藏經, The Goryeo Tripitaka), vols. 42-43. Seoul: Dongguk Daehakgyo Chulpanbu (동국대학교 출판부, Dongguk University Press), 1976.
    * Contains Huilin's *Yiqiejing Yinyi*.
-  Xuan Ying (玄應) and Kobayashi Yoshinori (小林芳規). *Issaikyō Ongi* (一切經音義). In *Kojisho Ongi Shūsei* (古辞書音義集成, Collection of Old Dictionaries with Phonetic and Semantic Glosses), vols. 7–9. Tokyo: Kyūko Shoin (汲古書院), 1980.
    * In addition to the Daiji-bon, includes the Hiroshima University manuscript (vols. 2–5) and the Tenri Library manuscript (vol. 9) of the Ishiyama-dera Issaikyō-bon, as well as Volume 18 of the Tenri Library manuscript (a late Kamakura period copy). Furthermore, Volumes 3–8 are supplemented from the Goryeo edition.
-  Numoto Katsuaki (沼本克明), Ikeda Shōju (池田証壽), and Hara Takushi (原卓志), eds. *Issaikyō Ongi Sakuin* (一切經音義索引, Index to the *Yiqiejing Yinyi*). In *Kojisho Ongi Shūsei* (古辞書音義集成, Collection of Old Dictionaries with Phonetic and Semantic Glosses), vol. 19. Tokyo: Kyūko Shoin (汲古書院), 1984.
    * An index of headword characters, phonetic glosses, and cited sources, based on the *Kojisho Ongi Shūsei* edition.
-  Kokusai Bukkyōgaku Daigakuin Daigaku Gakujutsu Frontier Jikkō Iinkai (国際仏教学大学院大学学術フロンティア実行委員会), ed. *Gen’ō Sen Issaikyō Ongi Nijūgokan* (玄應撰一切經音義二十五卷, Xuan Ying's *Yiqiejing Yinyi* in Twenty-Five Fascicles). In *Nihon Koshakyō Zenpon Sōkan* (日本古寫經善本叢刊, Series of Rare Old Japanese Manuscript Sutras), 1st series. Tokyo: Kokusai Bukkyōgaku Daigakuin Daigaku Gakujutsu Frontier Jikkō Iinkai (国際仏教学大学院大学学術フロンティア実行委員会), 2006.
    * Contains photoreproductions totaling 53 fascicles: 21 fascicles from the Kongō-ji manuscript, 20 fascicles from the Nanatsu-dera manuscript, Volume 15 from the Historiographical Institute, University of Tokyo manuscript (from the Nanatsu-dera Issaikyō), Volumes 6 and 7 from the Faculty of Letters, Kyoto University manuscript (from the Ishiyama-dera Issaikyō), and 9 fascicles from the Saihō-ji manuscript.
- Xu Shiyi (徐時儀), coll. and ann. *Yīqièjīng Yīnyì Sānzhǒng Jiàoběn Hékān* (一切經音義三種校本合刊, A Combined Edition of Three Collated Versions of the *Yiqiejing Yinyi*). Shanghai: Shanghai Guji Chubanshe (上海古籍出版社), 2008.
    * A collated and annotated edition of the Yinyi by Xuan Ying, Huilin, and Xilin (希麟). Revised edition published in 2012.



Recently, the following work, which comprehensively covers historical Chinese character pronunciation data, was published:

**The *Gǔyīn Huìzuǎn* (古音匯纂 - Compilation of Ancient Pronunciations)**

* Zong Fubang (宗福邦), Chen Shiyao (陳世鐃), and Yu Ting (于亭), chief eds. *Gǔyīn Huìzuǎn* (古音匯纂). Beijing: Shangwu Yinshuguan (商務印書館), 2019.
    * Comprehensively covers Old Chinese (上古, *Shànggǔ*), Middle Chinese (中古, *Zhōnggǔ*), and Modern Chinese (近代, *Jìndài*) character pronunciation data from the Pre-Qin period to the late Qing dynasty. Includes 127 primary cited works. A companion volume to the *Guxun Huizuan* (故訓匯纂).
