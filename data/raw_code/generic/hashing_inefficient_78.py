def group_by_last_char(words):
    mapping = {}
    for word in words:
        key = word[-1]
        if key not in mapping:
            mapping[key] = []
        mapping[key].append(word)
    return mapping