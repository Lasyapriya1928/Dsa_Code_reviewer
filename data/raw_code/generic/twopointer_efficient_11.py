def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    index = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result


print(sorted_squares([-4,-1,0,3,10]))