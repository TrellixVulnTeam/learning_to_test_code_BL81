from scripts.leet75.search_rotated_sorted_array import Solution


class Test:
    
    test_cases = [
        [[3, 4, 5, 6, 7, 8, 9], 4, 1],
        [[0, 1, 2], 0, 0]
    ]    

    def test_search(self):
        solution = Solution()
        for case, target, expected in self.test_cases:
            assert solution.search(case, target) == expected