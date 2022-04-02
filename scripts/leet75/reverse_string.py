from curses.ascii import SO
from typing import List


# REMEMBER: Big O is about time AND space complexity
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # cant do this because have to modify in place with O(1) extra memory
        # return s[::-1]
        
        for i in range(len(s)):
            s[i] = s[-1]
            print(s)


if __name__ == '__main__':
    str1 = ["h","e","l","l","o"]
    expected = ["o","l","l","e","h"]

    soln = Solution()
    assert soln.reverseString(str1) == expected



# Tricky!
# test_cases = [
#     ["h", "e", "l", "l", "o"], ["o","l","l","e","h"]
# ]
# print(test_cases[0])
# test_cases = [
#     [["h", "e", "l", "l", "o"], ["o","l","l","e","h"]]
# ]
# print(test_cases[0])

# for case, exp in test_cases:
#     print(case, exp)