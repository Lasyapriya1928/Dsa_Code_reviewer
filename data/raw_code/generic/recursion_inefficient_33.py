def all_paths(grid, r=0, c=0):
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    if r >= len(grid) or c >= len(grid[0]):
        return 0
    return all_paths(grid, r + 1, c) + all_paths(grid, r, c + 1)