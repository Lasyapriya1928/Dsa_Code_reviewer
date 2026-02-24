def reverse_chunks(nums, size):
    for start in range(0, len(nums), size):
        end = min(start + size - 1, len(nums) - 1)
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    return nums