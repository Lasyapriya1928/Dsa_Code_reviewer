def count_balanced(n, open_used=0, close_used=0):
    if open_used == n and close_used == n:
        return 1
    total = 0
    if open_used < n:
        total += count_balanced(n, open_used + 1, close_used)
    if close_used < open_used:
        total += count_balanced(n, open_used, close_used + 1)
    return total