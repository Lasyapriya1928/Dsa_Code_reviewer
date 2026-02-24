def common_elements(a, b):
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
    return result