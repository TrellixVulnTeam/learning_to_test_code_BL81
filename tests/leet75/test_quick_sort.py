from scripts.leet75.quick_sort import quick_sort, partition

class Test:
    test_cases = {
        "partition" : [
            [8, 7, 6, 1, 0, 9, 2], 2],
        "sort" : [[8, 7, 2, 1, 0, 9, 6],
            [0, 1, 2, 6, 7, 8, 9]]
    }
    testable_functions = []

    def test_partition(self):
        for key, value in self.test_cases.items():
            if key == "partition":
                assert self.test_cases[key][1] == partition(self.test_cases[key][0], 0, len(self.test_cases[key][0]) - 1)

    def test_quicksort(self):
        for key, value in self.test_cases.items():
            if key == "sort":
                assert self.test_cases[key][1] == quick_sort(self.test_cases[key][0], 0 , len(self.test_cases[key][0]) - 1)