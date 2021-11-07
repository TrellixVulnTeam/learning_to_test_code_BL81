from scripts.leet75.quick_sort import quick_sort, partition

class Test:
    test_cases = [
        [[8, 7, 6, 1, 0, 9, 2], 2]
    ]
    testable_functions = []

    def test_partition(self):
        for case, expected in self.test_cases:
            assert expected == partition(case)