def reverse_subarray(nums, start, end):
    i = start
    j = end
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums