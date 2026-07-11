---
title: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(7)"
date: 2026-07-11T00:00:00+09:00
draft: false
tags:
  - 廣韻
  - 集韻
  - 音韻学
  - 漢字データベース
  - Python
  - 宋本廣韻
  - HDIC
  - DHSJR
  - KRM
  - データ統合
  - 異体字
  - Unicode
categories:
  - デジタル人文学
  - 日本古辞書
summary: "前回(6)は廣韻側の字頭差分やCJKVI variantsから異体字JSONを作りました。今回(7)は、廣韻とは別の宋代韻書である集韻（Jiyun）のOCRテキストを取得・構造化し、その見出し字列記から異体字ペアを抽出して --itaiji-json に加えた結果をまとめます。"
---

## はじめに

前回の
[宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(6)](/posts/sbgy-phonological-data-linking-to-hdic-and-dhsjr-6/)
では、`廣韻.csv` と `sbgy.xml` の字頭差分や、CJKVI variants系データから異体字JSONを作成し、
`gy_dhsjr_link.py` の `--itaiji-json` に指定することで `unmatched` を大きく減らせることを確認しました。
一方で、`checked_unmatched_chars_in_cjkvi_variant.json` のような広い対応表は、
対応範囲が広い分だけ、採用の妥当性を個別に確認する必要があることも指摘しました。

今回は、これらとは系統の異なる異体字情報源を試します。廣韻ではなく、
同じ宋代に編まれたもう一つの韻書、**集韻（Jiyun）**です。
集韻は廣韻よりも収録字数が多く、1つの小韻（同音字群）に複数の字体をまとめて
列記する記述スタイルを持っています。この列記そのものが異体字情報として使えるのではないか、
というのが今回の出発点です。

なお、`--itaiji-json` に指定できるJSONファイルの一覧は
[`--itaiji-json` 用JSONファイル目録（更新版）](/posts/itaiji-json-inventory-2/)
として別途整理しました。今回作成した `jy_itaiji_pairs.json` もそちらに追記しています。

## 集韻データの入手

集韻のテキストも、廣韻と同じくChinese Text Project（ctext.org）が公開している
OCRテキストを利用します。欽定四庫全書本の該当巻を、巻ごとに保存HTMLとして取得しました。`~/codex/jy/`は今回の作業ディレクトリです。適宜各自の環境にあわせて修正してください。

```
~/codex/jy/ctext/jiyun_vol1_ctextext.html
~/codex/jy/ctext/jiyun_vol2_ctextext.html
...
~/codex/jy/ctext/jiyun_vol10_ctextext.html
```

集韻は全10巻構成で、`~/codex/jy/ctext/README.md` に出典情報を残しておくとよいでしょう。

```text
https://ctext.org/searchbooks.pl?if=en&searchu=%E9%9B%86%E9%9F%BB

集韻*（宋）丁度
Wiki section - community edited text. This resource was created automatically using OCR and contains uncorrected errors. This resour
ce has been partially corrected.
 《欽定四庫全書》本

https://ctext.org/wiki.pl?if=en&res=937344

《集韻 Jiyun》

Author  丁度
Dynasty Song
Base text
《欽定四庫全書》本
Data item       ctext:835462
```

OCRテキストであるため誤字が含まれている前提で扱います。


私は、上海図書館収蔵述古堂影宋鈔本影印の(宋) 丁度等編『集韻 : 附索引』（上海古籍出版社 1985）を適宜利用して、原文の確認を行っています。

なお、趙振鐸著『集韻校本(全3册)』（上海古籍出版社、2012年）も出ていますが、未見です。



## HTML構造化パイプライン



保存した集韻のHTMLを構造化TSV/JSONに変換する2段階のパイプラインがあります。


```bash
cd ~/codex/jy/scripts
python3 01_extract_raw.py --all   # HTML → vol{N}/jiyun_juan{N}_raw.json
python3 02_build_tables.py --all  # raw.json → groups.tsv / chars.tsv / toc.tsv
```

