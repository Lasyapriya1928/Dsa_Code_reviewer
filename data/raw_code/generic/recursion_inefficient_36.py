def hanoi(n, source, target, aux):
    if n == 0:
        return []
    moves = hanoi(n - 1, source, aux, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, aux, target, source))
    return moves