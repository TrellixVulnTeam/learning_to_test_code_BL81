"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""

array_ints = [1, 2, 3, 1]
length_of_nums = len(array_ints) > 1

first, last = array_ints[0], array_ints[-1]

print(length_of_nums and (first == last))

def same_first_last(nums):
    length_of_nums = len(nums) > 1
    first, last = nums[0], nums[-1]
    return (length_of_nums and (first == last))

print(same_first_last(array_ints))