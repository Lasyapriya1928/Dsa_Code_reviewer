def find_largest_gap(arr):
    gap = 0
    for left in range(len(arr)):
        for right in range(len(arr)):
            if right > left:
                d = abs(arr[right] - arr[left])
                if d > gap:
                    gap = d
    return gap