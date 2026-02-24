def rotate_array(nums):
    left = 0
    right = len(nums) - 1
    nums[left], nums[right] = nums[right], nums[left]
    return nums