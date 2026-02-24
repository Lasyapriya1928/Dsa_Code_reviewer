def triplet_equal_target(nums, target):
    n = len(nums)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if x != y and y != z and x != z:
                    if nums[x] + nums[y] + nums[z] == target:
                        return True
    return False