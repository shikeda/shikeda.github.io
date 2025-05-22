---
title: "Examples of Entry Data Files"
weight: 7
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Publication and Updates of Entry Data Files

This section covers the content and specific examples of **`Entry Data Files`**, as well as methods for their publication and updates using GitHub.

## Examples of Entry Data Files

A list of the publicly available data files is provided in the [Overview of Public Data](/en/docs/krm/02-data-overview/).
Here, we will explain the content of `krm_main`, which is the core **`Entry Data File`**, using it as an example.


Let's consider as examples the three **`Entries`** that were presented as specific illustrations in the [**`Entry Data Structure`**](./03-01-data-structure/) section: '加復', 'ー之', '助' (along with its **`variant characters` (*itaiji*)**), and '功'.

The data in TSV format is shown below. A "No." column has been added on the far left for explanatory purposes.


```text
No  entry_id	hanzi_id	kazama_location	tenri_location	volume_name	radical_name	volume_radical_index	hanzi_entry	original_entry	definition
1	F25133	S31605	K08084810	Tc090810	僧上	力	v8#83	功	〇	音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟
2	F25062	S31507	K08081810	Tc087810	僧上	力	v8#83	助	⿰目力	鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）
3	F25063	S31508	K08081821	Tc087821	僧上	力	v8#83	𦔳／助	■／〇	今正
4	F25121	S31590	K08084411	Tc090411	僧上	力	v8#83	加／復	〇／〇	シカノミナラス
5	F25122	S31592	K08084421	Tc090421	僧上	力	v8#83	ー（加）／之	〇／〇	同
```


The following is an explanation of the sample data shown above:

Entry 1, '**`Headword`**' '功', is an example of the **`Single Character Form`**.
This particular **`Entry`** has complex content within its **`Original Glosses`**; its **`Phonetic Gloss`** includes multiple **`Tone marks` (*shōten*)**, Sino-Japanese readings in kana (仮名字音, *kana jion*), and nasal sound symbols.
*(In the provided transcription format, details such as the distinction between circle and star types of **`Tone marks` (*shōten*)**, or the use of red versus black ink to differentiate **`Tone marks` (*shōten*)** from Sino-Japanese readings in kana, are not represented.)*
The **`Semantic Gloss in Chinese`** '續也' is a scribal error for '績也'.
The **`Japanese Native Reading` (*wakun*)** 'タシカニ' (*tashikani*) is questionable as it does not correspond to the semantic meaning of the **`Headword`** '功'.
Immediately following this *wakun*, there is a note '𭃄歟' (*setsu ka*; "perhaps 𭃄?"), and indeed, the character '切' has the *wakun* 'タシカニ' (*tashikani*).
The character '功' has a **`variant character` (*itaiji*)** '㓛', which is graphically similar to '切' and its **`variant character` (*itaiji*)** '𭃄'.
'切' is a **`graphically similar character`** to the **`Headword`** '功', and this particular *wakun* is thought to have resulted from confusion between these two graphically similar characters.
However, instead of altering the content of the **`Original Glosses`**, the note '𭃄歟' ("perhaps 𭃄?") was added by the compiler or scribe.
Such notes appended with '歟' (*ka*), like '𭃄歟', are treated as 'editorial notes' (*ango*, 案語) by the original compiler or a later scribe of the *Myōgishō*.

Entry 2, '**`Headword`**' '助' (whose original form is ⿰目力 in this **`Entry`**), is in **`Single Character Form`** and provides a **`Phonetic Gloss`** and **`Japanese Native Readings` (*wakun*)**.
The subsequent Entry 3, '**`Headword`**' '𦔳／助', is in **`Multi-Character Form`** and indicates **`variant characters` (*itaiji*)** through a **`Note on Character Form`** ("今正").
The '／' (full-width slash) is a separator used for **`Multi-Character Form`** **`Headwords`**. The number of characters in such a **`Headword`** can be determined from the number of segments separated by these slashes (e.g., one slash indicates two characters).

Entry 4, '**`Headword`**' '加／復', presents a **`Japanese Native Reading` (*wakun*)** for a compound term. Entry 5, '**`Headword`**' 'ー（加）／之', indicates that it shares the same *wakun* ('同').
The 'ー' in 'ー（加）／之' is a symbol used to concisely represent '加', the first character of the **`Headword`** in the preceding **`Entry`** (Entry 4, '加／復').


