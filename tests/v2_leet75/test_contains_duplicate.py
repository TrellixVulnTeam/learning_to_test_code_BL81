from scripts.v2_leet75.contains_duplicate import Solution


class Test:
    test_cases = [
        [[1,2,3,1], True],
        [[1,2,3,4], False],
        [[1,1,1,3,3,4,3,2,4,2], True],    
        [[], False],    
        [[0], False],    
    ]

    def test_contains_duplicate(self):
        soln = Solution()
        for case, expected in self.test_cases:
            assert soln.containsDuplicate(case) == expected
