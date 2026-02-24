def count_shared_elements(a, b):
    lookup = set(a)
    count = 0
    for item in b:
        if item in lookup:
            count += 1
    return count