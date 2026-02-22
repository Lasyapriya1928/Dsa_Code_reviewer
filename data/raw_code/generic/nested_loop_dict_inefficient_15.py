def count_same_values(d1, d2):
    count = 0

    for k1 in d1:
        for k2 in d2:
            if d1[k1] == d2[k2]:
                count += 1

    return count


d1 = {"x": 10, "y": 20, "z": 30}
d2 = {"a": 20, "b": 30, "c": 40}
print(count_same_values(d1, d2))