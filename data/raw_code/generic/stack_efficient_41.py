class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop() if self.data else None
    def top(self):
        return self.data[-1] if self.data else None

def evaluate_reverse_polish(tokens):
    s = Stack()
    for t in tokens:
        if t in "+-*":
            b = s.pop()
            a = s.pop()
            if t == '+':
                s.push(a + b)
            elif t == '-':
                s.push(a - b)
            else:
                s.push(a * b)
        else:
            s.push(int(t))
    return s.pop()