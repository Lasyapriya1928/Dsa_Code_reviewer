def find_all_pairs(nums):
    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                pairs.append((nums[i], nums[j]))
    return pairs