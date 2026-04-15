class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def editDistance(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1) or j == len(word2):
                return abs((len(word1)-i)-(len(word2)-j))

            if (i, j) in mem:
                return mem[(i, j)]

            if word1[i] == word2[j]:
                res = editDistance(i+1, j+1)
                mem[(i, j)] = res
                return res

            res = 1 + min(
                editDistance(i+1, j+1), # Try to replace ith char from word1
                editDistance(i+1, j), # Try to delete ith char from word1
                editDistance(i, j+1) # Try to add to word1
            )
            
            mem[(i, j)] = res
            return res

        return editDistance(0, 0)