from typing import List
class Solution:

    def test(self):
        nums = [1,1,1,2,2,3]
        assert self.topKFrequent(nums, 2) == [1, 2]

        nums = [1]
        assert self.topKFrequent(nums, 1) == [1]

        nums = [4,1,-1,2,-1,2,3]
        assert self.topKFrequent(nums, 2) == [-1, 2]

        print("All Tests Passed Succesfully!")
    
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