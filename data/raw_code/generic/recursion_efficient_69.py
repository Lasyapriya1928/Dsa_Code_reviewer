def kth_smallest(arr, k):
    if not arr:
        return None
    pivot = arr[len(arr)//2]
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return kth_smallest(lows, k)
    if k < len(lows) + len(pivots):
        return pivot
    return kth_smallest(highs, k - len(lows) - len(pivots))