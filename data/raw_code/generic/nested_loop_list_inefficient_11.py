def common_elements(list1, list2):
    result = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                result.append(list1[i])

    return result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common_elements(a, b))