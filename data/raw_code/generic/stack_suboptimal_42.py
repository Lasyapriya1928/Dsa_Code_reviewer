def dfs_stack(graph, start):
    stack = [start]
    visited = set()
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph.get(node, []):
                stack.append(neighbor)
    return order