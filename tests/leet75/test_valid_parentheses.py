from scripts.leet75.valid_parentheses import Solution


class Test:
    test_cases = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False]
    ]
    
    def test_isValid(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.isValid(case) == expected