"""
LC 20 - Valid Parentheses [easy]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mappings = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        
        for char in s:
            # if closing bracket..
            if char in mappings:
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
                else:
                    return False
            # opening brakcet..so add to stack    
            else:
                stack.append(char)
        
        return True if not stack else False
        
                
if __name__ == "__main__":
    s = "()"
    
    solution = Solution()
    print(solution.isValid(s))
    assert solution.isValid(s) == True