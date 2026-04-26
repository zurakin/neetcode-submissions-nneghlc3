class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        currentMin = nums[0]
        globalMin = nums[0]
        for i in range(1, N):
            currentMin = min(nums[i], currentMin+nums[i])
            globalMin = min(globalMin, currentMin)
        
        currentMax = nums[0]
        globalMax = nums[0]
        for i in range(1, N):
            currentMax = max(nums[i], currentMax + nums[i])
            globalMax = max(currentMax, globalMax)
        if globalMax < 0:
            return globalMax
        return max(sum(nums) - globalMin, globalMax)