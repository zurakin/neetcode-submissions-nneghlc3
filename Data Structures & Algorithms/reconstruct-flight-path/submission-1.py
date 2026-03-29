class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        neighbors = {}
        for src, dest in tickets:
            if src in neighbors:
                heapq.heappush(neighbors[src], dest)
            else:
                neighbors[src] = [dest]
        
        def dfs(node):
            path = []
            nodeNeighbors = neighbors[node] if node in neighbors else []
            while len(nodeNeighbors) > 0:
                neighbor = heapq.heappop(nodeNeighbors)
                neighborPath = dfs(neighbor)
                path = neighborPath + path
            return [node] + path
        return dfs("JFK")
