class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        for i in range(n):
            res += math.comb(n-i, i)
        return res