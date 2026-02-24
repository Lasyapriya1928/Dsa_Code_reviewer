def count_pairs_difference(nums, diff):
    nums.sort()
    left = 0
    right = 1
    count = 0
    while right < len(nums):
        if left == right:
            right += 1
            continue
        current = nums[right] - nums[left]
        if current == diff:
            count += 1
            left += 1
            right += 1
        elif current < diff:
            right += 1
        else:
            left += 1
    return count