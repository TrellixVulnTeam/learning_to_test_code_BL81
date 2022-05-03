# question logged 4-27-22


from typing import List

# Time/space analysis Solution1
# time: O(n) because two times through list, but only 1) keep fastest growing term and 2) drop constants
# space: O(1)? for dict?

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for k in counts:
            if counts[k] > 1: # "if any value appears at least twice"
                return True
        return False

class Solution2:
    pass
