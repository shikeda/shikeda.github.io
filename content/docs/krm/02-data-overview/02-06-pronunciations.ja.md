---
title: "krm_pronunciations"
weight: 16
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# krm_pronunciations

## 概要とファイル形式

観智院本類聚名義抄（以下、名義抄）の音注は、
反切、類音注、仮名注があり、それらに声点が施されることも多い。
日本漢字音のデータベースとしては、加藤大鶴氏らによる
「資料横断的な漢字音・漢語音データベース」（略称 DHSJR）が非常に充実した
内容を持っている。またその仕様も詳細に公開されている。
DHSJR の仕様に合わせたデータ公開を検討中である。


DHSJR ではデータ列の構成として 23 のカラム名を設定している。

HDIC に収録の名義抄との連携をとるためには、HDIC 側で作成する
データファイルに固有のカラム名を付けて、HDIC 内のデータファイルと
連携するための主キー (Primary Key) と外部キー (Foreign Key) 
を設定することが必要になる。

主キーとして、音注ID (`pronunciation_id`)、
外部キーとして、注文ID (`definition_seq_id`) を設定した。

名義抄は音注の形式が多様なので、これを分類するために
音注型 (`annotation_format`)を設定した。

DHSJR は日本語のカラム名となっているが、HDIC では
英字を用いているので、HDIC 内のデータ処理の
都合上、英字を用いたカラム名を設定することとした。


## 各カラムの説明

現在の試案は以下のとおりである。英語の説明と日本語の説明を併記した。
日本語の説明は DHSJR が規定しているものである。英語の説明は、
HDIC との対応をとりやすいように説明したものである。
DHSJR から英語の説明が公表されるまでの暫定的な措置である。

HDIC独自のカラム名は**太字**とした。



