def generate_permutations(nums):
    result = []

    def helper(path, remaining):
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            helper(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    helper([], nums)
    return result


nums = [1, 2, 3]
print(generate_permutations(nums))