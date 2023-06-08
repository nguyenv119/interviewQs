# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        The LCA is where the split occurs, where node >= p and node <= q, or vice versa
        So just iterate through
        '''
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else: return curr

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        '''
        Traverse tree in an in-order way, left to right, smallest to largest, we can sort the 
        tree into a list, then return the k - 1 index

        Ask in an interview: what if empty list?

        Test Cases:
            [1, 2, 3, 4], k = 1, return k - 1 index = 0 --> 1
            [1, 2, 3, 4, 5 ,6], k = 3, return k - 1 index: 2 --> 3
            [1], k = 1, return k - 1 index: 0 --> 1
            [], 

        Solution: O(n) time and space, since we traverse through entire tree, n elements to create a
        list of size n
        '''

        ls = self.inOrder(root, [])
        return ls[k - 1]

    def inOrder(self, root: Optional[TreeNode], ls: List[int]) -> List[int]:
        if root.left: self.inOrder(root.left, ls)
        ls.append(root.val)
        if root.right: self.inOrder(root.right, ls)
        return ls
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
        If its an empty tree, return []
        Not empty: 
            - Create a queue, and enter the node
            - Remove the node, so we have the reference, then for each children (we have ref),
                add it to the queue. Do it while the queue is not empty
        
        [15, 7]
        Popped: 20
        res: [[3], [9, 20], [15, 7]

        Theta(n) in space and time, since we iterate through the entire tree, through each
        element at most once, and create the queue 
        '''

        if root == []: return []
        res = []
        queue = deque()
        queue.append(root)
        res.append([root.val])

        while queue:
            level = []
            curr = queue.popleft() # O(1)
            if curr.left: 
                queue.append(curr.left)
                level.append(curr.left.val)
            if curr.right: 
                queue.append(curr.right)
                level.append(curr.right.val)

            res.append(level)

        return res
    
    def test(self):
        assert self.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8) == 6
        print("All Tests Passed Succesfully")

Soln = Solution()
Soln.test()
