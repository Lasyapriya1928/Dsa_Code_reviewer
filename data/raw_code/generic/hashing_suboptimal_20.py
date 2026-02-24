def find_difference(a, b):
    set_a = set(a)
    set_b = set(b)
    result = []
    for x in set_a:
        if x not in set_b:
            result.append(x)
    for y in set_b:
        if y not in set_a:
            result.append(y)
    return result