| DHSJR (Japanese) | HDIC (English)            | Key         | English Explanation                                                                 | Japanese Explanation (from DHSJR)                     |
| :--------------- | :------------------------ | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| ID               | dhsjr\_id                  |             | DHSJR unique ID for each single **`Hanzi (Chinese character)`** (integrated data only)                                                                                                                                                                                                            | 単字ごとのユニークID（統合データのみ）                            |
| **音注ID** | **`pronunciation_id`** | Primary Key | ID for each **`Phonetic Gloss`**. This is derived from `definition_seq_id` by extracting only those elements where the type (from `definition_type_name` in `krm_notes`) is **`Phonetic Gloss`**. Suffixes 'b', 'c', 'd' are appended for variant forms.                                           | 音注ID。kr\_definition\_sequence\_idから、注文の種類が音注のものだけを取り出したもの。変異形を追加したものには末尾にxを付した。 *(User indicates 'x' is incorrect, and 'b,c,d' is correct for variants)* |
| **注文ID** | **`definition_seq_id`** | Foreign Key | An identifier for each component of the **`Definition (Original Glosses)`** or for the **`Headword`** itself within an **`Entry`**. It is formed by appending a sequential suffix (e.g., "\_00" for the **`Headword`**, "\_01", "\_02" for subsequent elements) to the corresponding `entry_id`. | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に\_01、\_02のように追加したもの。見出しには\_00を追加する。 |
| 資料番号         | material\_id               |             | Material ID                                                                                                                                                                                                                                                                                     | 資料ID                                                |
| 資料名           | material\_name             |             | Name of the material                                                                                                                                                                                                                                                                            | 資料の名称                                            |
| 資料内漢字番号   | material\_character\_index  |             | Sequential number of a **`Hanzi (Chinese character)`**'s appearance in the material                                                                                                                                                                                                            | 漢字の資料内出現順の通し番号                                |
| 資料内漢語番号   | material\_word\_index       |             | Sequential number of a Chinese word's appearance in the material                                                                                                                                                                                                                              | 漢語の資料内出現順の通し番号                                |
| 単字\_見出し      | character\_headword        |             | **`Headword`** column for **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字の見出し列                                  |
| 単字\_出現形      | character\_form            |             | **`Hanzi (Chinese characters)`** that have **`Phonetic Glosses`** | 音注が付された漢字                                        |
| 漢語\_見出し      | word\_headword             |             | **`Headword`** column of Chinese words containing **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字を含む漢語の見出し列                              |
| 漢語\_出現形      | word\_form                 |             | Chinese words containing **`Hanzi (Chinese characters)`** with **`Phonetic Glosses`** | 音注が付された漢字を含む漢語                                  |
| 漢語\_alphabet  | word\_alpha                |             | Entered when there is an alphabetic representation of the Chinese word                                                                                                                                                                                                                          | 欧文による漢語の表記がある場合に入力されている。                                |
| 語種             | word\_type                 |             | Indicates the word type when there are mixed-language words (e.g., hybrid Sino-Japanese words)                                                                                                                                                                                              | 混種語がある場合に、語種を示す。                                  |
| 漢語内位置       | word\_position             |             | Position of the single **`Hanzi (Chinese character)`** within the Chinese word                                                                                                                                                                                                                  | 漢語内での単字の位置                                      |
| 単字長           | character\_mora\_count      |             | Number of morae for the single **`Hanzi (Chinese character)`** | 単字の拍数                                            |
| 声点             | tone\_marks                |             | **`Tone marks`** for single **`Hanzi (Chinese characters)`**, indicating Four Tones (平上去入), Six Tones (平平軽上去入軽入), and voicing (清濁).                                                                                                                                                     | 単字に対する四声（平上去入）、六声（平平軽上去入軽入）及び清濁。                    |
| 声点型           | tone\_pattern              |             | Combination of **`Tone marks`** for Chinese words. **`Hanzi (Chinese characters)`** without **`Tone marks`** are represented by a full-width asterisk (＊).                                                                                                                                      | 漢語に対する声点の組合せ。声点がない単字については＊で表す。                        |
| 仮名注           | kana\_notes                |             | **`Kana glosses`** (仮名注) for **`Hanzi (Chinese characters)`**, including kana-based *fanqie*.                                                                                                                                                                                             | 仮名表記による字音注（仮名反切を含む）                                |
| 仮名型           | kana\_pattern              |             | Combination of **`Kana glosses`** for Chinese words. **`Hanzi (Chinese characters)`** without **`Kana glosses`** are represented by a full-width asterisk (＊).                                                                                                                                    | 漢語に対する仮名注の組合せ。仮名注がない単字については＊で表す。                      |
| 反切             | fanqie                    |             | **`Fanqie spellings`** (反切) for single **`Hanzi (Chinese characters)`**.                                                                                                                                                                                                                   | 単字に対する反切注                                        |
| 類音             | similar\_sound             |             | **`Similar sound notes`** (類音注) for single **`Hanzi (Chinese characters)`**.                                                                                                                                                                                                                | 単字に対する類音注                                        |
| **音注型** | **`annotation_format`** |             | Pattern of combined phonetic information (e.g., **`Kana glosses`**, **`Fanqie spellings`**, **`Similar sound notes`**, **`Tone marks`**).                                                                                                                                                         | 仮名注、反切、類音、声点などの複数の音注が組み合わさった形式のパターン。                  |
| 節博士           | fushi\_hakase              |             | **`Fushi-hakase notations`** (melodic or intonational markings) attached to musical materials such as *Shōmyō* (Buddhist chant).                                                                                                                                                              | 声明等音楽資料に付される博士譜など                                |
| その他           | other\_phonetic\_annotations|             | Other types of **`Phonetic Glosses`**.                                                                                                                                                                                                                                                           | その他の音注                                            |
| 出現位置         | material\_location         |             | Location of single **`Hanzi (Chinese characters)`** and Chinese words within the material.                                                                                                                                                                                                      | 資料内の単字・漢語の所在                                    |
| 備考             | remarks\_pronunciation     |             | Matters to be noted regarding these phonetic elements.                                                                                                                                                                                                                                          | 注記すべき事柄                                            |




出現位置（material_location）は、
K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）の形式で示す。
たとえばK0201474は巻2、14頁、7行、4段に出現することを表す。

現在は、事例研究の[DHSJRとの連携](/docs/krm/08-case-studies/5-dhsjr/)にて
検討しているので、そちらも参照されたい。




