def count_paths(n, m):
    if n == 1 or m == 1:
        return 1
    return count_paths(n - 1, m) + count_paths(n, m - 1)