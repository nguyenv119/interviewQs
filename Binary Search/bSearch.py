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

    def search(self, nums: List[int], target: int) -> int:
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

soln = Solution()
soln.test()
