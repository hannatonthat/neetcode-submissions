class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1
