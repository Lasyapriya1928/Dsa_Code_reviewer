def common_unique_count(a, b):
    first = set(a)
    second = set(b)
    count = 0
    for item in first:
        if item in second:
            count += 1
    return count