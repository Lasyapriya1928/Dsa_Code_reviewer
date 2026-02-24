def min_pair_sum(values):
    smallest = float("inf")
    for a in range(len(values)):
        for b in range(len(values)):
            if a < b:
                current = values[a] + values[b]
                if current < smallest:
                    smallest = current
    return smallest