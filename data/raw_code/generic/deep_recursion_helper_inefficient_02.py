def generate_subsets(nums):
    result = []

    def helper(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        current.append(nums[index])
        helper(index + 1, current)
        current.pop()

        helper(index + 1, current)

    helper(0, [])
    return result


nums = [1, 2, 3]
print(generate_subsets(nums))