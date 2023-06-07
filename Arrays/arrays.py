from typing import List
class Solution:

    def test(self):
        assert self.subarraySum([1, 1, 1], 2) == 2
        assert self.subarraySum([1, 2, 3], 3) == 2
        assert self.subarraySum([1, 6, 3, 3, 10, 2], 13) == 2
        assert self.subarraySum([3, -1, 1, 1, 1], 0) == 1

        print("All Tests Passed Succesfully!")
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums is None:
            return 0

        check = {0: 1}
        sumSoFar = 0
        res = 0

        for num in nums:

            sumSoFar += num
            if (sumSoFar - k) in check: res += check[sumSoFar - k]
            
            if sumSoFar not in check: check[sumSoFar] = 1
            else: check[sumSoFar] += 1


        return res

    '''
        [1, -1, 1, 1, 1], k = 3

        0: 2
        1: 2
        2: 1
        3: 1

        res = 2

        Brute force: O(n^2) time, we go through each index and scan the rest of list to see if sum, and icnrm
        Better: Instead of finishing 1, then going to 6 and examining [6, 3] or [6, 3, 3] it is the same thing
        as [1, 6, 3] - [1], and [1, 6, 3, 3] - [1]. So lets just go through the array once, O(n)

        When we go through it once, say k = 13. In the brute force, the equivalent of getting to [3, 10] is
        the same as in this, where we can see [1, 6, 3, 3, 10] - [1, 6, 3] = 13. "Lets remove [1, 6, 3]", but
        how do we know to do this? When we sum up to [1, 6, 3] we see that it sums to 10, so we note
        that we've seen 10 before. So when we are up to [1, 6, 3, 3, 10], we ask "What can we remove to 
        make this work?", the sum is 23, so 23 - 13 = 10. And we have seen 10 before
        
        The approach is to keep count of how many times we a sum can be made, and when keep summing through
        the O(n) iteration, see if we can remove a portion, that we can find in our hashmap, and then add
        the number of times we have seen that sum to the answer

        O(n) time, since we iterate through array once, and O(n) space since our hashmap size is n at most
        since the number of distinct sums across n elements is n
    '''

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