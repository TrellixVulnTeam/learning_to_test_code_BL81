from scripts.hackerrank.dynamicArray import dynamicArray


class Test:
    
    test_cases = [
        [[1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]], 2, [7,3]
    ]
    testable_functions = [dynamicArray]
    
    def test_dynamic_array(self):
        for f in self.testable_functions:
            assert self.test_cases[-1] == dynamicArray(self.test_cases[1], self.test_cases[0])
                
                
if __name__ == "__main__":
    test = Test()
    print(test.test_cases[0])