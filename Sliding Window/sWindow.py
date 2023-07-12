from typing import List
class Solution:

    def test(self):
        assert self.maxArea([1,8,6,2,5,4,8,3,7]) == 49
        assert self.maxArea([1,1]) == 1

        print("All Tests Passed Succesfully!")
    
    def characterReplacement(self, s: str, k: int) -> int:
        
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
        - At this point, the solution for "AABABBA", k = 1 is AABA, being 4, but when 
        we got to BABBA, the length of the substring is 5, max number of same letter chars 
        is 3: 5 - 3 = 2, > 1, so we would move our left by 1 and not change the max 
        (since its an invalid substring). But, we didnt have a way to differentiate 
        between the max number of chars in the substring vs the string. IOW, the max 
        was actually A: 4, even though there were 2 A's outside the invalid 
        substring, "BABBA". 
        
        Solution: So, when we move our left pointer and not count the max length of 
        the substring when its invalid, we need to decrement the char that our left 
        pointer is no longer focused on

        O(n) since we traverse the string once, and O(1) in space since our hashmap 
        contains at most n indices for if the string has all unique characters, 
        but n is atmost 26 characters, so O(26) = O(1)

        '''
    
soln = Solution()
soln.test()