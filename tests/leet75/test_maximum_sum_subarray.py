from scripts.leet75.maximum_sum_subarray import Solution


class Test:
    
    test_cases = [
        [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
        [[5, 4, -1, 7, 8], 23],
        [[1], 1]
    ]
    
    def test_brute_force_maxSubArray(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.maxSubArrayBruteForce(case) == expected

    def test_maxSubArray(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.maxSubArray(case) == expected