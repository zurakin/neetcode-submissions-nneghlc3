class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        costs = [INF] * n
        costs[src] = 0

        for _ in range(k + 1):
            newCosts = costs[:]
            updated = False

            for s, d, price in flights:
                if costs[s] == INF:
                    continue
                if newCosts[d] > costs[s] + price:
                    newCosts[d] = costs[s] + price
                    updated = True

            costs = newCosts
            if not updated:
                break

        return costs[dst] if costs[dst] < INF else -1