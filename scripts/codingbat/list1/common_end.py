"""

Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""

a = [1, 2, 3]
b = [7, 3, 2]

first_a, last_a = a[0], a[-1]
first_b, last_b = b[0], b[-1]

cond = (first_a == first_b) or (last_a == last_b)
print(cond)

def common_end(a, b):
    first_a, last_a = a[0], a[-1]
    first_b, last_b = b[0], b[-1]
    return (first_a == first_b) or (last_a == last_b)

print(common_end(a, b))