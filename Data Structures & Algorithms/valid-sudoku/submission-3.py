class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for i in range(9):
                e = board[r][i]
                if e == ".":
                    continue
                if e not in seen:
                    seen.add(e)
                else:
                    print("row:", r)
                    return False 
        for c in range(9):
            seen = set()
            for i in range(9):
                e = board[i][c]
                if e == ".":
                    continue
                if e not in seen:
                    seen.add(e)
                else:
                    print("column:", c)
                    return False 
        for s in range(9):
            seen = set() 
            for i in range(9):
                r = 3 * (s // 3) + i // 3
                c = 3 * (s%3) + i % 3
                e = board[r][c]
                if e == ".":
                    continue
                if e not in seen:
                    seen.add(e)
                else:
                    print("square:", s)
                    return False 
        return True

