from scripts.leet75.maximum_product_subarray import Solution


class Test:
    test_cases = [
        [[2, 3, -2, 4], 6],
        [[-2 , 0, -1], 0]
    ]
    
    
    def test_max_product_subarray(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert solution.maxProduct(case) == expected

    