class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if int(target) != target:
            return False
        target = int(target)

        dp = [[False for _ in range(len(nums))] for _ in range(target+1)]
        dp[0] = [True for _ in range(len(nums))]
        for s in range(1, target+1):
            for i in range(len(nums)):
                dp[s][i] = nums[i]==s or i >= 1 and (dp[s][i-1] or (s-nums[i] > 0 and dp[s-nums[i]][i-1]))
        print(*dp, sep="\n")
        return dp[s][len(nums)-1]

    def canPartition2(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if int(target) != target:
            return False
        target = int(target)

        def dfs(target, i):
            if target < 0: 
                return False
            if target == 0:
                return True
            if i >= len(nums):
                return False
            return dfs(target-nums[i], i+1) or dfs(target, i+1)
        
        return dfs(target, 0)