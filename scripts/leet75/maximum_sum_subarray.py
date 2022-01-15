"""
https://leetcode.com/problems/maximum-subarray/
53. Maximum Subarray [easy]

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


from typing import List


class Solution:
    # can only do this ....
    # def max_sub_array_of_size_k(k, arr)
    # ...way if you know "k" aka length of the largest element
    
    # Input: [2, 1, 5, 1, 3, 2], k=3 
    # Output: 9
    # Explanation: Subarray with maximum sum is [5, 1, 3].
    
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum, window_sum = 0, 0
    #     window_start = 0
    #     k = 1
        
    #     for window_end in range(len(nums)):
    #         window_sum += nums[window_end]
            
    #         if 
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = nums[0]
        for i in range(1, len(nums)):
            curVal = nums[i]
            curSum = max(curVal, curSum + curVal)
            maxSum = max(maxSum, curSum)
        return maxSum
        
    def maxSubArrayBruteForce(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                temp = 0
                for k in range(i, j):
                    temp += nums[k]
                res.append(temp)
        return max(res)

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArrayBruteForce(nums))
    assert solution.maxSubArrayBruteForce(nums) == 6
    
    print(solution.maxSubArray(nums))
    assert solution.maxSubArray(nums) == 6