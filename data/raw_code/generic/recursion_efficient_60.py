def count_leaves(node):
    if node is None:
        return 0
    if not node.get("left") and not node.get("right"):
        return 1
    return count_leaves(node.get("left")) + count_leaves(node.get("right"))