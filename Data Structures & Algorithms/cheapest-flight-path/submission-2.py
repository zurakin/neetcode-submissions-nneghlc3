class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency = defaultdict(set)
        for s, d, cost in flights:
            adjacency[s].add((d, cost))
        
        startNode = (0, k, src) # priceSoFar, remainingStops, airport 
        visited = set([startNode])
        priorityQueue = [startNode]
        while priorityQueue:
            priceSoFar, remainingStops, airport = heapq.heappop(priorityQueue)
            if airport == dst:
                    return priceSoFar
            if remainingStops < 0:
                continue
            for neighborAirport, price in adjacency[airport]:
                neighborNode = (priceSoFar+price, remainingStops-1, neighborAirport)
                if neighborNode in visited:
                    continue
                visited.add(neighborNode)
                heapq.heappush(priorityQueue, neighborNode)

        return -1



        