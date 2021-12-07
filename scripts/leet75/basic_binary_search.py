
# - binary search is a searching algorithm for finding an elements position in a sorted array
# - binary search assumes you are working on a sorted list of items. If the elements are not already sorted, we must sort them first or binary search will not work

class Solution:
    def binary_search(self, array, x, low, high):
        # repeat until the pointers low and high meet eachother
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if array[mid] == x:
                return mid
            
            elif array[mid] < x:
                low = mid + 1
            
            else:
                high = mid - 1
       
        return -1    