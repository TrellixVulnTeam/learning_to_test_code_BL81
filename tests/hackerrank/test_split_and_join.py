from scripts.hackerrank.split_and_join import split_and_join


class Test:
    test_cases = []
    testable_functions = []

    def test_split_and_join(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected
    