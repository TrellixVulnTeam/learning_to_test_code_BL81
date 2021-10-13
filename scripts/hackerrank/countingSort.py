from collections import Counter

arr = [1, 1, 3, 2, 1]

def countingSort(arr):
    counts = {}
    for i in range(0, 101):
        counts[i] = counts.get(i, 0)
    for i in range(len(arr)):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
    # for element in arr:
    #     counts[element] = counts.get(element, 0) + 1
    #     print(element, counts)
    #print(counts)
    return [i for i in counts.values()]


print(countingSort(arr))

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14
# 16 17 18 19

# row 0 : col 0
# row 1 : col 1
# row 2 : col 2