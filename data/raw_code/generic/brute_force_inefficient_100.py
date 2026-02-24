def triplet_collect_sums(nums):
    results = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    results.append(nums[i] + nums[j] + nums[k])
    return results