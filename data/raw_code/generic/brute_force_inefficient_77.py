def triplet_any_equal(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if nums[i] == nums[j] or nums[j] == nums[k] or nums[i] == nums[k]:
                        return True
    return False