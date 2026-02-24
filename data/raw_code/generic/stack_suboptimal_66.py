def remove_k_adjacent(nums, k):
    stack = []
    for n in nums:
        if stack and stack[-1][0] == n:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([n, 1])
    result = []
    for val, count in stack:
        result.extend([val] * count)
    return result