from typing import Dict, List

class Solution:
    # def longestPalindrome(self, s: str) -> str:
        # for i in range(0, len(s)):
        #     for j in range(len(s), -1, -1):
        #         substring = s[i:j]
        #         if substring == substring[::-1] and len(substring) > 2:
        #             return substring
        # return ""
        
    def bf_longestPalindrome(self, s: str) -> str:    
        longest_palindrome = ""  
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                        longest_palindrome = substring
        return longest_palindrome

if __name__ == "__main__":
    s = "abbb"
    # s = "cbbd"
    solution = Solution()
    print(solution.bf_longestPalindrome(s))