def count_subarrays_with_sum(nums, k):
    left = 0
    total = 0
    count = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > k and left <= right:
            total -= nums[left]
            left += 1
        if total == k:
            count += 1
    return count