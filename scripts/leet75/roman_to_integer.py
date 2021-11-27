from typing import List, Dict


class Solution:
    counts = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    outliers = {
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900
    }
    
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in self.outliers:
                total += self.outliers[s[i:i+2]]
                i += 2
            else:
                total += self.counts[s[i]]
                i += 1  
        return total

solution = Solution()
strs = [("XIV", 14), ("XVII", 17), ("III", 3), ("MCMXCIV", 1994), ("IX", 9)]
for s in strs:
    # print(solution.romanToInt(s[0]))
    assert s[1] == solution.romanToInt(s[0])