from scripts.v2_leet75.contains_duplicate import Solution1, Solution2


class Test:
    test_cases = [
        [[1,2,3,1], True],
        [[1,2,3,4], False],
        [[1,1,1,3,3,4,3,2,4,2], True],    
        [[], False],    
        [[0], False],    
    ]

    def test_contains_duplicate(self):
        soln1, soln2 = Solution1(), Solution2()
        for case, expected in self.test_cases:
            assert soln1.containsDuplicate(case) == expected
            assert soln2.containsDuplicate(case) == expected
