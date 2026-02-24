def exclusive_time(n, logs):
    stack = []
    times = [0] * n
    prev = 0
    for log in logs:
        idx, typ, t = log.split(':')
        idx, t = int(idx), int(t)
        if typ == 'start':
            if stack:
                times[stack[-1]] += t - prev
            stack.append(idx)
            prev = t
        else:
            times[stack.pop()] += t - prev + 1
            prev = t + 1
    return times