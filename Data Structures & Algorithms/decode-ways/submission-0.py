class Solution:
    def numDecodings(self, s: str) -> int:   
        if len(s) == 0:
            return 1
        res = 0
        if s[0] == '0':
            return 0
        if 1 <= int(s[0]) <= 26:
            res += self.numDecodings(s[1:])
        if len(s) >= 2 and 1 <= int(s[0:2]) <= 26:
            res += self.numDecodings(s[2:])
        return res