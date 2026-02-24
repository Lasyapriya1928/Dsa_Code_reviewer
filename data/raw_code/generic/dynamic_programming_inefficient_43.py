def palindrome_partition_min_cut(s):
    n = len(s)
    dp = [0]*n
    pal = [[False]*n for _ in range(n)]
    for i in range(n):
        dp[i] = i
        for j in range(i+1):
            if s[i] == s[j] and (i-j < 2 or pal[j+1][i-1]):
                pal[j][i] = True
                dp[i] = 0 if j == 0 else min(dp[i], dp[j-1]+1)
    return dp[-1]