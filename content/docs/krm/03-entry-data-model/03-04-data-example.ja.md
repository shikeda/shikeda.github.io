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

### 項目データファイルの例

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
この和訓のすぐあとに「切歟」とあり、
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

カラム名とその内容説明は日本語と英語によって行った。

| Column Name          | English Explanation       | Japanese Explanation          |
|----------------------|---------------------------------|--------------|
| entry_id             | A heading **`Entry`** ID consisting of a 5-digit numeric ID starting with 'F'. For some added entry items, a 'b' suffix is appended.    | Fで始まる5桁の数値からなる見出し項目ID。一部、追加した掲出項目にはb番号を付す。   |
| hanzi_id             | A heading **`Hanzi (Chinese character)`** ID consisting of a 5-digit numeric ID starting with 'S'. For some added entry items, a 'b' suffix is appended.  | Sで始まる5桁の数値からなる見出し漢字ID。一部、追加した掲出字にはb番号を付す。      |
| kazama_location      | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.       | K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）、字順（1桁）を示すID。字順付与のルールの詳細は別に定める。   |
| tenri_location       | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + Character order (字順, *jijun*) (1 digit). Details of the rules for assigning Character order are defined separately.    | T・巻数（a/b/c）・天理版頁数（3桁）・行数（1桁）・段数（1桁）・字順（1桁）を示す。字順付与のルールの詳細は別に定める。  |
| volume_name          | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏下本, 仏下末, 法上, 法中, 法下, 僧上, 僧中, and 僧下.    | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す。   |
| radical_name         | Name of the radical, consisting of 120 radicals ranging from 人 to 雑, used to classify **`Hanzi (Chinese characters)`**.   | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す。   |
| volume_radical_index | Volume and radical number, ranging from v1#1 (Volume 1, Radical 1) to v10#120 (Volume 10, Radical 120), indicating the location of the **`Entry`** within the text. (Corresponds to 第1帖仏上 to 第10帖僧下).     | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。  |
| hanzi_entry          | The collated **`Headword`** (校訂漢字) principally uses Kangxi Dictionary form, including Unicode simplified **Chinese characters** (common-use forms, popular variants). For **Chinese characters** not included in Unicode, they are represented by the following methods: If representable by combining **Chinese character** components, input using IDS (Ideographic Description Sequence). For specific **Chinese characters** or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). **Chinese characters** not representable by any of the above methods, or characters unreadable in the original text (due to damage such as wormholes, etc.), are input as '■' (black square). **`Headwords`** consisting of multiple **Chinese characters** are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). | 校訂漢字は原則、康熙字典体（Unicodeの新字体（通用字体・俗字体）を含む）を用いる。Unicodeに収録されていない漢字については、以下の方法で表現する。漢字の部品の組み合わせで表現可能な場合は、IDS（漢字構成記述文字列）で入力する。特定の漢字やその部品で、IDSまたは標準Unicodeで表現が困難な場合は、CHISEおよびGlyphWikiの実体参照方式に基づいた簡略表記（例：CDP-8C55, koseki-00001）を用いる。上記のいずれの方法でも表現できない文字や、原典で判読不能な文字（虫損等）は、「■」（黒い四角）で入力する。複数漢字の見出しは「／」（全角スラッシュ）で区切る。省略符号「｜」は「ー」（長音符）で示し、全角括弧（）内に該当字を付記する。 |
| original_entry       | **`Headword`** based on the original character form. Typographical errors in the original are preserved. The representation of **Chinese characters** outside Unicode follows the rules for `hanzi_entry`. If the original-form **`Headword`** is not needed, '〇' is used.   | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の漢字の表現はhanzi_entryに準じる。原字形の掲出字が不要なら「〇」。  |
| definition           | The content of this `definition` column represents the **`Definition (Original Glosses)`**. It includes **`Notes on Character Form`**, **`Phonetic Glosses`**, **`Semantic Glosses in Chinese`**, **`Japanese Native Readings (*wakun*)`**, and **Other** relevant information, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.   | 注文は、字体注、音注、義注、和訓、その他からなる。これらをスペース区切りで入力。原則として「康熙字典体」に含まれる字形を入力。    |


## GitHub を利用した公開・更新

