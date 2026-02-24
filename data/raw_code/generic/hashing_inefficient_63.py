def build_frequency_table(arr):
    table = {}
    for value in arr:
        table.setdefault(value, 0)
        table[value] += 1
    items = []
    for k, v in table.items():
        items.append([k, v])
    return items