from collections import Counter
import heapq
from typing import List
class Solution:

    def test(self):
        assert self.characterReplacement("ABAB", 2) == 4
        assert self.characterReplacement("ABAB", 1) == 3
        assert self.characterReplacement("AABABBA", 1) == 4
        assert self.characterReplacement("ABCDEFGCCZ", 1) == 3
        assert self.characterReplacement("KO", 2) == 2
        assert self.characterReplacement("KSIKSIKSI", 4) == 7

        print("All Tests Passed Succesfully!")
    
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        Intuition: need to find substring within the string that when we replace k letters
        with the same letter gives us the longest substring with the same letter. The letters
        we dont replace will be the same letter. 

        ABCDEFG.....ZCC, k = 1
        How do we know ZCC is the answer? Replace Z with C
        AABABBA, k = 1, replace B with A. Why is AABABB not the answer, because there
        arent enough characters to replace. 

        How do we know this? Recall we are replacing with the same letter, and the other 
        chars are also the same letter. Why would this work with k = 3, enough chars

        How do we know if theres enough chars? AAAAAB, k = 1. Ans is 6. 6 - k = 5

        Substring - k = # same chars
        AAABCCCC, k = 2
        AAABC vs ABCCCC

        We will switch our left pointer when the substring is no longer valid (AAABC)
        At this point, right will be at C, increase left by 1
        
        - Use sliding window
        - Go through add chars in hashmap: char -> # occurences
        - See if len(substring) - k = # maxChars
        - If not, left += 1
        - Right always += 1, until right reaches len(s)

        Small Issue fixed: 
        - At this point, the solution for "AABABBA", k = 1 is AABA, being 4, but when we got to BABBA, the length of the 
        substring is 5, max number of same letter chars is 3: 5 - 3 = 2, > 1, so we would move our left by 1 and not change
        the max (since its an invalid substring). But, we didnt have a way to differentiate between the max number of chars
        in the substring vs the string. IOW, the max was actually A: 4, even though there were 2 A's outside the invalid
        substring, "BABBA". 
        
        Solution: So, when we move our left pointer and not count the max length of the substring when its invalid, we need to decrement
        the char that our left pointer is no longer focused on

        O(n) since we traverse the string once, and O(1) in space since our hashmap contains at most n indices for if the
        string has all unique characters, but n is atmost 26 characters, so O(26) = O(1)

        '''
        
        if s == "": return 0
        check = dict()
        m, res, left, right = 0, 0, 0, 0

        while right < len(s):
            if s[right] not in check: check[s[right]] = 1
            else: check[s[right]] += 1
            m = max(m, check[s[right]])

            sub = s[left:right + 1]

            if right - left + 1 - k > m: 
                check[s[left]] -= 1
                left += 1

            else: res = max(res, len(sub))

            right += 1

        return res
    
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
        # map = dict()
        # for num in nums:
        #     if num not in map: map[num] = 1
        #     else: map[num] += 1

        # res = []
        # for i in range(len(nums)): res.append([])
        # for key in map: res[map[key] - 1].append(key)

        # result = []
        # i = len(res) - 1
        # print(res)

        # while i >= 0 and k > 0:
        #     for num in res[i]:
        #         print(num)
        #         if num is not None:
        #             result.append(num)
        #             print(result)
        #             k -= 1
        #     i -= 1
            
        # return result

        ''' Hashmap array, O(n) Time and O(n) space, where keys are number, values are appearances
            Now have # times found. [3, 1, 2, 2, 3, 3] --> [3: 3, 1: 1, 2: 2]
            Then, make an array in order of appearances, most times can possible appear is n, so array size n, where
            inputs are list, because it can be [1, 2, 3, 4] say. So, [[1], [2], [3], [], [], []], k most, so start
            at end, then go back and add to result list, until we add k most
        '''
    
        '''
        Intuition: 
        - want most frequent elements, need count of elements, use counter
        - use maxHeap, so need heap, heapify, heapify what? Heapify dict
        - convert the variable we countered to a dict
        - Want k most, so heappop k times and add to result list

        O(n) space since we are making heap and Counter with size n
        O(nlogn) since at most we are popping n elements from the heap, and have to heapify down n times
        '''

        count = Counter(nums)
        heap = list()
        for num in count:
            heap.append((-count[num], num))

        heapq.heapify(heap)
        res = []

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res

    def containsDupe(self, nums: List[int]) -> bool:
        '''
        Idea: 
        Intuition: Iterate through list, if not appeared, add to set, if its in, means theres dupe, return true
        - duplicate = number appears 2+ times, how we know? keep track of numbers appeared once, 
        True if its appeared again. How we keep track, use DS, which fastest DS? Hashset

        O(n) in time and space, since we iterate through array atmost once, and hashset atmost n elements
        '''
        if nums is None: return False
        contains = False
        check = set()

        for i in range(len(nums)):
            if nums[i] not in check: check.add(nums[i])
            else: return True

        return False

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        We want the product of the product of the elements before and after, have to keep track
        we can have 2 arrays, one pass to calculate before, and one to calculate after, then 
        iterate through array and take product. 

        But this wastes space, so we can do 1 iteration calculating product, then the 2nd iteration
        we will simulataneously take product of reverse and multiplying it with the existing indices

        [1, 2, 3, 4]
        pre = 6
        [1, 1, 2, 6]

        post = 24
        res[i] = res[i] * post
        post = post * nums[i]
        [24, 12, 8, 6]

        O(n) time and space, since we are passing through array 2 times, and result is of size n

        '''
        if nums is None: return []
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

solution = Solution()
solution.test()