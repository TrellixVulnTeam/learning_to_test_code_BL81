from scripts.leet75.search_2D_matrix import Solution


class Test:
    test_cases = [
        # matrix, target, expected_bool
        [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5, True],
        [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20, False]
    ]
    
    def test_search_2D_matrix(self):
        solution = Solution()
        for case, target, expected in self.test_cases:
            assert solution.searchMatrix(case, target) == expected