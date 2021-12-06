from scripts.hackerrank.pageCount import pageCount


class Test:
    
    test_cases = [
        ([5, 3], 1)
    ]
    testable_functions = [pageCount]
    
    def test_pageCount(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case[0], case[1])
                