def stock_span(prices):
    stack = []
    span = []

    for i in range(len(prices)):
        count = 1
        while stack and prices[i] >= prices[stack[-1]]:
            count += span[stack.pop()]
        stack.append(i)
        span.append(count)

    return span


prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))