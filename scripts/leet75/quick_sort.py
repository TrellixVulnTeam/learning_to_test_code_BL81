from typing import List, Dict

# function to find partition position
def partition(array: List[List[int]], low: int, high: int) -> int:
    # select pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse all elements
    # compare each element with pivot
    for j in range(len(array)):
        if array[j] < pivot:
            # if element smaller than pivot found
            # swap it with greater element pointed to by i
            i += 1

            # swapping element at i with element at j 
            array[i], array[j] = array[j], array[i]
    
    # swap pivot element with greater element specified by i 
    array[i + 1], array[high] = array[high], array[i + 1]

    # return position from where partition is done
    return i + 1
        


def quick_sort(array, low, high):
    pass
