from scripts.leet75.product_except_self import Solution, Solution2

class Test:
    test_cases = [
        [[1,2,3,4], [24,12,8,6]],
        [[-1,1,0,-3,3], [0,0,9,0,0]]
    ]
    solution_objects = [Solution, Solution2]

    def test_product_except_self(self):
        for obj in self.solution_objects:
            o = obj()
            for case, expected in self.test_cases:
                assert expected == o.productExceptSelf(case)