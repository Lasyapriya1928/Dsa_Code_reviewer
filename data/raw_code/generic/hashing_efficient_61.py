def find_pairs_with_sum(nums, target):
    needed = {}
    result = []
    for i, v in enumerate(nums):
        if v in needed:
            result.append((needed[v], i))
        else:
            needed[target - v] = i
    return result