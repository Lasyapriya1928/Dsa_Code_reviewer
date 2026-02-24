def find_pair_gap(nums):
    gap = -1
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            current = nums[j] - nums[i]
            if current > gap:
                gap = current
            j += 1
    return gap