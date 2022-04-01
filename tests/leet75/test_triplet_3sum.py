from scripts.leet75.three_sum import Solution


class Test:
    test_cases = [
        [[-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]],
        [[], []],
        [[0], []]
    ]
    
    def test_three_sum(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert expected == solution.threeSum(case)