def are_disjoint(a, b):
    store = set(a)
    for element in b:
        if element in store:
            return False
    return True