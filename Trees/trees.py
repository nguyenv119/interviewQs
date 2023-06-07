# Definition for a binary tree node.
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

    def test(self):
        assert self.lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8) == 6
        print("All Tests Passed Succesfully")

Soln = Solution()
Soln.test()
