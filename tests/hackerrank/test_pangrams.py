from scripts.hackerrank.pangrams import Solution


class Test:
    
    
    test_cases = [
        ["We promptly judged antique ivory buckles for the prize", "not pangram"]
    ]
    
    def test_pangrams(self):
        solution = Solution()
        assert self.test_cases[0][1] == solution.pangrams(self.test_cases[0][0])