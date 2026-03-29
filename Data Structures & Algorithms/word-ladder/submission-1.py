class Solution:
    def getPattern(self, word, idx):
        return "".join([word[j] if j != idx else '.' for j in range(len(word))])

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = {}
        for wordIdx, word in enumerate(wordList):
            for i in range(len(word)):
                pattern = self.getPattern(word, i)
                if pattern in patterns:
                    patterns[pattern].append(wordIdx)
                else: 
                    patterns[pattern] = [wordIdx]
        visited = set(beginWord)
        queue = [(beginWord, 1)]

        while len(queue) > 0:
            current, pathLength = queue.pop(0)
            if current == endWord:
                return pathLength
            for i in range(len(current)):
                patternI = self.getPattern(current, i)
                if patternI not in patterns:
                    continue
                for wordIdx in patterns[patternI]:
                    word = wordList[wordIdx]
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, pathLength+1))
            
        return 0

