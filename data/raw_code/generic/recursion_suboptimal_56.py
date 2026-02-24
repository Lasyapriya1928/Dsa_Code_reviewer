def count_chars(s, i=0):
    if i >= len(s):
        return 0
    return 1 + count_chars(s, i + 1)