from scripts.leet75.maxNumberOfBalloons import Solution


class Test:
    test_cases = [
        ["nlaebolko", 1],
        ["loonbalxballpoon", 2],
        ["leetcode", 0]
    ]
    
    def test_maxNumberOfBalloons(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.maxNumberOfBalloons(case) == expected