"""
35. Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            print(f"returning {0}")
            return 0
        elif target > nums[-1]:
            print(f"returing {len(nums)}")
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                print(i)
                return i

if __name__ == '__main__':
    # case, target, expected_output
    test_cases = [
    [[1,3,5,6], 5, 2],
    [[1,3,5,6], 2, 1],
    [[1,3,5,6], 7, 4]
    ]

    for a, b, c in test_cases:
        print(a, b, c)