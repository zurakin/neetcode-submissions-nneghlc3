class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                j += 1
                res += 1
            
            j = 0 
            l = 0
            while i-j >= 0 and i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                l += 2
                j += 1
                res += 1
        return res
