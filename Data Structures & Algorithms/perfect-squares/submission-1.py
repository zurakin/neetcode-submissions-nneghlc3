class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}

        def search(n):
            res = float('inf')
            root = int(math.sqrt(n))
            if n < 0:
                return res
            if n == 0:
                return 0
            if n in mem:
                return mem[n]
            for j in range(root, 0, -1):
                res = min(res, 1 + search(n-j**2))
            mem[n] = res
            return res
        return search(n)