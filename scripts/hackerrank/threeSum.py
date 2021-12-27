# program to find a triplet that sums to a given value


def threeSum(array, target):
    for i in range(len(array) - 2):
        for j in range(i+1, len(array) - 1):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == target:
                    print(f'target found: {array[i]} + {array[j]} + {array[k]} = {target}')  
                    return True
    return False

def twoSum(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(f'target found: {array[i]} + {array[j]} = {target}')
                return True
    return False


if __name__ == "__main__":
    array = [1, 4, 45, 6, 10, 8]
    target = 22
    print(twoSum(array, target))
    print(threeSum(array, target))