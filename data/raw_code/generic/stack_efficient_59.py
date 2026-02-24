def remove_duplicates_once(nums):
    stack = []
    seen = set()
    for n in nums:
        if n not in seen:
            stack.append(n)
            seen.add(n)
    return stack