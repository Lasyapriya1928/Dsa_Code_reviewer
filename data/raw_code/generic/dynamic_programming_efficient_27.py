def max_sum_no_adjacent(nums):
    incl, excl = 0, 0
    for num in nums:
        new_excl = max(incl, excl)
        incl = excl + num
        excl = new_excl
    return max(incl, excl)