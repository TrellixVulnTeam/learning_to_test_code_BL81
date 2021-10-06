# bubble sort

def bubbleSort(nums):  # sourcery skip: remove-zero-from-range
    for i in range(len(nums)):
        swapped = False

        for j in range(0, len(nums) - i - 1):
            print(f"i: {i}, j: {j}...{nums[i], nums[j], nums[j+1]}")
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                print(f"swapped")
                swapped = True
            else:
                print(f"not swapped")
        print(f"next i...")
        if not swapped:
            print("already sorted...breaking")
            break

    return nums

#nums = [-2, 45, 0, 11, -9]
nums = [1, 2, 1]

print(bubbleSort(nums))