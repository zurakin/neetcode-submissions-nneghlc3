class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tokens = []
        for i in range(len(p)):
            if p[i] == '*':
                continue
            if i < len(p) - 1 and p[i+1] == '*':
                tokens.append(p[i:i+2])
            else:
                tokens.append(p[i])
            
        mem = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(tokens):
                return True

            if (i, j) in mem:
                return mem[(i, j)]
            
            if j >= len(tokens):
                return False

            token = tokens[j][0]
            repeated = len(tokens[j]) == 2

            if repeated and dfs(i, j+1): # Try to ignore pattern
                mem[(i, j)] = True
                return True
            
            if i >= len(s):
                return False
            
            if token == '.' or (i < len(s) and token == s[i]):
                if dfs(i+1, j+1):
                    mem[(i, j)] = True
                    return True
                if repeated and dfs(i+1, j):
                    mem[(i, j)] = True
                    return True
            mem[(i, j)] = False
            return False
        return dfs(0, 0)
                