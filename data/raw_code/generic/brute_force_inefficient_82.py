def triplet_max_product(nums):
    best = float("-inf")
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    product = nums[i] * nums[j] * nums[k]
                    if product > best:
                        best = product
    return best