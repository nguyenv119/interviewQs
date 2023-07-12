from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:

    def test(self):
        n5 = ListNode(5, None)
        n4 = ListNode(4, n5)
        n3 = ListNode(3, n4)
        n2 = ListNode(2, n3)
        n1 = ListNode(1, n2)

        assert self.reorderList([n1]) == []

        print("All Tests Passed Succesfully!")
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        So, we want to return 1st, last, 2nd, 2nd last...etc.
        If it's odd, the odd(middle) node will be the last
        1->2->3->4->5
        
        We need to find a way to get the 1st to point to last. Then, keep continuing
        until there's 1 element. How do we get 1st, last, then the next 1st, last. What is a 
        way we can keep shortening the original ll: deque()

        0. If null, return
        1. Add all to deque, have ref
        2. While deque size > 1: have popRightOriginal.next point to popLeft, and popLeft.next to 
        RightTop (new element on top of queue)

        Theta(n) in space since we add all n elements
        Theta(n) in time since we loop through and add all n elements, then loop through n elements
        and switch pointers
        """

        if head is None: return
        queue = deque()
        # Add nodes to queue
        curr = head
        while curr:
            queue.appendleft(curr)
            curr = curr.next
        # Go through queue and modify pointers
        while len(queue) > 1:  
            rear = queue.popleft()
        
            top = queue.pop()

            top.next = rear  # First should connect to last
            rear.next = queue[-1] if len(queue) != 0 else None  
        
        if len(queue) == 1:
            queue[0].next = None

soln = Solution()
soln.test()