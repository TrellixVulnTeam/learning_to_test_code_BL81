from scripts.leet75.maximum69number import Solution


class Test:
    test_cases = [
        [9669, 9969],
        [9999, 9999],
        [9996, 9999]
    ]

    def test_maximum69number(self):
        soln = Solution()
        for case, expected in self.test_cases:
            assert soln.maximum69Number(case) == expected
        