def count_grid_paths(n, m, memo=None):
    if memo is None:
        memo = {}
    if (n, m) in memo:
        return memo[(n, m)]
    if n == 1 or m == 1:
        return 1
    memo[(n, m)] = count_grid_paths(n - 1, m, memo) + count_grid_paths(n, m - 1, memo)
    return memo[(n, m)]