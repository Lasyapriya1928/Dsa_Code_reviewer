def char_frequency(s):
    freq = {}
    i = 0
    while i < len(s):
        c = s[i]
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        i += 1
    return freq