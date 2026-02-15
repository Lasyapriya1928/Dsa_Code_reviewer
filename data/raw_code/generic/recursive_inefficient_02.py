def recursion_binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursion_binary_search(arr, target, left, mid - 1)
    else:
        return recursion_binary_search(arr, target, mid + 1, right)

#Pattern: recursive
