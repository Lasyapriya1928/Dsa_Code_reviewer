def triplet_collect_indices(nums):
    indices = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    indices.append((i, j, k))
    return indices