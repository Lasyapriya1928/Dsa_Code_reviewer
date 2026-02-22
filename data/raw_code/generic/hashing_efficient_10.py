def first_unique_char(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for index, char in enumerate(s):
        if count[char] == 1:
            return index

    return -1


print(first_unique_char("leetcode"))