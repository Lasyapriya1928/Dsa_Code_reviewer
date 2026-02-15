def stack_next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(nums[i])

    return result

#Pattern: stack
