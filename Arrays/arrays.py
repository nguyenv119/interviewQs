from typing import List
class Solution:

    def test(self):
        assert self.containsDupe([1, 2, 3, 4]) == False
        assert self.containsDupe([1, 3, 2, 3, 4]) == True
        assert self.containsDupe([1, 1, 2, 3, 4, 2, -1, -1]) == True

        print("All Tests Passed Succesfully!")
    
    def maxProfit(self, prices: List[int]) -> int:
      maxProfit, left, right = 0, 0, 1
      while right < len(prices):
        if prices[left] < prices[right]:
          maxProfit = max(prices[right] - prices[left], maxProfit)
        else: left = right
        right += 1
        
      return maxProfit

      '''
      O(1) space because no matter size of array, we'll have 2 pointers and 1 local var
      O(n) time since we traverse array once

      Idea: 2 pointers, 1 tracking min value, one going through to subtract = maxProfit
      Intuition: 
      - we want profit, how? max - min
      - how max - min, get indices, 2 pointers
      - how we know its max profit? More than other profits, how? keep local variable
      - when we get new min, switch it, but guaranteed we can either get more profit from this min, since we already have the local variable
      - get answer? return max profit
      '''

    def subarraySum(self, nums: List[int], k: int) -> int:
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
        map = dict()
        for num in nums:
            if num not in map: map[num] = 1
            else: map[num] += 1

        res = []
        for i in range(len(nums)): res.append([])
        for key in map: res[map[key] - 1].append(key)

        result = []
        i = len(res) - 1
        print(res)

        while i >= 0 and k > 0:
            # print(i)
            for num in res[i]:
                print(num)
                if num is not None:
                    result.append(num)
                    print(result)
                    k -= 1
            i -= 1
            
        return result

        ''' Hashmap array, O(n) Time and O(n) space, where keys are number, values are appearances
            Now have # times found. [3, 1, 2, 2, 3, 3] --> [3: 3, 1: 1, 2: 2]
            Then, make an array in order of appearances, most times can possible appear is n, so array size n, where
            inputs are list, because it can be [1, 2, 3, 4] say. So, [[1], [2], [3], [], [], []], k most, so start
            at end, then go back and add to result list, until we add k most
        '''

    def containsDupe(self, nums: List[int]) -> bool:
        if nums is None: return False
        contains = False
        check = set()

        for i in range(len(nums)):
            if nums[i] not in check: check.add(nums[i])
            else: return True

        return False
    
    '''
    Idea: 
    Intuition: Iterate through list, if not appeared, add to set, if its in, means theres dupe, return true
    - duplicate = number appears 2+ times, how we know? keep track of numbers appeared once, 
    True if its appeared again. How we keep track, use DS, which fastest DS? Hashset

    O(n) in time and space, since we iterate through array atmost once, and hashset atmost n elements
    '''

solution = Solution()
solution.test()