[`01_extract_raw.py`](/downloads/scripts/jy/01_extract_raw.py) は、ctext.orgの保存ページ内で行数が最大のテーブルを本文とみなし、
各行の `td.ctext` を子ノード順に走査して `('char'|'note'|'anchor', text)` の
セグメント列に変換します。集韻データには、僻字画像（`<img alt="ctextchar:NNNN">`）が
見出し字位置だけでなく、注釈文（`inlinecomment`）の**途中**にも埋め込まれることがあるため、
再帰的なテキスト抽出でこれを拾う実装になっています。

[`02_build_tables.py`](/downloads/scripts/jy/02_build_tables.py) は、セクション見出しを次の3種に分類します。

- `front_matter`: 提要・韻例など、巻頭の前付け
- `toc`: 「平聲一」のような声調巻の見出しで、韻目索引（韻名・反切・独用/通用）が本文
- `entry`: 「一東」のような韻見出しで、実際の辞書本文

さらに、`entry` カテゴリ内では、見出し字ランが `〇` から始まる行を新しい小韻
（同音・異体字グループ）の開始とみなし、`(声調, 韻番号, 韻名)` ごとに
`xiaoyun_seq`（小韻通し番号）を振ります。末尾の注釈にある「文N」という記述から、
`declared_count`（宣言字数）も取り出します。

出力は巻ごとに次の4種のTSV/JSONです。

| ファイル | 内容 |
|---|---|
| `jiyun_juan{N}_raw.json` | 行単位のセグメント列 |
| `jiyun_juan{N}_groups.tsv` | 見出し字ラン＋直後の注1件＝1行 |
| `jiyun_juan{N}_chars.tsv` | 1文字＝1行に展開 |
| `jiyun_juan{N}_toc.tsv` | 巻頭韻目索引 |

## 見出し字列記は異体字集合である

集韻の記述には、次のような行があります（上聲《十二蠏》）。

```text
〇矖所蟹切視也文十二灑洒汛灑也或作洒汛躧徐行也𩎉𩌦𩋀履也或作𩌦亦省纚縰斯韜髪也或作縰斯𥸗瑟也
```

`groups.tsv` の1行1グループという構造に沿って読み解くと、これは次の6グループに分かれます。

| headword_run | note |
|---|---|
| 〇矖 | 所蟹切視也文十二 |
| 灑洒汛 | 灑也或作洒汛 |
| 躧 | 徐行也 |
| 𩎉𩌦𩋀 | 履也或作𩌦亦省 |
| 纚縰斯 | 韜髪也或作縰斯 |
| 𥸗 | 瑟也 |

`灑洒汛`・`𩎉𩌦𩋀`・`纚縰斯` の3グループは、headword_run に複数の文字が
連続して並んでいます。集韻は、1つの語に複数の字体がある場合、定義を字ごとに
繰り返さず、字体をまとめて並べてから語釈を1つだけ付けるという記述方式を取っているため、
これは「同一語の異体字集合」を意味します。実際、note にも「或作」（あるいは〜とも作る）
という異体字を示す言い回しが伴っています。

そこで、「`〇` マーカーを除いた headword_run の文字数が2以上」という条件で
`groups.tsv` を走査したところ、全10巻・`entry` 種別 40,620グループのうち
**9,308グループ**が該当しました。付随する note を無作為に確認したところ、
「或作」「亦作」「籒作」「隷作」「（古典名）作」など、ほぼ全件が異体字・字体差を
示す言い回しを伴っており、この抽出方針の信頼性を確認できました。

## ペア化の形式: 先頭字アンカーではなく全組み合わせ

`gy_dhsjr_link.py` の `build_itaiji_map()` は、JSON中の各 `{c1, c2}` ペアを
**独立した2字グループ**として処理します。ペアの中に廣韻収録字があれば、
もう一方をそれに正規化する、という仕組みで、複数のペアをまたいだ推移的な合流は
行いません。

