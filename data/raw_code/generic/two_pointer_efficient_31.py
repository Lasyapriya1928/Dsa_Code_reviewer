def sliding_window_max_sum(nums, k):
    left = 0
    total = 0
    best = 0
    for right in range(len(nums)):
        total += nums[right]
        if right - left + 1 > k:
            total -= nums[left]
            left += 1
        if right - left + 1 == k:
            best = max(best, total)
    return best