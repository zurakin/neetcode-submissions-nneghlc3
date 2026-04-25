class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float('inf')
        res = INF

        if not target:
            return 0

        windowSum = nums[0]
        i, j = 0, 0
        while True:
            if windowSum >= target:
                res = min(res, j-i+1)
                windowSum -= nums[i]
                i += 1
            else: 
                j += 1
                if j >= len(nums):
                    break
                windowSum += nums[j]


        if res == INF:
            return 0
        return res
