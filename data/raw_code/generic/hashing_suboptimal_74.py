def union_size(a, b):
    combined = set()
    for x in a:
        combined.add(x)
    for y in b:
        combined.add(y)
    return len(combined)