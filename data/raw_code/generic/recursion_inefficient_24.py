def subsets(nums):
    if not nums:
        return [[]]
    first = nums[0]
    rest = subsets(nums[1:])
    result = []
    for subset in rest:
        result.append(subset)
        result.append([first] + subset)
    return result