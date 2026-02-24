def count_subarrays_less_than_k(nums, k):
    left = 0
    total = 0
    count = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= k and left <= right:
            total -= nums[left]
            left += 1
        count += right - left + 1
    return count