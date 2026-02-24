def min_stack_operations(nums):
    stack = []
    mins = []
    for n in nums:
        stack.append(n)
        if not mins or n <= mins[-1]:
            mins.append(n)
    result = []
    while stack:
        val = stack.pop()
        if val == mins[-1]:
            mins.pop()
        result.append(val)
    return result