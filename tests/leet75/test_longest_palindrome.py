from scripts.leet75.longest_palindrome import Solution

class Test:
    test_cases = [
        ["abbb", "bbb"]
    ]
    
    def test_longest_palindrome(self, s: str) -> str:
        solution = Solution()
        assert self.test_cases[1] == solution.longestPalindrome(self.test_cases[0])