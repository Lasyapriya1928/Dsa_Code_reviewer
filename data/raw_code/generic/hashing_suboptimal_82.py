def count_values(nums):
    table = {}
    for n in nums:
        table[n] = table.get(n, 0) + 1
    total = 0
    for key in table:
        total += 1
    return total