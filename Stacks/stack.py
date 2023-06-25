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

    def generateParenthesis(self, n: int) -> List[str]:
        '''
        There is a max of n ( and n ) in each parentheses
        We need a way to determine what is a valid parentheses?

        --> When there is a starting ( that eventually ends with )
        How many ways can we rearrange ( such that it eventually ends with )

        For every x number of "(" we have, there are at most x number of ")":
        - ()) cannot work

        - We can keep adding ( n times, and after each time we add, we can either
        add another (, or a ), this is until we have completely added n (s, so in
        that case we have to add the remaining )
        --> should have a var calculating how many ( and ) we have added

        - beginning( and end) variables start out the same
        - When they are the same, we must add (, and when beginning < end, we can
        add either

        We can treat it like a stack, decision tree. Every time we add, we have 
        to see the restrictions on the () variables, and then call it recursively.
        Every time we finish adding, we pop as to rewind in the tree and allow
        other combinations to form

        '''

        stack = list()
        res = list()

        def helper(openAdded: int, closeAdded: int):
            if openAdded == closeAdded == n:
                res.append("".join(stack))
                return
            
            if openAdded < n:
                stack.append("(")
                helper(openAdded + 1, closeAdded)
                stack.pop()
            
            if closeAdded < openAdded:
                stack.append(")")
                helper(openAdded, closeAdded + 1)
                stack.pop()

        helper(0, 0)
        return res
    
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