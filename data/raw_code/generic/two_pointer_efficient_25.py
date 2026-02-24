def longest_subarray_sum_k(nums, k):
    left = 0
    total = 0
    max_len = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > k and left <= right:
            total -= nums[left]
            left += 1
        if total == k:
            max_len = max(max_len, right - left + 1)
    return max_len