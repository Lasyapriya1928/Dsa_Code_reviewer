def triplet_all_even(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if nums[i] % 2 == 0 and nums[j] % 2 == 0 and nums[k] % 2 == 0:
                        return True
    return False