from typing import Dict, List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Start from the outside of the string so that we are checking increasingly lesser lengths of the sub strings throughout the iterations and stop when a palindromic substring is found, so that we find the optimal (longest substring) first before we even get to the sub-optimal strings.
        """
        # for i in range(0, len(s)):
        #     for j in range(len(s), -1, -1):
        #         # reverse inclusive :)
        #         sub = s[i:j]
        #         print(sub, "-", i, j)
        #         if sub == sub[::-1]:
        #             print("is palindrome", sub, i, j)
        "***"
        # for i in range(len(s), 0, -1):
        #     for j in range(len(s)-i + 1):
        #         sub = s[j:j+i]
        #         if sub == sub[::-1]:
        #             print(sub, "-", i, j, j+i)

if __name__ == "__main__":
    s = "abbb"
    # s = "cbbd"
    solution = Solution()
    print(solution.longestPalindrome(s))
