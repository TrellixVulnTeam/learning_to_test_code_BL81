from scripts.hackerrank.isLeapYear import is_leap, is_leap2, is_leap3, is_leap4


class Test:
    
    test_cases = [
        [2004, True],
        [2008, True],
        [2012, True],
        [2016, True],
        [2005, False],
        [2009, False],
        [2013, False],
        [2017, False],
    ]
    testable_functions = [
        is_leap, is_leap2, is_leap3, is_leap4
    ]
    
    def test_is_leap(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case)
        