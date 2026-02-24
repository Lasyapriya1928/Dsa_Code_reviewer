def height_tree(node):
    if node is None:
        return 0
    left = height_tree(node.get("left"))
    right = height_tree(node.get("right"))
    return 1 + max(left, right)