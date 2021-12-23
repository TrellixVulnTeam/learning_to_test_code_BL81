from scripts.hackerrank.matchingStrings import matchingStrings


class Test:

    # strings, queries
    test_cases = [
        [["ab", "ab", "abc"], 
        ["ab", "abc", "bc"], [2, 1, 0]]
    ]
    testable_functions = [matchingStrings]
    
    
    def test_matchingStrings(self):
        for f in self.testable_functions:
            for strings, queries, expected in self.test_cases:
                assert f(strings, queries) == expected