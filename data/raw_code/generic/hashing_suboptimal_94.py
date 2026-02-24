def union_list(a, b):
    result = set(a)
    for item in b:
        result.add(item)
    return list(result)