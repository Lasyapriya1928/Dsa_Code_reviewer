def reverse_string_list(words):
    if not words:
        return []
    rest = reverse_string_list(words[1:])
    rest.append(words[0])
    return rest