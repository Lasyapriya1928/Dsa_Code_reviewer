def binary_strings_no_consecutive(n, last=0):
    if n == 0:
        return 1
    total = binary_strings_no_consecutive(n - 1, 0)
    if last == 0:
        total += binary_strings_no_consecutive(n - 1, 1)
    return total