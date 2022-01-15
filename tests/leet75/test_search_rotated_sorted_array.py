from scripts.leet75.search_rotated_sorted_array import Solution


class Test:
    
    test_cases = [
        [[4,5,6,7,0,1,2], 0, 4],
        [[4,5,6,7,0,1,2], 3, -1],
        [[1], 0, -1],
    ]    

    def test_search(self):
        solution = Solution()
        for case, target, expected in self.test_cases:
            assert solution.search(case, target) == expected