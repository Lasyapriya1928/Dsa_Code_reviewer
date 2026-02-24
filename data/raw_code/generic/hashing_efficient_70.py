def longest_distinct(nums):
    seen = set()
    left = 0
    best = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        best = max(best, right - left + 1)
    return best