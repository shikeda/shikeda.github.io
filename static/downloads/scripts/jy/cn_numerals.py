"""Chinese numeral -> int, tolerant of the '十'-dropping OCR artifact seen in
these ctext pages (e.g. '文三一' meaning 31, instead of the expected '三十一')."""

DIGITS = {'〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
          '六': 6, '七': 7, '八': 8, '九': 9}
UNITS = {'十': 10, '百': 100, '千': 1000}


def cn2num(s: str):
    if not s:
        return None
    if s.isdigit():
        return int(s)
    if any(u in s for u in UNITS):
        result = 0
        pending = None
        for ch in s:
            if ch in DIGITS:
                pending = DIGITS[ch]
            elif ch in UNITS:
                result += (pending if pending is not None else 1) * UNITS[ch]
                pending = None
            else:
                return None
        if pending is not None:
            result += pending
        return result
    # no 十/百/千 unit: OCR sometimes drops '十', e.g. '三一' for 31.
    # Fall back to reading each digit character literally.
    if all(ch in DIGITS for ch in s):
        return int(''.join(str(DIGITS[ch]) for ch in s))
    return None
