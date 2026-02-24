def next_warmer_day(temps):
    stack = []
    answer = [0] * len(temps)
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    return answer