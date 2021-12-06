from scripts.hackerrank.if_else import conditional, conditional2


class Test:
    
    test_cases = [
        [1, "Weird"],
        [22, "Not Weird"],
        [2, "Not Weird"],
        [29, "Weird"]
    ]
    testable_functions = [conditional, conditional2]
    
    def test_condtional(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case)
    
    