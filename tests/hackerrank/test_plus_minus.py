from scripts.hackerrank.plus_minus import plus_minus


class Test:
    # NOTE: Important note:
    # python will automatically truncate decimals in lists so need to explicitly delare precision
    test_cases = [
        ([1, 1, 0, -1, -1], [format(0.400000, '.6f'), format(0.400000, '.6f'), format(0.200000, '.6f')])
    ]
    testable_functions = [plus_minus]

    def test_plus_minus(self):
        for f in self.testable_functions:
            for [case, expected] in self.test_cases:
                print(case, expected)
                assert f(case) == expected