これは、3字以上の異体字集合を「先頭字とだけペアにする」形式（`{c1: 残りの字, c2: 先頭字}`
をすべての残りの字について作る）で出力すると、**先頭字が廣韻未収録で、
2番目以降のどれかが廣韻収録字という場合に、もう一方の字が救えない**ことを意味します。

`廣韻.csv` と突き合わせて実際に確認したところ、3字以上のグループは2,641件あり、

| 方式 | ペア数 | 廣韻に正規化できた字数 |
|---|---:|---:|
| 先頭字アンカー方式 | 12,502 | 5,695 |
| 全組み合わせ方式 | 21,237 | 6,001 |

全組み合わせ方式のほうが306字多く救えることが分かりました。ペアのスキーマ自体は
他の `itaiji_*.json` のような消費側スクリプトと
互換なので、スキーマを変えずに「集合内の全組み合わせを出す」方式を採用しました。

## 見つかったノイズと除外ルール

実際に抽出処理を実装し、出力を目視確認する過程で、想定していなかった
汚染パターンがいくつか見つかりました。

1. **末尾の余分な空白**: `'𢃘 '` のように、1文字＋空白が2トークンと誤認識される。
   → 空白トークンを除外。
2. **巻末書誌情報の混入**: 「集韻卷四」のような巻末表示や、
   「侍朝校對官中書」のような校訂官氏名の列記が、正しいセクション見出しの狭間で
   `entry` カテゴリのまま紛れ込む。前者は note が空文字列、後者は note が「臣」1文字
   という定型パターンを持つ。→ note が空または「臣」だけのグループを除外（24件）。
3. **OCR編集注記**: 「●缺字：韽」（「欠落文字：韽」の意）のような、
   ctext.orgのwiki編集時の注記が、異体字列記ではないのに条件に合致してしまう。
   → headword_run に「缺字」を含むグループを除外。
4. **本文中の `〇`**: 先頭マーカーではなく、「唐武后作〇」のように、
   印刷不能な字（則天文字）の代用として本文中に現れるケースがあった。
   → `〇` 自体をトークンから除外。
5. **巻末OCRの巨大な誤爆**: 「景祐元年三月太常博士…」という上奏文全体が、
   note なしの1グループ（88文字）として紛れ込む例があった。
   → headword_run の文字数が12を超えるグループを除外。

これらはいずれも、抽出結果を実際に確認しなければ気づけなかった問題です。
見積もり段階の検討だけでは想定できませんでした。

## `extract_itaiji_from_jiyun.py` の実行

以上を踏まえたスクリプトを [`extract_itaiji_from_jiyun.py`](/downloads/scripts/extract_itaiji_from_jiyun.py)
として実装し、実行しました。
実行フォルダは適宜、自分の環境に読み替えてください。

```bash
python3 scripts/extract_itaiji_from_jiyun.py \
  --jiyun-glob "../jy/vol*/jiyun_juan*_groups.tsv" \
  --output jy_itaiji_pairs.json
```

```text
groups scanned (category=entry): 40620
multi-char headword_run groups (candidate itaiji sets): 9308
  excluded as boilerplate (colophon/OCR-note, not real itaiji): 24
  excluded as oversized (> 12 chars, likely OCR contamination): 1
pairs before dedupe: 19074
distinct pairs written: 17494
wrote: jy_itaiji_pairs.json
```

**17,494ペア**の [`jy_itaiji_pairs.json`](/downloads/data/jy_itaiji_pairs.json)ができました。

## `--itaiji-json` に指定した結果

### KRM単体（30-048-02_RMK.tsv）での効果

まず、`jy_itaiji_pairs.json` 単独の効果を、類聚名義抄（KRM、`30-048-02_RMK.tsv`）
1ファイルに対して確認しました。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr 30-048-02_RMK.tsv \
  --gy 廣韻.csv \
  --itaiji-json jy_itaiji_pairs.json \
  --outdir linked_out_jy_itaiji_krm/
