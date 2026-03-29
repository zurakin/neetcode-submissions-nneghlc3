class Node:
    def __init__(self, final):
        self.final = final
        self.neighbors = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node(True)
        for word in wordDict: 
            current = root
            for c in word:
                if c not in current.neighbors:
                    current.neighbors[c] = Node(False)
                current = current.neighbors[c]
            current.final = True

        self.mem = {}
        self.wordDict = wordDict
        self.s = s
        self.trie = root
        return self.wordBreakRec(0)

    def wordBreakRec(self, i):
        if i >= len(self.s):
            return True
        if i in self.mem:
            return self.mem[i]
        
        current = self.trie
        for j in range(i, len(self.s)):
            # print(f"checking if {self.s[j]} in neighbors: {current.neighbors.keys()}")
            if self.s[j] not in current.neighbors:
                self.mem[i] = False
                return False
            current = current.neighbors[self.s[j]]
            if current.final:
                if self.wordBreakRec(j+1):
                    self.mem[i] = True
                    return True
        self.mem[i] = False
        return False