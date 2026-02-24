def combination_sum(nums, target):
    if target == 0:
        return [[]]
    if target < 0 or not nums:
        return []
    with_first = []
    for comb in combination_sum(nums, target - nums[0]):
        with_first.append([nums[0]] + comb)
    without_first = combination_sum(nums[1:], target)
    return with_first + without_first