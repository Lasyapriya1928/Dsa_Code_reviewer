def count_equal_values(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] == nums[j]:
                    total += 1
    return total