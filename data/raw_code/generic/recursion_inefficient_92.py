def dice_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for step in range(1, 7):
        total += dice_ways(n - step)
    return total