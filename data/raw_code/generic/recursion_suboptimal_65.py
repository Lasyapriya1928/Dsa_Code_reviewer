def count_letter(s, ch, i=0):
    if i == len(s):
        return 0
    return (1 if s[i] == ch else 0) + count_letter(s, ch, i + 1)