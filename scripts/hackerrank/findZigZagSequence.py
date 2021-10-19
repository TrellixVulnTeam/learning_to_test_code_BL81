import math

a = [2, 3, 5, 1, 4]
n = len(a)

a.sort()
print(f"a.sort(): {a}")
mid = int((n + 1)/2)
print(math.ceil(5/2))
print(f"mid: {mid}")

print(f"a[mid], a[n-1] before...: {a[mid], a[n-1]}")
a[mid], a[n-1] = a[n-1], a[mid]
print(f"a[mid], a[n-1] after...: {a[mid], a[n-1]}")


#NOTE: modify mid? should be arr[2]: 3 instead of arr[3]: 4
# therefore, a[mid - 1]?

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

arr = [2, 3, 5, 1, 4]
print(findZigZagSequence(arr, len(arr)))
