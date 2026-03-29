class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        def dfs(x, y) -> bool:
            if grid[y][x] != '1':
                return False 
            grid[y][x] = '0'
            for nx, ny in getNeighbors(x, y):
                dfs(nx, ny)
            return True
        

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
                res += int(dfs(x, y))
        return res