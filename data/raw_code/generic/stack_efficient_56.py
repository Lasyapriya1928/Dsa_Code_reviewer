def stock_span(prices):
    stack = []
    span = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        span.append(i + 1 if not stack else i - stack[-1])
        stack.append(i)
    return span