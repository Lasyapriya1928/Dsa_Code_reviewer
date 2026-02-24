def print_numbers(n):
    if n == 0:
        return []
    return print_numbers(n - 1) + [n]