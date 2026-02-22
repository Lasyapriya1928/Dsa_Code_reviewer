def find_duplicate_pairs(nums):
    n = len(nums)
    pairs = []

    for i in range(n):
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                pairs.append((nums[i], nums[j]))

    return pairs


nums = [1, 2, 3, 1, 2]
print(find_duplicate_pairs(nums))