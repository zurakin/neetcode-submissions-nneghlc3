class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                maxProfit += prices[i+1]-prices[i]
        return maxProfit