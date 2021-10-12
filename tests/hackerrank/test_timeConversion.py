from scripts.hackerrank.timeConversion import timeConversion

class Test:
    test_cases = []
    testable_functions = [timeConversion]

    def test_time_conversion(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    