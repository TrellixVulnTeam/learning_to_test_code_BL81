

def plus_minus(arr):
    total = len(arr)
    pos = len([val for val in arr if val > 0]) / total
    neg = len([val for val in arr if val < 0]) / total
    zero = len([val for val in arr if val == 0]) / total

    params = [pos, neg, zero]
    print(params)
    for i in range(len(params)):
        params[i] = format(params[i], '.6f')

    # NOTE: cant do this!
    # for p in params:
    #     p = 0
    
    return params


if __name__ == "__main__":
    arr = [1, 1, 0, -1, -1]
    result = plus_minus(arr)
    print([i for i in result])