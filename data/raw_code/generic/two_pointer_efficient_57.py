def sliding_window_min_length(nums, k):
    left = 0
    total = 0
    min_len = float("inf")
    for right in range(len(nums)):
        total += nums[right]
        while total >= k:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len