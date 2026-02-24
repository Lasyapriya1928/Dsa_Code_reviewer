def first_unique_char(s):
    table = {}
    for ch in s:
        table[ch] = table.get(ch, 0) + 1
    for idx, ch in enumerate(s):
        if table[ch] == 1:
            return idx
    return -1