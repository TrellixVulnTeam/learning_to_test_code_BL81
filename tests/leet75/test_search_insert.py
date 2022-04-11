from scripts.leet75.search_insert import Solution


class Test:
    # case, target, expected_output
    test_cases = [
        [[1,3,5,6], 5, 2],
        [[1,3,5,6], 2, 1],
        [[1,3,5,6], 7, 4]
    ]

    def test_search_insert(self):
        soln = Solution()
        for case, target, expected in self.test_cases:
            assert soln.searchInsert(case, target) == expected