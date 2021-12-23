

def rotateLeft(d, arr):
    return arr[d:] + arr[:d]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    print(rotateLeft(d, arr))

        