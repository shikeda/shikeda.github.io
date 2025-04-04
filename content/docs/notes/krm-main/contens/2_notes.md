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


KRM_def.tsvファイルに詳細な注釈情報を追加したファイルkrm_notes.tsvを作成した。
これは、TSV形式とJSON形式で用意した。
2025年3月の仕様変更後のファイル名であることを明示的に示すため、
大文字のKRMではなく小文字のkrmを用いて
krm_notes.tsvとkrm_notes.jsonという名称とした。

krm_notes.tsvを新とし、KRM_definitions.tsvを旧として、両者のカラム名を対照すれば次のようになる。



| New Column Name (v1.2.0) | Old Column Name (v1.1.55) |
|--------------------------|----------------------------|
| definition_seq_id        | KRID_no                    |
| kazama_entry_location    | KR2ID                      |
| hanzi_entry              | Entry                      |
| definition_elements      | Def                        |
| definition_type_code     | Def_code                   |
| definition_type_name     | Def_name                   |
| remarks_definition       | Remarks                    |


次に、カラム名の内容を英語と日本語で説明する。

| New Column Name (v1.2.0) | English explanation          | Japanese explanation             |
|--------------------------|-----------------------------------|----------------|
| definition_seq_id        | 5-digit numeric ID starting with 'F', sequentially assigned to heading entries. Definition components under each heading are ordered based on their appearance, and order indicators like _01, _02, etc., are appended accordingly. The heading itself is appended with _00.                      | 連番で与えられるFで始まる5桁の見出しの数値IDに加えて、見出しの下に記される注文の各要素を出現順に区分し、出現の順番に_01、_02のように追加したもの。見出しには_00を追加する。 |
| kazama_entry_location    | ID including location information (Kazama edition: K, Book(volume), page(xxx), line(y), column(zz)), ranked 1, 2, ..., n for multiple entries in a column. Where Book(volume) represents the volume number, page(xxx) the page number, line(y) the line number, and column(zz) the column number. | 位置情報（風間版：K、冊子（巻）、ページ（xxx）、行（y）、列（zz））を含むID。列に複数のエントリがある場合は、1、2、...、n の順位になる。                 |
| hanzi_entry              | Collated Hanzi characters, standardized to the Kangxi dictionary form, including Unicode-representable variant forms.                | 原文の漢字を校訂したもの。康熙字典体とするのを原則としたが、Unicodeで入力できる新字体（通用字体、俗字体）を残すこともある。                            |
| definition_elements      | Extracted components from the full definition, classified into 5 categories: glyph annotations, pronunciation annotations, meaning annotations, Japanese readings (wakun), and others, one component per entry.                 | 注文の全文から、字体注、音注、意義注、和訓、その他の５種に区分し、それぞれの要素を一つずつ抜き出したもの。         |
| definition_type_code     | 3-digit numeric code representing the definition type.         | 注文の種類を分類した3桁の数値。               |
| definition_type_name     | Indicates which of the following five categories the definition type belongs to: glyph annotation, pronunciation annotation, meaning annotation, wakun, and others.                                                                                                                               | 注文の種類を字体注、音注、意義注、和訓、その他の５種に区分して、そのいずれに該当するかをしめしたもの。                                          |
| remarks_definition       | Editor's notes providing additional context or information.           | 編集者による追加の文脈や情報を提供する注記。                                                                       |
