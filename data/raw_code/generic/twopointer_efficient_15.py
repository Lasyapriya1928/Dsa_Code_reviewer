def partition_array(nums, pivot):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] < pivot:
            left += 1
        elif nums[right] >= pivot:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]

    return nums


print(partition_array([9,12,3,5,14,10,10], 10))