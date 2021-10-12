from scripts.hackerrank.lonelyInteger import lonelyInteger

class Test:
    test_cases = [[1, 2, 3, 4, 3, 2, 1], 4]
    testable_functions = [lonelyInteger]

    def test_lonelyInteger(self):
        assert self.testable_functions[0](self.test_cases[0]) == self.test_cases[1]

    