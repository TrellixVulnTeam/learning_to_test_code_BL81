from scripts.hackerrank.lonelyInteger import lonelyInteger

class Test:
    test_cases = []
    testable_functions = [lonelyInteger]

    def test_lonelyInteger(arr):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    