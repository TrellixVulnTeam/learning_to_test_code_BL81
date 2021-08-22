"""

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

nums = [1, 2, 3]

# element_to_shift = nums.pop(0)
# print(element_to_shift)
# print(nums)
# nums.append(element_to_shift)
# print(nums)

def rotate_left3(nums):
    print(f"Original: {nums}")
    element_to_shift = nums.pop(0)
    nums.append(element_to_shift)
    print(f"Shifted: {nums}")

print(rotate_left3(nums))