def find_min_difference(arr):
    minimum = float('inf')
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                diff = abs(arr[i] - arr[j])
                if diff < minimum:
                    minimum = diff
    return minimum