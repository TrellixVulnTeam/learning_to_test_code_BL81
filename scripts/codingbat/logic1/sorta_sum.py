"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""

a = 3
b = 4
sum_two_ints = a + b

if (10 <= sum_two_ints <= 19):
    print(f"Forbidden:\noutput: 20") # 20
print(sum_two_ints)

def sorta_sum(a, b):
    sum_a_b = (a + b)
    if (10 <= sum_a_b <= 19):
        return 20
    return sum_a_b
    