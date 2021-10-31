"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List

class Solution:
    
    def contains_duplicate(self, nums: List[int]) -> bool:
        # sourcery skip: for-index-replacement
        seen = []
        duplicates = []

        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            seen.append(nums[i])
        print(seen, duplicates)
        return len(duplicates) > 0

    def contains_duplicate_sliding_window(self, nums: List[int]) -> bool:
        l, r = 0, 1
        nums.sort()

        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            else:
                l += 1
                r += 1
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    solution = Solution()
    print(solution.contains_duplicate(nums))