class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        self.res = []
        self.nums = nums
        self.target = target
        self.combinationSumRec([], 0, 0)
        return self.res

    def combinationSumRec(self, currentNumbers, currentSum, startingIdx):
        if currentSum == self.target:
            self.res.append(currentNumbers.copy())
            return

        if currentSum > self.target or startingIdx >= len(self.nums):
            return

        n = self.nums[startingIdx]
        currentNumbers.append(n)
        self.combinationSumRec(currentNumbers, currentSum+n, startingIdx)
        currentNumbers.pop()
        self.combinationSumRec(currentNumbers, currentSum, startingIdx+1)