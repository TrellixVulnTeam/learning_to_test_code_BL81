from scripts.hackerrank.countingSort import countingSort

class Test:
    test_cases = []
    testable_functions = []

    def test_countingSort(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    