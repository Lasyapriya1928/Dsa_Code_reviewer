def recursion_power(x, n):
    if n == 0:
        return 1
    return x * recursion_power(x, n - 1)

#Pattern: recursive
