def count_subarrays_at_most_sum(nums, limit):
    left = 0
    total = 0
    result = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > limit:
            total -= nums[left]
            left += 1
        result += right - left + 1
    return result