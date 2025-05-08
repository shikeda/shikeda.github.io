---
title: 類聚名義抄
weight: 1
# date: 2022-01-09
bookFlatSection: true
bookToc: true
# bookHidden: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 類聚名義抄全文テキストデータベース

## はじめに

『類聚名義抄』は日本古辞書の雄編として名高い。 
書名の読み方は「るいじゅみょうぎしょう」である。
源順撰『倭名類聚抄』の「類聚」と、空海撰『篆隷万象名義』の
「名義」とを採用して書名としたとされる。


ここでは、まず『類聚名義抄』とその諸本の概要を述べる。
次に『類聚名義抄』の完本として唯一の伝本である
観智院本について、その項目の構造を解説し、
その後、観智院本の本文入力方法の詳細を述べる。

なお、ここでの解説は、
池田証壽・劉冠偉・鄭門鎬・張馨方・李媛「観智院本『類聚名義抄』全文テキストデータベース―その構築方法と掲出項目数等の計量―」(『訓点語と訓点資料』144、2020)を再構成したものである。

## 内容

- [資料紹介](/docs/notes/krm-main/overview/)
- [公開データの概要](/docs/notes/krm-main/data-structure/)
    - [krm-main](/docs/notes/krm-main/contens/1-main/)
    - [krm-notes](/docs/notes/krm-main/contens/2-notes/)
    - [krm-wakun](/docs/notes/krm-main/contens/3-wakun/)
    - [krm-definitions](/docs/notes/krm-main/contens/4-definitions/)
    - [krm-pronunciations](/docs/notes/krm-main/contens/5-pronunciations/)
    - [krm-ndl](/docs/notes/krm-main/contens/6-ndl/)
- [項目データモデル](/docs/notes/krm-main/entry-data-model/)
    - [項目データ構造](/docs/notes/krm-main/entry-data-model/1-data-structure/)
    - [項目の種類](/docs/notes/krm-main/entry-data-model/2-types-of-entries/)
    - [文字表記に関する概念](/docs/notes/krm-main/entry-data-model/3-concepts-char/)
    - [項目データファイルの公開・更新](/docs/notes/krm-main/entry-data-model/4-data-example/)
- [項目データ入力](/docs/notes/krm-main/item-input/)
    - [掲出字・項目構造とID体系](/docs/notes/krm-main/item-input/1-id/)
    - [文字の符号化と表現](/docs/notes/krm-main/item-input/2-char/)
    - [書写・表記・注記における問題と対応](/docs/notes/krm-main/item-input/3-handling/)
- [注釈データ入力の詳細](/docs/notes/krm-main/notes-input/)
    - [基本方針](/docs/notes/krm-main/notes-input/1/)
    - [掲出字](/docs/notes/krm-main/notes-input/2/)
    - [字体注](/docs/notes/krm-main/notes-input/3/)
    - [音注](/docs/notes/krm-main/notes-input/4/)
    - [義注](/docs/notes/krm-main/notes-input/5/)
    - [和訓](/docs/notes/krm-main/notes-input/6/)
- [翻刻・注釈の組版の設定](/docs/notes/krm-main/notes-output/)
    - [花園明朝の設定](/docs/notes/krm-main/notes-output/1/)
    - [GlyphWikiの設定](/docs/notes/krm-main/notes-output/2/)
    - [sfkanbun.styの設定](/docs/notes/krm-main/notes-output/3/)
    - [VS CodeとTeX Live](/docs/notes/krm-main/notes-output/4/)
    - [オンラインツール](/docs/notes/krm-main/notes-output/5/)
- [進捗状況](/docs/notes/krm-main/progress/)
- [事例研究](/docs/notes/krm-main/case-study/)



## データベース構築の工程

観智院本『類聚名義抄』は古写本であり、その掲出字は難字が極めて多いので、次の手順によりデータベース構築を進めた。

**第一段階**：複製本をスキャニングして掲出字を一文字毎に切り出して観智院本『類聚名義抄』画像データベースを作成する。掲出字の画像ファイルは掲出字の所在に対応する名前を付ける。この画像ファイル名は後に掲出字IDとして利用する。

