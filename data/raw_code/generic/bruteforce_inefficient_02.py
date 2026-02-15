def brute_force_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += arr[k]
            max_sum = max(max_sum, total)
    return max_sum
