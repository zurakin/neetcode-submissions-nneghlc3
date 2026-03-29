class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []

        def getNeighbors(x, y):
            neighbors = []
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for dx, dy in directions:
                if 0 <= x+dx < len(heights[0]) and 0 <= y+dy < len(heights):
                    neighbors.append((x+dx, y+dy))
            return neighbors

        def explore(queue):
            visited = queue.copy()
            while len(queue) > 0:
                newQueue = set()
                for x, y in queue:
                    currentHeight = heights[y][x]
                    for nx, ny in getNeighbors(x, y):
                        if heights[ny][nx] >= currentHeight and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            newQueue.add((nx, ny))
                queue = newQueue
            return visited

        # Pacific
        queue = set()
        for x in range(len(heights[0])):
            queue.add((x, 0))
        for y in range(1, len(heights)):
            queue.add((0, y))
        pacific = set((coords[1], coords[0]) for coords in explore(queue))
        # print(sorted(list(pacific)))

        # Atlantic
        queue = set()
        for x in range(len(heights[0])):
            queue.add((x, len(heights)-1))
        for y in range(len(heights)-1):
            queue.add((len(heights[0])-1, y))
        atlantic = set((coords[1], coords[0]) for coords in explore(queue))
        # print(sorted(list(atlantic)))

        return list(pacific.intersection(atlantic))
                