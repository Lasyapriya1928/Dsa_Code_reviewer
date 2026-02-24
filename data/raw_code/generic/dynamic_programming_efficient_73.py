def max_coins_piles(piles):
    piles.sort()
    n = len(piles)
    dp = 0
    left = 0
    right = n-1
    for _ in range(n//3):
        right -= 1
        dp += piles[right]
        right -= 1
        left += 1
    return dp