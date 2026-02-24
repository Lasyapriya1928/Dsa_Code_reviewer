def difference_set(a, b):
    first = set(a)
    second = set(b)
    output = []
    for item in first:
        if item not in second:
            output.append(item)
    return output