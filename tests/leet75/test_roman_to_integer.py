from scripts.leet75.roman_to_integer import Solution


class Test:
    test_cases = [("XIV", 14), ("XVII", 17), ("III", 3), ("MCMXCIV", 1994), ("IX", 9)]
    
    def test_roman_to_int(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert expected == solution.romanToInt(case)