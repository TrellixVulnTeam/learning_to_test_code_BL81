from collections import Counter

arr = [1, 2, 3, 4, 3, 2, 1]

def lonelyInteger(arr):
    cnt = Counter(arr)
    wanted = {k for k,v in cnt.items() if v == 1}
    return (list(wanted)[0])

lonelyInteger(arr)