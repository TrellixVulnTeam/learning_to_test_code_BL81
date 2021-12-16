from scripts.hackerrank.gridChallenge import gridChallenge, gridChallenge2


class Test:
    
    test_cases = []
    testable_functions = [gridChallenge, gridChallenge2]
    
    
    def test_gridChallenge(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case)
                
                
if __name__ == "__main__":
    test = Test()
    