**第二段階**：作成済みの『篆隷万象名義』データベースに正宗敦夫編『類聚名義抄 第二巻』（風間書房、1955年）に収録の「漢字索引」を参照してその所在情報を追記する。諸橋轍次編『大漢和辞典』検字番号の順に並べ替えた『篆隷万象名義』のデータに「漢字索引」の所在情報を入力し、その上で観智院本の所在順に並べ替えを行い、観智院本の本文と照合し、「漢字索引」にない観智院本の段数と字順を追加する。

**第三段階**：観智院本『類聚名義抄』画像データベース（第一段階で作成）に『篆隷万象名義』データベースに含まれる各種情報（『大漢和辞典』検字番号、Unicode番号、漢字、『篆隷万象名義』の所在情報）と第二段階で作成したそれに対応する観智院本『類聚名義抄』の所在情報）を取り込んで、入力用の観智院本『類聚名義抄』テキストデータベースを作成する。

**第四段階**：観智院本『類聚名義抄』の複製本(天理図書館善本叢書和書之部第32-34巻)および観智院本『類聚名義抄』画像データベースを参照しながら、第三段階で作成した入力用の観智院本『類聚名義抄』テキストデータベースに掲出字と注文のテキスト情報を追加する。

**第五段階**：観智院本『類聚名義抄』画像データベースと観智院本『類聚名義抄』テキストデータベースとを統合して観智院本『類聚名義抄』データベースとし、新たに刊行されたカラー版の観智院本『類聚名義抄』の複製本(新天理図書館善本叢書第9-11巻)で本文内容の点検と修正を行う。本文内容の点検に際しては、掲出項目での熟語項目と異体項目との区別、注文での字体注・音注・義注・和訓の区別も行って、それらの情報を追加する。


**第六段階**：完成した観智院本『類聚名義抄』データベースをインターネットで公開し、検索サービスを行う。

## インターネットでの情報提供

HDICのインターネットでの情報提供は、メインサイト、検索画面及びテキストデータの三つからなる。
メインサイトは次のURLで、平安漢字字書総合データベース（HDIC）の概要（日本語、中国語、英語）と研究成果のリスト、関連サイトのリンク等をまとめている。

