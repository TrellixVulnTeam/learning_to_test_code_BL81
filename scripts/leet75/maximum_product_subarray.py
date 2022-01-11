"""
152. Maximum Product Subarray [medium]
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""


from typing import List, Dict


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totalMax = prevMax = prevMin = nums[0]
        for i, num in enumerate(nums[1:]):
            currentMin = min(num, prevMax*num, prevMin*num)
            currentMax = max(num, prevMax*num, prevMin*num)
            totalMax = max(currentMax, totalMax)
            prevMin = currentMin
            prevMax = currentMax
        return totalMax   
    
    
if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]

    solution = Solution()
    print(solution.maxProduct(nums))
    
                    
                    
        
        