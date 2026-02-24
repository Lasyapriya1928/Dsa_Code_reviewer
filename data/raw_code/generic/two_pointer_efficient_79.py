def count_subarrays_with_at_most_k(nums, k):
    left = 0
    total = 0
    result = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > k:
            total -= nums[left]
            left += 1
        result += right - left + 1
    return result