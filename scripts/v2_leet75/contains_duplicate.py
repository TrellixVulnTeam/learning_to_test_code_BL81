# question logged 4-27-22

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for k in counts:
            if counts[k] > 1: # "if any value appears at least twice"
                return True
        return False


if __name__ == '__main__':
    pass