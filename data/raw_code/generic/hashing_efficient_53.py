def max_length_unique(nums):
    seen = set()
    left = 0
    best = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            left += 1
        seen.add(nums[right])
        current = right - left + 1
        if current > best:
            best = current
    return best