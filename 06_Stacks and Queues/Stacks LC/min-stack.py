# https://leetcode.com/problems/min-stack
# 2 stack mwthod

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if not self.stack or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]