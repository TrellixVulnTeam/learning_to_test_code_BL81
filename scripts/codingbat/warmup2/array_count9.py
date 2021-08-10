"""
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

def array_count9(nums):
    pass

nums_array = [1, 2, 9]
count = 0
for num in nums_array:
    if num == 9:
        count += 1

print(count)
