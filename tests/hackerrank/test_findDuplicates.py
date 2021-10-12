from scripts.hackerrank.findDuplicates import findDuplicates

class Test:
    test_cases = [
        [[1, 2, 2, 3, 4], 2]

    ]
    testable_functions = [findDuplicates]
    def test_findDuplicates(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    