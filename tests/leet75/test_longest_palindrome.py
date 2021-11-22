from scripts.leet75.longest_palindrome import Solution
from typing import Dict, List

class Test:
    test_cases = [
        ["abbb", "bbb"],
        ["cbbd", "bb"]
    ]
    
    def test_longest_palindrome(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert expected == solution.longestPalindrome(case)
        
    def test_bf_longest_palindrome(self):
        solution = Solution()
        assert self.test_cases[0][1] == solution.bf_longestPalindrome(self.test_cases[0][0])
        assert self.test_cases[1][1] == solution.bf_longestPalindrome(self.test_cases[1][0])
        