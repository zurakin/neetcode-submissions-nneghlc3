class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adjacency = defaultdict(list)
        for s, d, price in flights:
            adjacency[s].append((d, price))

        # (cost, node, remainingStops)
        heap = [(0, src, k + 1)]
        
        # (node, remainingStops) -> min cost seen so far
        best = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops == 0:
                continue

            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            best[(node, stops)] = cost

            for neighbor, price in adjacency[node]:
                heapq.heappush(heap, (cost + price, neighbor, stops - 1))

        return -1