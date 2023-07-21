from collections import Counter
import heapq
from typing import List
class Solution:

    def test(self):
        assert self.isAnagram("abcdefg", "gfedcba")
        assert self.isAnagram("", "")
        assert self.isAnagram("apples", "aspple")

        print("All Tests Passed Succesfully!")

    def isAnagram(self, s: str, t: str) -> bool:

        '''
        We know that an anagram is 2 words with their character mixed. What do they
        have in common? How can we tell that 2 words are anagrams. Same length, sure,
        but they have the same number of chars. 

        Is there a way to determine if the number of chars of 
        each char is the same. We need a way to count the number of each character,
        then at the end compare the 2

        1. Use a Counter, Theta(2n) = Theta(n) time, where n is the # characters in each string. 
        Since we go through the string of n characters and count how many time each 
        char appears, do it twice, 2n. Then, at the end compare them.
        2. Use a hashmap ourselves

        Both Theta(2n) space
        '''

        #? Approach 1
        print(Counter(s))
        print(Counter(t))
        return Counter(s) == Counter(t)
    
        #? Approach 2
        mapS = dict()
        mapT = dict()

        for char in s:
            if char not in mapS: mapS[char] = 1
            else: mapS[char] += 1
        
        for char in t:
            if char not in mapT: mapT[char] = 1
            else: mapT[char] += 1
        
        return mapS == mapT

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Valid sudoku doesnt necesarilly have to contain all numbers in a row/column,
        just no duplicates!

        We can use a set to erase possiblity of duplicates
        Brute force: We can check every element in each row, then check in each column if there
        is no duplicates we continue and add that element in a set. Then theres the prob checking
        in each 3x3 box

        Can we use 3 sets, one for row, one for column, one for 3x3
        Maybe for 3x3 hashset, do to represent. Check dupes or invalid each box.

        How can we associate each box to the rows, cols? We know its 3x3, so in box hashset, 
        1st lines of boxes are 0'th index, and like the rows, they are index 0, 1, 2. How do we
        get them to be 0? Divide by 3. Same with 3, 4, 5, divide by 3 = 1 index. 

        So how can we check if theres a dupe? 
        --> Make 3 hashsets for each category
        --> When we iterate through 9x9 array, if ".", continue with iteration, dont matter
        --> we can check if board[r][c] exists in the row, column or square. If so, return False
        --> Else, add and keep iterating. At the end, no false so its valid, return true

        Theta(81) in time since we have to iterate through every element in board, regardless of
        whether its valid or not to check the element

        Theta(81) in space since we have to make the empty slots for the hashsets
        '''

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".": continue
                elif (board[r][c] in rows[r] 
                      or board[r][c] in cols[c]
                      or board[r][c] in squares[r // 3][c // 3]):
                      return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r // 3][c // 3].add(board[r][c])

        return True
    
    def longestConsecutive(self, nums: List[int]) -> int:

        map = set(nums)
        mostConsec = 0

        for num in nums:
            currConsec = 1
            if (num - 1) not in map: 
                while (num + currConsec) in map:
                    currConsec += 1
                mostConsec = max(mostConsec, currConsec)
        
        return mostConsec

        '''
        There can be multiple consecutive sequences, so we just have to choose
        the highest one. Dupes count as 1

        #* Brute Force? 
        - Have a max variable, go thorugh each element and scan rest of array...etc
        for longest sequence, update max var accordingly and return

        Need a way to get longest consecutive sequence, hashmap?
        - Iterate through n elements, make hashmap = O(n), number -> ___

        We know it is a consecutive sequence if there exists num +1, +2....etc
        So we have O(1) to search it in the hashmap

        #! To avoid redundancy, say checking [1, 2, 3...] where we know [0, 1, 2, 3...] is longer, we know this
        #! since 0 is the start of the sequence. How do we know something is the start of a sequence? There is no preceding number.
        #! So, we only need to check if there is a preceding number, else we know that it is not the start of the sequence

        - After we get number, ask map is there +1? If yes, is there +2? and keep
        incrementing currentMax, then at the end do globalMax = max(global, local)


        #? 1. Make set, no dupes
        #? 2. Init currConsec, mostConsec = 0, 0
        #? 3. Go through array, and iterate currConsec as long as there exists conse
        #? 4. mostConsec = max(currConsec, mostConsec)
        #? 5. return mostConsec

        O(2n) = O(n) since we traverse n elements to make map, and again for search
        O(n) space for the set
        '''

    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        '''
        If we didnt need to use constant space, we could use the solution from Two Sum I, with hashmap, Space O(n)
        But, we should think about pointers if we use O(1) space.

        target = numbers[i] + numbers[j] 
        Answer is a combination of indices, we know array is sorted, how does that help us as opposed to unsorted
        Unsorted = look randomly
        Sorted = is there a way to look at it in a non-random organized pattern. The organized pattern of sorted is we know
        the max, min...etc

        - Start with 2 pointers, left, right
        - If their sum is > target, move right back, vice versa if smaller
        - Do this while left < right, if it is then a solution doesnt exist since we cant have dupe indices as Answer

        O(n) in time since we traverse array once
        O(1) in space since we don't use auxiliary DS
        '''

        l, r = 0, len(numbers) - 1
        res = []

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target: 
                res.append(l + 1)
                res.append(r + 1)
                break
            elif sum < target: l += 1
            elif sum > target: r -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def helper(index: int, length: int, nums: List[int], res: List[List[int]], check: set()):
            l, r = index + 1, length
            while l < r:
                
                sum = nums[l] + nums[r]

                if sum == -1 * nums[index]:
                    if (nums[index], nums[l], nums[r]) not in check: 
                        res.append([nums[index], nums[l], nums[r]])
                        check.add((nums[index], nums[l], nums[r]))

                    l += 1
                    r -= 1

                elif sum < -1 * nums[index]: l += 1
                elif sum > -1 * nums[index]: r -= 1

        check = set()
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            helper(i, len(nums) - 1, nums, res, check)

        return res

        '''
        We need 3 numbers, where the same index cant be repeated in a triplet, 
        that sum to 0. 

        Brute force: go through array, for each iteration check every other element, 
        and in that iteration, check every other element: O(n^3)

        We can iterate through array, and then we need to see if the other 2 indices
        sum to negative of the number we are on. To make it easy, we can sort array
        beforehand, and do if its smaller, left pointer up, vice versa

        [-4,-1,-1,0,1,2]
        - so -1, we need sum to be 1: -1 and 2, so we stop
        - 2nd -1, 0 + 2 too big, so move down: 0, 1, stop

        Move until left = right so we get all possible: [-1,-1,0,1,2]
        To avoid dupes, we can use a set

        Solution is O(n^2) since each element requires we search up to n elements
        O(n) in space for the triplets
        '''

    def isValid(self, s: str) -> bool:
        '''
        In the case of ()[]{}, we need a way to verify that its valid: that right
        after the (, the ) is so that we can continue, valid so far. 


        - We know that when we see a closing bracket, the most recent open one must 
        also be an open bracket, in the case of up there, and also
        ([{}]). 
        - So we can use a stack to store all the open ones, and when we get to a
        closed one, we can check if it matches its open counterpart in the stack,
        then pop and keep going until reach end of string

        0. If the length is odd, false, can't ever have matching parentheses
        1. Init stack, and go through string
        2. If open, add
        3. If odd, check if top of stack is open counterpart, if not, False
        4. At the end, when if stack is empty (not stragglers left) return True

        O(n) in space since we store half the string, O(n/2) = O(n), n = # chars
        O(n) in time since we traverse the entire string, where n = # chars

        ()[]{}
        stack: 

        '''

        if len(s) % 2 != 0: return False
        stack = list()
        openParen = {"(": ")", "[": "]", "{": "}"}
        closedParen = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in openParen: stack.append(char)
            else: 
                if stack and closedParen[char] == stack[-1]: stack.pop()
                else: return False

        return False if stack else True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        res = list()
        index = 0

        for str in strs:
            word = ''.join(sorted(list(str)))
            if word not in map: 
                map[word] = index
                res.append([])
                res[index].append(str)
                index += 1
            else: res[map[word]].append(str)

        return res
    
        '''
        Hashmap, word -> index
        List[List[str]] where the indices contain a list 
        of permutations of the same word. 

        - If the sorted permutation isnt in hashmap, add it, and increment key by 1
        - If it is, get the index and append it to the result

        O(n) in space for our hashmap, storing n strings
        O(n) in time since we traverse strs once, and sort each word once

        {"eat": 0, "tan": 1, "bat": 2}
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        index = 3
        '''

    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        Intuition:
        --> Asks if s2 contains a variation of s1, rearrange s1 such that it is in s2
        Brute force, go through each index of char and compare it with s1, O(n^2)
        
        For a moment, forget permutation, how do we know if a substring is in a substring
        Sliding window?
        abc, aadasabc, compare substring of len(s1), and slide left pointer if no match

        So, now permutation: how do we know if 2 strings are permutations?
        use sorted(s1) == sorted(s2). If it is, return True.

        At the end, if right pointer reached end, means we havent found permutation, 
        return False

        O(2n) = O(n), since in the worst case, we would repeat elements we are comparing 
        at most one repeat, and Omega(n), if the substring is 1 char long

        O(2n) = O(n) since with the same logic as needing to go through twice number 
        of chars, we use that as storage space too
        '''

        lenStr, lenSub = len(s2), len(s1)
        left, right = 0, lenSub

        while right <= lenStr and left <= lenStr - lenSub + 1:
            if sorted(s1) == sorted(s2[left:right]): return True
            else: left += 1
            right += 1

        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Intuition: 
        We want to see if list contains dupes? How? if atleast 1 number appears more than once. How can we see
        if the number appears more than once, we need to keep a counter of the # apperances of the number.
        
        Brute force can be going through each index of the list, counting how many apperances storing it into a global max 
        variable, and change it if the number of appearnces increases. O(n^2) time, O(1) space

        We could use a Counter, and then iterate through that counter to see if any of the keys are >= 1, O(n) space and O(2n) time

        We know that a set gives us only the unique values, without duplicates. So if there are duplicates, the set will be smaller
        O(n) space and time

        '''
        #? Approach 1: use set to account for duplicates
        return len(set(nums)) != len(nums)
    
        #? Approach 2: use hashmap

        map = dict()
        for i in range(len(nums)):
            if nums[i] in map: return True
            else: map[nums[i]] = 1
        return False
    
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