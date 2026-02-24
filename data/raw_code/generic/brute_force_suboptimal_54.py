def total_pair_products(nums):
    total = 0
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            total += nums[x] * nums[y]
    return total