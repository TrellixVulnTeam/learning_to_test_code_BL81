arr = [
    [1, 2], 
    [3, 4]
]
    # 3 2
    # 1 4
nrows = len(arr)
ncols = len(arr[0])

reversed_cols = []
for col in range(ncols):
    tmp_col = []
    for row in range(nrows):
        print(arr[row][col])
        tmp_col.append(arr[row][col])
    tmp_col.reverse()
    reversed_cols.append(tmp_col)

print(f'reversed_cols: {reversed_cols}')
for col in range(ncols):
    if col == 0:
        for row in range(nrows):
            arr[row][col] = reversed_cols[col][row]
print(arr)


for element in arr:
    print(element, end="\n")
