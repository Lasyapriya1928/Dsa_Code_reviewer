def difference_elements(a, b):
    sb = set(b)
    result = []
    for val in a:
        if val not in sb:
            result.append(val)
    return result