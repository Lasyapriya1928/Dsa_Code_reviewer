def filter_existing(a, b):
    lookup = set(b)
    result = []
    for item in a:
        if item in lookup:
            result.append(item)
    return result