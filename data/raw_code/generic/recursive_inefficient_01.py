def recursion_factorial(n):
    if n <= 1:
        return 1
    return n * recursion_factorial(n - 1)

#Pattern: recursive
