---
title: "krm_notes"
weight: 12
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# krm_notes

`KRM_definitions.tsv` ファイルに詳細な注釈情報を追加したファイル `krm_notes.tsv` を作成した。
これは、TSV形式とJSON形式で用意した。
2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字の KRM ではなく小文字の krm を用いて
`krm_notes.tsv` と `krm_notes.json` という名称とした。

`krm_notes.tsv` を新とし、`KRM_definitions.tsv` を旧として、両者のカラム名を対照すれば次のようになる。



| New Column Name (v1.2.6) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| entry_id                 | KRID_n	                    |
| definition_seq_id        | KRID_no                    |
| kazama_location          | KRID                      |
| tenri_location           | KR_Tenri_p                |
| volume_name              | KR_vol_name               |
| radical_name             | KR_radical                |
| volume_radical_index     | KR_vol_radical            |
| hanzi_entry              | Entry                      |
| original_entry           | Entry_original            |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |

前述したように、
`krm_notes` の内部は次のような入れ子構造となっている。

![ER_notes diagram](/images/krm_notes_er.drawio.png)

次に、カラム名の内容を日本語で説明する。

| New Column Name (v1.2.6) | Japanese Explanation                                                                                                                                                                                                                                                                                                                               |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| entry_id                 | Fで始まる5桁の数値に_00を加えた見出し項目ID。一部、追加した掲出項目にはb番号を付す。                                                                                                                                                                                                                                                                                                     |
| definition_seq_id        | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。                                                                                                                                                                                                                                                       |
| kazama_location          | K・巻数（2桁）・風間版頁数（3桁）・行数（1桁）、段数（1桁）、字順（1桁）を示すID。字順付与のルールの詳細は別に定める。                                                                                                                                                                                                                                                                                    |
| tenri_location           | T・巻数（a/b/c）・天理版頁数（3桁）・行数（1桁）・段数（1桁）・字順（1桁）を示す。字順付与のルールの詳細は別に定める。                                                                                                                                                                                                                                                                                   |
| volume_name              | 巻名。「仏上」「仏中」「仏下本」「仏下末」「法上」「法中」「法下」「僧上」「僧中」「僧下」の10 巻を示す                                                                                                                                                                                                                                                                                              |
| radical_name             | 部首名。「人、彳、辵」から「風、酉、雑」までの120部を示す                                                                                                                                                                                                                                                                                                                     |
| volume_radical_index     | 巻。v・巻数（1-10）#・部首番号（1-120）を示す。v1#1(第1帖第1)〜v10#120(第10帖第120)。第1帖(仏上)〜第10帖(僧下)。                                                                                                                                                                                                                                                                       |
| hanzi_entry              | 校訂漢字は原則、康熙字典体（Unicodeの新字体（通用字体・俗字体）を含む）を用いる。Unicodeに収録されていない漢字については、以下の方法で表現する。漢字の部品の組み合わせで表現可能な場合は、IDS（漢字構成記述文字列）で入力する。特定の漢字やその部品で、IDSまたは標準Unicodeで表現が困難な場合は、CHISEおよびGlyphWikiの実体参照方式に基づいた簡略表記（例：CDP-8C55, koseki-00001）を用いる。上記のいずれの方法でも表現できない文字や、原典で判読不能な文字（虫損等）は、「■」（黒い四角）で入力する。複数漢字の見出しは「／」（全角スラッシュ）で区切る。省略符号「｜」は「ー」（長音符）で示し、全角括弧（）内に該当字を付記する。 |
| original_entry           | 原字形に準拠した見出し字。誤字はそのまま。Unicode外の漢字の表現はhanzi_entryに準じる。原字形の掲出字が不要なら「〇」。                                                                                                                                                                                                                                                                               |
| definition_elements      | 注文の全文から、字体注、音注、意義注、和訓、その他の５種に区分し、それぞれの要素を一つずつ抜き出したもの。                                                                                                                                                                                                                                                                                              |
| definition_type_code     | 注文の種類を分類した3桁の数値。                                                                                                                                                                                                                                                                                                                                   |
| definition_type_name     | 注文の種類を字体注、音注、意義注、和訓、その他の５種に区分して、そのいずれに該当するかを示したもの。                                                                                                                                                                                                                                                                                                 |
| remarks                  | 編集者による追加の文脈や情報を提供する注記                                                                                                                                                                                                                                                                                                                              |
