def has_pair_difference_k(nums, k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and abs(nums[i] - nums[j]) == k:
                return True
    return False