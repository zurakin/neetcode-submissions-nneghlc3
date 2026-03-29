class Node:
    def __init__(self):
        self.final = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 1 and len(board[0]) == 1:
            if board[0][0] in words:
                return [board[0][0]]
            return []
        root = Node()
        results = []

        def insert(trie: Node, word):
            current = trie
            for c in word:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.final = True


        for word in words:
            insert(root, word)
            

        def getNeighbors(position):
            x, y = position
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            neighbors = []
            for dx, dy in directions:
                if 0 <= x+dx < len(board[0]) and 0 <= y+dy < len(board):
                    neighbors.append((x+dx, y+dy))
            return neighbors

        
        def findWord(word, node: Node, position, visited):
            if node.final:
                results.append("".join(word))
                node.final = False
            for neighbor in getNeighbors(position):
                neighborChar = board[neighbor[1]][neighbor[0]]
                if neighbor in visited or neighborChar not in node.children:
                    continue
                word.append(neighborChar)
                visited.add(neighbor)
                findWord(word, node.children[neighborChar], neighbor, visited)
                visited.remove(neighbor)
                word.pop()

        for y in range(len(board)):
            for x in range(len(board[0])):
                findWord([], root, (x, y), set())
        return results

