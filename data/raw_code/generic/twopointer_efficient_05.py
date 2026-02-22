def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


print(two_sum_sorted([1,2,3,4,6], 6))