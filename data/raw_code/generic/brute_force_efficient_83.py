def first_pair_less_than(nums, limit):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y:
                if nums[x] + nums[y] < limit:
                    return (x, y)
    return None