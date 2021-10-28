from typing import Dict, List
import time
import numpy as np

def twoSum(arr: List[int], targetSum: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == targetSum:
                return [i, j]

def twoSumHashMap(arr: List[int], target: int) -> List[int]:
    prevMap = {} # val : index

    for idx, a in enumerate(arr):
        difference = target - a
        if difference in prevMap:
            return [prevMap[difference], idx]
        prevMap[a] = idx

def format_duration(duration: float) -> str:
    return f"{duration * 1000:.2f}ms"

class Solution:
    def twoSum(self, arr: List[int], targetSum: int) -> List[int]:
        for i in range(len(arr)):
            first_number = arr[i]
            for j in range(i+1, len(arr)):
                second_number = arr[j]
                if first_number + second_number == targetSum:
                    return [i, j]
        return False
                
    def twoSumHashMap(self, arr: List[int], targetSum: int) -> List[int]:
        prevMap = {} # val : index

        for idx, a in enumerate(arr):
            difference = targetSum - a
            if difference in prevMap:
                return [prevMap[difference], idx]
            prevMap[a] = idx
    

# just cause..
if __name__ == "__main__":
    nums = [2,7,11,15]
    targetSum = 9
    one_loop = []
    two_loop = []


    start = time.perf_counter()
    for i in range(10):
        print(f"{i}, {twoSumHashMap(nums, targetSum)}")
    duration = time.perf_counter() - start
    one_loop.append(duration)

    start = time.perf_counter()
    for i in range(10):
        print(f"{i}, {twoSum(nums, targetSum=targetSum)}")
    duration = time.perf_counter() - start
    two_loop.append(duration)

    formatted_one_loop = list(map(lambda x: format_duration(x), one_loop))
    print([i for i in formatted_one_loop])
    mean_one = np.mean(one_loop)
    print(f"mean: {format_duration(mean_one)}")
    print("mean: {}".format(mean_one))

    formatted_two_loop = list(map(lambda x: format_duration(x), two_loop))
    mean_two = np.mean(two_loop)
    print(f"mean: {format_duration(mean_two)}")

    print(f"average speed diff: mean_two - mean_one\n{format_duration(mean_two - mean_one)}")