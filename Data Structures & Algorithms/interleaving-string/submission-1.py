class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        mem = {}        
        def dfs(i, j, k):
            if k >= len(s3):
                return True
            if (i, j, k) in mem:
                return mem[(i, j, k)]
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1, j, k+1):
                mem[(i, j, k)] = True
                return True 
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j+1, k+1):
                mem[(i, j, k)] = True
                return True 
            mem[(i, j, k)] = False
            return False
        
        return dfs(0, 0, 0)
                