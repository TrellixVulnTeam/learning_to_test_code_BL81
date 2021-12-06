from scripts.hackerrank.maximalSquare import Solution

class Test:
    test_cases = [
        [[
            [1, 1, 0],
            [1, 1, 0],
            [1, 0, 1]], 4],
        [[
            [0, 1],
            [1, 0]], 1],
        [[
            [0]], 0]
    ]
    
    def test_maximalSquare(self):
        solution = Solution()
        for case, expected in self.test_cases:
            assert expected == solution.maximalSquare(case)
    
if __name__ == "__main__":
    test = Test()
    print(test.test_cases[2])