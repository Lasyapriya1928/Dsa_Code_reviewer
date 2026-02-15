def brute_force_pair(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                return True
    return False
