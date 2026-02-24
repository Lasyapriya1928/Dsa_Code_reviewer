def missing_number(nums):
    expected = set(range(len(nums) + 1))
    actual = set(nums)
    diff = expected - actual
    return diff.pop()