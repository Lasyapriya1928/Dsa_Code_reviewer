def sum_range(a, b):
    if a > b:
        return 0
    return a + sum_range(a + 1, b)