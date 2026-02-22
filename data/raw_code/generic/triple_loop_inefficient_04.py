def count_equal_triplets(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j < k:
                    if nums[i] == nums[j] == nums[k]:
                        count += 1

    return count


nums = [1, 2, 1, 1, 2]
print(count_equal_triplets(nums))