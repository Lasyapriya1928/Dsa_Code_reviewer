def stack_duplicate_elements(nums):
    stack = []
    for n in nums:
        stack.append(n)
        stack.append(n)
    return stack