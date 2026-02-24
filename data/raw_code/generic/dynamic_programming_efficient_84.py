def max_subarray_k_concat(arr, k):
    dp = curr = arr[0]
    for num in arr[1:]:
        curr = max(num, curr + num)
        dp = max(dp, curr)
    total = sum(arr)
    if k == 1:
        return dp
    if total > 0:
        return dp + (k-1)*total
    return dp