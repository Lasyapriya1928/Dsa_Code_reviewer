def triplet_min_product(nums):
    smallest = None
    n = len(nums)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a != b and b != c and a != c:
                    val = nums[a] * nums[b] * nums[c]
                    if smallest is None or val < smallest:
                        smallest = val
    return smallest