"""
LC 796. Rotate String [easy]

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
"""
# two strings
# bool
# if and only if
# shifts
# indexing
# position

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        """
        This question is kinda tricky because you need a groundtruth copy of the list to reference while you keep "popping" the first element. Postfixes is the solution to that even if ugly it demonstrates the rabbit hole that this question checks if you understand. Seems like a common pattern.

        This is sorta like a queue questions actually similar to how a stack is asked about in isValidParenthesis
        """
        counts = 0
        postfixes = list(s)

        while counts < len(s):
            print(s[1:], s[counts], s[1:] + postfixes[counts])
            s = s[1:] + postfixes[counts]
            if s == goal:
                return True
            counts += 1
        return False


if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"

    soln = Solution()
    print(soln.rotateString(s, goal))