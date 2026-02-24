def smallest_triplet_sum(nums):
    best = None
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    val = nums[i] + nums[j] + nums[k]
                    if best is None or val < best:
                        best = val
    return best