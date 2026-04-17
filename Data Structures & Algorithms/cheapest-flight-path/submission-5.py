class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency = defaultdict(set)
        for s, d, cost in flights:
            adjacency[s].add((d, cost))

        INF = float("inf")
        costs = [INF for _ in range(n)]
        costs[src] = 0

        def explore(i, newCosts):
            updateMade = False
            for neighbor, cost in adjacency[i]:
                costFromI = costs[i] + cost
                if newCosts[neighbor] > costFromI:
                    updateMade = True
                    newCosts[neighbor] = costFromI
            return updateMade

        for _ in range(k+1):
            cont = False
            newCosts = costs[:]
            for i in range(n):
                cont |= explore(i, newCosts)
            costs = newCosts
            if not cont:
                break
        return costs[dst] if costs[dst] < INF else -1
                