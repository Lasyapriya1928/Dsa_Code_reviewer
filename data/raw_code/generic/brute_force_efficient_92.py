def pair_sum_exists(nums, target):
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a != b and nums[a] + nums[b] == target:
                return True
    return False