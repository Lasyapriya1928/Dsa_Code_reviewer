def find_difference_count(a, b):
    sb = set(b)
    count = 0
    for val in a:
        if val not in sb:
            count += 1
    return count