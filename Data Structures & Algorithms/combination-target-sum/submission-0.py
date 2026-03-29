class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        self.res = []
        self.nums = sorted(nums)
        self.target = target
        self.combinationSumRec([], 0, 0)
        return self.res

    def combinationSumRec(self, currentNumbers, currentSum, startingIdx):
        for i in range(startingIdx, len(self.nums)):
            n = self.nums[i]
            currentNumbers.append(n)
            if currentSum + n == self.target:
                self.res.append(currentNumbers.copy())
            elif currentSum + n < self.target:
                self.combinationSumRec(currentNumbers, currentSum + n, i)
            currentNumbers.pop()
        
        