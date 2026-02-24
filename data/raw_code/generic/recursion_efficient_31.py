def count_nodes(tree):
    if tree is None:
        return 0
    return 1 + count_nodes(tree.get("left")) + count_nodes(tree.get("right"))