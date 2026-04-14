class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def getNeighbors(y, x):
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            neighbors = []
            for dy, dx in directions:
                if 0 <= y+dy < len(matrix) and 0 <= x+dx < len(matrix[0]) and matrix[y+dy][x+dx] > matrix[y][x]:
                    neighbors.append((y+dy, x+dx))

            return neighbors
        
        predecessors = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for ny, nx in getNeighbors(i, j):
                    predecessors[ny][nx] += 1
        
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if predecessors[i][j] == 0:
                    queue.append((i, j))
        pathLength = 0
        while queue:
            pathLength += 1
            newQueue = []
            for y, x in queue:
                for ny, nx in getNeighbors(y, x):
                    predecessors[ny][nx] -= 1
                    if predecessors[ny][nx] == 0:
                        newQueue.append((ny, nx))
            queue = newQueue
        return pathLength


