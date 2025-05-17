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

The **`Phonetic Glosses`** in the Kanchi-in manuscript of the *Ruiju Myōgishō* (hereafter *Myōgishō*) include **`Fanqie spellings`** (反切), **`Similar sound notes`** (類音注, *ruion-chū*), and **`Kana glosses`** (仮名注, *kana-chū*). These are often accompanied by **`Tone marks (*shōten*)`**.
As a database for Sino-Japanese character pronunciations, the **"Database of Historical Sino-Japanese Readings"** (abbreviated as DHSJR), developed by Professor Katō Taitsuru and others, offers exceptionally rich content. Its specifications are also publicly available in detail. We are currently considering releasing data aligned with the DHSJR specifications.

The DHSJR defines a data structure with 23 column names.

To facilitate linkage with the *Myōgishō* data included in HDIC, it is necessary for HDIC to assign unique column names to its own data files and to establish Primary Keys and Foreign Keys for interoperability between HDIC's internal data files.

For this purpose, `pronunciation_id` (音注ID) has been set as the Primary Key, and `definition_seq_id` (注文ID) as the Foreign Key.

Since the *Myōgishō* features diverse formats for its **`Phonetic Glosses`**, a classification field named `annotation_format` (音注型) has been established to categorize them.

While DHSJR uses Japanese column names, HDIC employs English ones. Therefore, for data processing convenience within HDIC, English column names have been adopted.

The current draft, with English and Japanese explanations side-by-side, is as follows. The Japanese explanations are those stipulated by DHSJR. The English explanations are formulated to facilitate correspondence with HDIC. This is a provisional measure until official English explanations are released by DHSJR.

HDIC's original column names are indicated in **bold**.

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

The `material_location` is indicated in the format: K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit). For example, `K0201474` indicates an appearance in Volume 2, Page 14, Line 7, Segment 4.

Currently, this is under consideration in the case study "[Linkage with DHSJR](/docs/krm/08-case-studies/5-dhsjr/)," which should also be consulted.

