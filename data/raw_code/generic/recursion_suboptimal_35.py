def count_uppercase(s, i=0):
    if i >= len(s):
        return 0
    return (1 if s[i].isupper() else 0) + count_uppercase(s, i + 1)