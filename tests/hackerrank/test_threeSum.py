from scripts.hackerrank.threeSum import threeSum, twoSum


class Test:
    test_cases_three = [
        [[1, 2, 3], 6, True]
    ]
    test_cases_two = [
        [[0, 0, 1, 2, 3], 0, True]
    ]
    
    def test_threeSum(self):
        for case, target, expected in self.test_cases_two:
            assert threeSum(case, target) == expected
    
    def test_twoSum(self):
        for case, target, expected in self.test_cases_two:
            assert twoSum(case, target) == expected
    
    
if __name__ == "__main__":
    tester = Test()
    print(tester.test_cases[0])
    for case, expected in tester.test_cases:
        print(case, expected)
