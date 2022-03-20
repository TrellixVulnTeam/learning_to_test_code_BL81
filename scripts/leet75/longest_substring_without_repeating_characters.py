"""
LeetCode 3 - Longest Substring Without Repeating Characters [Medium]

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        res = []

        for i in range(len(s)):
            for j in range(len(s)+1):
                temp = ""
                for k in range(i, j):
                    temp += s[k]
                
                if len(temp) == len(set(temp)):
                    res.append(temp)                
        
        max_substring = max(res, key=len)
        return len(max_substring) if max_substring else 0

if __name__ == "__main__":

    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstringBruteForce(s))
    print(solution.lengthOfLongestSubstring(s))