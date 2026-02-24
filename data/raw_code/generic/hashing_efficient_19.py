def can_construct(ransom, magazine):
    supply = {}
    for ch in magazine:
        supply[ch] = supply.get(ch, 0) + 1
    for ch in ransom:
        if ch not in supply or supply[ch] == 0:
            return False
        supply[ch] -= 1
    return True