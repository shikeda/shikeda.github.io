#!/usr/bin/env python3
import sys
import csv

# Unicode blocks: (start, end, japanese_name)
BLOCKS = [
    (0x4E00, 0x9FFC, "CJK統合漢字"),
    (0x3400, 0x4DB5, "CJK統合漢字拡張A"),
    (0x20000, 0x2A6DD, "CJK統合漢字拡張B"),
    (0x2A700, 0x2B739, "CJK統合漢字拡張C"),
    (0x2B740, 0x2B81D, "CJK統合漢字拡張D"),
    (0x2B820, 0x2CEA1, "CJK統合漢字拡張E"),
    (0x2CEB0, 0x2EBE0, "CJK統合漢字拡張F"),
    (0x30000, 0x3134A, "CJK統合漢字拡張G"),
    (0x31350, 0x323AF, "CJK統合漢字拡張H"),
    (0x2EBF0, 0x2EE5D, "CJK統合漢字拡張I"),
    (0xF900, 0xFAFF, "CJK互換漢字"),
    (0x2F800, 0x2FA1F, "CJK互換漢字補助"),
    (0xE0100, 0xE01EF, "字形選択子補助"),
    (0x2F00, 0x2FDF, "康熙部首"),
    (0x2E80, 0x2EFF, "CJK部首補助"),
    (0x31C0, 0x31EF, "CJKの筆画"),
    (0x2FF0, 0x2FFF, "IDC"),
]

def find_block(codepoint):
    for start, end, name in BLOCKS:
        if start <= codepoint <= end:
            return name
    return "該当なし"

def get_first_codepoint(text):
    # Pythonの文字列はUnicodeコードポイント単位でイテレートされる
    # （サロゲートペアは自動的に結合される）
    if not text:
        return None
    return ord(text[0])

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "dhsjr_gy_unmatched.tsv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "dhsjr_gy_unmatched.blocks.tsv"

    with open(input_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        rows = list(reader)

    header = rows[0]
    data_rows = rows[1:]

    out_header = header + ["16進Unicode番号", "ブロック"]
    out_rows = [out_header]

    for row in data_rows:
        # 単字_見出し列を取得（2列目、0-indexで1）
        moji = row[1] if len(row) > 1 else ""
        cp = get_first_codepoint(moji)
        if cp is None:
            hexcode = ""
            block = "該当なし"
        else:
            hexcode = format(cp, "04X")
            block = find_block(cp)
        out_rows.append(row + [hexcode, block])

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(out_rows)

    print(f"処理完了: {len(data_rows)}行を{output_path}に出力しました。")

if __name__ == "__main__":
    main()
