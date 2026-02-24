def common_count(a, b):
    total = 0
    for item in a:
        for element in b:
            if item == element:
                total += 1
    return total