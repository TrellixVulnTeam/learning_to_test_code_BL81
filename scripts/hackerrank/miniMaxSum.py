#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def one_removed(arr):
    one_removed = []
    for element in arr:
        arr_copy = arr[:]
        arr_copy.remove(element)
        one_removed.append(arr_copy)
    return one_removed

def miniMaxSum(two_dim_arry, *args, **kwargs):
    # Write your code here
    min_sum, max_sum = 100000000000, -1000000000000
    for arr in two_dim_arry:
        after_add = sum(arr)
        if after_add < min_sum:
            min_sum = after_add
        
        if after_add > max_sum:
            max_sum = after_add

    return [min_sum, max_sum]

# def test_minimax_sum(two_d_arr, expected):
#     inp1 = one_removed(two_d_arr)
#     assert miniMaxSum(inp1) == expected

    
if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 3, 5, 7, 9]
    expected = [16, 24]
    one_removed_2d_array = one_removed(arr)
    print(miniMaxSum(one_removed_2d_array))

    #test_minimax_sum(one_removed_2d_array, expected)
