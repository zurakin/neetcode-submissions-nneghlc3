class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = {}
        self.wordDict = wordDict
        return self.wordBreakRec(s)

    def wordBreakRec(self, s):
        if len(s) == 0:
            return True
        if s in self.mem:
            return self.mem[s]
        for word in self.wordDict:
            if s.startswith(word):
                if self.wordBreakRec(s[len(word): ]):
                    self.mem[s] = True
                    return True
        self.mem[s] = False
        return False