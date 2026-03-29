class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []
        self.s = s
        self.res = []
        self.backtrack([[s[0]]], 1)
        return self.res
        
    def backtrack(self, currentPartitions, i):
        validPalindromes = self.isPalindrome(currentPartitions[-1])
        if i >= len(self.s):
            if validPalindromes:
                self.res.append(["".join(p) for p in currentPartitions])
            return

        if validPalindromes:
            currentPartitions.append([self.s[i]])
            self.backtrack(currentPartitions, i+1)
            currentPartitions.pop()
        
        currentPartitions[-1].append(self.s[i])
        self.backtrack(currentPartitions, i+1)
        currentPartitions[-1].pop()
    
    def isPalindrome(self, s):
        return s == s[::-1]