class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack((i, j), set()):
                    return True
        return False

    def backtrack(self, current, visited):
        if current in visited:
            return False
        if self.board[current[0]][current[1]] != self.word[len(visited)]:
            return False
        if len(visited) == len(self.word)-1:
            return True
        res = False
        visited.add(current)
        for n in self.neighbors(current):
            res = self.backtrack(n, visited)
            if res: 
                break
        visited.remove(current)
        return res 
        
    def neighbors(self, coord):
        x, y = coord
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            if 0 <= x+dx < len(self.board) and 0 <= y+dy < len(self.board[0]):
                neighbors.append((x+dx, y+dy))
        return neighbors
