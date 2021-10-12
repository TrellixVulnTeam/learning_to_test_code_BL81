from scripts.hackerrank.miniMaxSum import miniMaxSum, one_removed

class Test:
    test_cases = [
        ([1, 3, 5, 7, 9], [16, 24])
    ]
    testable_functions = [miniMaxSum]

    def test_minimax_sum(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                two_d_arr = one_removed(case)
                assert f(two_d_arr) == expected

    