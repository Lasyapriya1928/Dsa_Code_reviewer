def all_triplet_indices(nums):
    out = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    out.append((i, j, k))
    return out