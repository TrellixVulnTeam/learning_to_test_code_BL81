from typing import List, Dict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        idx1, idx2 = 0, 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
                    idx1, idx2 = i, j
        if maxProfit <= 0:
            return 0
        return maxProfit

prices = [7, 1, 5, 3, 6, 4]                   
solution = Solution()
maxProfit = solution.maxProfit(prices)
print(f"max profit: {maxProfit}")