def sliding_window_average(nums, k):
    left = 0
    total = 0
    result = []
    for right in range(len(nums)):
        total += nums[right]
        if right - left + 1 > k:
            total -= nums[left]
            left += 1
        if right - left + 1 == k:
            result.append(total / k)
    return result