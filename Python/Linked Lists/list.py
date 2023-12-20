from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:

    def rec(self, n):
        if n == 1: return 1
        else: return self.rec(n - 1) + self.rec(n - 1)


    def test(self):
        print(f"1: {self.rec(1)}") 
        print(f"2: {self.rec(2)}") 
        print(f"3: {self.rec(3)}") 
        print(f"4: {self.rec(4)}") 
        print(f"5: {self.rec(5)}") 
        

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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        We want a solution that should reverse the list as we go from head to tail
        1 -> 2 -> 3 -> 4 -> 5

        1 <- 2 <- 3 <- 4 <- 5
        How do we point 2 to 1? We need a reference to 2, and set 2.next to 1. But then we also
        need a reference for 3. So, 3 references: curr, curr.next, and curr.next.next

        When do we stop the process: when curr.next is None
        So, while curr.next is not None: we set curr.next.next to curr, then move everything forward
        We should initialize the variables in the beginning, since curr.next isn't null in the loop,
        the 1 possibility of null, would be curr.next.next:

        Theta(n) in time since we traverse n elements, and pointer swaps are O(1)
        O(1) space since it is in place     

        '''
        prev = None
        curr = head
        while curr:
            next_node = curr.next   # Save current node's next before overwriting its value
            curr.next = prev        # Reverse direction by pointing previous back at this element
            prev = curr             # Move both nodes along towards each other
            curr = next_node       # Set up for next iteration

        return prev
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given 2 lists, sorted. We need to combine them into another list that is sorted
        O(1) space: rearrange pointers
        Scenarios: 
                
        Approach: 
        - Make a new list to combine the two. Should start with the smallest head (guaranteed smallest)
        - We have 2 pointers, iterate through the lists and compare them:
        a) The smaller goes onto the new list, the tail of the list: tail.next = newAdded
        - We go until one list has finished, while list1 and list2 is not None
        - Afterwards, add the remaining elements, just attach it with 1 tail.next = list1/list2

        Theta(1) space since it is in place
        O(m) where m is the length of the larger list
        '''

        if list1 is None and list2 is None: return None # Both are null lists
        if list1 is None: return list2 # 1 of them is None
        elif list2 is None: return list1

        if list1.val < list2.val: # Compare which head.val is smaller, add to res
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        tail = head # We have the ref to the original head, while keeping reference of tail
        
        while list1 and list2: # While a list remains
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1: tail.next = list1
        else: tail.next = list2

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        We want to remove the n'th node from the end of the list, whose size cannot be null
        If n = 1, return end of list: O(n) - TBD
        If n = sz, return head of list: Omega(1)

        Raw Approach:
        - Go through whole list, find length, and take length - n, to then start from root and 
        move forward, remove that node: (length - n - 1).next = (length - n).next

        If length - n == 0, return head.next: if we remove the 1st element

        Theta(n) since we traverse whole list
        Theta(1) since it is in place
        '''
        
        curr = head
        len = 1
        while curr.next is not None: # Go through list and find length
            len += 1
            curr = curr.next
    
        steps = len - n
        if steps == 0: return head.next # Removing 1st element

        curr = head # Set curr back to head, and iterate through steps - 1 times
        for i in range(steps - 1):
            curr = curr.next
        
        curr.next = curr.next.next # Remove the node from list
        return head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None) 
        head = res # Have ref to head to return
        while l1 and l2: # While both pointers to both lists arent null
            sum = l1.val + l2.val + res.val # Add list nodes and result node
            res.val = sum % 10
            if sum >= 10: # If greater than 10, add the next node as 1
                res.next = ListNode(1, None) 
            elif sum < 10 and (l1.next or l2.next): # May be end of list, so check. If not, add 0 as next
                res.next = ListNode(0, None)
            res = res.next # Continue through lists
            l1 = l1.next
            l2 = l2.next
        
        while l1: # Continue if l1 isnt completed
            sum = l1.val + res.val
            res.val = sum % 10
            if sum >= 10:
                res.next = ListNode(1, None)
            elif sum < 10 and l1.next:
                res.next = ListNode(0, None) 
            res = res.next
            l1 = l1.next
        while l2: # Continue if l2 isnt completed
            sum = l2.val + res.val
            res.val = sum % 10
            if sum >= 10:
                res.next = ListNode(1, None)
            elif sum < 10 and l2.next:
                res.next = ListNode(0, None) 
            res = res.next
            l2 = l2.next
        
        return head
    
        '''
        We need to add the numbers in 2 in each node of the lists together. The lists arent necesarilly
        the same length. 
        - When we add 2 numbers, if there is a carry over, the carry over value (sum / 10) gets added
        in the next sum, so we need to keep track of that.
        - We know they are single number digits, so the largest possible sum is 18. 

        1. Make the result list
        1.5. First, set dummy.val = 0, and our first sum changes dummy
        2. Go through 2 lists while one hasn't reached the end, and add nodes. Add the sum mod 10
        (last digit) to the last ListNode
        3. If there is a carry over, immedientally create a new next ListNode in our result and set 
        its value to 1
        4. When loop breaks, have 2 loops going through either list, whichever one is still full

        T: Theta(m) where m is the len(largestList) since we have to traverse through m nodes, n included
        S: Theta(1): in-place algorithm
        '''

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Raw Approach: Go through lists adding nodes into a set. If we see that the node exists in the set,
        return false, eventually it will reach this if there is a cycle. 
        Else, eventually it will finish, so return true at the end

        T: 
        - Omega(1) since in the best case, the next node points to the 1st node
        - O(n) where n is the number of elements in the list

        S: 
        - Omega(1) since in the best case, loop is in the 1st node pointing to the 1st
        - O(n) since we need to store n elements if we don't find a loop, or if we do and we've reached
        the end, and the end node points back somewhere

        '''
        if head is None: return False
        added = set()
        curr = head
        while curr.next: # Going through ll
            if curr in added: return True # O(1) search in hashset, check if we've seen it before
            added.add(curr)
            curr = curr.next
        return False

soln = Solution()
soln.test()