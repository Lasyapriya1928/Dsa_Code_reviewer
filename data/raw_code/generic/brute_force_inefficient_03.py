def max_pair_product(a):
    best = None
    i = 0
    while i < len(a):
        j = 0
        while j < len(a):
            if i != j:
                prod = a[i] * a[j]
                if best is None or prod > best:
                    best = prod
            j += 1
        i += 1
    return best