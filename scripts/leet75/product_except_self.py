import numpy as np
from typing import List, Dict

class Solution:

    # not O(n) solution like question asks, but works
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = 1
        result = []
        for index, num in enumerate(nums):
            # copy original nums and remove num at current loop index
            tmp = nums[:]
            tmp.remove(num)
            
            # mult. the remaining numbers together in the tmp list and increment the output
            for element in tmp:
                output *= element
            
            # append result of multiplication to results array
            result.append(output)

            # reset output to 1 for next number through loop
            output = 1

        return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))


