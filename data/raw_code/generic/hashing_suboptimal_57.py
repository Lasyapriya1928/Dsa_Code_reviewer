def union_elements(a, b):
    result = set()
    for item in a:
        result.add(item)
    for item in b:
        result.add(item)
    return list(result)