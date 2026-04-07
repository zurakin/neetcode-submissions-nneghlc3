class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)

        def getPatterns(word):
            patterns = []
            for i in range(len(word)):
                patterns.append(word[:i]+'.'+word[i+1:])
            return patterns

        wordGroups = {}
        for word in wordList:
            for pattern in getPatterns(word):
                if pattern not in wordGroups:
                    wordGroups[pattern] = set()
                wordGroups[pattern].add(word)
        
        print(wordGroups)
            
        def getNeighbors(word):
            neighbors = set()
            for pattern in getPatterns(word):
                neighbors = neighbors.union(wordGroups[pattern])
            return neighbors

        seen = set()
        queue = [beginWord]
        seen.add(beginWord)

        depth = 1
        while len(queue) > 0:
            print(queue)
            nextLevelNodes = []
            for node in queue:
                for n in getNeighbors(node):
                    if n == endWord:
                        return depth + 1
                    if n not in seen:
                        seen.add(n)
                        nextLevelNodes.append(n)
            depth += 1
            queue = nextLevelNodes
        return 0
                

