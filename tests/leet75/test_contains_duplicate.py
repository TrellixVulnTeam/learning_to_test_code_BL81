from scripts.leet75.contains_duplicate import Solution

"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Test:
    test_cases = [
        [[1,2,3,1], True],
        [[1,2,3,4], False]
    ]
    testable_functions = []
    solution = Solution()

    def test_solution(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.contains_duplicate(case)

    def test_solution_contains_duplicate_sort(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.contains_duplicate_sort(case)

    def test_contains_duplicate_hashset(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.contains_duplicate_hashset(case)