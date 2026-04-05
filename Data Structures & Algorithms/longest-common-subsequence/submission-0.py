class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        mem = {}
        def lcs(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            res = 0
            if text1[i] == text2[j]:
                res = 1 + lcs(i+1, j+1)
            res = max(res, lcs(i, j+1), lcs(i+1, j))
            mem[(i, j)] = res 
            return res
        
        return lcs(0, 0)
