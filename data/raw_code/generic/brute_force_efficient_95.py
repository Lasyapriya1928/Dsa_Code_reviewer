def first_pair_same_parity(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] % 2 == nums[j] % 2:
                    return (i, j)
    return None