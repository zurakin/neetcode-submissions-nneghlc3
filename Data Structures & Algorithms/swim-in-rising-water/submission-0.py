class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        goal = (len(grid)-1, len(grid[0])-1)
        visited = set()
        elevations = [(grid[0][0], (0, 0))]
        maxTime = 0
        
        while len(elevations) > 0:
            elevation, pos = heapq.heappop(elevations)
            if pos in visited:
                continue
            visited.add(pos)
            maxTime = max(maxTime, elevation)
            if pos == goal:
                return maxTime
            r, c = pos
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for dy, dx in directions:
                if 0 <= r+dy < len(grid) and 0 <= c+dx < len(grid[0]):
                    heapq.heappush(elevations, (grid[r+dy][c+dx], (r+dy, c+dx)))
        return maxTime

