def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2-1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
        
    output = []
    for i in range (n):
        if i == n-1:
            print(a[i])
            output.append(a[i])
        else:
            print(a[i], end = ' ')
            output.append(a[i])
    return output

# def findZigZagSequence2(a, n):
#     a.sort()
#     mid = int((n + 1)/2-1)
#     print(f'a before : {a}')
#     a[mid], a[n-1] = a[n-1], a[mid]
#     print(f'a after : {a}')
#     print(f'mid: {mid}, arr[mid]: {a[mid]}')
#     print(f'n-1: {n-1}, a[n-1]: {a[n-1]}')
#     #    1  2  3  4  5  6  7
#     #             M
#     #    1  2  3  7  5  6  4
#     #    1  2  3  7  6  5  4
#     output = a[:mid+1]
#     min1 = min(a[mid+1:])
#     max1 = max(a[mid+1:])
#     right_half = [i for i in range(min1, max1+1)]
#     result = [i for i in range(min1, max1+1)]
#     output += result[::-1]
#     print(f'result: {output}')


if __name__ == "__main__":
    a = [2, 3, 5, 1, 4]
    # a = [1, 2, 3, 4, 5, 6, 7]
    #    +  +  +  M  -  -  -
    #    1  2  3  7  5  6  4  
    #    1  2  3  7  6  5  4  
    # a = [2, 3, 5, 4, 1, 6, 7]
    # a = [1, 2, 3, 4, 5]
    # logic: put biggest number from rightmost of sorted array in the middle and then just keep swapping the right side of mid
    # sorted:
    #   [1, 2, 3, 4, 5]
    #    +  +  M  -  -
    #    1  2  3  5  4
    #    1  2  5  3  4
    #    1  4  5  3  2
    # answer: 
    #   [1, 4, 5, 3, 2]
    #    +  +  M  -  -
    n = 5
    print(findZigZagSequence(a, n))
    print(a[n-2])
    print(int(n+1)/2-1)
    
