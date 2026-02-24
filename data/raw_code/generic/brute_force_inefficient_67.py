def triplet_index_product(nums):
    result = []
    n = len(nums)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if x < y < z:
                    result.append(x * y * z)
    return result