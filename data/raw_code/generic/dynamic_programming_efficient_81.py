def longest_valid_parentheses(s):
    n = len(s)
    dp = [0] * n
    res = 0
    for i in range(1, n):
        if s[i] == ')':
            prev = i - dp[i-1] - 1
            if prev >= 0 and s[prev] == '(':
                dp[i] = dp[i-1] + 2
                if prev > 0:
                    dp[i] += dp[prev-1]
        res = max(res, dp[i])
    return res