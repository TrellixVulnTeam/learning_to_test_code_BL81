from scripts.leet75.implement_strstr import Solution


class Test:
    
    test_cases = [
        ["hello", "ll", 2],
        ["aaaaa", "bba", -1],
        ["a", "a", 0]
    ]

    def test_implement_strstr(self):
        soln = Solution()
        for arg1, arg2, expected in self.test_cases:
            assert soln.strStr(arg1, arg2) == expected
    
