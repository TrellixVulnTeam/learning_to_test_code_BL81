"""
LC 118 - Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""

from collections import Counter

class Solution:
    
    def maxNumberOfBalloons(self, text: str) -> int:
        pass
    
    def maxNumberOfBalloonsBruteForce(self, text: str) -> int:
        res = []
        counter = Counter(text)
        
        for c in counter:
            if c == "b":
                res.append(counter[c])
            elif c == "a":
                res.append(counter[c])
            elif c == "l":
                res.append(counter[c]//2)
            elif c == "o":
                res.append(counter[c]//2)
            elif c == "n":
                res.append(counter[c])  
        
        if len(set("balloon")) == len(res):
            return min(res)
        else:
            return 0
        

if __name__ == "__main__":
    text = "nlaebolko"
    
    solution = Solution()
    print(solution.maxNumberOfBalloonsBruteForce(text))
    