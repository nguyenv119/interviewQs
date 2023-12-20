from typing import List
class Solution:

    def test(self):
        assert self.search([1, 3, 4, 5, 6, 9, 10], 9) == 5
        assert self.search([1, 3, 4, 5, 6, 9, 10], 3) == 1
        assert self.search([1, 3, 4, 5, 6, 9, 10], 2) == -1
        print("All Tests Passed Succesfully!")
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        non-decreasing order: could be duplicates?
        O(log(m * n)) means a binary search for the matrix

        We know that the 1st num of every row is larger than the last num of prev row
        Binary search, we cut off half the possible solutions with every iteration
        Can we binary search the rows, then narrow it down to columns?

        If a num is between the 1st digit in the rows, it is in the prev row.
        - Binary search across the rows. If its not, return false
        - If it is, binary search across the row
        '''

        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            # If less than 1st value, shift up
            if target < matrix[mid][0]: bottom = mid
            # If larger than last value, shift down
            elif target > matrix[mid][-1]: top = mid
            # Falls in range of row we are on
            else: break

        if top > bottom: return False
        
        start, end = 0, len(matrix[0]) - 1

        mid = (top + bottom) // 2
        while start <= end:
            midInRow = (start + end) // 2
            # If less than mid value, shift down
            if target < matrix[mid][midInRow]: end = midInRow
            # If larger than mid value, shift up
            elif target > matrix[mid][midInRow]: start = midInRow
            # Found it
            else: return True

        # Exhausted all possibilities
        return False

    def bsearch(self, nums: List[int], target: int) -> int:
        '''
        When we want to search for an element in a sorted list, in O(logn), we can
        use binary search:

        The reason it is logn, is that we can half our options through each iteration.
        Start in the middle, and check if it is larger/smaller/same as our target

        Same: we have found it, return index
        Smaller: Search the larger part of the array, start of search becomes middle
        Larger: Search the smaller part of the array, end of search becomes middle

        T: O(logn), Omega(1)
        S: Theta(1)
        '''

        start, end = 0, len(nums) - 1
        while start <= end: 
            mid = (end + start) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                end = mid - 1 # Search for left side of array, excluding mid
            else: start = mid + 1 # Search for right side of array, excluding mid
        
        return -1

    def searchRotated(self, nums: List[int], target: int) -> int:
        '''
        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        Example 2:

        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
        Example 3:

        Input: nums = [1], target = 0
        Output: -1
        
        Binary Search
        Divide based on middle value relation to a certain thing - what is it? Know ascending
        Left and right part, pivot is the largest element

        Basecase: if nums[middle] == target
        Either left pr right: 

        [4,5,6,7,0,1,2]
        [1,4,5,8,9,-1,0]
        [8,9,10,2,3,4,5,6,7]

        

        '''

    def findMin(self, nums: List[int]) -> int:
        '''
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        Example 1:

        Input: nums = [3,4,5,1,2]
        Output: 1
        Explanation: The original array was [1,2,3,4,5] rotated 3 times.
        Example 2:

        Input: nums = [4,5,6,7,0,1,2]
        Output: 0
        Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
        Example 3:

        Input: nums = [11,13,15,17]
        Output: 11
        Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
        '''


soln = Solution()
soln.test()
