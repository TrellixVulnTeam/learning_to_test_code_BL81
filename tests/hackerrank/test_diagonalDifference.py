from scripts.hackerrank.diagonalDifference import diagonalDifference

class Test:
    test_cases_list = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
    test_cases_expected = 2
    testable_functions = [diagonalDifference]

    def test_diagonalDifference(self):
        assert self.testable_functions[0](self.test_cases_list) == self.test_cases_expected
