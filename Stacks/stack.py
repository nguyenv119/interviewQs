from typing import List
class MinStack:
    arr: List[int]
    currMin: int
    '''
    currMin = inf
    currMin2 = inf
    [1, -10]

    if length is 2: if 
    '''

    def __init__(self):
        arr = list()

    def push(self, val: int) -> None:
        self.arr.append(val)

        if len(self.arr) >= 2:
            if val <= self.currMin: 
                self.currMin2 = self.currMin
                self.currMin = val
            else: self.currMin2 = val

        else: self.currMin = val

        return None

    def pop(self) -> None:
        self.arr.remove(self.arr[0])
        self.currMin = self.currMin2

        return None

    def top(self) -> int:
        return self.arr[0]

    def getMin(self) -> int:
        return self.currMin

    def test(self):
        minStack =  MinStack()
        assert print(minStack) == []
        minStack.push(-2)
        assert print(minStack) == [-2]
        minStack.push(0)
        assert print(minStack) == [-2, 0]
        minStack.push(-3)
        assert print(minStack) == [-2, 0, -3]
        assert minStack.getMin() == -3
        minStack.pop()
        assert minStack.top() == 0
        assert minStack.getMin() == -2

        print("All Tests Passed Succesfully!")
