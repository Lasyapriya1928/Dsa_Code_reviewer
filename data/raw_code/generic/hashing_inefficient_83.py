def index_mapping(arr):
    mapping = {}
    for i in range(len(arr)):
        mapping[arr[i]] = i
    result = []
    for k, v in mapping.items():
        result.append((k, v))
    return result