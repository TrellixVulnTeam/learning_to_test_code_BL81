from scripts.leet75.maxArea import Solution


class Test:
    test_cases = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49]
    ]
    
    
    def test_maxArea(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.maxArea(case) == expected
            