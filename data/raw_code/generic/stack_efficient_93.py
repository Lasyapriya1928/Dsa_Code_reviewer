def asteroid_collision_variant(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while stack and a < 0 < stack[-1]:
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop()
                alive = False
                break
            else:
                alive = False
                break
        if alive:
            stack.append(a)
    return stack