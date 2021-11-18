from scripts.leet75.final_value_after_operations import Solution

class Test:
    test_cases = [
        [["--X","X++","X++"], 1]
    ]
        
    def test_solution(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert expected == solution.final_value_after_operations(case)
