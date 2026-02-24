def reverse_dictionary(d):
    reversed_map = {}
    for key in d:
        reversed_map[d[key]] = key
    return reversed_map