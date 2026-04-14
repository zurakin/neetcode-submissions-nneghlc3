class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) == 0:
            return len(t) == 0
        if len(t) == 0:
            return 0

        def countIdenticalChars(s): # Count how many identical chars come after each char
            suffix = [1 for _ in range(len(s))]
            for i in range(len(s)-2, -1, -1):
                if s[i] == s[i+1]:
                    suffix[i] = 1 + suffix[i+1]
            return suffix

        mem = {}
        sIdenticalChars = countIdenticalChars(s)
        tIdenticalChars = countIdenticalChars(t)

        def backtrack(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            
            res = 0
            
            if s[i] == t[j]:
                for pickCount in range(tIdenticalChars[j]+1):
                    res += math.comb(sIdenticalChars[i], pickCount) * backtrack(i+sIdenticalChars[i], j+pickCount)
            else:
                res += backtrack(i+sIdenticalChars[i], j)
            mem[(i, j)] = res
            return res
        
        return backtrack(0, 0)
