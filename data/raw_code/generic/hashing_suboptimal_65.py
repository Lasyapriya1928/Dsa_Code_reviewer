def difference_between_lists(a, b):
    second = set(b)
    output = []
    for element in a:
        if element not in second:
            output.append(element)
    return output