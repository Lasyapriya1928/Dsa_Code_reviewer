def fib_variant(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = fib_variant(n - 1)
    b = fib_variant(n - 2)
    return a + b