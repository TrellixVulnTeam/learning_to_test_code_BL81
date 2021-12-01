
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # get frequency count w/ dictionary
    counts = {}
    for number in ar:
        counts[number] = counts.get(number, 0) + 1
    
    for key in counts:
        counts[key] = int(counts[key] / 2)
        
    return sum([counts[key] for key in counts])

def sockMerchant2(n, arr):
    arr.sort()
    print(arr)
    matches = 0
    l, r = 0, 1
    while r < len(arr):
        print(f'l,r: {l, r, arr[l], arr[r]}')
        if arr[l] == arr[r]:
            matches += 1
            l += 2
            r += 2
        else:
            r += 1
            l += 1
    return matches
        
    
if __name__ == "__main__":
    ar = [1, 2, 1, 2, 1, 3, 2, 1]
    #     1  1  1  2  2  2  3
    print(sockMerchant2(7, ar))
    