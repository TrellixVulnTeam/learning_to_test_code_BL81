from typing import List

# function to find partition position
def partition(array: List[int], low: int, high: int) -> int:
    # select pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse all elements
    # compare each element with pivot
    for j in range(low, high):
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
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array

if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 9, 6]
    print("Unsorted array")
    print(data)

    size = len(data)
    quick_sort(data, 0, size - 1)
    print("Sorted array in ascending order:")
    print(data)