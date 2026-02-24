def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]
        for p in permutations(rest):
            result.append([nums[i]] + p)
    return result