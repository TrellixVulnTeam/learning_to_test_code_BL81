# NOTE: remember python3 -m pytest tests/ from root dir
# NOTE: need that special path in constructor of tests dir
from scripts.leet75.twoSum import twoSum, Solution
"""
nums = [2,7,11,15], target = 9, Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]"""

class Test:
    test_cases = [
        ([[2, 7, 11, 15], 9], [0, 1]),
        ([[3, 2, 4], 6], [1, 2]),
        ([[3, 3], 6], [0, 1]) 
    ]
    testable_functions = [twoSum]
    solution = Solution()

    def test_twoSum(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case[0], case[1]) == expected

    def test_solution_twoSum(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.twoSum(case[0], case[1])

    def test_solution_twoSumHashMap(self):
        pass