class Solution:
    def numDecodings(self, s: str) -> int:
        self.mem = [None for _ in range(len(s))]
        return self.numDecodingsRec(s, 0)

    def numDecodingsRec(self, s: str, i: int) -> int:
        if i >= len(s):
            return 1
        if self.mem[i] is not None:
            return self.mem[i]
        res = 0
        if s[i] == '0':
            return 0
        if 1 <= int(s[i]) <= 26:
            res += self.numDecodingsRec(s, i+1)
        if i+1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
            res += self.numDecodingsRec(s, i+2)
        self.mem[i] = res
        return res