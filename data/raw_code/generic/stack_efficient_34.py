def histogram_widths(heights):
    stack = []
    widths = [0] * len(heights)
    for i in range(len(heights)):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        widths[i] = i - stack[-1] - 1 if stack else i
        stack.append(i)
    return widths