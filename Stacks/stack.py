from typing import List
from collections import deque

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
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        We have to return an array, where each i'th element corresponds to the i'th temperature,
        and whose value is the number of days we have to wait until it gets warmer, or until
        we see a value larger than it

        [1, 2, 3, 4]
        [1, 1, 1, 0]

        Brute force: we can go through every element, and examine every other element in the array,
        keeping track of the spaces between the original element and of where the nearest value
        larger than it is: O(n^2) time, since we have to iterate through the array n(n-1) / 2 times

        When we go through, we should remember what was before it so we can resolve if necesarry.
        We know that every number in this previous spot, will be in descending order, so When
        we find something, we can resolve all of these.

        For instance, [1, 2, 3, 4] If they were not in descending order, we would continuously
        resolve the numbers 1 at a time. However: [3, 2, 1, 4], 4 would resolve all 3, 2, 1. But
        what about [3, 2, 1, 2] 2 would only resolve one of them, so how would we resolve and keep 
        it at the same time for 3.

        We can use a regular list to keep track of the numbers. We know that the result is the same size
        as the original list. So, in this case, we can resolve it by adding 1 at the 2nd index, but since
        our checking array is the same size as the original array, we know its index, and can keep track
        of how far temps are from one another

        1. Make checking list same size as temperature
        2. Add 1st element and start at the 1th index
        3. Go through list: if number is bigger than top of stack, add distance between indices: i'th index and index of top of stack
        4. While a stack exists(not empty), pop and add index(i) - top of stack's index to res



        Theta(n) in space since we are adding every time every element to our queue
        Theta(n) in time since we always iterate through the array once, and pop n elements

        [73,74,75,71,69,72,76,73]
        res = [1,1,0,0,0,0,0,0]
        check = [[0, 73]_, [1, 74]_, [2, 75], [3, 71], [4, 69], [5, 72]] 
        '''

        res = [0] * len(temperatures)
        stack = [] # idx, temp

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append([idx, temp])
        return res

        

        
    
    def test(self):
        assert self.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
        assert self.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
        assert self.dailyTemperatures([30,60,90]) == [1,1,0]

        print("All Tests Passed Succesfully!")

minStack =  MinStack()
minStack.test()