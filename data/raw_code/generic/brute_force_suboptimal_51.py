def max_difference_pair(arr):
    diff = float("-inf")
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > diff:
                diff = arr[j] - arr[i]
    return diff