from typing import List
class Solution:

    def test(self):
        assert self.maxArea([1,8,6,2,5,4,8,3,7]) == 49
        assert self.maxArea([1,1]) == 1

        print("All Tests Passed Succesfully!")
    
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            minHeight = min(height[l], height[r])
            maxArea = max(maxArea, (r - l) * minHeight)
            if height[l] <= height[r]: l += 1
            else: r -= 1
        
        return maxArea

        '''
        max = base x height
        Need a way to get the 2 highest pillars furthest away from each other
        Brute force: O(n^2) going through each pillar and finding largest maxArea

        We know that the smaller height is the limiting factor
        - So lets start out 
        with pointers, all the way to left, all the way right
        - We want to discard the smaller height, so go in whichever is the smaller
        - Keep track of area

        O(n) soln since we traverse array once inwards
        O(1) space since no auxiliary DS used
        '''
    
soln = Solution()
soln.test()