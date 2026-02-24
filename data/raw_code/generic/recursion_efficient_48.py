def count_binary_strings(n, last=0):
    if n == 0:
        return 1
    if last == 1:
        return count_binary_strings(n - 1, 0)
    return count_binary_strings(n - 1, 0) + count_binary_strings(n - 1, 1)