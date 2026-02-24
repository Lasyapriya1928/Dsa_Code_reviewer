def count_characters(s):
    counter = {}
    for ch in s:
        counter[ch] = counter.get(ch, 0) + 1
    return len(counter)