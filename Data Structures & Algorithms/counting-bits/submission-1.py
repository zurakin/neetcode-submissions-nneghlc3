class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        while len(res) < n+1:
            for i in range(min(n+1-len(res), len(res))):
                res.append(1+res[i])
        return res