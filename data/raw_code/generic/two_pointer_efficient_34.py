def longest_k_distinct(nums, k):
    left = 0
    counts = {}
    max_len = 0
    for right in range(len(nums)):
        counts[nums[right]] = counts.get(nums[right], 0) + 1
        while len(counts) > k:
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len