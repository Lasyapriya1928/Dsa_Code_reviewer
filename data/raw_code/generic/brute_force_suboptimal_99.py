def count_pairs_absolute(nums, value):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == value:
                count += 1
    return count