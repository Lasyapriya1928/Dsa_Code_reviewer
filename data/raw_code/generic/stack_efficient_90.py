def min_stack(nums):
    stack = []
    min_values = []
    for n in nums:
        stack.append(n)
        if not min_values or n <= min_values[-1]:
            min_values.append(n)
    return min_values[-1] if min_values else None