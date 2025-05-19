---
title: "英文での年月日の形式"
date: 2025-05-19T13:14:53+09:00
# bookComments: false
# bookSearchExclude: false
---
# 英文での年月日の形式

いろいろな形式がある。

1. "20 April 2025" (日 月 年): この形式は、DD Month YYYY となり、月を数字ではなく名前で書くため、04/05/2025 のような数字のみの表記（これが4月5日なのか5月4日なのか混乱を招く）よりもはるかに明確。国際的にも比較的理解されやすい形式。
2. "April 20, 2025" (月 日, 年): こちらも月を名前で書くため明確です。アメリカ英語圏ではこちらが標準。

1の形式のものをチェックして2に修正。

**正規表現の例**

```
\b([1-9]|[12][0-9]|3[01])\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b
```


Perl や grep -P (Perl互換正規表現) などで大文字・小文字を区別しないオプション (i) を使うことを前提とすれば、月名の部分は簡略化できる。

```
/\b([1-9]|[12]\d|3[01])\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b/i
```

**grepで検索**

```
grep -E -i '\b([1-9]|[12][0-9]|3[01])\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+[0-9]{4}\b' YourFile.txt
```
または、-rn と--includeをつけて、再帰的に特定の拡張子のファイルを検索。

```
grep -rn -E -i '\b([1-9]|[12][0-9]|3[01])\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+[0-9]{4}\b' ./ --include=*.json
```

**Perlで検索**

```
perl -ne 'print if /\b([1-9]|[12]\d|3[01])\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b/i' YourFile.txt
```