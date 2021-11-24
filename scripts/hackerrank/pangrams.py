from abc import ABC
from typing import Dict, List
import string

class Solution:
    
    def pangrams(self, s: str) -> str:
        s = s.lower()
        counts = {}
        acsii_lowercase = string.ascii_lowercase
        for letter in acsii_lowercase:
            counts[letter] = counts.get(letter, 0) + 1
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        if any(v for (k, v) in counts.items() if v == 1):
            return "not pangram"
        else:
            return "pangram"
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.pangrams("We promptly judged antique ivory buckles for the next prize")) # pangram
    print(solution.pangrams("We promptly judged antique ivory buckles for the prize")) # not pangram