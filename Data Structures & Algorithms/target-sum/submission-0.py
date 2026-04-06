class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        def findTargetRec(target, i):
            if i >= len(nums):
                return int(target == 0)
            if (target, i) in mem:
                return mem[(target, i)]
            res = findTargetRec(target-nums[i], i+1) +  findTargetRec(target+nums[i], i+1)
            mem[(target, i)] = res 
            return res
        return findTargetRec(target, 0)