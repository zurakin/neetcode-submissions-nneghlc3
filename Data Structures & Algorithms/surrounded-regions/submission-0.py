class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def getNeighbors(x, y):
            neighbors = []
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for dx, dy in directions:
                if 0 <= x+dx < len(board[0]) and 0 <= y+dy < len(board):
                    neighbors.append((x+dx, y+dy))
            return neighbors

        def dfs(x, y):
            if board[y][x] != 'O':
                return
            board[y][x] = '.'
            for nx, ny in getNeighbors(x, y):
                dfs(nx, ny)
        
        for x in range(len(board[0])):
            dfs(x, 0)
            dfs(x, len(board)-1)
        for y in range(1, len(board)-1):
            dfs(0, y)
            dfs(len(board[0])-1, y)

        for y in range(len(board)):
            for x in range(len(board[0])):
                c = board[y][x]
                if c == '.':
                    board[y][x] = 'O'
                elif c == 'O':
                    board[y][x] = 'X'