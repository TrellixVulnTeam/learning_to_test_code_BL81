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

    # def reverseStringRecursive(self, s: List[str]) -> None:
    #     final_result = ""
    #     def helper(s, final):
    #         ss = "".join(s)
    #         if len(ss) == 0:
    #             return s
    #         else:
    #             res = helper(ss[1:], final) + ss[0]
    #             print(f'res: {res}')
    #             final += res
    #             print(f'final: {final}')
    #             return final        
    #     return helper(s, final_result)    

if __name__ == '__main__':
    input1 = ["h","e","l","l","o"]
    expected = ["o", "l", "l", "e", "h"]
    # input1 = []
    # expected = []

    soln = Solution()
    print(soln.reverseString(list(input1)))
    assert soln.reverseString(list(input1)) == expected

    # soln = Solution()
    # print(soln.reverseStringRecursive(list(input1)))
    # assert soln.reverseStringRecursive(list(input1)) == expected

