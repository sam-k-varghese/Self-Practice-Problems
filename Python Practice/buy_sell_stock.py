# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pro = float("inf")
        max_pro = 0
        for i in range(0, len(prices)):
            min_pro = min(min_pro,prices[i])
            max_pro = max(max_pro, prices[i]-min_pro)
        return max_pro
        

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))