class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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