"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

"""

nums = [1, 2, 3]
print(nums)
larger = nums[0] if nums[0] > nums[-1] else nums[-1]
for i in range(len(nums)):
    nums[i] = larger
print(nums)

def max_end3(nums):
    larger = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = larger
    return nums