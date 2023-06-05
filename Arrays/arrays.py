class Solution:

    def test(self):
        string = "51230100"
        assert self.removeTrailingZeros(string) == "512301"

        string = "123"
        assert self.removeTrailingZeros(string) == "123"

        string = "1023"
        assert self.removeTrailingZeros(string) == "1023"

        string = "10230000000"
        assert self.removeTrailingZeros(string) == "1023"
        print("All Tests Passed Succesfully!")


    def removeTrailingZeros(self, num: str) -> str:
        if len(num) == 0:
            return ""
        
        index = len(num) - 1
        # Start from end, and while the char is a 0 and we havent gotten to the first char yet, increment count by 1 if it is a 0, then when its not, break
        while (index >= 0 and num[index] == "0"):
            index -= 1

        # Then, return the substring from the start up to the index. If the index
        return num[:index + 1]
    
solution = Solution()
solution.test()