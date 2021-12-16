from scripts.hackerrank.balancedSums import balancedSumsBug, balancedSums


class Test:
    
    test_cases = [
        [[1, 2, 3], "NO"],
        [[1, 2, 3, 3], "YES"],
        [[5, 6, 8, 11], "YES"]
    ]
    testable_functions = [balancedSumsBug, balancedSums]
    
    def test_balancedSums(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case)
    
    
if __name__ == "__main__":
    test = Test()
    print(test.test_cases[0])