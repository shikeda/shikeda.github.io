---
title: 観智院本類聚名義抄
weight: 10
---

## 類聚名義抄

『類聚名義抄』は日本古辞書の雄編として名高い。 
書名の読み方は「るいじゅみょうぎしょう」である。
源順撰『倭名類聚抄』の「類聚」と、空海撰『篆隷万象名義』の
「名義」とを採用して書名としたとされる。


ここでは、まず『類聚名義抄』とその諸本の概要を述べる。
次に『類聚名義抄』の完本として唯一の伝本である
観智院本について、その項目の構造を解説し、
その後、観智院本の本文入力方法の詳細を述べる。

なお、ここでの解説は。
池田証壽・劉冠偉・鄭門鎬・張馨方・李媛「観智院本『類聚名義抄』全文テキストデータベース―その構築方法と掲出項目数等の計量―」(『訓点語と訓点資料』144、2020)を再構成したものである。

### 内容

- [概要](/docs/notes/krm-main/overview/)
- [公開データの概要](/docs/notes/krm-main/data-structure/)
- [項目データ構造](/docs/notes/krm-main/data-structure/)
    - [krm_main](/docs/notes/krm-main/contens/1_main/)
    - [krm_notes](/docs/notes/krm-main/contens/2_notes/)
    - [krm_wakun](/docs/notes/krm-main/contens/3_wakun/)
    - [krm_definitions](/docs/notes/krm-main/contens/4_definitions/)
    - [krm_pronunciations](/docs/notes/krm-main/contens/5_pronunciations/)
    - [krm_ndl](/docs/notes/krm-main/contens/6_ndl/)
- [項目データ入力](/docs/notes/krm-main/item-input/)
- [掲出字データ入力の詳細](/docs/notes/krm-main/headword-input/)
- [注文データ入力の詳細](/docs/notes/krm-main/def-input/)
    - [基本方針](/docs/notes/krm-main/def-input/1/)
    - [字体注](/docs/notes/krm-main/def-input/2/)
    - [音注](/docs/notes/krm-main/def-input/3/)
    - [義注](/docs/notes/krm-main/def-input/4/)
    - [和訓](/docs/notes/krm-main/def-input/5/)
    - [その他](/docs/notes/krm-main/def-input/6/)
- [注釈データ入力の詳細](/docs/notes/krm-main/notes-input/)
    - [基本方針](/docs/notes/krm-main/notes-input/1/)
    - [掲出字](/docs/notes/krm-main/notes-input/2/)
    - [字体注](/docs/notes/krm-main/notes-input/3/)
    - [音注](/docs/notes/krm-main/notes-input/4/)
    - [義注](/docs/notes/krm-main/notes-input/5/)
    - [和訓](/docs/notes/krm-main/notes-input/6/)


### データベース構築の工程

観智院本『類聚名義抄』は古写本であり、その掲出字は難字が極めて多いので、次の手順によりデータベース構築を進めた。

**第一段階**：複製本をスキャニングして掲出字を一文字毎に切り出して観智院本『類聚名義抄』画像データベースを作成する。掲出字の画像ファイルは掲出字の所在に対応する名前を付ける。この画像ファイル名は後に掲出字IDとして利用する。

**第二段階**：作成済みの『篆隷万象名義』データベースに正宗敦夫編『類聚名義抄 第二巻』（風間書房、1955年）に収録の「漢字索引」を参照してその所在情報を追記する。諸橋轍次編『大漢和辞典』検字番号の順に並べ替えた『篆隷万象名義』のデータに「漢字索引」の所在情報を入力し、その上で観智院本の所在順に並べ替えを行い、観智院本の本文と照合し、「漢字索引」にない観智院本の段数と字順を追加する。

**第三段階**：観智院本『類聚名義抄』画像データベース（第一段階で作成）に『篆隷万象名義』データベースに含まれる各種情報（『大漢和辞典』検字番号、Unicode番号、漢字、『篆隷万象名義』の所在情報）と第二段階で作成したそれに対応する観智院本『類聚名義抄』の所在情報）を取り込んで、入力用の観智院本『類聚名義抄』テキストデータベースを作成する。

**第四段階**：観智院本『類聚名義抄』の複製本(天理図書館善本叢書和書之部第32-34巻)および観智院本『類聚名義抄』画像データベースを参照しながら、第三段階で作成した入力用の観智院本『類聚名義抄』テキストデータベースに掲出字と注文のテキスト情報を追加する。

**第五段階**：観智院本『類聚名義抄』画像データベースと観智院本『類聚名義抄』テキストデータベースとを統合して観智院本『類聚名義抄』データベースとし、新たに刊行されたカラー版の観智院本『類聚名義抄』の複製本(新天理図書館善本叢書第9-11巻)で本文内容の点検と修正を行う。本文内容の点検に際しては、掲出項目での熟語項目と異体項目との区別、注文での字体注・音注・義注・和訓の区別も行って、それらの情報を追加する。


**第六段階**：完成した観智院本『類聚名義抄』データベースをインターネットで公開し、検索サービスを行う。

#### インターネットでの情報提供

HDICのインターネットでの情報提供は、メインサイト、検索画面及びテキストデータの三つからなる。
メインサイトは次のURLで、平安漢字字書総合データベース（HDIC）の概要（日本語、中国語、英語）と研究成果のリスト、関連サイトのリンク等をまとめている。

https://hdic.jp

検索画面は次のURLで、平安漢字字書総合データベース（HDIC）を検索するHDIC Viewerを利用できる。HDIC Viewerは劉冠偉が維持・管理を行っており、パソコンの他、スマートフォンでの検索を可能としている。


https://viewer.hdic.jp

hdic.jpのサイトの維持・管理には、守岡知彦氏による技術支援を受けていおり、感謝申し上げる。

テキストデータは次のURLで、平安漢字字書総合データベース（HDIC）で作成したテキストファイルを公開している。データの修正の記録を保存し、『篆隷万象名義』と『新撰字鏡』の全文テキストデータベースの最新版を提供している。

https://github.com/shikeda/HDIC

以上のURLは将来において変更の可能性が高い。構築したデータの維持と管理は大きな課題である。

### 謝辞

観智院本『類聚名義抄』全文テキストデータベースの構築と公開は、天理図書館当局から特別に御許可を賜り推進しているものであり、天理図書館善本叢書の版元である八木書店各位にも格別の御配慮を賜っている。ここに記して感謝の意を表する。


