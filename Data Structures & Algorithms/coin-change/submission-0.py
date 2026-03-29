class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = {0: 0}
        self.coins = coins 
        return self.coinChangeRec(amount)

    def coinChangeRec(self, amount: int) -> int: 
        if amount in self.mem:
            return self.mem[amount]
        if amount < 0:
            return -1
        minSteps = float('inf')
        found = False
        for c in self.coins:
            coinRes = self.coinChangeRec(amount-c)
            if coinRes >= 0:
                minSteps = min(minSteps, 1 + coinRes)
                found = True
        if not found:
            minSteps = -1
        self.mem[amount] = minSteps
        return minSteps
        

