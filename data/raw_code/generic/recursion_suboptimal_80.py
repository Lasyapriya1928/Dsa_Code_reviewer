def count_consonants(s, i=0):
    if i == len(s):
        return 0
    if s[i].lower() not in "aeiou":
        return 1 + count_consonants(s, i + 1)
    return count_consonants(s, i + 1)