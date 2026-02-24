def count_distinct_subarrays(nums):
    left = 0
    seen = set()
    total = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        total += right - left + 1
    return total