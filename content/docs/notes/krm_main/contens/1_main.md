---
title: "krm_main"
weight: 11
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# krm_main


観智院本類聚名義抄（以下、名義抄）デーベースの中核となるファイルを解説する。
従来公開していたのは、KRM.tsvという名称のTSVファイルである。

掲出字、注文、巻、部首、風間書房版と天理善本叢書版の所在などに関する情報を
収録する。

2025年3月に、カラム名、声点の表示法の仕様を変更した。仕様変更後の
ファイルであることを明示するために、krm_main.tsvという名称にした。
これにはJSON形式も用意した。

新旧のカラム名を対照すれば次のようになる。


| New Column Name (v1.2.0) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| hanzi_id                 | KRID_sn                    |
| kazama_entry_location    | KR2ID                      |
| kazama_hanzi_location    | KRID                       |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original             |
| definition               | Def                        |
| -                        | Remarks                    |

Remarksは次のkrm_notesにまとめることとして、省略した。

次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.0) | English explanation           | Japanese explanation                    |
|--------------------------|-----------------------------|-------------------------------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F', followed by '_00'.               | Fで始まる5桁の数値に_00を加えた見出し項目ID。     |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'.           | Sで始まる5桁の数値からなる見出し漢字ID。         |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number.                                                              | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| kazama_hanzi_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 0 for single-character headwords, and 1, 2, ..., n for multiple-character headwords or entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. | K・巻数(2桁)・風間書房版ページ数(3桁)・行数(1桁)・段数(1桁)・字順(1桁)を示すID。掲出字が単字なら字順は0、複字なら1, 2, ..., n。一段に複数項目あれば単字でも1, 2, ..., n。            |
| tenri_location           | Location information from the Tenri edition (T, volume(volume letters), page(xxx), line(y), column(zz)). Where volume(volume letters) represents the volume letters, page(xxx) the page number, line(y) the line number, and column(zz) the column number.   | 八木書店版の掲出字ID。T・巻数（a/b/c）・ページ数（3桁数）・行数（1桁）・段数（1桁）・字順（1桁）を示す。最後の字順の示し方は掲出字IDの場合に同じとする。八木書店『天理図書館善本叢書』に基づく。        |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.            | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す。                              |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.                   | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す。       |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.           | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。            |
| hanzi_entry              | Corrected hanzi are principally in the Kangxi Dictionary form. Unicode simplified characters (common-use characters, popular variants) may also be retained. Multiple-kanji headwords are separated by / (full-width slash). The abbreviation symbol "｜" is represented by "ー" (long vowel mark), with the corresponding character in parentheses. | 校訂漢字は原則、康熙字典体。Unicodeの新字体（通用字体・俗字体）は残すことも可。複数漢字の見出しは／で区切る。省略符号「｜」はーで示し、（）に該当字。 |
| original_entry           | Headword close to original form. Errors as is. Non-Unicode variants: IDS or ■. Like hanzi_entry, "〇" if no original-glyph headword needed. | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の異体字はIDS/■で表記。hanzi_entryに準じ、原字形の掲出字が不要なら「〇」。    |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.    | 注文は、字体注、音注、義注、和訓、その他からなる。これらをスペース区切りで入力。原則として「康熙字典体」に含まれる字形を入力。                 |



