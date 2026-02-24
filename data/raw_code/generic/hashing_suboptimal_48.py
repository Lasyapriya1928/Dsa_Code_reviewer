def find_common_prefix(words):
    groups = {}
    for word in words:
        prefix = word[:1]
        groups.setdefault(prefix, []).append(word)
    return groups