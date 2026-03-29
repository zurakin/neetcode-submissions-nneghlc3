class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0 
        minimumSoFar = prices[0]
        for i in range(1, len(prices)):
            bestProfit = max(bestProfit, prices[i]-minimumSoFar)
            minimumSoFar = min(minimumSoFar, prices[i])
        return bestProfit