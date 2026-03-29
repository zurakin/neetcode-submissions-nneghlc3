class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currentSum = nums[0]
        for n in nums[1:]:
            if currentSum < 0:
                currentSum = n
            else:    
                currentSum += n
            res = max(res, currentSum)
        return res
