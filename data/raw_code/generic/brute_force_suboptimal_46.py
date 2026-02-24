def exists_smaller_before(arr):
    for i in range(len(arr)):
        found = False
        for j in range(i):
            if arr[j] < arr[i]:
                found = True
        if not found and i != 0:
            return False
    return True