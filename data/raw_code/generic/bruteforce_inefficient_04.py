def brute_force_triplet(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if nums[i] + nums[j] + nums[k] == 0:
                    return True
    return False

#Pattern: bruteforce
