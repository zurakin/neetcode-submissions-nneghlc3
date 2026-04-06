class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 

        tPlus1Holding = 0
        tPlus1NotHolding = 0
        tPlus2Holding = 0
        tPlus2NotHolding = 0 
        for i in range(len(prices)-2, -1, -1):
            currentPriceHolding = max(tPlus2NotHolding, prices[i+1]-prices[i] + tPlus1Holding)
            currentPriceNotHolding = max(tPlus1NotHolding, prices[i+1]-prices[i] + tPlus1Holding)
            res = max(res, currentPriceNotHolding) 
            tPlus1Holding, tPlus2Holding = currentPriceHolding, tPlus1Holding 
            tPlus1NotHolding, tPlus2NotHolding = currentPriceNotHolding, tPlus1NotHolding 
        return res