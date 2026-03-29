class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = [[]]
        self.nums = nums
        self.backtrack([], 0)
        return self.res

    def backtrack(self, currentList, i):
        if i >= len(self.nums): 
            return
        currentList.append(self.nums[i])
        self.res.append(currentList.copy())
        self.backtrack(currentList, i+1)
        currentList.pop()
        i += 1
        while i < len(self.nums) and self.nums[i] == self.nums[i-1]:
            i += 1
        if i < len(self.nums):
            self.backtrack(currentList, i)