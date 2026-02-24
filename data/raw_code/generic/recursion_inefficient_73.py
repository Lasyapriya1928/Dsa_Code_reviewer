def subsets_count(n):
    if n == 0:
        return 1
    return subsets_count(n - 1) * 2