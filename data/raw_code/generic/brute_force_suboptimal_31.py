def check_strict_increase(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[i]:
                return False
    return True