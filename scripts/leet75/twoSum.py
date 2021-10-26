from typing import Dict, List

nums = [2,7,11,15]

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
                
