def max_pair_difference(nums):
    maximum = float("-inf")
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                diff = nums[j] - nums[i]
                if diff > maximum:
                    maximum = diff
    return maximum