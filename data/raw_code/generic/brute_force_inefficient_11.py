def count_inversions(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] > nums[j]:
                total += 1
    return total