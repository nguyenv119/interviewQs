from typing import List
class Solution:

    def test(self):
        matrix = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
        assert self.matrixSum(matrix) == 15

        matrix = [[1]]
        assert self.matrixSum(matrix) == 1

        matrix = [[1,8,16,15,12,9,15,11,18,6,16,4,9,4],[3,19,8,17,19,4,9,3,2,10,15,17,3,11],[13,10,19,20,6,17,15,14,16,8,1,17,0,2],[12,20,0,19,15,10,7,10,2,6,18,7,7,4],[17,14,2,2,10,16,15,3,9,17,9,3,17,10],[17,6,19,17,18,9,14,2,19,12,10,18,7,9],[5,6,5,1,19,8,15,2,2,4,4,1,2,17],[12,16,8,16,7,6,18,13,18,8,14,15,20,11],[2,10,19,3,15,18,20,10,6,7,0,8,3,7],[11,5,10,13,1,3,4,7,1,18,20,17,19,2],[0,3,20,6,19,18,3,12,2,11,3,1,19,0],[6,5,3,15,6,1,0,17,13,19,3,8,2,7],[2,20,9,11,13,5,1,16,14,1,19,3,12,6]]
        assert self.matrixSum(matrix) == 190

        print("All Tests Passed Succesfully!")
    

    def matrixSum(self, nums: List[List[int]]) -> int:
        if nums == [[]]:
            return 0

        score = 0
        return self.helperMatrixSum(nums, score)
    
    def helperMatrixSum(self, nums: List[List[int]], score: int) -> int:
        if nums == [[]]:
            return 0
        
        globalMax = float('-inf')
        for i in range(len(nums)):
            localMax = max(nums[i])
            globalMax = max(globalMax, localMax)
            nums[i].remove(localMax)

        score += int(globalMax)

        if len(nums[0]) >= 1: score = self.helperMatrixSum(nums, score)
        return score
    

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k < 0 or nums == []: return []
        if len(nums) == 1: return nums
        
        map = dict()
        for num in nums:
            if num not in map: map[num] = 1
            else: map[num] += 1
        print(map)

        lisT = [[] for _ in range(len(nums))]
        for key, value in map.items():
            lisT[value - 1].append(key)
        print(lisT)

        result = list()
        i = len(lisT) - 1
        while (k > 0 and i >= 0):
            if lisT[i] != []:
                result.extend(lisT[i])
                k -= len(lisT[i])
            i -= 1

        print(result)
        return result

        ''' Hashmap array, O(n) Time and O(n) space, where keys are number, values are appearances
            Now have # times found. [3, 1, 2, 2, 3, 3] --> [3: 3, 1: 1, 2: 2]
            Then, make an array in order of appearances, most times can possible appear is n, so array size n, where
            inputs are list, because it can be [1, 2, 3, 4] say. So, [[1], [2], [3], [], [], []], k most, so start
            at end, then go back and add to result list, until we add k most
        '''

solution = Solution()
solution.test()