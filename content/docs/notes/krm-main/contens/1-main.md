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

| New Column Name (v1.2.5) | Old Column Name (v1.1.347) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n                     |
| hanzi_id                 | KRID_sn                    |
| -                        | KR2ID                      |
| kazama_location          | KRID                       |
| tenri_location           | KR_Tenri_p                 |
| volume_name              | KR_vol_name                |
| radical_name             | KR_radical                 |
| volume_radical_index     | KR_vol_radical             |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original             |
| definition               | Def                        |
| -                        | Remarks                    |

KR2IDは省略し、kazama_locationをKRIDに対応させた。

Remarksは次のkrm_notesにまとめることとして、省略した。


次に、カラム名の内容を英語と日本語で説明する。ここではv1.2.5の内容を
記載する。





| New Column Name (v1.2.5) | English Explanation           | Japanese Explanation                    |
|--------------------------|-----------------------------|-------------------------------------------|
| entry_id                 | A heading item ID formed by a 5-digit numeric ID starting with 'F'.          | Fで始まる5桁の数値からなる見出し項目ID。     |
| hanzi_id                 | A heading Hanzi ID consisting of a 5-digit numeric ID starting with 'S'.           | Sで始まる5桁の数値からなる見出し漢字ID。         |
| kazama_location    | An ID indicating K + Volume (2 digits) + Kazama Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  | K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）、字順（1桁）を示すID。字順付与のルールの詳細は別に定める。    |
| tenri_location           | An ID indicating T + Volume (a/b/c) + Tenri Edition Page (3 digits) + Line (1 digit) + Segment (1 digit) + 字順 (1 digit). Details of the rules for assigning 字順 are defined separately.  |T・巻数（a/b/c）・天理版頁数（3桁）・行数（1桁）・段数（1桁）・字順（1桁）を示す。字順付与のルールの詳細は別に定める。     |
| volume_name              | Name of the volume, consisting of 10 volumes: 仏上, 仏中, 仏末本, 仏末下, 法上, 法中, 法下, 僧上, 僧中, and 僧下.            | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す。                              |
| radical_name             | Hanzi name of the radical, consisting of 160 radicals ranging from 人 to 雑, used to classify Hanzi characters.                   | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す。       |
| volume_radical_index     | Volume and radical number, ranging from v1#1 to v10#120, indicating the location of the entry within the text.           | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。            |
| hanzi_entry              | The collated headword characters principally use Kangxi Dictionary form, including Unicode simplified characters (common-use forms, popular variants). For characters not included in Unicode, they are represented by the following methods: If representable by combining kanji components, input using IDS (Ideographic Description Sequence). For specific kanji or their components, if representation by IDS or standard Unicode is difficult, use simplified notations based on the entity reference systems of CHISE and GlyphWiki (e.g., CDP-8C55, koseki-00001). Characters not representable by any of the above methods, or characters unreadable in the original text (worm-eaten, etc.), are input as '■' (black square). Headwords consisting of multiple kanji are separated by '／' (full-width slash). The abbreviation symbol '｜' is indicated by 'ー' (long vowel mark), and the corresponding character is appended in full-width parentheses (). | 校訂漢字は原則、康熙字典体（Unicodeの新字体（通用字体・俗字体）を含む）を用いる。Unicodeに収録されていない漢字については、以下の方法で表現する。漢字の部品の組み合わせで表現可能な場合は、IDS（漢字構成記述文字列）で入力する。特定の漢字やその部品で、IDSまたは標準Unicodeで表現が困難な場合は、CHISEおよびGlyphWikiの実体参照方式に基づいた簡略表記（例：CDP-8C55, koseki-00001）を用いる。上記のいずれの方法でも表現できない文字や、原典で判読不能な文字（虫損等）は、「■」（黒い四角）で入力する。複数漢字の見出しは「／」（全角スラッシュ）で区切る。省略符号「｜」は「ー」（長音符）で示し、全角括弧（）内に該当字を付記する。 |
| original_entry           | Headword based on the original character form. Errors are left as is. The representation of kanji outside Unicode follows the rules for hanzi_entry. If the original-form headword is not needed, '〇' is used. | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の漢字の表現はhanzi_entryに準じる。原字形の掲出字が不要なら「〇」。  |
| definition               | Includes glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and other relevant notes, separated by spaces. As a general rule, character forms included in the "Kangxi Dictionary style" should be used.    | 注文は、字体注、音注、義注、和訓、その他からなる。これらをスペース区切りで入力。原則として「康熙字典体」に含まれる字形を入力。                 |



