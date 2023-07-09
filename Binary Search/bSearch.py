from typing import List
class Solution:

    def test(self):
        

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


soln = Solution()
soln.test()