[https://hdic.jp](https://hdic.jp)

検索画面は次のURLで、平安漢字字書総合データベース（HDIC）を検索するHDIC Viewerを利用できる。HDIC Viewerは劉冠偉が維持・管理を行っており、パソコンの他、スマートフォンでの検索を可能としている。


[https://viewer.hdic.jp](https://viewer.hdic.jp)

hdic.jpのサイトの維持・管理には、守岡知彦氏による技術支援を受けていおり、感謝申し上げる。

テキストデータは次のURLで、
平安漢字字書総合データベース（HDIC）で作成したテキストファイルを公開している。
データの修正の記録を保存し、宋本『玉篇』、高山寺本『篆隷万象名義』、天治本『新撰字鏡』の全文テキストデータベースの最新版を提供している。

[https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC)

観智院本『類聚名義抄』は、2025年3月に仕様変更を行い、
その全文テキストデータベースの最新版は次のURLで提供している。

[https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2)

以上のURLは将来において変更の可能性がある。
構築したデータの維持と管理は大きな課題である。


## 謝辞

観智院本『類聚名義抄』全文テキストデータベースの構築と公開は、天理図書館当局から特別に御許可を賜り推進しているものであり、天理図書館善本叢書の版元である八木書店各位にも格別の御配慮を賜っている。ここに記して感謝の意を表する。

#  *Ruiju Myōgishō*

## Introduction

The *Ruiju Myōgishō* is renowned as a masterpiece among old Japanese dictionaries. The book title is read as "ruiju myōgishō." It is said that the title was formed by taking "Ruiju" from Minamoto no Shitagō's Wamyō Ruijushō and "Myōgi" from Kūkai's *Tenrei Banshō Myōgi*.


Here, we will first describe the outline of the *Ruiju Myōgishō* and its various versions. Next, regarding the Kanchi-in manuscript, which is the only extant complete manuscript of the *Ruiju Myōgishō*, we will explain the structure of its entries, and then describe the details of the input method for the text of the Kanchi-in manuscript.

Furthermore, the explanation here is a reconstruction of Ikeda Shoju, Liu Guanwei, Jun Munho, Zhang Xinfang, and Li Yuan, "Full-text Database of *Ruiju Myogi-sho*, Kanchi-in MS : A Look at Development Methods and Calculating the Number of Headwords." (*Kuntengo to Kuten Shiryō* 144, 2020).

## Contents

- [Overview](/docs/notes/krm-main/overview/)
- [Overview of Public Data](/docs/notes/krm-main/data-structure/)
- [Item Data Structure](/docs/notes/krm-main/data-structure/)
    - [krm-main](/docs/notes/krm-main/contens/1-main/)
    - [krm-notes](/docs/notes/krm-main/contens/2-notes/)
    - [krm-wakun](/docs/notes/krm-main/contens/3-wakun/)
    - [krm-definitions](/docs/notes/krm-main/contens/4-definitions/)
    - [krm-pronunciations](/docs/notes/krm-main/contens/5-pronunciations/)
    - [krm-ndl](/docs/notes/krm-main/contens/6-ndl/)
- [Item Data Input](/docs/notes/krm-main/item-input/)
    - [Head Characters, Entry Structure, and ID System](/docs/notes/krm-main/item-input/1-id/)
    - [Character Encoding and Representation](/docs/notes/krm-main/item-input/2-char/)
    - [Problems and Handling in Writing, Notation, and Annotations](/docs/notes/krm-main/item-input/3-handling/)
- [Details of Definitions Data Input](/docs/notes/krm-main/def-input/)
    - [Basic Policy](/docs/notes/krm-main/def-input/1/)
    - [Glyph Annotations](/docs/notes/krm-main/def-input/2/)
    - [Pronunciation Annotations](/docs/notes/krm-main/def-input/3/)
    - [Meaning Annotations](/docs/notes/krm-main/def-input/4/)
    - [Japanese Reading](/docs/notes/krm-main/def-input/5/)
    - [Other](/docs/notes/krm-main/def-input/6/)
- [Details of My Notes Data Input (currently notes, aiming for comprehensive commentary)](/docs/notes/krm-main/notes-input/)
    - [Basic Policy](/docs/notes/krm-main/notes-input/1/)
    - [Headword](/docs/notes/krm-main/notes-input/2/)
    - [Glyph Notes](/docs/notes/krm-main/notes-input/3/)
    - [Pronunciation Notes](/docs/notes/krm-main/notes-input/4/)
    - [Meaning Notes](/docs/notes/krm-main/notes-input/5/)
    - [Japanese Reading Notes](/docs/notes/krm-main/notes-input/6/)
- [Typesetting Settings for Transcriptions and Annotations](/docs/notes/krm-main/notes-output/)
- [Project Progress](/docs/notes/krm-main/progress/)
- [Historical Research on Japanese: A Case Study of the KRM Manuscript](/docs/notes/krm-main/case-study/)

## Database Construction Process

The *Ruiju Myōgishō* of the Kanchi-in manuscript is an old handwritten manuscript, and because it contains an extremely large number of difficult characters, we proceeded with database construction using the following steps.

**Step 1:** Scan the facsimile edition and cut out each listed character to create an image database of the *Ruiju Myōgishō* of the Kanchi-in manuscript. The image files of the listed characters are named according to the location of the listed character. This image file name will later be used as the listed character ID.


**Step 2:** Add the location information to the existing *Tenrei Banshō Myōgi* database by referring to the "Kanji Index" included in Atsuo Masamune's *Ruiju Myōgishō Volume 2* (Kazama Shobō, 1955). Input the location information from the "Kanji Index" into the *Tenrei Banshō Myōgishō* data rearranged in the order of the *Dai Kanwa Jiten* index numbers compiled by Tetsuji Morohashi. Then, rearrange it according to the order of locations in the Kanchi-in manuscript, collate it with the text of the Kanchi-in manuscript, and add the page numbers and character order of the Kanchi-in manuscript that are not found in the "Kanji Index."

**Step 3:** Take in various information included in the *Tenrei Banshō Myōgishō* database (*Dai Kanwa Jiten* index numbers, Unicode numbers, kanji characters, location information in the *Tenrei Banshō Myōgishō*) and the corresponding location information of the *Ruiju Myōgishō* Kanchi-in manuscript created in Step 2, into the *Ruiju Myōgishō* Kanchi-in manuscript image database (created in Step 1) to create an input database for the *Ruiju Myōgishō* Kanchi-in manuscript text.

**Step 4:** While referring to the facsimile edition of the *Ruiju Myōgishō* Kanchi-in manuscript (Tenri Library Rare Books Series, Japanese Books Section, Volumes 32-34) and the *Ruiju Myōgishō* Kanchi-in manuscript image database, add the text information for the listed characters and their explanations ("chūmon/chūbun") to the input database for the *Ruiju Myōgishō* Kanchi-in manuscript text created in Step 3.

**Step 5:** Integrate the *Ruiju Myōgishō* Kanchi-in manuscript image database and the *Ruiju Myōgishō* Kanchi-in manuscript text database to form the *Ruiju Myōgishō* Kanchi-in manuscript database. Then, check and revise the text content using the newly published color facsimile edition of the *Ruiju Myōgishō* Kanchi-in manuscript (New Tenri Library Rare Books Series, Volumes 9-11). When checking the text content, also distinguish between compound word entries and variant character entries in the listed items, and distinguish between font annotations, pronunciation annotations, meaning annotations, and Japanese glosses in the explanations, and add this information.

**Step 6:** Publish the completed *Ruiju Myōgishō* Kanchi-in manuscript database on the internet and provide a search service.


## Online Information Provision

HDIC's online information provision consists of three parts: the main site, the search screen, and the text data. The main site is available at the following URL and summarizes the overview of the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC) (in Japanese, Chinese, and English), a list of research results, links to related sites, etc.
[https://hdic.jp](https://hdic.jp)

The search screen is available at the following URL, where you can use the HDIC Viewer to search the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC). The HDIC Viewer is maintained and managed by [Liu Guanwei](https://researchmap.jp/liuguanwei?lang=en) and allows searches not only on personal computers but also on smartphones.
[https://viewer.hdic.jp](https://viewer.hdic.jp)

We would like to express our gratitude to [Tomohiko Morioka](https://researchmap.jp/morioka-tomohiko?lang=en) for his technical support in maintaining and managing the hdic.jp website.

The text data is available at the following URL, where we publish the text files created by the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC). 

We preserve records of data revisions and provide the latest versions of the full-text databases for the Song Dynasty edition of the *Yupian*, the Kozanji manuscript of the *Tenrei Banshō Myōgi*, and the Tenji manuscript of the *Shinsen Jikyō*.

[https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC)


The *Ruiju Myōgishō* of the Kanchi-in manuscript underwent a specification change in March 2025, and the latest version of its full-text database is available at the following URL:

[https://github.com/shikeda/HDIC/tree/master/v1.2](https://github.com/shikeda/HDIC/tree/master/v1.2)

Please note that the above URLs are subject to change in the future.
Maintaining and managing the constructed data is a significant challenge.

## Acknowledgements

The construction and publication of the full-text database of the *Ruiju Myōgishō* of the Kanchi-in manuscript are being carried out with special permission from the authorities of Tenri Library, and we have also received exceptional consideration from Yagi Shoten, the publisher of the Tenri Library Rare Books Series. We hereby express our gratitude for this.

This work was supported by JSPS KAKENHI Grant Numbers 16H03422, 19H00526 and 23K17500.
