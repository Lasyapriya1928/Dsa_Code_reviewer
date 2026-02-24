def calculate_span(prices):
    stack = []
    span = []
    for price in prices:
        count = 1
        while stack and stack[-1][0] <= price:
            count += stack.pop()[1]
        stack.append((price, count))
        span.append(count)
    return span