class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        words = [word + " " for word in words]
        adjacencyList = defaultdict(set)
        incomingEdges = defaultdict(int)

        def buildGraph(rangeBeg, rangeEnd, compareIdx):
            if rangeBeg >= rangeEnd:
                return
            
            currentChar = None
            nextRangeBeg = None 
            nextRangeEnd = None
            for i in range(rangeBeg, rangeEnd+1):
                word = words[i]
                if compareIdx >= len(word):
                    continue 
                if currentChar is None:
                    currentChar = word[compareIdx]
                    nextRangeBeg = i
                    nextRangeEnd = i
                elif currentChar == word[compareIdx]:
                    nextRangeEnd = i
                else:
                    if word[compareIdx] not in adjacencyList[currentChar]:
                        adjacencyList[currentChar].add(word[compareIdx])
                        incomingEdges[word[compareIdx]] += 1
                    buildGraph(nextRangeBeg, nextRangeEnd, compareIdx+1)
                    currentChar = word[compareIdx]
                    nextRangeBeg = i
                    nextRangeEnd = i
            if nextRangeBeg is not None:
                buildGraph(nextRangeBeg, nextRangeEnd, compareIdx+1)
        
        buildGraph(0, len(words)-1, 0)
        if incomingEdges[' '] > 0:
            return ""
        # print(*adjacencyList.items(), sep="\n")

        allChars = set()
        for word in words:
            allChars.update(list(word))

        res = []
        queue = deque()
        for char in allChars:
            if incomingEdges[char] == 0:
                queue.append(char)

        while len(queue) > 0:
            char = queue.popleft()
            if char != ' ':
                res.append(char)
            for nextChar in adjacencyList[char]:
                incomingEdges[nextChar] -= 1
                if incomingEdges[nextChar] == 0:
                    queue.append(nextChar)
        return "".join(res) if len(res) == len(allChars)-1 else ""
