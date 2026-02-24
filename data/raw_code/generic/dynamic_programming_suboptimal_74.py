def ways_to_reach_target(types, target):
    dp = [0]*(target+1)
    dp[0] = 1
    for count, marks in types:
        new = dp[:]
        for t in range(target+1):
            for c in range(1, count+1):
                if t + c*marks <= target:
                    new[t + c*marks] += dp[t]
        dp = new
    return dp[target]