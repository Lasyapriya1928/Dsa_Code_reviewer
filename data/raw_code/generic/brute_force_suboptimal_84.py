def count_pairs_even_sum(arr):
    count = 0
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if (arr[i] + arr[j]) % 2 == 0:
                count += 1
            j += 1
        i += 1
    return count