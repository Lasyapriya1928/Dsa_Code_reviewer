def element_exists_twice(data):
    i = 0
    while i < len(data):
        j = i + 1
        while j < len(data):
            if data[i] == data[j]:
                return True
            j += 1
        i += 1
    return False