

class Solution:
    def __init__(self):
        pass


if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    l, r = 0, 1
    maxsum = 0
    while r < len(nums):
        for i in range(2, len(nums)+1):
            part_left = nums[l]
            part_right = sum(nums[l+1:i])
            print(part_left, part_right)
            if part_left + part_right > maxsum:
                maxsum = part_left + part_right
            # maxsum = max(nums[l] + sum(nums[1:i]), maxsum)
        l += 1
        r += 1
    print(maxsum)
