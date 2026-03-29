class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = set()
        queue = [(0, 0)]
        while len(queue) > 0:
            nodeAmount, pathLength = queue.pop(0)
            if nodeAmount in visited:
                continue
            visited.add(nodeAmount)
            for c in coins:
                neighborAmount = nodeAmount + c
                neighborLength = pathLength + 1
                if neighborAmount == amount:
                    return neighborLength
                elif neighborAmount < amount:
                    queue.append((neighborAmount, neighborLength))
        return -1



    def coinChange1(self, coins: List[int], amount: int) -> int:
        self.mem = {0: 0}
        self.coins = coins 
        self.gcd = math.gcd(*coins)
        return self.coinChangeRec(amount)

    def coinChangeRec(self, amount: int) -> int: 
        if amount in self.mem:
            return self.mem[amount]
        if amount < 0 or amount % self.gcd != 0:
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
        

