"""
LC 15. 3Sum [Medium]

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        target = 0
        
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[k]])
        return self.filter_results(res)
    
    def filter_results(self, l):
        res = []
        
        for elem in l:
            elem.sort()
            if elem not in res:
                res.append(elem)
        return res
    
    def filter_test(self, l):
        res = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                # remove triplets with Counter() from collections
                if Counter(l[i]) != Counter(l[j]):
                    res.append(l[i])
        return(res)
            

    
if __name__ == "__main__":
    from collections import Counter
    
    nums = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]
    # nums = [1, 4, 45, 6, 10, 8] # 22
    
    solution = Solution()
    res = solution.threeSum(nums)

    print(f'result: {res}')
    print("---")
    print(f'expected: {expected}')
    assert sorted(res) == sorted(expected)
    
    # same nums in different order 
    t = [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
    print(solution.filter_test(t))
    
"""    
def find3Numbers(A, arr_size, sum):
    
        # Fix the first element as A[i]
        for i in range( 0, arr_size-2):
    
            # Fix the second element as A[j]
            for j in range(i + 1, arr_size-1):
                
                # Now look for the third number
                for k in range(j + 1, arr_size):
                    if A[i] + A[j] + A[k] == sum:
                        print("Triplet is", A[i],
                            ", ", A[j], ", ", A[k])
                        return True
        
        # If we reach here, then no
        # triplet was found
        return False
    
    # Driver program to test above function
    A = [1, 4, 45, 6, 10, 8]
    sum = 22
    arr_size = len(A)
    find3Numbers(A, arr_size, sum)
    """