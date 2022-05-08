from typing import List


class Solution:
    def isValidParenthesis(self, s: str) -> bool:
        mappings = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char in mappings: # closing
                if stack[-1] == mappings[char]:
                    stack.pop()
                else: 
                    return False
            else: # opening
                stack.append(char)

        # return True if not stack else False
        return not stack


if __name__ == "__main__":
    soln = Solution()
    
    s = "()"
    assert soln.isValidParenthesis(s) == True
    print(soln.isValidParenthesis(s))

    s = "{}"
    assert soln.isValidParenthesis(s)
    print(soln.isValidParenthesis(s))

    s = "(]"
    assert soln.isValidParenthesis(s) == False
    print(soln.isValidParenthesis(s))