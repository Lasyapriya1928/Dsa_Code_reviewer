def triplet_even_sum(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if (nums[i] + nums[j] + nums[k]) % 2 == 0:
                        return True
    return False