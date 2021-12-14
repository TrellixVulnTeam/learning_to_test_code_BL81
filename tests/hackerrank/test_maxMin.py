from scripts.hackerrank.maxMin import maxMin, maxMin2, maxMinBug


class Test:
    
    test_cases = [
        #["k", "arr"]
        [2, [1, 4, 7, 2], 1],
        [3, [10, 100, 300, 200, 1000, 20, 30], 20]
    ]
    testable_functions = [maxMin, maxMinBug, maxMin2]
    
    
    def test_maxMin(self):
        for f in self.testable_functions:
            for case in self.test_cases:
                assert case[2] == f(case[0], case[1])
                
if __name__ == "__main__":
    test = Test()
    print(test.test_cases[0])