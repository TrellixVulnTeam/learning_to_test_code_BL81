

def balancedSums(arr):
    total = sum(arr)
    add = 0
    for element in arr:
        if add == total-element-add:
            return "YES"
        add += element
    return "NO"


def balancedSumsBug(arr):
    """
    This is my solution to this problem. It fails a couple of the hidden tests cases on leetcode because it says it takes too long to run. Need hackerrank subscription to see input that fails so need to track down why this is too slow for hackerrank to accept.
    """
    for idx, number in enumerate(arr):
        before = arr[:idx]
        after = arr[idx+1:]
        if sum(before) == sum(after):
            return "YES"
    return "NO"

if __name__ == "__main__":
    arr = [5, 6, 8, 11]
    print(sum(arr))
    print(balancedSumsBug(arr))