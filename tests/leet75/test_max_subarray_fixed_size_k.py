from scripts.leet75.max_subarray_fixed_size_k import Solution

"""
Find the max sum subarray of a fixed size K
"""

class Test:
    test_cases = [
        [[4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 0]
    ]
    solution = Solution()

    def test_max_sum_subarray(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.max_sum_subarray(case)