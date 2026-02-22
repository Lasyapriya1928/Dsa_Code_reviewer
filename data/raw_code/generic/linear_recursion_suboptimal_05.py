def sum_array(nums, index=0):
    if index == len(nums):
        return 0
    return nums[index] + sum_array(nums, index + 1)


nums = [1, 2, 3, 4]
print(sum_array(nums))