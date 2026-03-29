class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0: 
            return [[]]
        frequencies = {}
        for c in candidates:
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
        self.frequencies = list(frequencies.items())
        self.res = []
        self.target = target
        self.combinationSumRec([], 0, 0)
        return self.res

    def combinationSumRec(self, currentList, currentSum, i):
        if i >= len(self.frequencies) or currentSum >= self.target:
            return
        
        self.combinationSumRec(currentList, currentSum, i+1)
        for _ in range(self.frequencies[i][1]):
            currentList.append(self.frequencies[i][0])
            currentSum += self.frequencies[i][0]
            print(currentList, currentSum)
            if currentSum == self.target:
                self.res.append(currentList.copy())
            else:
                self.combinationSumRec(currentList, currentSum, i+1)

        currentSum -= self.frequencies[i][1] * self.frequencies[i][0]
        for _ in range(self.frequencies[i][1]):
            currentList.pop()


