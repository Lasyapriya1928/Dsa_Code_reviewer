def next_smaller_indices(arr):
    stack = []
    res = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res