def triplet_all_positive(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if nums[i] > 0 and nums[j] > 0 and nums[k] > 0:
                        return True
    return False