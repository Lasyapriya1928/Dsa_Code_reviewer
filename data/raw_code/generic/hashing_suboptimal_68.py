def find_unique_in_two(a, b):
    sa = set(a)
    sb = set(b)
    result = []
    for x in sa:
        if x not in sb:
            result.append(x)
    return result