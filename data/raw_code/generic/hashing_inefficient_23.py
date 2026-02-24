def frequency_map(values):
    table = {}
    for element in values:
        if element not in table:
            table[element] = 0
        table[element] += 1
    result = []
    for key in table.keys():
        result.append((key, table[key]))
    return result