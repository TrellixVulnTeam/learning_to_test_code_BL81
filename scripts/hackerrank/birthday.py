import itertools
from typing import Dict, List
from itertools import permutations
from collections import Counter

class Solution:
    def birthday(self, s: List[int], d: int, m: int) -> List[int]:
        matches = []
        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                if sum(s[i:j]) == d and len(s[i:j]) == m:
                    matches.append((s[i:j]))
        return len(matches)
        
        
if __name__ == "__main__":
    params = {"s" : [[2, 2, 1, 3, 2],  [1, 2, 1, 3, 2]],
               "d" : [[4], [3]],
               "m" : [[2], [2]]
    }
    solution = Solution()
    print(params["d"][1][0])
    print(solution.birthday(params["s"][1], params["d"][1][0], params["m"][1][0]))
    # difference between append and += for lists?