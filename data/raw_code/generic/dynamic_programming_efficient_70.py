def count_good_strings(low, high, zero, one):
    dp = [0]*(high+1)
    dp[0] = 1
    total = 0
    for i in range(1, high+1):
        if i-zero >= 0:
            dp[i] += dp[i-zero]
        if i-one >= 0:
            dp[i] += dp[i-one]
        if low <= i <= high:
            total += dp[i]
    return total