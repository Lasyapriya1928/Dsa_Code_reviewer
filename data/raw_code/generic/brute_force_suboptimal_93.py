def count_pairs_strict(nums):
    count = 0
    for i in range(len(nums)):
        j = 0
        while j < len(nums):
            if i < j and nums[i] < nums[j]:
                count += 1
            j += 1
    return count