def find_max(nums, index=0):
    if index == len(nums) - 1:
        return nums[index]

    current = nums[index]
    rest_max = find_max(nums, index + 1)
    return current if current > rest_max else rest_max


nums = [3, 7, 2, 9, 5]
print(find_max(nums))