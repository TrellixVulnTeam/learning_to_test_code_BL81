from scripts.leet75.product_except_self import Solution

class Test:
    test_cases = [
        [[1,2,3,4], [24,12,8,6]],
        [[-1,1,0,-3,3], [0,0,9,0,0]]
    ]
    testable_functions = []
    solution = Solution()
    
    def test_product_except_self(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.productExceptSelf(case)