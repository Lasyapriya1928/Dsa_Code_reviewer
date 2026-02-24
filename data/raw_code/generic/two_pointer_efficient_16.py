def find_pair_difference(nums, diff):
    nums.sort()
    left = 0
    right = 1
    while right < len(nums):
        if left == right:
            right += 1
            continue
        current = nums[right] - nums[left]
        if current == diff:
            return True
        if current < diff:
            right += 1
        else:
            left += 1
    return False