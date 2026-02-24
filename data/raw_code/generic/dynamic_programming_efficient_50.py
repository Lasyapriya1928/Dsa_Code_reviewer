def can_partition_k_subsets(nums, k):
    total = sum(nums)
    if total % k:
        return False
    target = total // k
    used = [False]*len(nums)
    def backtrack(start, k, curr_sum):
        if k == 1:
            return True
        if curr_sum == target:
            return backtrack(0, k-1, 0)
        for i in range(start, len(nums)):
            if not used[i] and curr_sum + nums[i] <= target:
                used[i] = True
                if backtrack(i+1, k, curr_sum+nums[i]):
                    return True
                used[i] = False
        return False
    return backtrack(0, k, 0)