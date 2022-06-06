from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int):

nums = [2, 7, 11, 15]
target = 9

for i, num in enumerate(nums):
    first = nums[i]
    for j, num in enumerate(nums):
        second = nums[j]
        if first + second == target:
            print(i, j)
