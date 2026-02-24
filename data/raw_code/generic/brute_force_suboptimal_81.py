def count_pairs_with_sum(nums, target):
    total = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] + nums[j] == target:
                    total += 1
    return total