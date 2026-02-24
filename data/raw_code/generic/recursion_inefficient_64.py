def staircase(n):
    if n <= 1:
        return 1
    return staircase(n - 1) + staircase(n - 2)