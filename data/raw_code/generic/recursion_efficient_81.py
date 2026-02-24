def max_depth_list(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    depths = []
    for item in lst:
        depths.append(max_depth_list(item))
    return 1 + max(depths)