from scripts.hackerrank.arrayManipulation import arrayManipulation


class Test:
    
    test_cases = []
    testable_functions = [arrayManipulation]
    
    
    def test_arrayManipulation(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

        