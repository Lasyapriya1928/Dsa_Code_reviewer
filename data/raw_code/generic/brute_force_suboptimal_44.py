def position_matches(a, b):
    matches = []
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                if a[i] == b[j]:
                    matches.append(i)
    return matches