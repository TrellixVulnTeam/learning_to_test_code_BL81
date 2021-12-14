import numpy as np
from typing import List, Dict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = postfix * res[j]
            postfix = postfix * nums[j]
        return res

class Solution2:

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
    
    solution = Solution2()
    print(solution.productExceptSelf(nums))


