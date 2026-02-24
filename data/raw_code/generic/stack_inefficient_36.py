def stack_sort(nums):
    stack = []
    temp = []
    for n in nums:
        while stack and stack[-1] > n:
            temp.append(stack.pop())
        stack.append(n)
        while temp:
            stack.append(temp.pop())
    return stack