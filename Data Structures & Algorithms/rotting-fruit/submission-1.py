class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        queue = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    queue.append((x, y))
                elif grid[y][x] == 1:
                    freshCount += 1
        
        def getNeighbors(x, y):
            neighbors = []
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            for dx, dy in directions:
                if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
                    neighbors.append((x+dx, y+dy))
            return neighbors
        rottenCount = 0
        time = 0
        while len(queue) > 0:
            newQueue = []
            for x, y in queue:
                for nx, ny in getNeighbors(x, y):
                    if grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        rottenCount += 1
                        newQueue.append((nx, ny))
            queue = newQueue
            if len(queue) > 0:
                time += 1
        print(rottenCount, freshCount)
        return time if rottenCount == freshCount else -1