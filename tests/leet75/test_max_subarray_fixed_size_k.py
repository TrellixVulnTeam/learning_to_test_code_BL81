from scripts.leet75.max_subarray_fixed_size_k import max_subarray_of_size_k


class Test:
    test_cases = [
        [[2, 1, 5, 1, 3, 2], 3, 9],
        [[1, 1, 1, 1], 4, 4]
    ]
    testable_functions = [max_subarray_of_size_k]
    
    def test_max_subarray_of_size_k(self):
        for f in self.testable_functions:
            for case, k, expected in self.test_cases:
                assert f(case, k) == expected