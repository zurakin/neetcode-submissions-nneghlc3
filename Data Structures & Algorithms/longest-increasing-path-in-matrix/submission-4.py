class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        mem = {}

        def getNeighbors(y, x):
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            neighbors = []
            for dy, dx in directions:
                if 0 <= y+dy < len(matrix) and 0 <= x+dx < len(matrix[0]) and matrix[y+dy][x+dx] > matrix[y][x]:
                    neighbors.append((y+dy, x+dx))

            neighbors.sort(key = lambda pos: matrix[pos[0]][pos[1]], reverse=True)
            return neighbors

        def dfs(y, x):
            if (y, x) in mem:
                return mem[y, x]
            res = 0
            for neighbor in getNeighbors(y, x):
                res = max(res, dfs(*neighbor))
            res += 1
            mem[(y, x)] = res
            return res
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res

        