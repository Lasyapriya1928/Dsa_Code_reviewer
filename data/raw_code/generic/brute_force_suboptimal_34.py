def count_matching_positions(a, b):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j and a[i] == b[j]:
                count += 1
    return count