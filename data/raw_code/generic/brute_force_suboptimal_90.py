def count_pairs_multiple_of_three(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) % 3 == 0:
                total += 1
    return total