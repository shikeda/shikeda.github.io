---
title: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(4)"
date: 2026-06-30
draft: false
tags:
  - 廣韻
  - 音韻学
  - 漢字データベース
  - Python
  - 宋本廣韻
  - HDIC
  - DHSJR
  - KRM
  - データ統合
  - 異体字
categories:
  - デジタル人文学
  - 日本古辞書
summary: "宋本廣韻の音韻データをHDICやDHSJRにつなぐ方法(3)の続き。"
---


## はじめに

加藤大鶴・石山裕慈・佐々木勇編『[日本語と漢字音・漢語音　データベースが切り開く新しい世界](https://bensei.jp/index.php?main_page=product_book_info&products_id=103910)』（アジア遊学320、勉誠社、2026年7月）の目次を勉誠社のサイトから引用してみよう。

- **第1部　漢字音研究を知る**
    - 漢字音研究の現在（石山裕慈）
    - 呉音・漢音の歴史と資料（佐々木勇）
    - 漢音奨励と訓読（湯沢質幸）
    - 中近世の同時代字音たる唐宋音について（岡島昭浩）
    - 漢字音と国語音の交渉（肥爪周二）

- **第2部　人文情報学と漢字音研究**
    - 「漢字音の一元化」について（大島英之）
    - 日本仏教研究者が漢字音研究から受けた恩恵（師茂樹）
    - DHSJRの設計と概略（加藤大鶴）
    - DHSJRにおける漢字字体の正規化の試み（大島英之）
    - 漢字音・漢語音データベースと『大般若経字抄』（中澤信幸）
    - 「資料横断的な漢字音・漢語音データベース」の語彙資源化の試み（高田智和）
    - 古辞書・音義・音釈類の漢字音注記の源流を探る―研究の軌跡とデジタル世界の夢（池田証寿）

- **第3部　漢字音研究の最先端**
    - 改編本『類聚名義抄』の音注増補と切韻（鈴木裕也）
    - 石山寺本守護国界主陀羅尼経長保頃点の漢字音（肥爪周二）
    - 明治大正期の外国語対訳辞書における漢字音・漢語音をめぐって（石山裕慈）
    - 妙一記念館本『仮名書き法華経』の声点加点―同時期の字音直読資料との比較から知られること（佐々木勇）
    - 呉音読されるスタイルでの漢音去声の上声化（坂水貴司）
    - 資料横断的な漢字音・漢語音データベース（DHSJR）における連声濁（浅田健太朗）
    - 漢語アクセントにおける低起上昇類内の揺れ（加藤大鶴）

漢字字体の処理について特に関連する論考を見ると、加藤大鶴「DHSJRの設計と概略」には次のように見える。

>さて、前節で例示した「大樂」は文献によっては「大学」とも記される。検索の際に目的とする漢字を網羅的に検索するには、異なる字体の存在は障害となってしまう。そこで各データ入力者が文献ごとに判断した字体は「単字_出現形」「漢語_出現形」列に収め、正規化（異なる字体を包摂する代表字体を設けた）字体を「単字_見出し」「漢語_見出し」列に収めた。字体の統合作業においては、「jisx0213-variants.txt」(https://github.com/cjkvi/cjkvi-variants/blob/master/jisx0213-variants.txt)に基づき、JIS第四水準までの範囲で旧字体を見出し列に掲げた。これを越えるユニコード内の統合については、本書大島論文を参照のこと。

うかつなことに類聚名義抄のデータ（30-048-2_RMK.tsv）の提供にあたっては、ここにいう正規化作業を行わずに提供してしまった。
DHSJRの正規化のルールに従えば、「単字_出現形」の「万」「与」の「単字_見出し」はそれぞれ「萬」「與」となる。

確かに`30-048-2_RMK.tsv`では次のように正規化の処理がなされている。

```tsv
30-048-02       類聚名義抄_天理図書館_観智院本  21314   21026   萬      万      萬      万                     1武願反                          K0808521
30-048-02       類聚名義抄_天理図書館_観智院本  27543   27071   與      与      與      与                     1上      上                              音預〈上〉                      K1010242
```

私のおぼろげな記憶だと`krm_pronunciations.tsv`ではこのような処理を行っていなかった。上記の2例について調べてみると、確かに「正規化」の処理がなされていた。


```tsv
F25139_01       F25139_01       30-048-02       類聚名義抄_天理図書館_観智院本  21314   16951   万      万     万      万                                                                      武願反                         K0808521 音注声点無_反切
F31962_02       F31962_02       30-048-02       類聚名義抄_天理図書館_観智院本  27543   21964   与      与     与      与                                      上      上                              音預（上）             K1010242 音注声点有_類音注等
```

この点は、HDICとDHSJRとの大きな違いなので、留意しておくことが必要である。当面は、正規化済みの`30-048-2_RMK.tsv`で検討して行くこととする。

次に、大島英之「DHSJRにおける漢字字体の正規化の試み」では、DHSJRの`単字_見出し`での異体字の扱いを詳しく検討しており、参考になる。`単字_見出し`は廣韻データに寄せるための正規化処理を行い、DHSJRの`単字_出現形`では各資料に用いられる字体をそのまま残すということで対処しようとしている。

>DHSJRの統合データでは、同一字種の異体字が混在しており、漢字字体の正規化が課題となっていた。本稿では、中古音情報との接続可能性を重視し、「JIS X 0213関係字」と「宋本広韻データ」という二つのデータを用いて、そもそも正規化対象とすべきか、正規化対象とする場合にはどの字体を見出しとすべきかといった判断を行い、八二四字種からなる異体字リストを作成した。このリストを用いた正規化を試行し、二六二字の字体揺れを解消した。


本稿の(3)まででは、類聚名義抄（`30-048-02_RMK.tsv`）を例にして、廣韻データに未収録字となった例をどうやって連携させるかを検討してきたが、上記の大島論文で用いた「宋本広韻データ」は「漢字データベースプロジェクト」の`sbgy.xml`であり、これをCSV形式に変換して利用したとのことである。ただし、大島論文では、類聚名義抄は対象外として、漢字字体の正規化を論じている。類聚名義抄にはあまりにも異体字が多く、その判断は妥当と思われる。


以下では、`gy_dhsjr_link.py`を利用したアプローチを類聚名義抄（`30-048-02_RMK.tsv`）以外のDHSJR収録資料について適用してみよう。




## DHSJR収録74資料の調査

`gy_dhsjr_link.py`を利用して、DHSJRに収録するすべての資料と廣韻データとの対応状況を調査するには二つの方法がある。

ひとつは、DHSJR収録74資料をすべてまとめた`DHSJR_data_all.tsv`を`--dhsjr`オプションで指定する方法。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr DHSJR_data_all.tsv \
  --gy 廣韻.csv \
  --outdir ./linked_out
```


もうひとつは、DHSJR収録74資料をすべてまとめた`DHSJR/data`フォルダを`--dhsjr-dir
`オプションで指定する方法。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr-dir ./DHSJR/data \
  --gy 廣韻.csv \
  --outdir ./linked_out
```

`DHSJR_data_all.tsv`を`--dhsjr`オプションで指定した結果は次のとおり。

```
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all2/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all2/dhsjr_gy_unmatched.tsv (22012 行)
  → linked_out_dhsjr_all2/dhsjr_gy_multi.tsv (98047 行)
完了。
```

`dhsjr_gy_unmatched.tsv`は22012行あるが、その概要を調べるには、`check_blocks.py`と`summarize_gy_unmatched_blocks.py`を用いる。結果は次のとおり。

対象ファイル: `dhsjr_gy_unmatched.blocks.tsv`

- 総行数: 22,012 行
- ブロック種類: 13 種

## 集計表

| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大5件） |
|---------|-----:|-----:|--------------:|--------------|
| CJK統合漢字 | 16,910 | 76.8% | 1,445 | `膖` U+8196、`毘` U+6BD8、`撃` U+6483、`糩` U+7CE9、`渇` U+6E07 |
| CJK統合漢字拡張B | 2,298 | 10.4% | 1,859 | `𪙁` U+2A641、`𢮎` U+22B8E、`𦡲` U+26872、`𦚻` U+266BB、`𦞲` U+267B2 |
| IDC | 1,423 | 6.5% | 1,278 | `⿰⺼胃` U+2FF0、`⿰⺼冊` U+2FF0、`⿰土虒` U+2FF0、`⿰赤皮` U+2FF0、`⿰⺼蚩` U+2FF0 |
| CJK統合漢字拡張A | 871 | 4.0% | 477 | `䏶` U+43F6、`䑌` U+444C、`㙈` U+3648、`䔧` U+4527、`䖟` U+459F |
| CJK統合漢字拡張F | 210 | 1.0% | 85 | `𮞒` U+2E792、`𮓪` U+2E4EA、`𮌤` U+2E324、`𮢶` U+2E8B6、`𮓌` U+2E4CC |
| 該当なし | 123 | 0.6% | 16 | `□` U+25A1、` ⿳艹宀⿰衤殳` U+0020、`■` U+25A0、`〓` U+3013、`【⿰辛風】` U+3010 |
| CJK互換漢字 | 83 | 0.4% | 26 | `僧` U+FA31、`響` U+FA69、`禎` U+FA53、`祥` U+FA1A、`暑` U+FA43 |
| CJK統合漢字拡張C | 51 | 0.2% | 44 | `𪾼` U+2AFBC、`𪺲` U+2AEB2、`𪝀` U+2A740、`𪜾` U+2A73E、`𪮧` U+2ABA7 |
| CJK統合漢字拡張E | 32 | 0.1% | 28 | `𫣗` U+2B8D7、`𫪦` U+2BAA6、`𫾂` U+2BF82、`𬂡` U+2C0A1、`𬂶` U+2C0B6 |
| CJK統合漢字拡張G | 5 | 0.0% | 5 | `𱂕` U+31095、`𰧫` U+309EB、`𰢚` U+3089A、`𰊊` U+3028A、`𰢟` U+3089F |
| CJK統合漢字拡張H | 4 | 0.0% | 4 | `𱱋` U+31C4B、`𱖞` U+3159E、`𱹫` U+31E6B、`𱵒` U+31D52 |
| CJK互換漢字補助 | 1 | 0.0% | 1 | `沿` U+2F8FC |
| CJK統合漢字拡張D | 1 | 0.0% | 1 | `𫞳` U+2B7B3 |



CJK統合漢字にあげられた例を見ると、毘` U+6BD8は`毗` U+6BD7、`撃` U+6483は`擊` U+64CA、`渇` U+6E07は`渴` U+6E34であれば、`廣韻.csv`とつなげることができると予想される。

念のため、`--itaiji-json`オプションに`itaiji_gy_compare.json`を指定して、`gy_dhsjr_link.py`を実行してみよう。

```bash
python3 gy_dhsjr_link.py \
  --dhsjr DHSJR_data_all.tsv \
  --gy 廣韻.csv \
  --itaiji-json itaiji_gy_compare.json \
  --outdir ./linked_out_dhsjr_all2
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  異体字マップ件数: 581
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all2/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all2/dhsjr_gy_unmatched.tsv (15622 行)
  → linked_out_dhsjr_all2/dhsjr_gy_multi.tsv (100869 行)
完了。
```

`dhsjr_gy_unmatched.tsv`は22012行から15622行に激減した。`check_blocks.py`と`summarize_gy_unmatched_blocks.py`を用いて概要をしらべた結果は次のとおり。


対象ファイル: `dhsjr_gy_unmatched.blocks.tsv`

- 総行数: 15,622 行
- ブロック種類: 13 種

## 集計表

| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大5件） |
|---------|-----:|-----:|--------------:|--------------|
| CJK統合漢字 | 10,699 | 68.5% | 1,321 | `膖` U+8196、`毘` U+6BD8、`撃` U+6483、`糩` U+7CE9、`渇` U+6E07 |
| CJK統合漢字拡張B | 2,178 | 13.9% | 1,776 | `𪙁` U+2A641、`𢮎` U+22B8E、`𦡲` U+26872、`𦞲` U+267B2、`𣫘` U+23AD8 |
| IDC | 1,423 | 9.1% | 1,278 | `⿰⺼胃` U+2FF0、`⿰⺼冊` U+2FF0、`⿰土虒` U+2FF0、`⿰赤皮` U+2FF0、`⿰⺼蚩` U+2FF0 |
| CJK統合漢字拡張A | 813 | 5.2% | 455 | `䏶` U+43F6、`䑌` U+444C、`㙈` U+3648、`䔧` U+4527、`䖟` U+459F |
| CJK統合漢字拡張F | 210 | 1.3% | 85 | `𮞒` U+2E792、`𮓪` U+2E4EA、`𮌤` U+2E324、`𮢶` U+2E8B6、`𮓌` U+2E4CC |
| 該当なし | 123 | 0.8% | 16 | `□` U+25A1、` ⿳艹宀⿰衤殳` U+0020、`■` U+25A0、`〓` U+3013、`【⿰辛風】` U+3010 |
| CJK互換漢字 | 83 | 0.5% | 26 | `僧` U+FA31、`響` U+FA69、`禎` U+FA53、`祥` U+FA1A、`暑` U+FA43 |
| CJK統合漢字拡張C | 50 | 0.3% | 43 | `𪾼` U+2AFBC、`𪺲` U+2AEB2、`𪝀` U+2A740、`𪜾` U+2A73E、`𪮧` U+2ABA7 |
| CJK統合漢字拡張E | 32 | 0.2% | 28 | `𫣗` U+2B8D7、`𫪦` U+2BAA6、`𫾂` U+2BF82、`𬂡` U+2C0A1、`𬂶` U+2C0B6 |
| CJK統合漢字拡張G | 5 | 0.0% | 5 | `𱂕` U+31095、`𰧫` U+309EB、`𰢚` U+3089A、`𰊊` U+3028A、`𰢟` U+3089F |
| CJK統合漢字拡張H | 4 | 0.0% | 4 | `𱱋` U+31C4B、`𱖞` U+3159E、`𱹫` U+31E6B、`𱵒` U+31D52 |
| CJK互換漢字補助 | 1 | 0.0% | 1 | `沿` U+2F8FC |
| CJK統合漢字拡張D | 1 | 0.0% | 1 | `𫞳` U+2B7B3 |

CJK統合漢字にあげられた例を見ると、毘` U+6BD8、`撃` U+6483、`渇` U+6E07などが残っている。
これは、`廣韻.csv`と`sbgy.xml`のどちらも
`毗` U+6BD7、`擊` U+64CA、`渴` U+6E34を用いているため、DHSJRとつなぐことができなかったのである。

DHSJRの「単字_見出し」の正規化の方針によれば、毘→毗、撃→擊、渇→渴のように変換されるはずであるが、その処理がなされていないためと見られる。

次に若干例をあげておく。

```tsv
20-001-01       大般若波羅蜜多経_根津美術館     15      11      毘      毘      毘鉢舍那        毘鉢舍那       11                       〔墨〕ヒ        ヒハチシヤナ                                    3：0012b08      音写字
20-001-01       大般若波羅蜜多経_根津美術館     34      21      撃      撃      飄撃上涌        飄撃上涌       22       〔朱〕入        去入＊＊        〔墨〕キヤク    ヘウキヤク＊ユウ                                       3：0013c17
20-001-01       大般若波羅蜜多経_根津美術館     61      40      渇      渇      渇者得飮        渇者得飮       12                       〔墨〕カチ      カチ＊＊＊ 
30-058-01       仮名書き法華経_妙一記念館       529     153     毗      毘      毗摩質多羅阿修羅王      毘摩質多羅阿修羅王                      1                               ひ      ひましちたらあしゆらわう               1-0010-4         T0262_.09.0002b01       1       0010-4
30-058-01       仮名書き法華経_妙一記念館       7901    3738    渴      渇      飢渴    飢渇                   2入      上入    かつ    けかつ                                  2-0247-4                T0262_.09.0014a16      20247-4
30-058-01       仮名書き法華経_妙一記念館       7949    3766    毗      毘      毗舎闍鬼        毘舍闍鬼       1ひ      ひしやしやくゐ                          濁      2-0249-4                T0262_.09.0014a25       2      0249-4
50-041-01       邦訳日葡辞書    1347    695     毘      毘      毘嵐風  毘嵐風  birampŭ         1       1      ビ      ビラムプゥ 
70-054-01       和仏小辞典_神戸大学     262     125     撃      撃      駁撃    駁撃    bakugeki               2geki    40
```

大島論文には、付録として「字体の正規化リスト（暫定案）」が添えられているが、電子版の公開はまだのようであるし、DHSJRを利用する上での注意として指摘するにとどめておく。

## `jisx0213-variants.txt`を`--itaji-json`オプションで利用する

DHSJRの正規化は、`jisx0213-variants.txt`を利用しているので、その内容を`gy_dhsjr_link.py`の`--itaji-json`オプションで利用可能なJSON形式に変換して、どの程度、廣韻データとつなげるかを検討してみよう。

`jisx0213-variants.txt`のフォーマットは次のようである。

```text
jisx0213/variant,<rev>,jisx0213/variant
jisx0213/variant,<name>,関連字（JIS X 0213）
#
𥫣,jisx0213/variant,籅
#
𧯇,jisx0213/variant,豅
#
```

これを次のJSON形式に変換すればいい。

```json
[
  {
    "c1": "𪔝",
    "c2": "𪔜"
  },
  {
    "c1": "眾",
    "c2": "衆"
  }
]
```

ここでは、awk の oneliner で変換してみよう。生成するファイル名は`itaiji_jisx0213.json`としておく。


```bash
awk -F, '
BEGIN{print "["}
/^#/||/^jisx0213\/variant,/{next}
{
    sub(/\r$/, "", $3)
    if(n++) print ","
    printf "  {\n    \"c1\": \"%s\",\n    \"c2\": \"%s\"\n  }",$1,$3
}
END{print "\n]"}
' jisx0213-variants.txt > itaiji_jisx0213.json
```


`--itaiji-json`オプションに`itaiji_jisx0213.json`を指定して、`gy_dhsjr_link.py`を実行してみよう。

```bash
python3 gy_dhsjr_link.py   --dhsjr DHSJR_data_all.tsv   --gy 廣韻.csv   --itaiji-json itaiji_jisx0213.json   --outdir ./linked_out_dhsjr_all_x0213
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  異体字マップ件数: 891
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all_x0213/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all_x0213/dhsjr_gy_unmatched.tsv (14350 行)
  → linked_out_dhsjr_all_x0213/dhsjr_gy_multi.tsv (100141 行)
```


`itaiji_gy_compare.json`を併用した結果は次のとおり。

```bash
python3 gy_dhsjr_link.py   --dhsjr DHSJR_data_all.tsv   --gy 廣韻.csv   --itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json   --outdir ./linked_out_dhsjr_all_x0213_2
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  異体字マップ件数: 1403
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all_x0213_2/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all_x0213_2/dhsjr_gy_unmatched.tsv (10907 行)
  → linked_out_dhsjr_all_x0213_2/dhsjr_gy_multi.tsv (101762 行)
完了。
```

`itaiji_jisx0213.json`、`itaiji_gy_compare.json`、`itaiji_krm_gy_attested.json`の三つを併用すると、
`dhsjr_gy_unmatched.tsv`は更に 9117 行まで減らすことができる。
ただ、`itaiji_krm_gy_attested.json`は類聚名義抄に特化して独自に作成したデータなので、
`itaiji_jisx0213.json`、`itaiji_gy_compare.json`の二つを`--itaiji-json`に指定して得た`dhsjr_gy_unmatched.tsv`10907 行を検討してみることにする。


対象ファイル: `dhsjr_gy_unmatched.blocks.tsv`

- 総行数: 10,907 行
- ブロック種類: 13 種

## 集計表

| ブロック | 件数 | 割合 | ユニーク文字数 | 例（最大5件） |
|---------|-----:|-----:|--------------:|--------------|
| CJK統合漢字 | 6,087 | 55.8% | 1,066 | `膖` U+8196、`糩` U+7CE9、`姉` U+59C9、`悦` U+60A6、`胸` U+80F8 |
| CJK統合漢字拡張B | 2,154 | 19.7% | 1,771 | `𪙁` U+2A641、`𢮎` U+22B8E、`𦡲` U+26872、`𦞲` U+267B2、`𣫘` U+23AD8 |
| IDC | 1,423 | 13.0% | 1,278 | `⿰⺼胃` U+2FF0、`⿰⺼冊` U+2FF0、`⿰土虒` U+2FF0、`⿰赤皮` U+2FF0、`⿰⺼蚩` U+2FF0 |
| CJK統合漢字拡張A | 810 | 7.4% | 452 | `䏶` U+43F6、`䑌` U+444C、`㙈` U+3648、`䔧` U+4527、`䖟` U+459F |
| CJK統合漢字拡張F | 210 | 1.9% | 85 | `𮞒` U+2E792、`𮓪` U+2E4EA、`𮌤` U+2E324、`𮢶` U+2E8B6、`𮓌` U+2E4CC |
| 該当なし | 123 | 1.1% | 16 | `□` U+25A1、` ⿳艹宀⿰衤殳` U+0020、`■` U+25A0、`〓` U+3013、`【⿰辛風】` U+3010 |
| CJK統合漢字拡張C | 50 | 0.5% | 43 | `𪾼` U+2AFBC、`𪺲` U+2AEB2、`𪝀` U+2A740、`𪜾` U+2A73E、`𪮧` U+2ABA7 |
| CJK統合漢字拡張E | 32 | 0.3% | 28 | `𫣗` U+2B8D7、`𫪦` U+2BAA6、`𫾂` U+2BF82、`𬂡` U+2C0A1、`𬂶` U+2C0B6 |
| CJK互換漢字 | 7 | 0.1% | 4 | `契` U+F909、`益` U+FA17、`精` U+FA1D、`杻` U+F9C8 |
| CJK統合漢字拡張G | 5 | 0.0% | 5 | `𱂕` U+31095、`𰧫` U+309EB、`𰢚` U+3089A、`𰊊` U+3028A、`𰢟` U+3089F |
| CJK統合漢字拡張H | 4 | 0.0% | 4 | `𱱋` U+31C4B、`𱖞` U+3159E、`𱹫` U+31E6B、`𱵒` U+31D52 |
| CJK互換漢字補助 | 1 | 0.0% | 1 | `沿` U+2F8FC |
| CJK統合漢字拡張D | 1 | 0.0% | 1 | `𫞳` U+2B7B3 |

CJK統合漢字にあげられた例を見ると、毘` U+6BD8、`撃` U+6483、`渇` U+6E07などは消えているので、`itaiji_jisx0213.json`で処理した分はDHSJRと廣韻データとをつなぐことができたと見られる。

`姉` U+59C9は`姊` U+59CAが廣韻データにあるのだろうと予想される。
`悦` U+60A6は`悅` U+6085、`胸` U+80F8 は`胷` U+80F7であろう。
こうした例を対照した異体字ペアのJSONファイルをうまいこと作成する方法はないだろうか。




## `cjkvi-simplified.txt`と`cjkvi-variants.txt`を`--itaji-json`オプションで利用する

[`https://github.com/cjkvi/cjkvi-variants`](https://github.com/cjkvi/cjkvi-variants/)で公開された異体字の対照表を眺めてみると、
`cjkvi-simplified.txt`と`cjkvi-variants.txt`とが使えそうである。

```bash
% grep "[姉姊悦悅胸胷]" *.txt
cjkvi-simplified.txt:姉,cjkvi/simplified,姊
cjkvi-simplified.txt:胷,cjkvi/simplified,胸
cjkvi-variants.txt:恱,cjkvi/variant,悅
```

awk の oneliner で`itaiji_cjkv_simplified-variants.json`を生成してみよう。

```bash
awk -F, 'BEGIN{print "["}/^#/||/^cjkvi\//||/^$/{next}{sub(/\r$/,"",$1);sub(/\r$/,"",$3);if(n++)print ",";printf "  {\n    \"c1\": \"%s\",\n    \"c2\": \"%s\"\n  }",$1,$3}END{print "\n]"}' cjkvi-simplified.txt cjkvi-variants.txt > itaiji_cjkv_simplified-variants.json
```

`itaiji_cjkv_simplified-variants.json`を`gy_dhsjr_link.py`の`--itaiji-json`オプションに追加して実行。

```bash
python3 gy_dhsjr_link.py  --dhsjr DHSJR_data_all.tsv   --gy 廣韻.csv   --itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json   --outdir ./linked_out_dhsjr_all_cjkv

廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  [itaiji] JSON読み込み: itaiji_cjkv_simplified-variants.json
  異体字マップ件数: 7682
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all_cjkv/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all_cjkv/dhsjr_gy_unmatched.tsv (8857 行)
  → linked_out_dhsjr_all_cjkv/dhsjr_gy_multi.tsv (102726 行)
完了。
```

## `jp-old-style.txt`を追加

[姉姊悦悅胸胷]の例がなかったので見落としていいたが、`jp-old-style.txt`も使えそうである。

awk の oneliner で`itaiji_jp-old.json`を生成してみよう。


```bash
awk 'BEGIN{FS="[[:space:]]+";print "["}/^#/||NF<2{next}{sub(/\r$/,"",$1);sub(/\r$/,"",$2);if(n++)print ",";printf "  {\n    \"c1\": \"%s\",\n    \"c2\": \"%s\"\n  }",$1,$2}END{print "\n]"}' jp-old-style.txt > itaiji_jp-old.json
```

この`itaiji_jp-old.json`を`gy_dhsjr_link.py`の`--itaiji-json`オプションに追加して実行。

```bash
python3 gy_dhsjr_link.py  --dhsjr DHSJR_data_all.tsv   --gy 廣韻.csv   --itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json   --outdir ./linked_out_dhsjr_all_cjkv-jp

廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  [itaiji] JSON読み込み: itaiji_cjkv_simplified-variants.json
  [itaiji] JSON読み込み: itaiji_jp-old.json
  異体字マップ件数: 7686
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all_cjkv-jp/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all_cjkv-jp/dhsjr_gy_unmatched.tsv (8857 行)
  → linked_out_dhsjr_all_cjkv-jp/dhsjr_gy_multi.tsv (102726 行)
完了。
```

結果を見ると、`説`と`說`とでうまく行っていない。
そこで、`itaiji_krm_unverified_20260626.json`を追加して処理してみることとした。


## `itaiji_krm_unverified_20260626.json`を追加

```bash
python3 gy_dhsjr_link.py   --dhsjr DHSJR_data_all.tsv   --gy 廣韻.csv   --itaiji-json itaiji_jisx0213.json,itaiji_gy_compare.json,itaiji_cjkv_simplified-variants.json,itaiji_jp-old.json,itaiji_krm_unverified_20260626.json   --outdir ./linked_out_dhsjr_all_cjkv-jp
廣韻インデックスを構築中…
  廣韻 ユニーク字数: 19585
異体字マップを構築中…
  [itaiji] JSON読み込み: itaiji_jisx0213.json
  [itaiji] JSON読み込み: itaiji_gy_compare.json
  [itaiji] JSON読み込み: itaiji_cjkv_simplified-variants.json
  [itaiji] JSON読み込み: itaiji_jp-old.json
  [itaiji] JSON読み込み: itaiji_krm_unverified_20260626.json
  異体字マップ件数: 7700
処理中: DHSJR_data_all.tsv
  → linked_out_dhsjr_all_cjkv-jp/DHSJR_data_all_gy_linked.tsv (387265 行)
  → linked_out_dhsjr_all_cjkv-jp/dhsjr_gy_unmatched.tsv (7523 行)
  → linked_out_dhsjr_all_cjkv-jp/dhsjr_gy_multi.tsv (103586 行)
完了。
```

## 調査結果（baseline 比）

baseline（異体字マップなし）を基準とした行数変化です。`unmatched` の減少のうち `multi` への移行分と、単一マッチとして解消された分を分けて示します。

| 条件 | 異体字マップ件数 | unmatched 行数 | unmatched Δ※ | multi 行数 | multi Δ※ | unmatched 減少のうち multi へ | 単一マッチ化 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline（指定なし） | 0 | 22,012 | — | 98,047 | — | — | — |
| `itaiji_gy_compare.json` | 581 | 15,622 | **−6,390** | 100,869 | **+2,822** | 2,822 | 3,568 |
| `itaiji_jisx0213.json` | 891 | 14,350 | **−7,662** | 100,141 | **+2,094** | 2,094 | 5,568 |
| jisx0213 + gy_compare | 1,403 | 10,907 | **−11,105** | 101,762 | **+3,715** | 3,715 | 7,390 |
| 上記 + `itaiji_cjkv_simplified-variants.json` | 7,682 | 8,857 | **−13,155** | 102,726 | **+4,679** | 4,679 | 8,476 |
| 上記 + `itaiji_jp-old.json` | 7,686 | 8,857 | **−13,155** | 102,726 | **+4,679** | 0 | 0 |
| 上記 + `itaiji_krm_unverified_20260626.json` | 7,700 | 7,523 | **−14,489** | 103,586 | **+5,539** | 860 | 474 |

※ **unmatched Δ**・**multi Δ** は baseline 比。最下2行の「unmatched 減少のうち multi へ」「単一マッチ化」は、**直前の行からの増分**（jp-old 追加時は 0、krm_unverified 追加時は −1,334 / +860）。

- **unmatched 減少のうち multi へ**（baseline 比の行）… |unmatched Δ| のうち、multi 行数増加に対応する部分。
- **単一マッチ化**（baseline 比の行）… unmatched から消えたが multi に入らなかった分（= |unmatched Δ| − multi Δ）。

`DHSJR_data_all_gy_linked.tsv` は全条件で **387,265 行**のまま変化しません。

### baseline から見た累計（最終条件）

最終行（jisx0213 + gy_compare + cjkv + jp-old + krm_unverified）を baseline と比較すると次のとおりです。

| 指標 | baseline | 最終 | 差 |
| --- | ---: | ---: | ---: |
| unmatched | 22,012 | 7,523 | **−14,489**（65.8% 減） |
| multi | 98,047 | 103,586 | **+5,539** |
| 単一マッチ化（累計） | — | — | **8,950** |

### `jp-old-style.txt` 追加の所見

`itaiji_jp-old.json` を加えても異体字マップは **7,682 → 7,686**（+4 ペア）にしか増えず、**unmatched・multi の行数はいずれも 8,857 / 102,726 のまま**でした。`姉`/`姊`・`悦`/`悅`・`胸`/`胷` のような新字体↔旧字体の例は、DHSJR 全体の未収録行数にはほとんど効いていません。一方、`説`/`說` のように依然 unmatched に残る例もあり、jp-old だけでは不足していることが確認できました。

### `itaiji_krm_unverified_20260626.json` 追加の所見

KRM 未収録字の手作業ペア（(2) で作成した 45 ペアを含むリスト）を重ねると、マップは **7,686 → 7,700**（+14 ペア）、unmatched は **8,857 → 7,523**（**−1,334 行**）まで減りました。うち **860 行**は multi 側へ移行し、**474 行**は単一マッチとして解消されたとみなせます。`説`/`說` のような例も、このリストに含まれるペアで処理された可能性があります。

### まとめ

- CJKV 簡体字・異体字表（3 ファイル併用）までで、baseline 比 **unmatched −13,155 行**（22,012 → 8,857）まで削減できました。
- `jp-old-style.txt` 由来の 4 ペア追加は、**このデータセットでは行数に影響しませんでした**。
- `itaiji_krm_unverified_20260626.json` の追加で、さらに **−1,334 行**（8,857 → 7,523）。連載 (1) の KRM 単資料ベースの知見が、DHSJR 全体にも転用できることを示しています。
- いずれの段階でも **linked 行数は不変**であり、異体字正規化の効果は主に unmatched の減少と multi の増加として現れます。
