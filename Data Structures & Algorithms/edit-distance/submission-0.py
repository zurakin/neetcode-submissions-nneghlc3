class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def backtrack(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1) or j == len(word2):
                return abs((len(word1)-i)-(len(word2)-j))

            if (i, j) in mem:
                return mem[(i, j)]

            res = float('inf')
            if word1[i] == word2[j]:
                return backtrack(i+1, j+1)

            # Try to replace ith char from word1
            res = min(res, 1+backtrack(i+1, j+1))

            # Try to delete ith char from word1
            res = min(res, 1+backtrack(i+1, j))

            # Try to add to word1
            res = min(res, 1+backtrack(i, j+1))

            mem[(i, j)] = res

            return res

        return backtrack(0, 0)