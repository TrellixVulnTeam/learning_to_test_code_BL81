


def arrayManipulation(n, queries):
    arr = [0] * n
    print(arr)
    # prev_bounds = (1, 5)
    prev_bounds = queries[0][0], queries[0][1]
    prev_value = 0

    for i in range(0, len(queries)):
        start, stop, value = queries[i]
        print(start, stop, value)
        
        for j in range(start-1, prev_bounds[1]):
            arr[j] = value + prev_value
        
        for k in range(prev_bounds[1], stop):
            print(k)
            arr[k] = value
        
        print(arr)
        prev_bounds = start, stop
        prev_value = value
    return max(arr)

if __name__ == "__main__":
    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]
    ]
    n = 10
    print(arrayManipulation(n, queries))
