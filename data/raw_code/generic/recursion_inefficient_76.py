def triple_step(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)