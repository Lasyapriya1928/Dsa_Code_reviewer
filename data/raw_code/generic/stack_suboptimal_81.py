def reverse_stack_inplace(nums):
    stack = []
    for x in nums:
        stack.append(x)
    nums.clear()
    while stack:
        nums.append(stack.pop())
    return nums