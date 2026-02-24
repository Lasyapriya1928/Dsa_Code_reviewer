def triplet_with_target(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if nums[i] + nums[j] + nums[k] == target:
                        return (i, j, k)
    return None