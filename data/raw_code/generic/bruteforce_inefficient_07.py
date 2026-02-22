def count_zero_sum_triplets(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        count += 1

    return count


nums = [-1, 0, 1, 2, -1, -4]
print(count_zero_sum_triplets(nums))