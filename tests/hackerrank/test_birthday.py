from scripts.hackerrank.birthday import Solution
from typing import Dict, List


class Test:
    params = {"s" : [[2, 2, 1, 3, 2],  [1, 2, 1, 3, 2]],
               "d" : [[4], [3]],
               "m" : [[2], [2]]
    }
    test_cases = [params, [2, 2]]
    
    def test_birthday(self):
        solution = Solution()
        assert self.test_cases[1][0] == solution.birthday(self.test_cases[0]["s"][0], self.test_cases[0]["d"][0][0], self.test_cases[0]["m"][0][0])
        
        assert self.test_cases[1][1] == solution.birthday(self.test_cases[0]["s"][1], self.test_cases[0]["d"][1][0], self.test_cases[0]["m"][1][0])