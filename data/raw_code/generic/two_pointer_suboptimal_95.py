def count_unique_pairs(nums):
    nums.sort()
    left = 0
    right = 1
    count = 0
    while right < len(nums):
        if nums[left] != nums[right]:
            count += 1
        left += 1
        right += 1
    return count