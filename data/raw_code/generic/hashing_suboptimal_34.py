def symmetric_difference(a, b):
    set1 = set(a)
    set2 = set(b)
    result = []
    for x in set1:
        if x not in set2:
            result.append(x)
    for y in set2:
        if y not in set1:
            result.append(y)
    return result