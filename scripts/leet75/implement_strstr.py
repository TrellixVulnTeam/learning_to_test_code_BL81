
# two strings
# first occurence
# Great question to ask during interview...
# What should we return when needle is an empty string?
# Answer: for purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf()

from curses import has_ic


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0
        
        result = haystack.find(needle)
        print(f'result: {result}')
        if result > -1:
            return result
        else:
            return -1


if __name__ == '__main__':
    needle = "a"
    haystack = "a"
    
    soln = Solution()
    print(soln.strStr(haystack, needle))
    assert soln.strStr("hello", "ll") == 2
    assert soln.strStr("aaaaa", "bba") == -1

