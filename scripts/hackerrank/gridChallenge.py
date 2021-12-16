import string

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        new=sorted(grid[i])
        grid[i]=''.join(new)
    for m in range(len(grid[0])):
        for n in range(len(grid)-1):
            print(m, n, grid[n][m])
            if grid[n][m]>grid[n+1][m]:
                return 'NO'
    return 'YES'

def gridChallenge2(grid):
    # Write your code here
    # first, sort the rows alpha-wiseby reassigning them
    # can't use row.sort() because strings are immutable and dont have sort method
    counter = 0
    # CANT DO row = "".join(sorted(grid[i])) here!!!
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))
        
    nrows = len(grid)
    ncols = len(grid[0])
    for j in range(ncols):
        temp = []
        for i in range(nrows):
            temp.append(grid[i][j])
        # print(temp, sorted(temp))
        if temp != sorted(temp):
            #print("NO")
            continue
            
        else:
            counter += 1
    # print(f'counter: {counter} ncols: {ncols}')
    if counter == ncols:
        return("YES") 
    else:
        return "NO"      
            

if __name__ == "__main__":
    grid = [
            "abc", 
            "ade", 
            "efg"
        ]
    # grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

    print(gridChallenge(grid))
    print(gridChallenge2(grid))