def count_matching_elements(a, b):
    lookup = set(a)
    total = 0
    for x in b:
        if x in lookup:
            total += 1
    return total