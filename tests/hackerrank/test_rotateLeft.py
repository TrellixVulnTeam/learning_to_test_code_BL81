from scripts.hackerrank.rotateLeft import rotateLeft

class Test:
    
    test_cases = [
        [list(range(1, 6)), 2, [3, 4, 5, 1, 2]],
        [list(range(1, 6)), 1, [2, 3, 4, 5, 1]],
        [list(range(1, 6)), 5, [1, 2, 3, 4, 5]],
        [list(range(1, 6)), 4, [5, 1, 2, 3, 4]],

    ]
    
    testable_functions = [rotateLeft]
    
    def test_rotateLeft(self):
        for f in self.testable_functions:
            for case in self.test_cases:
                assert f(case[1], case[0]) == case[-1]
    
    
if __name__ == "__main__":
    arr = list(range(1, 6))
    t = Test()
    print(t.test_cases[0])
    
