def contains_pair_multiple(nums, m):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if (nums[i] + nums[j]) % m == 0:
                    return True
    return False