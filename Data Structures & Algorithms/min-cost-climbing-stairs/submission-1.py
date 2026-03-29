class Solution:
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        costs = [0 for _ in range(len(cost)+1)]
        for i in range(2, len(cost)+1):
            costs[i] = min(cost[i-1]+costs[i-1], cost[i-2]+costs[i-2])
        return costs[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minus1 = 0
        minus2 = 0
        currentCost = 0
        for i in range(2, len(cost)+1):
            currentCost = min(cost[i-1]+minus1, cost[i-2]+minus2)
            minus2 = minus1
            minus1 = currentCost
        return currentCost


