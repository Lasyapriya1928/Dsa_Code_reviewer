def triplet_all_negative(nums):
    size = len(nums)
    for a in range(size):
        for b in range(size):
            for c in range(size):
                if a != b and b != c and a != c:
                    if nums[a] < 0 and nums[b] < 0 and nums[c] < 0:
                        return True
    return False