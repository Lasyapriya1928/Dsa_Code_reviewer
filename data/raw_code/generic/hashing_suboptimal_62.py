def count_common(a, b):
    seen = set(a)
    total = 0
    for item in b:
        if item in seen:
            total += 1
    return total