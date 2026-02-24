def all_triplet_sums(nums):
    results = []
    length = len(nums)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if i != j and j != k and i != k:
                    results.append(nums[i] + nums[j] + nums[k])
    return results