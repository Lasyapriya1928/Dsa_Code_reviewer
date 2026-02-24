def stack_filter_even(nums):
    stack = []
    for n in nums:
        if n % 2 == 0:
            stack.append(n)
    return stack