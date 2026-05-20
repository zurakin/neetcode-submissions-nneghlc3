class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        W = len(grid[0])
        H = len(grid)
        dp = [[-1 for _ in range(W)] for _ in range(H)]
        for i in range(H-1, -1, -1):
            for j in range(W-1, -1, -1):
                dp[i][j] = grid[i][j]
                if j < W-1 or i < H-1:
                    right = dp[i][j+1] if j < (W-1) else float('inf')
                    bottom = dp[i+1][j] if i < (H-1) else float('inf')
                    dp[i][j] += min(right, bottom)
        return dp[0][0]