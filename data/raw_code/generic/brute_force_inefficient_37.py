def count_all_pairs(nums):
    total = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                total += 1
    return total