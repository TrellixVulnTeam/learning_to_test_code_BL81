from scripts.interview_questions_notion.quickSortRecursive import partition, quickSort

class Test:
    test_cases = [([8, 7, 2, 1, 0, 9, 6], sorted([8, 7, 2, 1, 0, 9, 6]))]
    testable_functions = [quickSort]
    partition_function = [partition]
    partition_test_cases = [
        ([8, 7, 2, 1, 0, 9, 6], 3)
        
        ]

    def test_partition(self):
        for f in self.partition_function:
            for [case, expected] in self.partition_test_cases:
                assert f(case, 0, len(case) - 1) == expected

    def test_quickSortRecursive(self):
        for f in self.testable_functions:
            for [case, expected] in self.test_cases:
                assert f(case, 0, len(case) - 1) == expected

