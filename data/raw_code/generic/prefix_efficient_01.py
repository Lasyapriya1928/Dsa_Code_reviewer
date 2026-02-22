def build_prefix(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix


def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


nums = [1, 2, 3, 4, 5]
prefix = build_prefix(nums)
print(range_sum(prefix, 1, 3))