from scripts.leet75.basic_binary_search import Solution


class Test:
    test_cases = [
        [[3, 4, 5, 6, 7, 8, 9], 4, 1],
        [[3, 4, 5, 6, 7, 8, 9], 4, 1]

    ]
        
    def test_binary_search(self):
        solution = Solution()
        for case in self.test_cases:
            assert case[2] == solution.binary_search(case[0], case[1], 0, len(case[0]) - 1)
    
    
if __name__ == "__main__":
    t = Test()
    # for x, y, z in t.test_cases:
    #     print(x, y, z)
    for x in t.test_cases:
        print(x[0])