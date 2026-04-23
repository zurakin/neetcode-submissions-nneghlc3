class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:       
        occurences = defaultdict(int)
        res = 0
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            res += occurences[currentSum-k]
            occurences[currentSum] += 1
        res += occurences[k]
        return res
            

