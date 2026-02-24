def find_two_numbers(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return (nums[l], nums[r])
        if s < target:
            l += 1
        else:
            r -= 1
    return None