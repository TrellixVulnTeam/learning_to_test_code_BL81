from typing import Dict, List
import time

def twoSum(arr: List[int], targetSum: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == targetSum:
                return [i, j]

class Solution:
    def twoSum(self, arr: List[int], targetSum: int) -> List[int]:
        for i in range(len(arr)):
            first_number = arr[i]
            for j in range(i+1, len(arr)):
                second_number = arr[j]
                if first_number + second_number == targetSum:
                    return [i, j]
        return False
                
    def twoSumHashMap(self, arr: List[int], target: int) -> List[int]:
        pass

if __name__ == "__main__":
    nums = [2,7,11,15]
    targetSum = 9
    for i in range(10):
        start = time.perf_counter()
        print(f"{i}, {twoSum(nums, targetSum=targetSum)}")
        duration = time.perf_counter() - start
        print(f"{duration * 1000:.1f}ms")