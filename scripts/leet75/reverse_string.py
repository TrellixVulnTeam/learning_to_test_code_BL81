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
        
        l, r = 0, len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


if __name__ == '__main__':
    # input1 = ["h","e","l","l","o"]
    input1 = []
    expected = []

    soln = Solution()
    print(soln.reverseString(list(input1)))
    assert soln.reverseString(list(input1)) == expected



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