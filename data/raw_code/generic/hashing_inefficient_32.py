def build_index_map(items):
    mapping = {}
    idx = 0
    while idx < len(items):
        mapping[items[idx]] = idx
        idx += 1
    return mapping