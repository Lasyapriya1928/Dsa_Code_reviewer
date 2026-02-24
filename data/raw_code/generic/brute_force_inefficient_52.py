def triplet_indices_sum(nums):
    result = []
    n = len(nums)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a < b < c:
                    result.append(a + b + c)
    return result