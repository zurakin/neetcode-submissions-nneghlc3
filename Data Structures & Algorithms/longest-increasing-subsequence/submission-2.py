class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        def dfs(previousIdx, i):
            if (previousIdx, i) in mem:
                return mem[(previousIdx, i)]
            if i >= len(nums):
                return 1

            # option 1: skip i
            longest = dfs(previousIdx, i+1)

            # option 2: consider i if possible
            if nums[i] > nums[previousIdx]:
                longest = max(longest, 1 + dfs(i, i+1))
            
            mem[(previousIdx, i)] = longest
            return longest
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i, i+1))
        return res