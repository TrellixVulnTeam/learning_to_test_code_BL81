from itertools import permutations
from typing import List


def maxMinBug(k: int, arr: List[int]) -> int:
    """
    NOTE: This function fails a "hidden" test cases on leet code that requires a premium subscription. Need to continue thinking about what tests this function is failing.
    """
    output = 1e10
    perms = permutations(arr, k)
    for p in perms:
        print(p)
        minv, maxv = min(p), max(p)
        unfairness = maxv - minv
        output = min(output, unfairness)
    return output

"""
Leetcode discussions entry regarding logic of solution: "Since we take the max and min of the same array, we know that given the sorted array the maximum is going to be arr[i+k] (the rightmost (greatest) element in the sorted array for k element) and the minimum is going to be arr[i] (the leftmost (smallest)) assume k=3, i=0, a=[3,10,23,24,25], if you have [3,10,23], max[3,10,23] = a[i+k] and min[3,10,23] = a[i]
"""

def maxMin(k, arr):
    arr.sort()
    diff_arr = []
    i = 0
    while k+i <= len(arr):
        diff_arr.append(arr[(k+i) - 1] - arr[i])
        i += 1
    return min(diff_arr)


def maxMin2(k, arr):
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))
            
if __name__ == "__main__":
    case = [2, [1, 4, 7, 2], [1]]
    print(maxMin(case[0], case[1]))
    print(case[2])
