def power_linear(x, n):
    if n == 0:
        return 1
    return x * power_linear(x, n - 1)