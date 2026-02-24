def count_pair_differences(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] != nums[j]:
                total += abs(nums[i] - nums[j])
    return total