class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            while l < r and prices[l] >= prices[r]:
                l += 1
            profit = prices[r] - prices[l]
            res = max(res, profit)
        
        return res