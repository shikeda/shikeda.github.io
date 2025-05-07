---
title: "krm_pronunciations"
weight: 15
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# krm_pronunciations


観智院本類聚名義抄（以下、名義抄）の音注は、
反切、類音注、仮名注があり、それらに声点が施されることも多い。
日本漢字音のデータベースとしては、加藤大鶴氏らによる
「資料横断的な漢字音・漢語音データベース」（略称DHSJR）が非常に充実した
内容を持っている。またその仕様も詳細に公開されている。
DHSJRの仕様に合わせたデータ公開を検討中である。


DHSJRではデータ列の構成として23のカラム名を設定している。

HDICに収録の名義抄との連携をとるためには、HDIC側で作成する
データファイルに固有のカラム名を付けて、HDIC内のデータファイルと
連携するための主キー (Primary Key) と外部キー (Foreign Key) 
を設定することが必要になる。

主キーとして、音注ID (pronunciation_id)、
外部キーとして、注文ID (definition_seq_id) を設定した。

名義抄は音注の形式が多様なので、これを分類するために
音注型 (annotation_format)を設定した。

DHSJRは日本語のカラム名となっているが、HDICでは
英字を用いているので、HDIC内のデータ処理の
都合上、英字を用いたカラム名を設定することとした。

現在の試案は以下のとおりである。英語の説明と日本語の説明を併記した。
日本語の説明はDHSJRが規定しているものである。英語の説明は、
HDICとの対応をとりやすいように説明したものである。
DHSJRから英語の説明が公表されるまでの暫定的な措置である。

HDIC独自のカラム名は**太字**とした。

| DHSJR  | HDIC | Key         | English Explanation     | Japanese Explanation         |
|-------------|----------------------------|-------------|------|----------------------|
| ID        | dhsjr_id      |             | DHSJR unique ID for each single character (integrated data only)     | 単字ごとのユニークID（統合データのみ）    |
| **音注ID**        | **pronunciation_id**     | Primary Key | Pronunciation annotation ID, extracted from definition_sequence_id, containing only entries where the type of order is pronunciation annotation. Variant forms are appended with 'b', 'c'.    | 音注ID。kr_definition_sequence_idから、注文の種類が音注のものだけを取り出したもの。変異形を追加したものには末尾にxを付した。 |
| **注文ID**        | **definition_seq_id**     | Foreign Key | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00. | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。 |
| 資料番号        | material_id      |             | Material ID  | 資料ID       |
| 資料名         | material_name      |             | Name of the material      | 資料の名称  |
| 資料内漢字番号     | material_charcter_index   |             | Sequential number of character appearance in the material    | 漢字の資料内出現順の通し番号      |
| 資料内漢語番号     | material_word_index        |             | Sequential number of word appearance in the material     | 漢語の資料内出現順の通し番号       |
| 単字_見出し      | character_headword         |             | Headword column of characters with phonetic annotations    | 音注が付された漢字の見出し列   |
| 単字_出現形      | character_form      |             | Characters with phonetic annotations    | 音注が付された漢字            |
| 漢語_見出し      | word_headword        |             | Headword column of words containing characters with phonetic annotations   | 音注が付された漢字を含む漢語の見出し列      |
| 漢語_出現形      | word_form      |             |  Words containing characters with phonetic annotations    | 音注が付された漢字を含む漢語         |
| 漢語_alphabet | word_alpha                 |             | Entered when there is an alphabetic representation of the word      | 欧文による漢語の表記がある場合に入力されている。                                                                     |
| 語種          | word_type                  |             |  Indicates the word type when there are mixed-language words    | 混種語がある場合に、語種を示す。    |
| 漢語内位置       | word_position              |             | Position of the single character within the word   | 漢語内での単字の位置      |
| 単字長         | character_mora_count       |             | Number of morae for the single character     | 単字の拍数     |
| 声点          | tone_marks   |             | Four tones (even, rising, departing, entering), six tones (even-light, rising, departing, entering-light) and voicing for single characters     | 単字に対する四声（平上去入）、六声（平平軽上去入軽入）及び清濁。     |
| 声点型         | tone_pattern               |             | Combination of tonal marks for words. Characters without tonal marks are represented by *       | 漢語に対する声点の組合せ。声点がない単字については＊で表す。    |
| 仮名注         | kana_notes   |             | Phonetic annotation in kana notation (including kana fanqie)     | 仮名表記による字音注（仮名反切を含む）                                                                          |
| 仮名型         | kana_pattern               |             | Combination of kana annotations for words. Characters without kana annotations are represented by *.         | 漢語に対する仮名注の組合せ。仮名注がない単字については＊で表す。      |
| 反切          | fanqie                     |             | Fanqie annotation for single characters     | 単字に対する反切注      |
| 類音          | similar_sound              |             | Similar sound annotation for single characters    | 単字に対する類音注         |
| **音注型**         | **annotation_format**          |             | Pattern of combined phonetic annotations (e.g., kana, fanqie, similar sound, tone marks).  | 仮名注、反切、類音、声点などの複数の音注が組み合わさった形式のパターン。    |
| 節博士         | fushi_hakase               |             | Hakase notation attached to musical materials such as Shōmyō   | 声明等音楽資料に付される博士譜など        |
| その他         | other_phonetic_annotations |             | Other phonetic annotations      | その他の音注                                                                                       |
| 出現位置        | material_location          | Foreign Key | Location of single characters and words within the material       | 資料内の単字・漢語の所在                                                                                 |
| 備考          | remarks_pronunciation      |             | Matters to be noted         | 注記すべき事柄           |

現在は、事例研究の[DHSJRとの連携](/docs/notes/krm-main/case-study/5/)にて
検討しているので、そちらも参照されたい。



