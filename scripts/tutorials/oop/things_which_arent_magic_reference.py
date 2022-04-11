# https://ains.co/blog/things-which-arent-magic-flask-part-1.html
# KZ 4-7-22


class NotFlask:
    pass



if __name__ == "__main__":
    # nums = [1, 3, 5, 6]
    nums = [1, 3, 5, 6]
    target = 5

    if target < nums[0]:
        print(f"returning {0}")
        # return 0
    elif target > nums[-1]:
        print(f"returing {len(nums)}")
        # return len(nums)

    for i in range(len(nums)):
        if nums[i] == target:
            print(f'target found: {nums[i]}@{i}')
            # return i
        elif nums[i] > target:
            print(i-1)