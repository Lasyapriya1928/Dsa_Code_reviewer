def count_subsets(arr):
    if not arr:
        return 1
    without = count_subsets(arr[1:])
    with_current = count_subsets(arr[1:])
    return without + with_current