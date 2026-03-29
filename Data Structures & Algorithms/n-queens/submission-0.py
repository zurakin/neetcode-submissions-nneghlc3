class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.n = n
        self.backtrack(set(), 0)
        solutions = []
        for result in self.res:
            solution = [['.' for _ in range(n)] for _ in range(n)]
            for pos in result:
                solution[pos[1]][pos[0]] = 'Q'
            solution = ["".join(r) for r in solution]
            solutions.append(solution)
        return solutions

    def backtrack(self, queens, startingRow):
        for y in range(startingRow, self.n):
            for x in range(self.n):
                if self.availablePosition((x, y), queens):
                    queens.add((x, y))
                    if len(queens) >= self.n:
                        self.res.append(queens.copy())
                    else:
                        self.backtrack(queens, y+1)
                    queens.remove((x, y))


    def availablePosition(self, pos, queens):
        for q in queens:
            if self.conflict(q, pos):
                return False
        return True

    def conflict(self, pos1, pos2) -> bool:
        return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0]-pos2[0]) == abs(pos1[1]-pos2[1])
