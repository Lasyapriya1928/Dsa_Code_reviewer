def sum_triangle(n):
    if n == 1:
        return 1
    return n + sum_triangle(n - 1)