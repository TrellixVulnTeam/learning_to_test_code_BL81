from typing import List

def partition(array, low, high):
    # find pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse and find element less than pivot
    # low, high
    for j in range(low, high):
        if array[j] < pivot:
            # increment i
            i += 1

            # swap element less than pivot with greater element pointed by i
            array[i], array[j] = array[j], array[i]
    # swap pivot element with greater element pointed by i
    array[i+1], array[high] = array[high], array[i+1]

    # return the position from where partition is done
    return i+1
        

def quick_sort(array, low, high):
    if low < high:
        # get partition index
        pi = partition(array, low, high)

        # call recursively on left side
        quick_sort(array, low, pi - 1)

        # call recursively on right side
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