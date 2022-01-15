from time import perf_counter
from typing import List
from itertools import permutations 


"""
LeetCode 121 Best Time To Buy And Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

    def maxProfitNonWorking(self, prices: List[int]) -> int:
        """
        This solution fails test cases on LC because it exceeds the time limit.
        """
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
        if maxProfit <= 0:
            return 0
        return maxProfit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]                   
    solution = Solution()
    maxProfit = solution.maxProfit(prices)
    print(f"max profit: {maxProfit}")

    nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    for i in range(len(nums)):
        print(nums[i:i+3])

