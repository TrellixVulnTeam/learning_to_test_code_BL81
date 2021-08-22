"""

Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""

array = [1, 2, 6]
array = [13, 6, 1, 2, 3]
first, last = array[0], array[-1]

if (first == 6) or (last == 6):
    print("True")
else:
    print("False")

def first_last6(nums):
    first, last = nums[0], nums[-1]
    return (first == 6) or (last == 6)

print(first_last6(array))