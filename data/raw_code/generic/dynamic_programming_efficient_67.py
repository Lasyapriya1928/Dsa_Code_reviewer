def job_scheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)
    dp = [0]*(n+1)
    import bisect
    ends = [job[1] for job in jobs]
    for i in range(1, n+1):
        s, e, p = jobs[i-1]
        idx = bisect.bisect_right(ends, s)
        dp[i] = max(dp[i-1], dp[idx] + p)
    return dp[n]