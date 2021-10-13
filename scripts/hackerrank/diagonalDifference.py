
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
# left-to-right diagonal: 1 + 5 + 9 = 15
# right-to-left diagonal: 3 + 5 + 9 = 17
# | 15 - 17 | = 2

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14
# 16 17 18 19

# row 0 : col 0
# row 1 : col 1
# row 2 : col 2

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

def diagonalDifference2(arr):
    nrows = len(arr)
    ncols = len(arr[0])

    col_idx = 0
    left_right_sum = 0
    for row in range(nrows):
        #print(f"col index: {col_idx}")
        for col in range(ncols):
            #print(f"row col {row, col, arr[row][col]}")
            if col == col_idx:
                left_right_sum += arr[row][col_idx]        
        col_idx += 1

    col_idx = len(arr) - 1
    right_left_sum = 0
    for row in range(nrows):
        for col in range(0, ncols):
            print(arr[row][col])
            if col == col_idx:
                print(arr[row][col])
                right_left_sum += arr[row][col_idx]
        col_idx -= 1
    print(left_right_sum, right_left_sum)
    return abs(left_right_sum - right_left_sum)


if __name__ == "__main__":
    #print(diagonalDifference(arr))
    print(diagonalDifference2(arr))