def intersection(a, b):
    store = set(a)
    result = []
    for item in b:
        if item in store:
            result.append(item)
    return result