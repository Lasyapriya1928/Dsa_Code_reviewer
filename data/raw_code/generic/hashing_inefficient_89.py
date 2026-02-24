def map_char_positions(s):
    mapping = {}
    for idx in range(len(s)):
        ch = s[idx]
        if ch not in mapping:
            mapping[ch] = []
        mapping[ch].append(idx)
    flattened = []
    for key in mapping:
        flattened.extend(mapping[key])
    return flattened