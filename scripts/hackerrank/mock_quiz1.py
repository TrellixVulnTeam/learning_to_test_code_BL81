import math
# find median

arr = [5, 3, 1, 2, 4]

def findMedian(arr):
    sorted_arr = sorted(arr)
    middle = math.ceil(len(sorted_arr) // 2)
    return sorted_arr[middle]


print(findMedian(arr))