def first_pair_equal_sum(nums, target):
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a != b:
                if nums[a] + nums[b] == target:
                    return [a, b]
    return []