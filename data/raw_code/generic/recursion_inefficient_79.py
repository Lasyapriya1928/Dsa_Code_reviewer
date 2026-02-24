def sum_power(n, p):
    if n == 0:
        return 0
    return n ** p + sum_power(n - 1, p)