```

| 条件 | `unmatched` | `multi` |
|---|---:|---:|
| itaiji無し | 5,545 | 6,582 |
| `jy_itaiji_pairs.json` 単独 | 4,604 | 6,897 |
| 差分 | **−941** | **+315** |

KRM単体では、`unmatched` が941行（約17%）減りました。集韻は類聚名義抄と同じく
漢籍系の字体・異体字を多く含むため、KRM側の見出し字との相性が比較的よいと考えられます。

### DHSJR全体での効果: 単独と、既存の組み合わせへの追加

次に、`~/DHSJR/data` 配下の全74ファイルを対象に、
`jy_itaiji_pairs.json` 単独の効果と、連載(6)の組み合わせに追加した場合の
限界的な効果を、それぞれ確認しました。

```text
baseline（itaiji無し）:                              unmatched=21,848  multi=98,191
jy_itaiji_pairs.json 単独:                            unmatched=18,876  multi=98,763
(6)の組み合わせ（7ファイル）再実行:                    unmatched= 3,414  multi=104,958
(6)の組み合わせ + jy_itaiji_pairs.json:                unmatched= 3,373  multi=104,974
```

（`(6)の組み合わせ`は `itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_unverified_20260626.json,gy_kakko_itaiji.json,checked_unmatched_chars_in_cjkvi_variant.json`。連載(6)当時の数値〔`unmatched=3,480`/`multi=104,847`〕とは、その後のDHSJR側データ修正により若干のずれがあるため、今回改めて再実行した値を基準にしています。）

| 比較 | `unmatched`差分 | `multi`差分 |
|---|---:|---:|
| baseline → jy単独 | **−2,972**（−13.6%） | +572 |
| (6)組み合わせ → (6)組み合わせ+jy | **−41**（−1.2%） | +16 |

`jy_itaiji_pairs.json` は、単独で使うと baseline から2,972行（約14%）の
`unmatched` を削減する、それなりに強い効果を持っています。KRM単体での941行という
数字も、この一部です。

しかし、すでに `itaiji_cjkv_simplified-variants.json`（16,786ペア）や
`checked_unmatched_chars_in_cjkvi_variant.json`（4,002ペア）を含む広い組み合わせに
追加すると、限界的な効果はわずか41行（1.2%）まで縮小します。これは、
集韻由来の異体字ペアの多くが、CJKV系の広い対応表とすでに重なっていることを
示しています。

これは「効果がない」ということではありません。集韻は廣韻・CJKVI variantsとは
独立した情報源であり、他のJSONではカバーされない字も一定数含んでいます
（実際に41行は純増しています）。むしろ、**情報源ごとの重なりを定量的に確認できた**
ことが、この比較の意味です。広い対応表を積み増していくと、新しい情報源を足すたびの
限界効果は必然的に小さくなっていきます。

## `--itaiji-json` 目録の更新

今回作成した `jy_itaiji_pairs.json` を含む一覧は、
[`--itaiji-json` 用JSONファイル目録（更新版）](/posts/itaiji-json-inventory-2/)
にまとめました。連載(6)時点の目録はそのまま保持し、新しいファイルとして追加しています。

## 今後の課題

### 限界効果41行の内訳

「(6)の組み合わせ + jy_itaiji_pairs.json」で `unmatched` から解消された41行を
実際に洗い出すと、資料番号ごとに次のような偏りがありました。

| 資料番号 | 件数 |
|---|---:|
| 30-048-02（類聚名義抄／KRM・RMK） | **29** |
| 90-046-01 | 6 |
| 70-054-01 | 3 |
| 70-042-01 | 1 |
| 30-005-02 | 1 |
| 20-045-01 | 1 |

41件中29件（約71%）が類聚名義抄（`30-048-02_RMK.tsv`）でした。KRM単体テストで
見えた効果（941行減）は偶然ではなく、DHSJR全体という広い母集団の中でも、
集韻由来の異体字対応は類聚名義抄に選択的に効いていることが分かります。

解消された28字（延べ41件）と、`jy_itaiji_pairs.json` 経由で正規化された先の
廣韻字頭は次のとおりです。

| 単字_見出し | → 正規化先（廣韻） | 廣韻候補（韻＋声調） |
|---|---|---|
| 㥼 | 㒚 | 魂上／殷去 |
| 㵅 | 㶒 | 覃去 |
| 䁯 | 䁋 | 添入／添入 |
| 伅 | 敦 | 灰平／魂平／寒平／魂去 |
| 冖 | 羃 | 青入 |
| 嚆 | 呼 | 模平 |
| 帡 | 庰 | 清去 |
| 捗 | 荹 | 模平／模去 |
| 滾 | 混 | 魂上 |
| 瀕 | 頻 | 真平 |
| 篬 | 箐 | 清平 |
| 縙 | 䩸 | 鍾平／鍾去 |
| 莇 | 耡 | 魚平／魚去 |
| 蚙 | 䰼 | 侵平／侵上／覃上 |
| 蜳 | 𧑒 | 魂平 |
| 蟕 | 觜 | 支平／支平／支上 |
| 袻 | 䙇 | 仙平 |
| 轕 | 輵 | 寒入 |
| 鉥 | 怵 | 真入 |
| 霺 | 㵟 | 脂平／微平 |
| 𣚇 | 㯱 | 豪平 |
| 𣣈 | 唸 | 先去／添去 |
| 𥅆 | 那 | 歌平／歌上／歌去 |
| 𥺙 | 棱 | 登平 |
| 𦁊 | 挂 | 佳去 |
| 𦞈 | 喉 | 侯平 |
| 𧝐 | 裼 | 青入 |
| 𩬻 | 鬌 | 支平／歌上／歌上 |

「瀕→頻」「嚆→呼」のように偏旁の一部を共有する組み合わせが目立ちます。
廣韻候補が2件以上ある字（伅・蚙・蟕・𥅆・𩬻など）は、この時点で `unmatched` から
`multi` へ移っただけで、音韻地位はまだ一意に決まっていません。

### 今後の作業

1. 上記28字のうち廣韻候補が複数ある字について、`dhsjr_gy_multi.tsv` の該当行を
   確認し、集韻由来の対応が実際に妥当かを精査する。
2. 集韻の `chars.tsv` が持つ声調・韻・小韻情報を使い、`--sgy` のような
   声調ヒントによる `multi` の絞り込みに活用できないか検討する（本連載とは
   別の観点だが、`~/codex/sbgy-dhsjr/scripts/join_rmk_with_jiyun.py` として
   着手済み）。
3. 単独では効果があっても組み合わせでは限界効果が小さい、という今回の傾向が、
   他の情報源（NIHU異体字テーブル等）にも当てはまるか確認する。
4. `ㄑ`（U+3111、注音符号）のような、OCR誤読と思われる孤立トークンが
   ごく少数残っている。実害は小さいが、廣韻に実在しない記号がまぎれ込む
   パターンとして記録しておく。
5. 類聚名義抄に選択的に効いている理由（漢籍系字体の重なりが大きいのか、
   単に未対応字が多く残っていた資料だったのか）を、他の資料番号の
   `unmatched` 残存率と比較しながら検討する。

## おわりに

本稿では、廣韻とは別の宋代韻書である集韻のOCRテキストを取得・構造化し、
その見出し字列記という記述上の特徴から異体字ペアを抽出しました。
抽出方針自体は単純ですが、実データを確認する過程で、巻末書誌情報や
OCR編集注記の混入など、事前の想定にはなかった除外ルールが複数必要になりました。

効果測定では、`jy_itaiji_pairs.json` 単独ではKRM単体で941行、DHSJR全体でも
2,972行の `unmatched` 削減という、それなりに大きな効果を確認できました。
一方、既存の広い異体字JSON群に追加した場合の限界効果は41行にとどまり、
情報源同士の重なりが可視化される結果となりました。

次回は、今回課題として挙げた `multi` の中身の精査、
特に集韻由来の対応によって新たに `multi` に入った例を具体的に見ていきたいと思います。
