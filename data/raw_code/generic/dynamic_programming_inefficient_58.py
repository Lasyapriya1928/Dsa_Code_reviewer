def maximum_sum_with_deletion(arr):
    n = len(arr)
    dp0 = [0]*n
    dp1 = [0]*n
    dp0[0] = arr[0]
    dp1[0] = 0
    result = arr[0]
    for i in range(1, n):
        dp0[i] = max(arr[i], dp0[i-1] + arr[i])
        dp1[i] = max(dp0[i-1], dp1[i-1] + arr[i])
        result = max(result, dp0[i], dp1[i])
    return result