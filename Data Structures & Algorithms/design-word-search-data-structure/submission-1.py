class Node:
    def __init__(self):
        self.children = {}
        self.final = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.final = True
        

    def search(self, word: str) -> bool: 
        def dfs(word, node):
            if len(word) == 0:
                return node.final
            c = word[0]
            if c == '.':
                for child in node.children.values():
                    if dfs(word[1:], child):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(word[1:], node.children[c])
        return dfs(word, self.root)
                
        
