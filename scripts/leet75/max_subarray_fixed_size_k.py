"""
Sliding Window Technique is one of the most used coding patterns that solve various complex problems in an optimized way by reducing time complexity and space complexity.

Problem Statement
Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'.
"""


def max_subarray_of_size_k(arr, k):
    max_sum, window_sum = 0, 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def bf_max_subarray_of_size_k(arr, k):
    res = []
    for i in range(len(arr)):
        for j in range(i, len(arr)+1):
            temp = arr[i:j]
            if len(temp) == 3:
                res.append(temp)
    # return max([sum(ele) for ele in res])
    # replace unneeded comprehension with generator
    return max(sum(ele) for ele in res)
    

if __name__ == "__main__":
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_subarray_of_size_k(nums, k))
    assert max_subarray_of_size_k(nums, k) == 9
    print(bf_max_subarray_of_size_k(nums, k))
