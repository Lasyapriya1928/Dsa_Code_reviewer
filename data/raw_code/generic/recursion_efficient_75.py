def balanced_parentheses(n, open_count=0, close_count=0):
    if open_count == n and close_count == n:
        return 1
    total = 0
    if open_count < n:
        total += balanced_parentheses(n, open_count + 1, close_count)
    if close_count < open_count:
        total += balanced_parentheses(n, open_count, close_count + 1)
    return total