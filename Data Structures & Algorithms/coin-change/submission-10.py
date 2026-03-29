class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = set()
        queue = [[0]]
        pathLength = 0
        while len(queue) > 0:
            nodeAmounts = queue.pop(0)
            neighbors = []
            for nodeAmount in nodeAmounts:
                if nodeAmount in visited:
                    continue
                visited.add(nodeAmount)
                if nodeAmount == amount:
                    return pathLength
                if nodeAmount > amount:
                    continue
                for c in coins:
                    neighbors.append(nodeAmount + c)
            pathLength += 1
            if len(neighbors) > 0:
                queue.append(neighbors)
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
        

