def triplet_sum_list(nums):
    sums = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    sums.append(nums[i] + nums[j] + nums[k])
    return sums