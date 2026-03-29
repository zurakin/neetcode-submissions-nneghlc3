class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y) -> int:
            if grid[y][x] != 1:
                return 0 
            grid[y][x] = 0
            res = 1
            for nx, ny in getNeighbors(x, y):
                res += dfs(nx, ny)
            return res
        

        def getNeighbors(x, y):
            res = []
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for dx, dy in directions: 
                if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
                    res.append((x+dx, y+dy))
            return res

        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res = max(res, dfs(x, y))
        return res