def any_triplet_negative(nums):
    size = len(nums)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if i != j and j != k and i != k:
                    if nums[i] < 0 and nums[j] < 0 and nums[k] < 0:
                        return True
    return False