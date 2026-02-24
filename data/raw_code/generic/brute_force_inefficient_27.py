def zero_sum_triplet(nums):
    length = len(nums)
    for x in range(length):
        for y in range(length):
            for z in range(length):
                if x != y and y != z and x != z:
                    if nums[x] + nums[y] + nums[z] == 0:
                        return True
    return False