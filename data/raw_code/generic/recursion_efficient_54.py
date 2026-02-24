def search_rotated(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            return search_rotated(arr, target, low, mid - 1)
        return search_rotated(arr, target, mid + 1, high)
    if arr[mid] < target <= arr[high]:
        return search_rotated(arr, target, mid + 1, high)
    return search_rotated(arr, target, low, mid - 1)