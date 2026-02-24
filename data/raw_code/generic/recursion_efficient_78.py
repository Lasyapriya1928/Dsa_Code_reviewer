def matrix_paths(grid, r=0, c=0, memo=None):
    if memo is None:
        memo = {}
    if (r, c) in memo:
        return memo[(r, c)]
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    if r >= len(grid) or c >= len(grid[0]):
        return 0
    memo[(r, c)] = matrix_paths(grid, r + 1, c, memo) + matrix_paths(grid, r, c + 1, memo)
    return memo[(r, c)]