The same content is shown below in JSON format.
While this format enhances readability, it also increases the data volume, so loading the file may take some time even when using a high-performance editor like VS Code.


```
[
    {
        "entry_id": "F25133",
        "hanzi_id": "S31605",
        "kazama_location": "K08084810",
        "tenri_location": "Tc090810",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "功",
        "original_entry": "〇",
        "definition": "音工（L-R）「コウ（_N）」「クウ（_N）」　續也　事也　成也　タシカニ（LHLH）　𭃄歟"
    },
    {
        "entry_id": "F25062",
        "hanzi_id": "S31507",
        "kazama_location": "K08081810",
        "tenri_location": "Tc087810",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "助",
        "original_entry": "⿰目力",
        "definition": "鉏據反　タスク（LL_）　マサル（HH_）　ハサム　和自ヨ（_L）"
    },
    {
        "entry_id": "F25063",
        "hanzi_id": "S31508",
        "kazama_location": "K08081821",
        "tenri_location": "Tc087821",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "𦔳／助",
        "original_entry": "■／〇",
        "definition": "今正"
    },
    {
        "entry_id": "F25121",
        "hanzi_id": "S31590",
        "kazama_location": "K08084411",
        "tenri_location": "Tc090411",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "加／復",
        "original_entry": "〇／〇",
        "definition": "シカノミナラス"
    },
    {
        "entry_id": "F25122",
        "hanzi_id": "S31592",
        "kazama_location": "K08084421",
        "tenri_location": "Tc090421",
        "volume_name": "僧上",
        "radical_name": "力",
        "volume_radical_index": "v8#83",
        "hanzi_entry": "ー（加）／之",
        "original_entry": "〇／〇",
        "definition": "同"
    },
]
```

## Description of Columns (Headers) in Entry Data Files

Data for the `Entries` of the Myōgishō is stored in `krm_main.tsv` and `krm_main.json`. These files constitute the primary data.

For details on column names and their descriptions, please refer to the [Overview of Public Data](/en/docs/krm/02-data-overview/).


## Publication and Updates via GitHub

The Integrated Database of Hanzi Dictionaries in Early Japan (HDIC) has been publicly available via GitHub since October 2015. The repository can be accessed at [https://github.com/shikeda](https://github.com/shikeda).

A summary of the Chinese character dictionaries included in the HDIC and the initial publication dates of their full-text databases is as follows:

-   *Sōhon Gyokuhen* (宋本玉篇, *Songben Yupian*; abbr. SYP) – First published: October 20, 2015
-   Kōsan-ji manuscript *Tenrei Banshō Meigi* (篆隷万象名義; abbr. KTB) – First published: September 1, 2016
-   Tenji manuscript *Shinsen Jikyō* (新撰字鏡; abbr. TSJ) – First published: June 28, 2018
-   Kanchiin manuscript *Ruiju Myōgisho* (類聚名義抄; abbr. KRM) – First published: March 11, 2022

An explanation of what GitHub is and the significance of publishing research data through this system can be summarized as follows:

GitHub is widely used as a platform for managing and publishing software source code. In recent years, however, it has also been utilized in various research fields, including the humanities, for sharing and publishing research data. GitHub is built upon a version control system called "Git," which records the entire editing history and clearly preserves the an audit trail of changes. This makes it possible to track who made what changes and when, thereby enhancing the transparency and reproducibility of research data.

Furthermore, GitHub facilitates collaborative editing among multiple individuals. Features such as pull requests and issues allow for dialogue and peer-review-like interactions with other researchers to be recorded. Its appeal also lies in features like document creation using Markdown notation and the ability to view file-specific revision histories, making it relatively easy to use even for humanities researchers who do not write programs.

The significance of placing data on GitHub extends beyond mere storage. It enables "open science" practices, where research progress is incrementally published, and improvements are made based on external feedback. It is particularly well-suited for structured humanities data, such as data on Sino-Japanese character readings (like *Kan-on* and *Go-on* based on historical sources), transcribed texts, and lexicographical information, with many existing examples of its use.

Moreover, data on GitHub can be linked with Zenodo, a research data repository, to assign a formal DOI (Digital Object Identifier) and publish it in an academically stable manner. For instance, the "Database of Historical Sino-Japanese Readings" (DHSJR) utilizes GitHub for data construction, and this data is then registered with Zenodo and published with a DOI, making it internationally citable and reusable. In this way, GitHub is playing a significant role as a foundation for the long-term sharing and utilization of digital resources in the humanities.

