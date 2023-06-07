class MinStack:

    def __init__(self):
        self.stack = list()
        self.stackMin = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackMin: self.stackMin.append(min(val, self.stackMin[-1]))
        else: self.stackMin.append(val)
        return None

    def pop(self) -> None:
        if self.stack: self.stack.pop()
        if self.stackMin: self.stackMin.pop()
        return None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stackMin[len(self.stack) - 1]

    def test(self):
        minStack =  MinStack()
        assert minStack.stack == []
        minStack.push(-2)
        assert minStack.stack == [-2]
        minStack.push(0)
        assert minStack.stack == [-2, 0]
        minStack.push(-3)
        assert minStack.stack == [-2, 0, -3]
        assert minStack.getMin() == -3
        minStack.push(-3)
        assert minStack.stack == [-2, 0, -3, -3]
        assert minStack.getMin() == -3
        minStack.pop()
        minStack.pop()
        assert minStack.top() == 0
        assert minStack.getMin() == -2

        print("All Tests Passed Succesfully!")

minStack =  MinStack()
minStack.test()