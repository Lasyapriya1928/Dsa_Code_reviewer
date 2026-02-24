def count_true(values, i=0):
    if i == len(values):
        return 0
    return (1 if values[i] else 0) + count_true(values, i + 1)