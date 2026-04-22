class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        H, W = len(matrix), len(matrix[0])
        self.W = W
        self.H = H
        self.dp = [[0 for _ in range(W)] for _ in range(H)]
        self.dp[H-1][W-1] = matrix[H-1][W-1]
        for i in range(H-1, -1, -1):
            for j in range(W-1, -1, -1):
                res = matrix[i][j]
                if i+1 < H:
                    res += self.dp[i+1][j]
                if j+1 < W:
                    res += self.dp[i][j+1]
                if i+1 < H and j+1 < W:
                    res -= self.dp[i+1][j+1]
                self.dp[i][j] = res
        # print(*self.dp, sep="\n")
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.dp[row1][col1]
        if row2+1 < self.H:
            res -= self.dp[row2+1][col1]
        if col2+1 < self.W:
            res -= self.dp[row1][col2+1]
        if row2+1 < self.H and col2+1 < self.W:
            res += self.dp[row2+1][col2+1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)