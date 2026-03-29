class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.backtrack(0)
        return self.res

    def backtrack(self, i):
        if i == len(self.nums) - 1:
            self.res.append(self.nums.copy())
        for j in range(i, len(self.nums)):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.backtrack(i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
    