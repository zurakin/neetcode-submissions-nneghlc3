class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = [None for _ in range(len(nums))]
        return self.robHouse(nums, 0)

    def robHouse(self, nums, i):
        if i > len(nums)-1:
            return 0
        if self.dp[i] is not None:
            return self.dp[i]

        if i == len(nums)-1:
            self.dp[i] = nums[i]
        else:
            self.dp[i] = max(nums[i] + self.robHouse(nums, i+2), self.robHouse(nums, i+1))
        return self.dp[i]