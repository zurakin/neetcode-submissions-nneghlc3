class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2

        def dfs(s, idx):
            if s > target:
                return False
            if s == target:
                return True
            for i in range(idx, len(nums)):
                if dfs(nums[i] + s, i+1):
                    return True
            return False

        return dfs(0, 0)


