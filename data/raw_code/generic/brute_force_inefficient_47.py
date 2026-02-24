def triplet_all_distinct(nums):
    n = len(nums)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if x != y and y != z and x != z:
                    if nums[x] != nums[y] and nums[y] != nums[z] and nums[x] != nums[z]:
                        return True
    return False