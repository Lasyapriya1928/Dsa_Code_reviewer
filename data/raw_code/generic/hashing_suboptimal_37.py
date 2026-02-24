def common_unique(a, b):
    store = set(a)
    result = set()
    for item in b:
        if item in store:
            result.add(item)
    return list(result)