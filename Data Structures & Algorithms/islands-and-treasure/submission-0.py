class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        queue = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    queue.add((x, y))

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def getNeighbors(node):
            neighbors = []
            x, y = node 
            for dx, dy in directions:
                if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid[0]) and grid[y+dy][x+dx] == inf:
                    neighbors.append((x+dx, y+dy))
            return neighbors

        distance = 0
        while len(queue) > 0:
            newQueue = set()
            for node in queue:
                if 0 < grid[node[1]][node[0]] < inf: 
                    continue
                grid[node[1]][node[0]] = distance
                for neighbor in getNeighbors(node):
                    print(neighbor)
                    newQueue.add(neighbor)
            # print(*grid, sep="\n")
            # print("---------")
            queue = newQueue
            distance += 1
        