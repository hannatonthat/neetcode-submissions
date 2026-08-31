class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPrice = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currPrice = prices[r] - prices[l]
                maxPrice = max(maxPrice, currPrice)
            else:
                l = r
            r += 1
        
        return maxPrice