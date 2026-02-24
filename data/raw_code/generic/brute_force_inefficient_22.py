def three_equal(nums):
    n = len(nums)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a != b and b != c and a != c:
                    if nums[a] == nums[b] == nums[c]:
                        return True
    return False