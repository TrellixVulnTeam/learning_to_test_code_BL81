from time import perf_counter
from typing import List
from itertools import permutations 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
        if maxProfit <= 0:
            return 0
        return maxProfit

    def maxProfitSlidingWindow(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l += 1
            r += 1
        return maxProfit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]                   
    solution = Solution()
    maxProfit = solution.maxProfit(prices)
    print(f"max profit: {maxProfit}")

    nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    for i in range(len(nums)):
        print(nums[i:i+3])

