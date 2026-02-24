def search_tree(node, target):
    if node is None:
        return False
    if node.get("value") == target:
        return True
    return search_tree(node.get("left"), target) or search_tree(node.get("right"), target)