def count_vowels(s, idx=0):
    if idx >= len(s):
        return 0
    add = 1 if s[idx].lower() in "aeiou" else 0
    return add + count_vowels(s, idx + 1)