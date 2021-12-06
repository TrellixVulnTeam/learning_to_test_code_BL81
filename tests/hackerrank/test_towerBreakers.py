from scripts.hackerrank.towerBreakers import towerBreakers

class Test:
    test_cases = [
        [[2, 2], 2],
        [[1, 4], 1]
    ]
    testable_functions = [towerBreakers]
    
    def test_towerBreakers(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case[0], case[1])