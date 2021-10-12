
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
# left-to-right diagonal: 1 + 5 + 9 = 15
# right-to-left diagonal: 3 + 5 + 9 = 17
# | 15 - 17 | = 2

def diagonalDifference(arr):
    nrows = len(arr)
    ncols = len(arr[0])

    left_right = [(0, 0), (1, 1), (2, 2)]
    left_right_sum = 0
    right_left = [(0, 2), (1, 1), (2, 0)]
    right_left_sum = 0

    for row in range(nrows):
        for col in range(ncols):
            if (row, col) in left_right:
                left_right_sum += arr[row][col]
            if (row, col) in right_left:
                right_left_sum += arr[row][col]
    return abs(right_left_sum - left_right_sum)

if __name__ == "__main__":
    print(diagonalDifference(arr))