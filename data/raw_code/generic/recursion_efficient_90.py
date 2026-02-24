def find_peak(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low == high:
        return low
    mid = (low + high) // 2
    if arr[mid] < arr[mid + 1]:
        return find_peak(arr, mid + 1, high)
    return find_peak(arr, low, mid)