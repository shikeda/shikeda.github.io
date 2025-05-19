---
title: "項目データファイルの公開・更新"
weight: 7
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# 項目データファイルの公開・更新

項目データファイルの内容と具体例の提示、GitHub を利用した公開・更新の方法に触れる。

### 項目データファイルの例

公開のデータファイルのリストは[公開データの概要](/docs/krm/02-data-overview/)に一覧している。
ここでは項目データファイルの基本データとなる`krm_main` を例にその内容を解説する。


[項目データ構造](./03-01-data-structure/)において
具体例として示した、「加復」と「ー之」、「助」とその異体字、「功」の三つの 項目を例にしてみよう。

TSV形式のファイルを次に示す。
一番左に説明のためのNoを追加している。

```text
No  entry_id	hanzi_id	kazama_location	tenri_location	volume_name	radical_name	volume_radical_index	hanzi_entry	original_entry	definition
1	F25133	S31605	K08084810	Tc090810	僧上	力	v8#83	功	〇	音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟
2	F25062	S31507	K08081810	Tc087810	僧上	力	v8#83	助	⿰目力	鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）
3	F25063	S31508	K08081821	Tc087821	僧上	力	v8#83	𦔳／助	■／〇	今正
4	F25121	S31590	K08084411	Tc090411	僧上	力	v8#83	加／復	〇／〇	シカノミナラス
5	F25122	S31592	K08084421	Tc090421	僧上	力	v8#83	ー（加）／之	〇／〇	同
```
1の「功」は単字形式の例である。
この例は、音注に複数の声点、仮名字音、鼻音記号が見えており、複雑な内容を持つ。
声点の圏点と星点の区別、声点と仮名字音の朱墨の別は省略する。
漢字意味注の「續也」は「績也」の誤写。
和訓「タシカニ」は「功」字の字義に対応せず不審である。
この和訓のすぐあとに「𭃄歟」とあり、
「切」字に「タシカニ」の和訓がある。
「功」には異体字「㓛」があり、これは「切」およびその異体字「𭃄」に近似した字形である。
「切」は掲出字「功」の形近字であり、その混同による和訓と考えられる。
しかし、注文内容を改変することなく「𭃄歟」という注記を加えたものである。
「𭃄歟」のように「歟」を添えた注記を名義抄の撰者または書写者による「案語」として扱う。

2の「助」は単字形式によって音注と和訓を示す。
次の3の「𦔳／助」は複字形式であり、字体注によって異体字を示す。
「／」は複字形式を示す区切りの符号であり、その「／」の数から
、掲出字の字数を計算できる。

4の「加／復」は熟語の和訓を示しており、5の「ー（加）／之」は同訓であることを示す。「ー」は
前項の「加」を簡略に表示する符号である。

次は同じ内容を JSON 形式で示したものである。
見やすくなるがその分のデータ量が増加するので、VS Code のような高機能のエディターを使っても
読み込みに多少の時間を要する。

```
[
    {
        "entry_id": "F25133",
        "hanzi_id": "S31605",
        "kazama_location": "K08084810",
        "tenri_location": "Tc090810",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "功",
        "original_entry": "〇",
        "definition": "音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟"
    },
    {
        "entry_id": "F25062",
        "hanzi_id": "S31507",
        "kazama_location": "K08081810",
        "tenri_location": "Tc087810",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "助",
        "original_entry": "⿰目力",
        "definition": "鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）"
    },
    {
        "entry_id": "F25063",
        "hanzi_id": "S31508",
        "kazama_location": "K08081821",
        "tenri_location": "Tc087821",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "𦔳／助",
        "original_entry": "■／〇",
        "definition": "今正"
    },
    {
        "entry_id": "F25121",
        "hanzi_id": "S31590",
        "kazama_location": "K08084411",
        "tenri_location": "Tc090411",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "加／復",
        "original_entry": "〇／〇",
        "definition": "シカノミナラス"
    },
    {
        "entry_id": "F25122",
        "hanzi_id": "S31592",
        "kazama_location": "K08084421",
        "tenri_location": "Tc090421",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "ー（加）／之",
        "original_entry": "〇／〇",
        "definition": "同"
    },
]
```

## 項目データファイルのカラム（ヘッダ）の記述内容

名義抄の項目のデータはkrm_main.tsvおよびkrm_main.jsonに格納される。これが基本データとなる。

カラム名とその内容説明の詳細は、[公開データの概要](../02-data-overview/)を参照されたい。

## GitHub を利用した公開・更新

平安時代漢字字書総合データベース（Integrated Database of Hanzi Dictionaries in Early Japan、略称HDIC）は、2015年10月以来、現在に至るまでGitHubを通して公開されている。アドレスは
[https://github.com/shikeda](https://github.com/shikeda)である。

収録する漢字字書の名称とその全文テキストデータベースの初版公開の年月日をまとめれば次のとおり。

- 宋本玉篇（*Songben Yupian*、略称SYP）　初版公開日：2015年10月20日
- 篆隷万象名義（Kosan-ji manuscript *Tenrei Banshō Meigi*、略称KTB）　初版公開日：2016年9月1日
- 新撰字鏡（Tenji manuscript *Shinsen Jikyō*、略称TSJ）　初版公開日：2018年6月28日
- 類聚名義抄（Kanchi-in manuscript *Ruiju Myōgisho*、略称KRM）　初版公開日：2022年3月11日

GitHub とは何かを説明し、このシステムを通して研究データを公開する意義をまとめれば次のようになる。

GitHubは、ソフトウェアのソースコードを管理・公開するためのプラットフォームとして広く使われているが、近年では人文系を含むさまざまな研究分野において、研究データの共有や公開にも活用されている。GitHubの基盤には「Git」というバージョン管理システムがあり、過去の編集履歴をすべて記録し、変更の経緯を明確に残すことができる。これにより、誰が、いつ、どのような変更を行ったのかを追跡でき、研究データの透明性や再現性を高めることが可能となる。

さらに、GitHub上では複数人での共同編集が容易であり、プルリクエストやイシューといった仕組みを用いることで、他の研究者との対話や査読的なやりとりも記録できる。また、Markdown記法による文書作成や、ファイル単位での修正履歴の閲覧機能などにより、プログラムを書かない人文系研究者でも比較的容易に扱える点も魅力の一つである。

GitHubにデータを置く意義は、単なる保存だけにとどまらない。研究の途中経過を段階的に公開し、外部からのフィードバックを受けながら改善していくという「オープンサイエンス」的な実践も可能となる。特に、資料に基づく漢字音や漢語音のデータ、翻刻文、辞書的情報といった構造化された人文学データとの親和性が高く、実際に多くの事例が存在する。

また、GitHub上のデータは、Zenodoという研究データリポジトリと連携することで、正式なDOI（Digital Object Identifier）を付与して学術的に安定した形で公開することができる。たとえば「資料横断的な漢字音・漢語音データベース（DHSJR）」では、GitHub上で構築されたデータがZenodoに登録され、DOIを通じて国際的な引用と再利用が可能な形で公開されている。このように、GitHubは人文学におけるデジタル資料の長期的な共有と利活用の基盤として、大きな役割を果たしつつある。


