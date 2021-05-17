class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tmp = []
        self.min1 = []

    def push(self, val: int) -> None:
        self.tmp.append(val)
        if not self.min1:
            self.min1.append(val)
        else:
            self.min1.append(min(val, self.min1[-1]))

    def pop(self) -> None:
        self.tmp.pop()
        self.min1.pop()

    def top(self) -> int:
        return self.tmp[-1]

    def getMin(self) -> int:
        return self.min1[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
