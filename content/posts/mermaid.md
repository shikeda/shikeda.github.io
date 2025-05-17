---
title: "Hugo BookテーマでのMermaid"
date: 2025-05-18
# bookComments: false
# bookSearchExclude: false
---

# Hugo Book テーマでの Mermaid の扱い


VS Codeで次の Mermaidで作図したER図は表示されるが、Hugo の book では図が描けない。
どうしたら表示できるか。

次の方法でできました。

ショートコードを使います。

**Mermaid.js を最新版に差し替える**

layouts/shortcodes/mermaid.html

に次を追加。

```
{{ if not (.Page.Scratch.Get "mermaid") }}
<!-- Load latest Mermaid.js from CDN -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: true });
</script>
{{ .Page.Scratch.Set "mermaid" true }}
{{ end }}

<pre class="mermaid{{ with .Get "class" }} {{ . }}{{ end }}">
  {{- .Inner -}}
</pre>
```



{{< mermaid >}}
erDiagram

    main {
        string entry_id PK
        string hanzi_id
        string kazama_location FK
        string tenri_location
        string volume_name
        string radical_name
        string volume_radical_name
        string hanzi_entry
        string original_entry
        string definition
    }

    headword_chars {
        string hanzi_id PK
        string entry_id FK
        string constituent_char
        int character_order
        string kazama_location_id
        string tenri_location_id
        string img_file_name
    }

    notes {
        string definition_seq_id PK
        string entry_id FK
        string kazama_location
        string tenri_location
        string volume_name
        string radical_name
        string volume_radical_index
        string hanzi_entry
    }

    definition_core {
        string definition_seq_id PK
        string original_entry
        string definition_elements
        int definition_type_code
        string definition_type_name
        text remarks
    }

    wakun {
        string wakun_id PK
        string definition_seq_id FK
        string kazama_location FK
        string hanzi_entry
        string wakun_elements
        string wakun_form
        string wakun_standard_hanzi
        string wakun_variant_in_hanzi
        string variant_hanzi_for_wakun
        string japanknowledge_id
    }

    main ||--o{ headword_chars : has
    main ||--o{ notes : has
    notes ||--|| definition_core : "includes"
    notes ||--o{ wakun : has
{{< /mermaid >}}
