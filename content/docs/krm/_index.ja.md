---
title: "KRM Documentation"
weight: 1
# date: 2022-01-09
#bookFlatSection: true
#bookToc: true
# bookHidden: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# KRM Documentation

*観智院本類聚名義抄データベース(KRM)のための学術的・技術的文書*

## 本文書について

**KRM Documentation**は、観智院本『類聚名義抄』全文テキストデータベース（KRM Database）の公式な学術的・技術的参照文書である。原資料である写本、公開データファイル、項目データモデル、データ入力の規則、注釈方針、組版環境、進捗状況、関連する事例研究について記す。

本文書は、KRMデータを直接利用する読者――日本語史・辞書学・デジタル人文学の研究者――のほか、KRMデータベースがどのように構築され、維持されているかを知りたい読者を対象とする。

- **著者：** 池田証寿、北海道大学名誉教授
- **文書バージョン：** 0.9（完全なドラフト。今回の再編の完了をもってVersion 1.0とする予定）
- **ドラフト完成日：** 2026年8月15日
- **公開日：** *ドラフト — Version 1.0の時点で確定*
- **最終更新日：** 2026年8月15日
- **プロジェクトサイト：** [https://shikeda.github.io/](https://shikeda.github.io/)
- **文書サイト：** [https://shikeda.github.io/docs/krm/](https://shikeda.github.io/docs/krm/)
- **文書のライセンス：** [CC BY-SA 4.0](https://github.com/shikeda/krm/blob/main/LICENSE)
- **推奨引用形式：** *（ドラフト — Version 1.0の時点で確定）* Ikeda, Shōju. *KRM Documentation*. Version 0.9. [https://shikeda.github.io/docs/krm/](https://shikeda.github.io/docs/krm/).
- **関係：** KRM DocumentationはKRMデータベースを記述する文書である。KRMデータベースはGitHubおよびZenodoを通じて配布されている（後述の[対象データベースについて](#対象データベースについて)を参照）。

なお、ここでの解説は、 池田証壽・劉冠偉・鄭門鎬・張馨方・李媛「観智院本『類聚名義抄』全文テキストデータベース―その構築方法と掲出項目数等の計量―」(『訓点語と訓点資料』144、2020)に述べたところと重複するところがあるが、筆頭著者の池田が、全面的な見直しをはかり、用語を整理し、その後の調査内容を大幅に追加して新たにまとめ直したものである。

## 対象データベースについて

本文書は、**KRM: Database of the Kanchi-in Manuscript of the Ruiju Myōgishō**（KRM）――観智院本の全文テキストデータ化に、所在情報・本文校勘・出典考証を加えたもの――について記す。KRMは単なるデータセットではなく、そのリポジトリには処理用のPythonスクリプトとローカル検索用のWebアプリケーションも含まれる。

- **リポジトリ：** [https://github.com/shikeda/krm](https://github.com/shikeda/krm)
- **KRMデータバージョン：** v1.2.6
- **KRMデータセットDOI：** [10.5281/zenodo.15481563](https://doi.org/10.5281/zenodo.15481563)
- **データの引用：** Ikeda, Shōju. (2025). *KRM: Database of the Kanchi-in Manuscript of the Ruiju Myōgishō*. Version v1.2.6. Zenodo. [https://doi.org/10.5281/zenodo.15481563](https://doi.org/10.5281/zenodo.15481563).
- **KRMデータのライセンス：** [CC BY-SA 4.0](https://github.com/shikeda/krm/blob/main/LICENSE)
- **ソフトウェアのライセンス：** [MIT License](https://github.com/shikeda/krm/blob/main/scripts/LICENSE)（`scripts/`および`webapp/`に適用）

**リポジトリの構成：**

| パス | 内容 |
| --- | --- |
| `krm_*.tsv`, `krm_*.json` | 公開されているKRMデータファイル（掲出字、注文、注釈、和訓など） |
| `scripts/` | データ変換・保守用のPythonユーティリティスクリプト（MIT License） |
| `webapp/` | ローカル全文検索アプリケーション（Next.js；MIT License） |
| `docs/` | リポジトリの説明文書（本Documentationサイトとは別） |
| `examples/`, `images/`, `diff/` | 補足的な用例・画像・変更記録 |

## HDICプロジェクトとの関係

KRMは、**平安時代漢字字書総合データベース（HDIC）**を構成する漢字字書データベースのひとつである。HDICプロジェクト全体（その背景、他の構成データベース、検索ツールHDIC Viewer）については、[HDICプロジェクトのホームページ](/)を参照されたい。

## 類聚名義抄について

KRMデータベースは、十二世紀に真言宗の僧侶が編纂した漢字字書、観智院本『類聚名義抄』にもとづく。観智院本は、改編本系の完本として現存する唯一の伝本であり、日本語語彙史、日本漢字音史、日本における漢字字体史の研究にとって貴重な資料である。

『類聚名義抄』は日本古辞書の雄編として名高い。書名の読み方は「るいじゅみょうぎしょう」である。源順撰『倭名類聚抄』の「類聚」と、空海撰『篆隷万象名義』の「名義」とを採用して書名としたとされる。

詳細は[第1章：類聚名義抄の概要](./01-introduction/)を参照。

## 本文書の構成

第1章から第5章までが**Core Documentation**（中核文書）であり、KRMの項目データモデル・入力規則・注釈方針に関する主要な参照文書である。第6章から第9章は、組版設定・進捗記録・事例研究などの補足資料である。

本文書は次の章から構成される。

1. **[類聚名義抄の概要](./01-introduction/)** ── 原資料である写本：その諸本、編者、成立年代、価値、構成。
2. **[公開データの概要](./02-data-overview/)** ── KRMのデータファイルとその構造。
3. **[項目データモデル](./03-entry-data-model/)** ── KRMの項目を支える概念モデル。
4. **[項目データ入力](./04-entry-input/)** ── 掲出字、ID、文字の符号化、翻刻の規則。
5. **[注釈作成の基本方針](./05-annotation-policy/)** ── 注釈の方針と方法論、具体例を含む。
6. **[翻刻・注釈の組版の設定](./06-typesetting/)** ── 翻刻・注釈のための組版環境。
7. **[進捗状況](/docs/krm/07-progress/)** ── 開発記録（日本語のみ）。
8. **[事例研究](/docs/krm/08-case-studies/)** ── 応用的な研究事例（詳細はja版、en版は要旨のみ）。
9. **[構築の経緯](./09-development-history/)** ── KRMデータベースがどのように構築されたか。

章の移動にはサイドバーのナビゲーションを利用されたい。

## 謝辞

観智院本『類聚名義抄』全文テキストデータベースの構築と公開は、天理図書館当局から特別に御許可を賜り推進しているものであり、天理図書館善本叢書の版元である八木書店各位にも格別の御配慮を賜っている。ここに記して感謝の意を表する。

この研究は日本学術振興会科学研究費補助金（課題番号25370506、16H03422、19H00526、23K17500、25K00466、26K21717）の成果の一部である。記して感謝の意を表する。
